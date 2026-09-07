import json
import os
import re
import shutil
import sqlite3
import subprocess
import tempfile

from flask import Flask, jsonify, render_template, request

from problems import PROBLEMS

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROBLEMS_BY_ID = {p["id"]: p for p in PROBLEMS}

COMPILE_TIMEOUT = 30
RUN_TIMEOUT = 10


def get_problem(pid):
    problem = PROBLEMS_BY_ID.get(pid)
    if not problem:
        raise KeyError(f"Problem {pid} not found")
    return problem


def serialize_problem_meta(p):
    return {
        "id": p["id"],
        "slug": p["slug"],
        "title": p["title"],
        "difficulty": p["difficulty"],
        "topics": p["topics"],
    }


def serialize_problem_full(p):
    data = serialize_problem_meta(p)
    data.update(
        {
            "description": p["description"],
            "hint": p["hint"],
            "judge": p["judge"],
            "languages": p["languages"],
            "boilerplate": p["boilerplate"],
            "samples": p["samples"],
        }
    )
    if p["judge"] == "browser":
        data["browserHtml"] = p["browser_html"]
        data["browserStyle"] = p.get("browser_style", "")
        data["browserTests"] = [
            {"name": t["name"], "hidden": t["hidden"], "steps": t["steps"], "expect": t["expect"]}
            for t in p["browser_tests"]
        ]
    if p["languages"] == ["sql"]:
        data["databases"] = [
            {"name": db["name"], "hidden": db["hidden"], "schema": db["schema"], "seed": db["seed"]}
            for db in p["databases"]
        ]
    return data


# ------------------------------------------------------------------ #
# Java judge — user submits a complete program whose public class may
# have any name; the file is renamed to match so javac accepts it, and
# each test case is fed to stdin and stdout is compared.
# ------------------------------------------------------------------ #

PUBLIC_CLASS_RE = re.compile(r"\bpublic\s+(?:final\s+|abstract\s+)*class\s+(\w+)")


def judge_java(code, tests, workdir):
    m = PUBLIC_CLASS_RE.search(code)
    class_name = m.group(1) if m else "Main"
    src_file = os.path.join(workdir, f"{class_name}.java")
    with open(src_file, "w") as f:
        f.write(code)
    stdin = "\n".join(t["input"] for t in tests) + "\n"

    compile_res = subprocess.run(
        ["javac", "-d", workdir, src_file],
        cwd=workdir, capture_output=True, text=True, timeout=COMPILE_TIMEOUT,
    )
    if compile_res.returncode != 0:
        return {"compile_error": compile_res.stderr.strip()}

    run_res = subprocess.run(
        ["java", "-cp", workdir, class_name],
        cwd=workdir, input=stdin, capture_output=True, text=True, timeout=RUN_TIMEOUT,
    )
    if run_res.returncode != 0:
        return {"runtime_error": (run_res.stderr or "Unknown runtime error").strip()[-2000:]}
    outputs = run_res.stdout.strip().splitlines()
    return {"outputs": outputs}


# ------------------------------------------------------------------ #
# C++ judge — user submits a complete program; each test case is fed
# to its stdin and stdout is compared.
# ------------------------------------------------------------------ #

def judge_cpp(code, tests, workdir):
    stdin = "\n".join(t["input"] for t in tests) + "\n"
    src_file = os.path.join(workdir, "solution.cpp")
    with open(src_file, "w") as f:
        f.write(code)

    compile_res = subprocess.run(
        ["g++", "-std=c++17", "-O2", "-o", os.path.join(workdir, "solution"), src_file],
        cwd=workdir, capture_output=True, text=True, timeout=COMPILE_TIMEOUT,
    )
    if compile_res.returncode != 0:
        return {"compile_error": compile_res.stderr.strip()}

    run_res = subprocess.run(
        [os.path.join(workdir, "solution")],
        cwd=workdir, input=stdin, capture_output=True, text=True, timeout=RUN_TIMEOUT,
    )
    if run_res.returncode != 0:
        return {"runtime_error": (run_res.stderr or "Unknown runtime error").strip()[-2000:]}
    outputs = run_res.stdout.strip().splitlines()
    return {"outputs": outputs}


def format_input(input_str):
    """Human-readable rendering of a test input: JSON matrices are shown as
    bracketed rows, stdin-style inputs are shown verbatim."""
    try:
        return format_matrix(input_str)
    except (ValueError, TypeError):
        return input_str


def format_matrix(json_str):
    rows = json.loads(json_str)
    if rows and isinstance(rows[0], list):
        return "\n".join("[" + ", ".join(str(x) for x in row) + "]" for row in rows)
    return "\n".join(str(x) for x in rows)


# ------------------------------------------------------------------ #
# SQL judge
# ------------------------------------------------------------------ #

def build_sql_db(seed, schema_sql):
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.executescript(schema_sql)
    for table, rows in seed.items():
        placeholders = ", ".join("?" for _ in rows[0])
        cur.executemany(f"INSERT INTO {table} VALUES ({placeholders})", rows)
    conn.commit()
    return conn


def run_sql_query(query, seed, schema_sql):
    """Returns (ok, headers, rows) or (False, error_message, None)."""
    try:
        conn = build_sql_db(seed, schema_sql)
    except Exception as e:
        return False, f"Database setup error: {e}", None
    try:
        cur = conn.execute(query)
        headers = [d[0] for d in cur.description] if cur.description else []
        rows = cur.fetchall()
        return True, headers, rows
    except Exception as e:
        return False, str(e), None
    finally:
        conn.close()


def cells_equal(a, b):
    fa = isinstance(a, (int, float)) and not isinstance(a, bool)
    fb = isinstance(b, (int, float)) and not isinstance(b, bool)
    if fa and fb:
        return abs(float(a) - float(b)) < 0.005
    if fa or fb:
        return False
    return str(a).strip() == str(b).strip()


def rows_equal(r1, r2):
    return len(r1) == len(r2) and all(
        len(c1) == len(c2) and all(cells_equal(a, b) for a, b in zip(c1, c2))
        for c1, c2 in zip(r1, r2)
    )


def format_table(headers, rows):
    out = []
    out.append(" | ".join(str(h) for h in headers))
    out.append("-" * max(20, sum(len(str(h)) + 3 for h in headers)))
    for row in rows:
        out.append(" | ".join(
            f"{v:.2f}" if isinstance(v, float) else str(v) for v in row
        ))
    return "\n".join(out)


def judge_sql(query, databases, include_hidden):
    results = []
    all_pass = True
    for db in databases:
        if db["hidden"] and not include_hidden:
            continue
        ok, headers, rows = run_sql_query(query, db["seed"], db["schema"])
        if not ok:
            results.append({
                "database": db["name"], "hidden": db["hidden"], "passed": False,
                "error": headers, "expected": None, "actual": None,
            })
            all_pass = False
            continue
        expected = run_sql_query(db["reference_query"], db["seed"], db["schema"])
        exp_ok, exp_headers, exp_rows = expected
        passed = rows_equal(rows, exp_rows)
        if not passed:
            all_pass = False
        results.append({
            "database": db["name"], "hidden": db["hidden"], "passed": passed,
            "expected": format_table(exp_headers, exp_rows) if exp_ok else "reference query failed",
            "actual": format_table(headers, rows),
            "error": None,
        })
    return results, all_pass


# ------------------------------------------------------------------ #
# Routes
# ------------------------------------------------------------------ #

@app.after_request
def no_cache(response):
    # always revalidate HTML so new deploys (buttons, layout) show up instantly
    if response.content_type and "text/html" in response.content_type:
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/problems")
def api_problems():
    return jsonify([serialize_problem_meta(p) for p in PROBLEMS])


@app.route("/api/problems/<int:pid>")
def api_problem(pid):
    try:
        problem = get_problem(pid)
    except KeyError:
        return jsonify({"error": "Problem not found"}), 404
    return jsonify(serialize_problem_full(problem))


@app.route("/api/run", methods=["POST"])
def api_run():
    return do_judge(request.get_json(force=True), submit=False)


@app.route("/api/submit", methods=["POST"])
def api_submit():
    return do_judge(request.get_json(force=True), submit=True)


def do_judge(payload, submit):
    pid = payload.get("problem_id")
    language = payload.get("language", "")
    code = payload.get("code", "")
    try:
        problem = get_problem(pid)
    except KeyError:
        return jsonify({"error": "Problem not found"}), 404

    if not code.strip():
        return jsonify({"error": "Code is empty"}), 400

    # ---------------- Browser-judged (JS/DOM) ---------------- #
    if problem["judge"] == "browser":
        return jsonify({"judge": "browser", "code": code})

    # ---------------- SQL ---------------- #
    if language == "sql":
        results, all_pass = judge_sql(code, problem["databases"], include_hidden=submit)
        return jsonify({
            "judge": "sql", "passed": all_pass,
            "passed_count": sum(1 for r in results if r["passed"]),
            "total": len(results),
            "results": results,
        })

    # ---------------- Java / C++ ---------------- #
    if language not in ("java", "cpp"):
        return jsonify({"error": f"Unsupported language: {language}"}), 400

    tests = problem["tests"]
    if not submit:
        tests = [t for i, t in enumerate(tests) if i in problem["samples"]]

    # each test case gets its own process so a crash mid-way can't
    # corrupt later cases' outputs
    outputs = []
    for t in tests:
        workdir = tempfile.mkdtemp(prefix="judge_")
        try:
            if language == "java":
                outcome = judge_java(code, [t], workdir)
            else:
                outcome = judge_cpp(code, [t], workdir)
        except subprocess.TimeoutExpired:
            outcome = {"timeout": True}
        finally:
            shutil.rmtree(workdir, ignore_errors=True)
        if "compile_error" in outcome:
            return jsonify({"judge": "compile", "compile_error": outcome["compile_error"]})
        if "runtime_error" in outcome:
            return jsonify({"judge": "runtime", "runtime_error": outcome["runtime_error"]})
        if "timeout" in outcome:
            return jsonify({"judge": "timeout", "error": "Time Limit Exceeded"})
        # a program may print multiple lines per test (e.g. one prime per
        # line); the whole stdout of the run is the test's output
        outputs.append("\n".join(outcome["outputs"]))
    results = []
    for i, t in enumerate(tests):
        actual = outputs[i].strip() if i < len(outputs) else "(no output)"
        expected = t["expected"]
        if problem.get("io_style") == "lines":
            # multi-line outputs (e.g. one prime per line): compare
            # token-by-token so trailing whitespace is never fatal
            passed = actual.split() == expected.split()
        else:
            passed = actual == expected
        results.append({
            "index": i, "hidden": t["hidden"], "passed": passed,
            "input": format_input(t["input"]), "expected": expected, "actual": actual,
        })
    return jsonify({
        "judge": "code",
        "passed": all(r["passed"] for r in results),
        "passed_count": sum(1 for r in results if r["passed"]),
        "total": len(results),
        "results": results,
    })


if __name__ == "__main__":
    print("Practice platform running at http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)
