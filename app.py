import json
import os
import re
import shutil
import sqlite3
import subprocess
import tempfile

from flask import Flask, jsonify, render_template, request, send_from_directory

from problems import PROBLEMS

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROBLEMS_BY_ID = {p["id"]: p for p in PROBLEMS}

PDF_DIR = os.path.join(BASE_DIR, "extracted", "downloaded")

# PDFs served under /pdfs/<file> and shown in the "PDF Resources" section.
# label = course name shown on the card; tag = grouped category.
PDF_LIBRARY = [
    {"file": "Accenture_Technical_-_All_Questions_Set.pdf", "label": "Accenture Technical — All Questions Set", "tag": "Technical MCQ", "desc": "Big bank of technical MCQs across all topics."},
    {"file": "Accenture_Code_MCQ.pdf", "label": "Accenture Code MCQ (Pseudocode)", "tag": "Pseudocode", "desc": "32 pseudocode-tracing questions with answers (also playable as quiz #21)."},
    {"file": "Accenture_Paper_Solution.pdf", "label": "Accenture Paper Solution", "tag": "Full Paper", "desc": "Actual on-campus paper with solutions — cloud, DevOps, OS, networks (also quiz #22)."},
    {"file": "Accenture_Pseudocode_Solution_20_DEC.pdf", "label": "Accenture Pseudocode Solution — 20 Dec", "tag": "Pseudocode", "desc": "Worked pseudocode solutions from the 20 Dec exam."},
    {"file": "Accenture_20_Dec_Tech_Assessment.pdf", "label": "Accenture 20 Dec (Tech Assessment)", "tag": "Full Paper", "desc": "Technical assessment paper from the 20 Dec exam."},
    {"file": "Accenture_PYQ_Recent_Set.pdf", "label": "Accenture PYQ (Recent Set)", "tag": "Full Paper", "desc": "Recent previous-year questions with full solutions (web-based tasks included)."},
    {"file": "Accenture_11_October_2025_-_Coding_Set.pdf", "label": "Accenture 11 October 2025 — Coding Set", "tag": "Coding", "desc": "On-campus coding questions from the 11 Oct 2025 exam."},
    {"file": "Accenture_Coding_20_Dec.pdf", "label": "Accenture Coding — 20 Dec", "tag": "Coding", "desc": "Coding questions from the 20 Dec exam."},
    {"file": "Previous_Years_Coding_Full_Questions.pdf", "label": "Previous Years Coding (Full Questions)", "tag": "Coding", "desc": "367-page compilation of every previous-years coding question."},
    {"file": "Top_60_SQL_Queries_for_interviews_PDF.pdf", "label": "Top 60 SQL Queries for Interviews", "tag": "SQL", "desc": "Classic SQL interview query drills with sample tables."},
    {"file": "Cognizant__Accenture_Web_Based.pdf", "label": "Cognizant + Accenture Web Based", "tag": "Web Based", "desc": "Previous-year web-based (JS/HTML) questions from Cognizant & Accenture."},
    {"file": "Pseudocodes_Complete.pdf", "label": "Pseudocodes Complete", "tag": "Pseudocode", "desc": "Full pseudocode MCQ collection — every pattern with answers."},
    {"file": "CN_MCQ_Complete.pdf", "label": "CN MCQ Complete", "tag": "Networking", "desc": "Complete computer-networks MCQ bank with solutions."},
    {"file": "Cloud_MCQ.pdf", "label": "Cloud MCQ", "tag": "Cloud", "desc": "Cloud computing MCQs — services, deployment models, virtualization."},
    {"file": "Network_Security.pdf", "label": "Network Security", "tag": "Security", "desc": "Network-security MCQs — firewalls, cryptography, attacks."},
    {"file": "Microsoft_Office_MCQ.pdf", "label": "Microsoft Office MCQ", "tag": "MS Office", "desc": "Word / Excel / PowerPoint MCQs asked in Accenture assessments."},
    {"file": "Path_Game_20_DEC.pdf", "label": "Path Game — 20 Dec", "tag": "Game Based", "desc": "Accenture path-finding game exercise from the 20 Dec exam."},
    {"file": "Path_Finder_Game.pdf", "label": "Path Finder Game", "tag": "Game Based", "desc": "Path-finder grid game — rules and solved example."},
    {"file": "The_Hidden_Path_-_Game_Based_Accenture.pdf", "label": "The Hidden Path — Game Based", "tag": "Game Based", "desc": "Hidden-path game assessment walkthrough."},
    {"file": "Accenture_Memory_Game__Ex-2_.pdf", "label": "Accenture Memory Game (Ex-2)", "tag": "Game Based", "desc": "Memory-game assessment example 2 with answers."},
    {"file": "Accenture_Memory_Game__Ex-3_.pdf", "label": "Accenture Memory Game (Ex-3)", "tag": "Game Based", "desc": "Memory-game assessment example 3 with answers."},
    {"file": "Accenture_Full_Paper.pdf", "label": "Accenture Full Paper (162 pages)", "tag": "Full Paper", "desc": "Complete full-length paper — all sections in one document."},
    {"file": "Verbal_Ability.pdf", "label": "Verbal Ability Sheet", "tag": "Cheatsheets", "desc": "Verbal-ability formulas & concepts cheatsheet."},
    {"file": "Aptitude_Cheatsheet.pdf", "label": "Aptitude Cheatsheet", "tag": "Cheatsheets", "desc": "Quantitative-aptitude formulas & shortcuts cheatsheet."},
    {"file": "Reasoning.pdf", "label": "Reasoning Sheet", "tag": "Cheatsheets", "desc": "Logical-reasoning concepts & tricks cheatsheet."},
    {"file": "OOPS_Java_notes.pdf", "label": "OOPS Java Notes", "tag": "Notes", "desc": "Object-oriented programming in Java — interview notes."},
    {"file": "Python_Interview_Questions.pdf", "label": "Python Interview Questions", "tag": "Notes", "desc": "Top Python interview questions with answers."},
    {"file": "OOPS_Python.pdf", "label": "OOPS Python", "tag": "Notes", "desc": "Object-oriented programming in Python — notes & examples."},
    {"file": "MVC_and_Rest_API.pdf", "label": "MVC & REST API", "tag": "Notes", "desc": "MVC architecture and REST API interview notes."},
]

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
    if p["judge"] == "quiz":
        # questions without the answer key — grading happens server-side
        data["questions"] = [
            {"n": i + 1, "q": q["q"], "options": q["options"]}
            for i, q in enumerate(p["questions"])
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


@app.route("/api/pdfs")
def api_pdfs():
    items = []
    for p in PDF_LIBRARY:
        path = os.path.join(PDF_DIR, p["file"])
        if os.path.exists(path):
            items.append({**p, "size_kb": os.path.getsize(path) // 1024})
    return jsonify(items)


@app.route("/pdfs/<path:filename>")
def serve_pdf(filename):
    return send_from_directory(PDF_DIR, filename)


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


@app.route("/api/quiz/submit", methods=["POST"])
def api_quiz_submit():
    payload = request.get_json(force=True)
    pid = payload.get("problem_id")
    answers = payload.get("answers", [])  # list of selected option indexes (or null)
    try:
        problem = get_problem(pid)
    except KeyError:
        return jsonify({"error": "Problem not found"}), 404
    if problem["judge"] != "quiz":
        return jsonify({"error": "Not a quiz problem"}), 400

    questions = problem["questions"]
    results = []
    correct = 0
    for i, q in enumerate(questions):
        picked = answers[i] if i < len(answers) else None
        ok = picked == q["answer"]
        if ok:
            correct += 1
        results.append({
            "n": i + 1,
            "picked": picked,
            "answer": q["answer"],
            "passed": ok,
        })
    score = round(correct * 100.0 / len(questions)) if questions else 0
    return jsonify({
        "judge": "quiz",
        "passed": correct == len(questions),
        "correct": correct,
        "total": len(questions),
        "score": score,
        "results": results,
    })


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
