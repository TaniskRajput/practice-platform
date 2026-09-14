/* PracticeCode frontend */

const CM_MODES = {
  java: "text/x-java",
  cpp: "text/x-c++src",
  sql: "text/x-sql",
  javascript: "javascript",
};
const LANG_LABELS = {
  java: "Java",
  cpp: "C++",
  sql: "MySQL-ish (SQLite)",
  javascript: "JavaScript",
};

let problems = [];
let pdfs = [];
let current = null; // full problem payload
let editor = null;
let currentLang = null;
let previewTimer = null;
let judgePending = null; // {resolve} for browser judge
let currentUser = null; // {id, username, email} or null
let userSolved = {}; // {problem_id: true}
let userSubmissions = []; // all submissions for current user

const $ = (id) => document.getElementById(id);

/* ============================================================== */
/* AUTH & USER MANAGEMENT */
/* ============================================================== */

const auth = {
  async checkAuth() {
    const res = await fetch("/api/auth/me");
    const data = await res.json();
    currentUser = data.user;
    return currentUser;
  },

  async register(username, email, password) {
    const res = await fetch("/api/auth/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, email, password }),
    });
    if (res.ok) {
      currentUser = await res.json();
      return true;
    }
    return false;
  },

  async login(email, password) {
    const res = await fetch("/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
    if (res.ok) {
      currentUser = await res.json();
      return true;
    }
    return false;
  },

  async logout() {
    await fetch("/api/auth/logout", { method: "POST" });
    currentUser = null;
    closeAuthModal();
  },
};

function openAuthModal(isRegister = false) {
  const modal = $("auth-modal");
  const form = $("auth-form");
  const title = $("auth-title");
  const toggleText = $("auth-toggle-text");
  const toggleLink = $("auth-toggle-link");
  const usernameGroup = $("username-group");

  if (isRegister) {
    title.textContent = "Register";
    toggleText.textContent = "Already have an account?";
    toggleLink.textContent = "Login";
    usernameGroup.classList.remove("hidden");
    $("auth-submit").textContent = "Register";
  } else {
    title.textContent = "Login";
    toggleText.textContent = "Don't have an account?";
    toggleLink.textContent = "Register";
    usernameGroup.classList.add("hidden");
    $("auth-submit").textContent = "Login";
  }

  form.dataset.mode = isRegister ? "register" : "login";
  $("auth-error").classList.add("hidden");
  modal.classList.remove("hidden");
  $("auth-email").focus();
}

function closeAuthModal() {
  $("auth-modal").classList.add("hidden");
}

function updateUserMenu() {
  const loginBtn = $("btn-login");
  const userMenu = $("user-menu");
  const userName = $("user-name");

  if (currentUser) {
    loginBtn.classList.add("hidden");
    userMenu.classList.remove("hidden");
    userName.textContent = `Hi, ${currentUser.username}!`;
  } else {
    loginBtn.classList.remove("hidden");
    userMenu.classList.add("hidden");
  }
}

async function loadUserProgress() {
  if (!currentUser) return;

  try {
    const res = await fetch("/api/user/progress");
    if (res.ok) {
      const data = await res.json();
      userSolved = data.solved.reduce((o, id) => ({ ...o, [id]: true }), {});
      userSubmissions = data.submissions;
    }
  } catch (e) {
    console.error("Failed to load progress:", e);
  }
}

/* ============================================================== */
/* localStorage helpers */
/* ============================================================== */
const store = {
  getSolved() {
    if (currentUser) return userSolved; // Use server data if logged in
    try {
      return JSON.parse(localStorage.getItem("pc_solved") || "{}");
    } catch {
      return {};
    }
  },
  setSolved(pid) {
    if (currentUser) {
      userSolved[pid] = true;
    } else {
      const s = this.getSolved();
      s[pid] = true;
      localStorage.setItem("pc_solved", JSON.stringify(s));
    }
  },
  solvedCount() {
    return Object.keys(this.getSolved()).length;
  },

  async getCode(pid, lang) {
    if (currentUser) {
      const res = await fetch(`/api/user/code/${pid}/${lang}`);
      if (res.ok) {
        const data = await res.json();
        return data.code || null;
      }
    }
    return localStorage.getItem(`pc_code_${pid}_${lang}`) || null;
  },

  setCode(pid, lang, code) {
    localStorage.setItem(`pc_code_${pid}_${lang}`, code);
    if (currentUser) {
      fetch(`/api/user/code/${pid}/${lang}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code }),
      }).catch((e) => console.error("Failed to save code:", e));
    }
  },

  getLang(pid) {
    return localStorage.getItem(`pc_lang_${pid}`) || null;
  },
  setLang(pid, lang) {
    localStorage.setItem(`pc_lang_${pid}`, lang);
  },

  getSubs(pid) {
    if (currentUser) {
      return userSubmissions.filter((s) => s.problem_id === pid);
    }
    try {
      return JSON.parse(localStorage.getItem(`pc_subs_${pid}`) || "[]");
    } catch {
      return [];
    }
  },

  addSub(pid, sub) {
    if (currentUser) {
      userSubmissions.unshift({ ...sub, problem_id: pid });
    } else {
      const subs = this.getSubs(pid);
      subs.unshift(sub);
      localStorage.setItem(`pc_subs_${pid}`, JSON.stringify(subs.slice(0, 30)));
    }
  },
};

/* ---------------- Problem list ---------------- */
let listFilter = "all"; // "all" | "pseudo"

async function loadProblems() {
  const res = await fetch("/api/problems");
  problems = await res.json();
  renderList();
}

function renderList() {
  const solved = store.getSolved();
  const shown = problems.filter(
    (p) => listFilter === "all" || p.judge === "quiz",
  );
  let html = "";
  shown.forEach((p, i) => {
    if (i === 0 && listFilter === "pseudo") {
      html += `<tr class="list-section-row"><td colspan="5" class="list-section">Pseudocode Quizzes</td></tr>`;
    }
    const diffClass = p.difficulty.toLowerCase();
    const topics = p.topics
      .map((t) => `<span class="topic-chip">${t}</span>`)
      .join("");
    html += `<tr data-id="${p.id}">
      <td>${solved[p.id] ? '<span class="check">&#10003;</span>' : '<span class="check" style="color:var(--text-dim)">&mdash;</span>'}</td>
      <td style="color:var(--text-dim)">${p.id}</td>
      <td><b>${p.title}</b></td>
      <td><span class="diff ${diffClass}">${p.difficulty}</span></td>
      <td>${topics}</td>
    </tr>`;
  });
  $("problem-rows").innerHTML = html;
  document.querySelectorAll("#problem-rows tr").forEach((tr) => {
    tr.addEventListener("click", () => openProblem(+tr.dataset.id));
  });
  $("solved-counter").innerHTML =
    `Solved <b>${store.solvedCount()}</b>/${problems.length}`;
}

/* ---------------- Problem view ---------------- */
async function openProblem(pid) {
  const res = await fetch(`/api/problems/${pid}`);
  current = await res.json();

  $("list-view").classList.add("hidden");
  $("problem-view").classList.remove("hidden");
  $("ph-number").textContent = current.id + ".";
  $("ph-title").textContent = current.title;
  $("ph-difficulty").textContent = current.difficulty;
  $("ph-difficulty").className = "diff " + current.difficulty.toLowerCase();
  $("ph-topics").textContent = current.topics.join(" · ");
  $("results").innerHTML = "";

  if (current.judge === "quiz") {
    renderQuiz();
    return;
  }

  // language selector
  const sel = $("lang-select");
  sel.innerHTML = current.languages
    .map((l) => `<option value="${l}">${LANG_LABELS[l] || l}</option>`)
    .join("");
  currentLang = store.getLang(current.id) || current.languages[0];
  sel.value = currentLang;

  // description tab
  $("tab-desc").innerHTML = current.description;
  // hint tab
  $("tab-hint").innerHTML =
    `<h3>Hint</h3><div class="hint-box">${current.hint}</div>`;

  buildTabs();
  initEditor();

  if (current.judge === "browser") renderPreview();
  if (current.languages[0] === "sql") renderDataset();
  switchTab(current.judge === "browser" ? "preview" : "desc");
}

async function initEditor() {
  const saved = await store.getCode(current.id, currentLang);
  const boiler = current.boilerplate[currentLang] || "";
  if (!editor) {
    editor = CodeMirror($("editor"), {
      lineNumbers: true,
      theme: "material-darker",
      indentUnit: 4,
      tabSize: 4,
      extraKeys: {
        "Ctrl-Enter": () => runCode(),
        "Cmd-Enter": () => runCode(),
      },
    });
    editor.on("change", () => {
      store.setCode(current.id, currentLang, editor.getValue());
      if (current.judge === "browser") schedulePreview();
    });
  }
  editor.setOption("mode", CM_MODES[currentLang]);
  editor.setValue(saved !== null ? saved : boiler);
}

function buildTabs() {
  const tabs = [
    { id: "desc", label: "Description" },
    ...(current.languages[0] === "sql"
      ? [{ id: "dataset", label: "Schema & Data" }]
      : []),
    ...(current.judge === "browser"
      ? [{ id: "preview", label: "Live Preview" }]
      : []),
    { id: "hint", label: "Hint" },
    { id: "subs", label: "Submissions" },
  ];
  $("desc-tabs").innerHTML = tabs
    .map(
      (t, i) =>
        `<div class="tab${i === 0 ? " active" : ""}" data-tab="${t.id}">${t.label}</div>`,
    )
    .join("");
  document.querySelectorAll("#desc-tabs .tab").forEach((el) => {
    el.addEventListener("click", () => switchTab(el.dataset.tab));
  });
}

function switchTab(tabId) {
  document.querySelectorAll("#desc-tabs .tab").forEach((el) => {
    el.classList.toggle("active", el.dataset.tab === tabId);
  });
  ["desc", "hint", "subs", "preview", "dataset"].forEach((t) => {
    $("tab-" + t).classList.toggle("hidden", t !== tabId);
  });
  if (tabId === "subs") renderSubmissions();
  if (tabId === "preview" && current && current.judge === "browser")
    renderPreview();
}

function renderSubmissions() {
  const subs = store.getSubs(current.id);
  if (!subs.length) {
    $("tab-subs").innerHTML =
      `<p style="color:var(--text-dim)">No submissions yet. Hit <b>Run</b> to test samples or <b>Submit</b> for the full judge.</p>`;
    return;
  }
  $("tab-subs").innerHTML = subs
    .map(
      (s) => `<div class="sub-item">
      <span class="sub-verdict ${s.passed ? "ac" : "wa"}">${s.passed ? "Accepted" : "Wrong Answer"}</span>
      <span>${s.detail}</span>
      <span class="sub-meta">${LANG_LABELS[s.lang] || s.lang} · ${new Date(s.time).toLocaleString()}</span>
    </div>`,
    )
    .join("");
}

/* ---------------- Editor ---------------- */
async function initEditor() {
  const saved = await store.getCode(current.id, currentLang);
  const boiler = current.boilerplate[currentLang] || "";
  if (!editor) {
    editor = CodeMirror($("editor"), {
      lineNumbers: true,
      theme: "material-darker",
      indentUnit: 4,
      tabSize: 4,
      extraKeys: {
        "Ctrl-Enter": () => runCode(),
        "Cmd-Enter": () => runCode(),
      },
    });
    editor.on("change", () => {
      store.setCode(current.id, currentLang, editor.getValue());
      if (current.judge === "browser") schedulePreview();
    });
  }
  editor.setOption("mode", CM_MODES[currentLang]);
  editor.setValue(saved !== null ? saved : boiler);
}

function resetCode() {
  if (!confirm("Reset code to the original boilerplate?")) return;
  editor.setValue(current.boilerplate[currentLang] || "");
  store.setCode(current.id, currentLang, editor.getValue());
}

/* ---------------- Auto-structure (formatting) ---------------- */

/* Brace-based re-indenter for Java / C++ / JavaScript.
   Aware of string literals, char literals, and // and block comments. */
function formatBraces(code) {
  const IND = "    ";
  let out = "";
  let depth = 0;
  let paren = 0; // parens on the current statement — `for (…;…;…)` must not split
  let buf = "";
  let lastKind = "nl"; // what caused the last flush: "stmt" or "nl"
  const blocks = []; // per open block: saved paren depth + whether opener was `do`
  const n = code.length;
  let i = 0;

  const flush = (kind) => {
    const t = buf.trim();
    if (!t) {
      buf = "";
      lastKind = kind;
      return;
    }
    if (t.startsWith("//") && lastKind === "stmt" && out.length) {
      // trailing comment after a statement — keep it on the same line
      out = out.replace(/\n$/, " " + t + "\n");
    } else {
      out += IND.repeat(Math.max(depth, 0)) + t + "\n";
    }
    buf = "";
    lastKind = kind;
  };

  while (i < n) {
    const c = code[i];

    // string / char / template literals — copied verbatim, braces inside ignored
    if (c === '"' || c === "'" || c === "`") {
      const q = c;
      buf += c;
      i++;
      while (i < n) {
        buf += code[i];
        if (code[i] === "\\") {
          buf += code[i + 1] ?? "";
          i += 2;
          continue;
        }
        i++;
        if (code[i - 1] === q) break;
      }
      continue;
    }

    // line comments
    if (c === "/" && code[i + 1] === "/") {
      const j = code.indexOf("\n", i);
      buf += j === -1 ? code.slice(i) : code.slice(i, j);
      i = j === -1 ? n : j;
      continue;
    }

    // block comments — re-indented on their own lines
    if (c === "/" && code[i + 1] === "*") {
      const j = code.indexOf("*/", i);
      const seg = code.slice(i, j === -1 ? n : j + 2);
      flush("stmt");
      for (const l of seg.split("\n")) {
        const t = l.trim();
        if (t) out += IND.repeat(Math.max(depth, 0)) + t + "\n";
      }
      lastKind = "stmt";
      i = j === -1 ? n : j + 2;
      continue;
    }

    if (c === "(") {
      paren++;
      buf += c;
      i++;
      continue;
    }
    if (c === ")") {
      paren = Math.max(paren - 1, 0);
      buf += c;
      i++;
      continue;
    }

    if (c === "{") {
      const isDo = buf.trim() === "do";
      buf = buf.replace(/\s+$/, "") + " {";
      flush("stmt");
      blocks.push({ paren, isDo });
      paren = 0;
      depth++;
      i++;
      continue;
    }

    if (c === "}") {
      const frame = blocks.pop() ?? { paren: 0, isDo: false };
      flush("stmt");
      depth = Math.max(depth - 1, 0);
      paren = frame.paren;
      // "} else {", "} catch (...) {", "} finally {" always join;
      // "} while (...);" joins only when closing a `do` block
      let j = i + 1;
      while (j < n && /[ \t]/.test(code[j])) j++;
      const m = code.slice(j, j + 8).match(/^(else|catch|finally|while)\b/);
      if (m && (m[1] !== "while" || frame.isDo)) {
        let k = j + m[1].length;
        let cond = "";
        while (k < n && code[k] !== "{" && code[k] !== ";") {
          cond += code[k];
          k++;
        }
        if (code[k] === "{") {
          buf =
            ("} " + m[1] + cond).replace(/\s+/g, " ").replace(/\s+$/, "") +
            " {";
          flush("stmt");
          depth++;
          i = k + 1;
          continue;
        }
        buf = ("} " + m[1] + cond).replace(/\s+/g, " ") + ";";
        flush("stmt");
        i = k + 1;
        continue;
      }
      // `});` / `}))` — closers after a nested block (arrow fn in a call, etc.)
      let k2 = j;
      while (k2 < n && /[ \t\n]/.test(code[k2])) k2++;
      if (code[k2] === ")") {
        let suffix = "";
        while (k2 < n && code[k2] === ")") {
          suffix += ")";
          k2++;
        }
        if (code[k2] === ";") {
          suffix += ";";
          k2++;
        }
        buf = "}" + suffix;
        flush("stmt");
        i = k2;
        continue;
      }
      buf = "}";
      flush("stmt");
      i++;
      continue;
    }

    if (c === ";") {
      buf += paren > 0 ? "; " : ";";
      if (paren === 0) flush("stmt");
      i++;
      continue;
    }

    if (c === "\n") {
      flush("nl");
      i++;
      continue;
    }

    buf += c;
    i++;
  }
  flush("nl");
  return out.replace(/\n{3,}/g, "\n\n").trim() + "\n";
}

/* SQL formatter: uppercases keywords, puts each major clause on its own line,
   breaks top-level commas (SELECT/ORDER BY lists) one per line, and indents
   subqueries by parenthesis depth. String literals and comments are preserved. */
function formatSql(code) {
  const IND = "    ";
  const CLAUSE =
    /^(SELECT|FROM|WHERE|GROUP BY|HAVING|ORDER BY|LIMIT|LEFT JOIN|RIGHT JOIN|INNER JOIN|FULL JOIN|CROSS JOIN|JOIN|UNION ALL|UNION)\b/;

  // protect literals and comments from rewriting
  const store = [];
  const protect = (re) =>
    code.replace(re, (m) => {
      store.push(m);
      return `\u0000${store.length - 1}\u0000`;
    });
  let s = protect(/'(?:[^']|'')*'/g);
  s = protect(/--[^\n]*/g);
  s = protect(/\/\*[\s\S]*?\*\//g);

  // collapse whitespace, uppercase keywords
  s = s.replace(/\s+/g, " ");
  s = s.replace(
    /\b(select|from|where|group\s+by|having|order\s+by|limit|inner\s+join|left\s+join|right\s+join|full\s+join|cross\s+join|join|on|as|and|or|not|in|is|null|like|between|distinct|case|when|then|else|end|asc|desc|union\s+all|union|count|sum|avg|min|max|cast|coalesce|strftime|substring|round|abs)\b/gi,
    (m) => m.toUpperCase(),
  );

  // newline before major clauses
  s = s.replace(
    /\b(SELECT|FROM|WHERE|GROUP BY|HAVING|ORDER BY|LIMIT|LEFT JOIN|RIGHT JOIN|INNER JOIN|FULL JOIN|CROSS JOIN|JOIN|UNION ALL|UNION)\b/g,
    "\n$1",
  );
  // newline after top-level commas (column / order-by lists)
  let tmp = "";
  let d = 0;
  for (const ch of s) {
    if (ch === "(") d++;
    if (ch === ")") d = Math.max(d - 1, 0);
    if (ch === "," && d === 0) {
      tmp += ",\n";
      continue;
    }
    tmp += ch;
  }
  s = tmp;

  // indent: clause lines at paren depth, continuations one level deeper
  const outLines = [];
  let depth = 0;
  for (let line of s.split("\n")) {
    line = line.trim();
    if (!line) continue;
    const base = Math.max(depth + (CLAUSE.test(line) ? 0 : 1), 0);
    outLines.push(IND.repeat(base) + line);
    for (const ch of line) {
      if (ch === "(") depth++;
      else if (ch === ")") depth = Math.max(depth - 1, 0);
    }
  }

  let out = outLines.join("\n");
  out = out.replace(/\u0000(\d+)\u0000/g, (_, idx) => store[+idx]);
  return out.trim() + "\n";
}

function formatCode() {
  if (!editor || !current) return;
  const code = editor.getValue();
  let formatted;
  try {
    formatted = currentLang === "sql" ? formatSql(code) : formatBraces(code);
  } catch (e) {
    return; // never destroy user code on a formatter bug
  }
  if (formatted !== code) {
    editor.setValue(formatted); // change event persists code + refreshes preview
  }
}

/* ---------------- Run / Submit ---------------- */
async function runCode() {
  await judge(false);
}
async function submitCode() {
  await judge(true);
}

async function judge(submit) {
  if (!current) return;
  setButtonsBusy(true);
  $("results").innerHTML =
    `<div class="results-header"><span class="verdict pending">${submit ? "Judging…" : "Running…"}</span></div>`;
  $("results").classList.remove("hidden");
  $("results").style.display = "block";

  try {
    if (current.judge === "browser") {
      const results = await browserJudge(submit);
      renderBrowserResults(results, submit);
    } else {
      const payload = {
        problem_id: current.id,
        language: currentLang,
        code: editor.getValue(),
      };
      const res = await fetch(submit ? "/api/submit" : "/api/run", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      const data = await res.json();
      renderServerResults(data, submit);
    }
  } catch (e) {
    $("results").innerHTML =
      `<div class="results-header"><span class="verdict wa">Error</span></div><pre class="error-pre">${escapeHtml(String(e))}</pre>`;
  } finally {
    setButtonsBusy(false);
  }
}

function setButtonsBusy(busy) {
  $("btn-run").disabled = busy;
  $("btn-submit").disabled = busy;
}

/* ---------------- Server results rendering ---------------- */
function renderServerResults(data, submit) {
  const box = $("results");

  if (data.error) {
    box.innerHTML = `<div class="results-header"><span class="verdict wa">Error</span></div><pre class="error-pre">${escapeHtml(data.error)}</pre>`;
    return;
  }
  if (data.judge === "compile") {
    box.innerHTML = `<div class="results-header"><span class="verdict ce">Compilation Error</span></div><pre class="error-pre">${escapeHtml(data.compile_error)}</pre>`;
    recordSubmission(false, "Compilation Error", submit);
    return;
  }
  if (data.judge === "runtime") {
    box.innerHTML = `<div class="results-header"><span class="verdict rte">Runtime Error</span></div><pre class="error-pre">${escapeHtml(data.runtime_error)}</pre>`;
    recordSubmission(false, "Runtime Error", submit);
    return;
  }
  if (data.judge === "timeout") {
    box.innerHTML = `<div class="results-header"><span class="verdict tle">Time Limit Exceeded</span></div>`;
    recordSubmission(false, "Time Limit Exceeded", submit);
    return;
  }

  // SQL results
  if (data.judge === "sql") {
    const cases = data.results
      .map((r) => {
        if (r.error) {
          return `<div class="test-case">
            <div class="test-head"><span class="tc-badge fail">ERROR</span> ${escapeHtml(r.database)}</div>
            <pre class="error-pre">${escapeHtml(r.error)}</pre>
          </div>`;
        }
        return `<div class="test-case">
          <div class="test-head"><span class="tc-badge ${r.passed ? "pass" : "fail"}">${r.passed ? "PASSED" : "WRONG"}</span>
            ${escapeHtml(r.database)} ${r.hidden ? '<span class="tc-badge hidden-tag">hidden</span>' : ""}</div>
          <div class="sql-tables">
            <div><h4>Your output</h4><pre class="${r.passed ? "" : "wrong"}">${escapeHtml(r.actual)}</pre></div>
            <div><h4>Expected</h4><pre>${escapeHtml(r.expected)}</pre></div>
          </div>
        </div>`;
      })
      .join("");
    box.innerHTML = `<div class="results-header">
        <span class="verdict ${data.passed ? "ac" : "wa"}">${data.passed ? "Accepted" : "Wrong Answer"}</span>
        <span style="color:var(--text-dim);font-weight:400">${data.passed_count}/${data.total} datasets passed</span>
      </div>${cases}`;
    recordSubmission(
      data.passed,
      `${data.passed_count}/${data.total} datasets`,
      submit,
    );
    return;
  }

  // Code results (java/cpp)
  const cases = data.results
    .map((r) => {
      if (r.hidden) {
        return `<div class="test-case hidden-case">
          <div class="test-head"><span class="tc-badge ${r.passed ? "pass" : "fail"}">${r.passed ? "PASSED" : "FAILED"}</span>
            Hidden test case</div>
        </div>`;
      }
      return `<div class="test-case">
        <div class="test-head"><span class="tc-badge ${r.passed ? "pass" : "fail"}">${r.passed ? "PASSED" : "WRONG"}</span>
          Test case ${r.index + 1}</div>
        <div class="tc-io">
          <div><div class="io-label">Input (matrix)</div><pre>${escapeHtml(r.input)}</pre></div>
          <div>
            <div class="io-label">Expected</div><pre>${escapeHtml(r.expected)}</pre>
            <div class="io-label" style="margin-top:8px">Your output</div><pre class="${r.passed ? "" : "wrong"}">${escapeHtml(r.actual)}</pre>
          </div>
        </div>
      </div>`;
    })
    .join("");
  box.innerHTML = `<div class="results-header">
      <span class="verdict ${data.passed ? "ac" : "wa"}">${data.passed ? "Accepted" : "Wrong Answer"}</span>
      <span style="color:var(--text-dim);font-weight:400">${data.passed_count}/${data.total} test cases passed</span>
    </div>${cases}`;
  recordSubmission(
    data.passed,
    `${data.passed_count}/${data.total} test cases`,
    submit,
  );
}

function recordSubmission(passed, detail, submit) {
  if (!submit) return;
  if (passed) store.setSolved(current.id);
  const sub = { time: Date.now(), passed, detail, lang: currentLang };
  store.addSub(current.id, sub);
  renderList();

  // Also send to server if logged in
  if (currentUser) {
    fetch("/api/record-submission", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        problem_id: current.id,
        language: currentLang,
        code: editor.getValue(),
        passed: passed,
        verdict: detail,
      }),
    }).catch((e) => console.error("Failed to record submission:", e));
  }
}

/* ---------------- Browser judge (JS/DOM) ---------------- */
function setFrameHtml(frame, html) {
  if (frame.dataset.blobUrl) URL.revokeObjectURL(frame.dataset.blobUrl);
  const blob = new Blob([html], { type: "text/html" });
  const url = URL.createObjectURL(blob);
  frame.dataset.blobUrl = url;
  frame.src = url;
}

function counterPreviewDoc(userCode, tests) {
  const style =
    current.browserStyle ||
    `
    body { font-family: -apple-system, "Segoe UI", sans-serif; display: flex; justify-content: center; padding-top: 60px; background: #fafafa; }
    .counter-container { text-align: center; background: #fff; border: 1px solid #ddd; border-radius: 14px; padding: 34px 44px; box-shadow: 0 4px 18px rgba(0,0,0,.08); }
    #count { font-size: 56px; margin-bottom: 18px; color: #222; }
    .btn-group { display: flex; gap: 12px; justify-content: center; }
    button { width: 52px; height: 52px; font-size: 24px; border-radius: 10px; border: 1px solid #ccc; cursor: pointer; background: #f3f3f3; }
    button:hover { background: #e8e8e8; }
    #status-msg { margin-top: 18px; font-size: 14px; color: #c0392b; min-height: 20px; }
  `;
  const safeCode = userCode.replace(/<\/script/gi, "<\\/script");
  let html = `<!DOCTYPE html><html><head><style>${style}</style></head><body>`;
  html += current.browserHtml;
  html += `<script>window.onerror = function(msg){ parent.postMessage({type:'judge-runtime-error', error:String(msg)}, '*'); };<\/script>`;
  html += `<script>${safeCode}<\/script>`;
  if (tests) {
    const runner = `
      (function () {
        var results = [];
        var tests = ${JSON.stringify(tests)};

        function styleValue(el, prop) {
          if (!el) return '(missing)';
          if (prop === 'className') return el.className;
          if (prop === 'disabled') return String(el.disabled);
          return (el.style[prop] || '').toLowerCase();
        }

        function applyStep(s) {
          if (s.click) {
            document.getElementById(s.click).click();
          } else if (s.type) {
            var el = document.getElementById(s.type);
            el.value = s.value;
            el.dispatchEvent(new Event('input', { bubbles: true }));
          } else if (s.select) {
            var sel = document.getElementById(s.select.id);
            sel.value = s.select.value;
            sel.dispatchEvent(new Event('change', { bubbles: true }));
          } else if (s.rowBtn) {
            var rows = document.querySelectorAll('#cartBody tr');
            var btns = rows[s.rowBtn.row].querySelectorAll('button.btn');
            btns[s.rowBtn.which].click();
          }
        }

        function checkExpect(t, e) {
          var ok = true;
          var parts = [];
          if (e.count !== undefined) {
            var c = document.getElementById('count').textContent.trim();
            ok = ok && (c === e.count);
            parts.push('count = ' + c + ' (expected ' + e.count + ')');
          }
          if (e.msg !== undefined) {
            var m = document.getElementById('status-msg').textContent.trim();
            ok = ok && (m === e.msg);
            parts.push('status = "' + m + '" (expected "' + e.msg + '")');
          }
          if (e.color !== undefined) {
            var msgEl = document.getElementById('feedback-msg');
            var color = (msgEl.style.color || '').toLowerCase();
            ok = ok && (color === e.color);
            parts.push('msg = "' + msgEl.textContent.trim() + '" color = ' + color +
              ' (expected "' + e.msg + '" ' + e.color + ')');
          }
          if (e.text !== undefined) {
            var el = document.getElementById(e.text.id);
            var v = el.textContent.trim();
            ok = ok && (v === e.text.value);
            parts.push('#' + e.text.id + ' = "' + v + '" (expected "' + e.text.value + '")');
          }
          if (e.qty !== undefined) {
            var rows2 = document.querySelectorAll('#cartBody tr');
            var q = rows2[e.qty.row].querySelector('.qty').textContent.trim();
            ok = ok && (q === e.qty.value);
            parts.push('row ' + (e.qty.row + 1) + ' qty = ' + q + ' (expected ' + e.qty.value + ')');
          }
          if (e.subtotal !== undefined) {
            var rows3 = document.querySelectorAll('#cartBody tr');
            var st = rows3[e.subtotal.row].querySelector('.subtotal').textContent.trim();
            ok = ok && (st === e.subtotal.value);
            parts.push('row ' + (e.subtotal.row + 1) + ' subtotal = "' + st + '" (expected "' + e.subtotal.value + '")');
          }
          if (e.style !== undefined) {
            var target = document.querySelector(e.style.selector);
            var actual = styleValue(target, e.style.property);
            ok = ok && (actual === e.style.value);
            parts.push(e.style.selector + ' ' + e.style.property + ' = ' + actual +
              ' (expected ' + e.style.value + ')');
          }
          if (e.style2 !== undefined) {
            var target2 = document.querySelector(e.style2.selector);
            var actual2 = styleValue(target2, e.style2.property);
            ok = ok && (actual2 === e.style2.value);
            parts.push(e.style2.selector + ' ' + e.style2.property + ' = ' + actual2 +
              ' (expected ' + e.style2.value + ')');
          }
          if (e.storage !== undefined) {
            var stored;
            try { stored = window.localStorage.getItem(e.storage.key); } catch (err) { stored = '(unavailable)'; }
            stored = stored === null ? 'null' : String(stored);
            ok = ok && (stored === e.storage.value);
            parts.push('localStorage.' + e.storage.key + ' = ' + stored +
              ' (expected ' + e.storage.value + ')');
          }
          if (e.visible !== undefined) {
            var vis = [];
            var hid = [];
            document.querySelectorAll('.product li').forEach(function (li) {
              (li.style.display === 'none' ? hid : vis).push(li.textContent.trim());
            });
            var same = vis.length === e.visible.length &&
              e.visible.every(function (x) { return vis.indexOf(x) !== -1; }) &&
              hid.length === e.hidden.length &&
              e.hidden.every(function (x) { return hid.indexOf(x) !== -1; });
            ok = ok && same;
            parts.push('visible = [' + vis.join(', ') + '] (expected [' + e.visible.join(', ') + '])');
          }
          return { ok: ok, actual: parts.join('; ') };
        }

        tests.forEach(function (t) {
          try {
            t.steps.forEach(applyStep);
            var r = checkExpect(t, t.expect);
            var expectedParts = [];
            if (t.expect.count !== undefined) expectedParts.push('count = ' + t.expect.count);
            if (t.expect.msg !== undefined) expectedParts.push('status = "' + t.expect.msg + '"');
            if (t.expect.color !== undefined) expectedParts.push('msg = "' + t.expect.msg + '" color = ' + t.expect.color);
            if (t.expect.text !== undefined) expectedParts.push('#' + t.expect.text.id + ' = "' + t.expect.text.value + '"');
            if (t.expect.qty !== undefined) expectedParts.push('row ' + (t.expect.qty.row + 1) + ' qty = ' + t.expect.qty.value);
            if (t.expect.subtotal !== undefined) expectedParts.push('row ' + (t.expect.subtotal.row + 1) + ' subtotal = "' + t.expect.subtotal.value + '"');
            if (t.expect.style !== undefined) expectedParts.push(t.expect.style.selector + ' ' + t.expect.style.property + ' = ' + t.expect.style.value);
            if (t.expect.style2 !== undefined) expectedParts.push(t.expect.style2.selector + ' ' + t.expect.style2.property + ' = ' + t.expect.style2.value);
            if (t.expect.storage !== undefined) expectedParts.push('localStorage.' + t.expect.storage.key + ' = ' + t.expect.storage.value);
            if (t.expect.visible !== undefined) expectedParts.push('visible = [' + t.expect.visible.join(', ') + ']');
            results.push({ name: t.name, hidden: t.hidden, pass: r.ok,
              expected: expectedParts.join('; '),
              actual: r.actual });
          } catch (e) {
            results.push({ name: t.name, hidden: t.hidden, pass: false,
              expected: 'no error', actual: 'Error: ' + e.message });
          }
        });
        parent.postMessage({ type: 'judge-result', results: results }, '*');
      })();
    `;
    html += `<script>${runner}<\/script>`;
  }
  html += `</body></html>`;
  return html;
}

function browserJudge(submit) {
  const tests = current.browserTests.filter((t) => submit || !t.hidden);
  return new Promise((resolve) => {
    const frame = $("judge-frame");
    const timer = setTimeout(() => {
      judgePending = null;
      resolve(
        tests.map((t) => ({
          name: t.name,
          hidden: t.hidden,
          pass: false,
          expected: t.name,
          actual:
            "Timed out — check your code for errors (e.g. a runtime error during initialization)",
        })),
      );
    }, 5000);

    judgePending = (msg) => {
      clearTimeout(timer);
      judgePending = null;
      if (msg.type === "judge-runtime-error") {
        resolve(
          tests.map((t) => ({
            name: t.name,
            hidden: t.hidden,
            pass: false,
            expected: t.name,
            actual: `Runtime error: ${msg.error}`,
          })),
        );
      } else {
        resolve(msg.results);
      }
    };
    setFrameHtml(frame, counterPreviewDoc(editor.getValue(), tests));
  });
}

window.addEventListener("message", (e) => {
  if (
    e.data &&
    (e.data.type === "judge-result" || e.data.type === "judge-runtime-error")
  ) {
    if (judgePending) judgePending(e.data);
  }
});

function renderBrowserResults(results, submit) {
  const passedCount = results.filter((r) => r.pass).length;
  const passed = passedCount === results.length;
  const cases = results
    .map(
      (r) => `<div class="test-case">
      <div class="test-head"><span class="tc-badge ${r.pass ? "pass" : "fail"}">${r.pass ? "PASSED" : "FAILED"}</span>
        ${escapeHtml(r.name)} ${r.hidden ? '<span class="tc-badge hidden-tag">hidden</span>' : ""}</div>
      ${
        r.pass
          ? ""
          : `<div class="tc-io">
        <div><div class="io-label">Expected</div><pre>${escapeHtml(r.expected)}</pre></div>
        <div><div class="io-label">Your output</div><pre class="wrong">${escapeHtml(r.actual)}</pre></div>
      </div>`
      }
    </div>`,
    )
    .join("");
  $("results").innerHTML = `<div class="results-header">
      <span class="verdict ${passed ? "ac" : "wa"}">${passed ? "Accepted" : "Wrong Answer"}</span>
      <span style="color:var(--text-dim);font-weight:400">${passedCount}/${results.length} test cases passed</span>
    </div>${cases}`;
  recordSubmission(
    passed,
    `${passedCount}/${results.length} test cases`,
    submit,
  );
}

/* ---------------- MCQ Quiz mode ---------------- */
function quizSelections() {
  try {
    return JSON.parse(localStorage.getItem(`pc_quiz_${current.id}`) || "[]");
  } catch {
    return [];
  }
}
function saveQuizSelections(sel) {
  localStorage.setItem(`pc_quiz_${current.id}`, JSON.stringify(sel));
}

function renderQuiz() {
  // quiz mode replaces the editor panel with the question list
  $("editor-panel-quiz").classList.remove("hidden");
  $("editor-panel").classList.add("hidden");
  $("list-view").classList.add("hidden");
  $("problem-view").classList.remove("hidden");
  $("ph-number").textContent = current.id + ".";
  $("ph-title").textContent = current.title;
  $("ph-difficulty").textContent = current.difficulty;
  $("ph-difficulty").className = "diff " + current.difficulty.toLowerCase();
  $("ph-topics").textContent = current.topics.join(" · ");
  $("results").innerHTML = "";

  const saved = quizSelections();
  const LETTERS = ["A", "B", "C", "D", "E", "F"];
  $("quiz-questions").innerHTML = current.questions
    .map((q) => {
      const picked = saved[q.n - 1];
      const opts = q.options
        .map((o, oi) => {
          const checked = picked === oi ? " checked" : "";
          return `<label class="quiz-option${checked ? " picked" : ""}">
            <input type="radio" name="quiz-q${q.n}" value="${oi}"${checked}>
            <span class="quiz-letter">${LETTERS[oi]}</span>
            <span class="quiz-opt-text">${o}</span>
          </label>`;
        })
        .join("");
      return `<div class="quiz-question" data-n="${q.n}">
        <div class="quiz-q-head"><span class="quiz-q-num">Q${q.n}</span></div>
        <div class="quiz-q-text">${q.q}</div>
        <div class="quiz-opts">${opts}</div>
      </div>`;
    })
    .join("");
  updateQuizProgress();

  document
    .querySelectorAll("#quiz-questions .quiz-option input")
    .forEach((inp) => {
      inp.addEventListener("change", () => {
        const n = +inp.name.replace("quiz-q", "");
        const sel = quizSelections();
        sel[n - 1] = +inp.value;
        saveQuizSelections(sel);
        // re-mark picked styling within this question
        document
          .querySelectorAll(`#quiz-questions [data-n="${n}"] .quiz-option`)
          .forEach((lab) => {
            lab.classList.toggle("picked", lab.querySelector("input").checked);
          });
        updateQuizProgress();
      });
    });

  $("tab-desc").innerHTML = current.description;
  $("tab-hint").innerHTML =
    `<h3>Hint</h3><div class="hint-box">${current.hint}</div>`;
  buildTabs();
  switchTab("desc");
}

function updateQuizProgress() {
  const sel = quizSelections();
  const answered = current.questions.filter(
    (q) => sel[q.n - 1] !== undefined && sel[q.n - 1] !== null,
  ).length;
  $("quiz-progress").textContent =
    `${answered}/${current.questions.length} answered`;
  $("quiz-submit").disabled = answered < current.questions.length;
  $("quiz-submit").title =
    answered < current.questions.length
      ? "Answer every question to submit"
      : "";
}

function clearQuiz() {
  if (!confirm("Clear all selected answers for this quiz?")) return;
  saveQuizSelections([]);
  renderQuiz();
}

async function submitQuiz() {
  const sel = quizSelections();
  setButtonsBusy(true);
  $("results").innerHTML =
    `<div class="results-header"><span class="verdict pending">Grading…</span></div>`;
  try {
    const res = await fetch("/api/quiz/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ problem_id: current.id, answers: sel }),
    });
    const data = await res.json();
    renderQuizResults(data);
  } catch (e) {
    $("results").innerHTML =
      `<div class="results-header"><span class="verdict wa">Error</span></div><pre class="error-pre">${escapeHtml(String(e))}</pre>`;
  } finally {
    setButtonsBusy(false);
  }
}

function renderQuizResults(data) {
  if (data.error) {
    $("results").innerHTML =
      `<div class="results-header"><span class="verdict wa">Error</span></div><pre class="error-pre">${escapeHtml(data.error)}</pre>`;
    return;
  }
  const box = $("results");
  const summary = `<div class="results-header">
      <span class="verdict ${data.passed ? "ac" : "wa"}">${data.correct === data.total ? "Perfect Score" : "Quiz Graded"}</span>
      <span style="color:var(--text-dim);font-weight:400">${data.correct}/${data.total} correct (${data.score}%)</span>
    </div>`;
  const rows = data.results
    .filter((r) => !r.passed)
    .map((r) => {
      const q = current.questions[r.n - 1];
      const picked =
        r.picked === null || r.picked === undefined
          ? "— (no answer)"
          : `${"ABCDEF"[r.picked]}. ${q.options[r.picked]}`;
      const right = `${"ABCDEF"[r.answer]}. ${q.options[r.answer]}`;
      return `<div class="test-case">
        <div class="test-head"><span class="tc-badge fail">WRONG</span> Q${r.n}</div>
        <div class="quiz-review">
          <div class="quiz-review-row"><span class="io-label">Your answer</span><span class="quiz-review-text wrong">${escapeHtml(picked)}</span></div>
          <div class="quiz-review-row"><span class="io-label">Correct answer</span><span class="quiz-review-text">${escapeHtml(right)}</span></div>
        </div>
      </div>`;
    })
    .join("");
  box.innerHTML =
    summary +
    (rows ||
      `<p style="color:var(--text-dim)">All answers correct — nothing to review.</p>`);
  recordSubmission(data.passed, `${data.correct}/${data.total} correct`, true);
  box.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

/* ---------------- Live preview ---------------- */
function schedulePreview() {
  clearTimeout(previewTimer);
  previewTimer = setTimeout(renderPreview, 600);
}

function renderPreview() {
  if (!current || current.judge !== "browser") return;
  setFrameHtml($("preview-frame"), counterPreviewDoc(editor.getValue(), null));
}

/* ---------------- SQL dataset tab ---------------- */
function renderDataset() {
  const db = current.databases.find((d) => !d.hidden);
  // parse column names out of the CREATE TABLE statements in the schema
  const headersFor = (table) => {
    const m = (db.schema || "").match(
      new RegExp(`CREATE TABLE ${table}\\s*\\(([^;]+)\\)`, "i"),
    );
    if (!m) return [];
    return m[1]
      .split(",")
      .map((col) => col.trim().split(/\s+/)[0].replace(/"/g, ""))
      .filter((c) => !/^(PRIMARY|FOREIGN|UNIQUE|CHECK|CONSTRAINT)$/i.test(c));
  };
  const tables = Object.entries(db.seed)
    .map(([name, rows]) => {
      const headers = headersFor(name);
      return `<h3>${name}</h3>
        <table class="schema-table">
          <thead><tr>${headers.map((h) => `<th>${h}</th>`).join("")}</tr></thead>
          <tbody>${rows
            .map((r) => `<tr>${r.map((c) => `<td>${c}</td>`).join("")}</tr>`)
            .join("")}</tbody>
        </table>`;
    })
    .join("");
  $("tab-dataset").innerHTML = `<h3>${db.name} (SQLite)</h3>
    <p style="color:var(--text-dim)">Your query runs against this dataset when you press <b>Run</b>, and against this plus a hidden dataset when you press <b>Submit</b>.</p>
    ${tables}`;
}

/* ---------------- Utils ---------------- */
function escapeHtml(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

/* ---------------- PDF Resources ---------------- */
async function loadPdfs() {
  const res = await fetch("/api/pdfs");
  pdfs = await res.json();
  renderPdfs();
}

function renderPdfs() {
  // group by tag, preserving the library's ordering of tags
  const groups = [];
  const byTag = {};
  for (const p of pdfs) {
    if (!byTag[p.tag]) {
      byTag[p.tag] = [];
      groups.push(p.tag);
    }
    byTag[p.tag].push(p);
  }
  $("pdf-groups").innerHTML = groups
    .map((tag) => {
      const cards = byTag[tag]
        .map(
          (
            p,
          ) => `<a class="pdf-card" href="/pdfs/${encodeURIComponent(p.file)}" target="_blank" rel="noopener">
            <div class="pdf-card-top">
              <span class="pdf-icon">&#128196;</span>
              <span class="pdf-size">${p.size_kb >= 1024 ? (p.size_kb / 1024).toFixed(1) + " MB" : p.size_kb + " KB"}</span>
            </div>
            <div class="pdf-label">${escapeHtml(p.label)}</div>
            <div class="pdf-desc">${escapeHtml(p.desc)}</div>
          </a>`,
        )
        .join("");
      return `<div class="pdf-group"><h2 class="pdf-group-title">${escapeHtml(tag)}</h2>
        <div class="pdf-grid">${cards}</div></div>`;
    })
    .join("");
}

/* ---------------- Wiring ---------------- */
$("nav-home").addEventListener("click", showList);
$("nav-problems").addEventListener("click", (e) => {
  e.preventDefault();
  showList();
});
$("nav-pseudo").addEventListener("click", (e) => {
  e.preventDefault();
  showPseudocode();
});
$("nav-pdfs").addEventListener("click", (e) => {
  e.preventDefault();
  showPdfs();
});
$("back-to-list").addEventListener("click", (e) => {
  e.preventDefault();
  showList();
});

function showList() {
  listFilter = "all";
  $("problem-view").classList.add("hidden");
  $("pdf-view").classList.add("hidden");
  $("list-view").classList.remove("hidden");
  $("editor-panel-quiz").classList.add("hidden");
  $("editor-panel").classList.remove("hidden");
  document.querySelector("#list-view .page-title").textContent = "Problems";
  $("nav-problems").classList.add("active");
  $("nav-pseudo").classList.remove("active");
  $("nav-pdfs").classList.remove("active");
  current = null;
  renderList();
}

function showPseudocode() {
  listFilter = "pseudo";
  $("problem-view").classList.add("hidden");
  $("pdf-view").classList.add("hidden");
  $("list-view").classList.remove("hidden");
  $("editor-panel-quiz").classList.add("hidden");
  $("editor-panel").classList.remove("hidden");
  document.querySelector("#list-view .page-title").textContent = "Pseudocode";
  $("nav-problems").classList.remove("active");
  $("nav-pseudo").classList.add("active");
  $("nav-pdfs").classList.remove("active");
  current = null;
  renderList();
}

function showPdfs() {
  listFilter = "all";
  $("problem-view").classList.add("hidden");
  $("list-view").classList.add("hidden");
  $("editor-panel-quiz").classList.add("hidden");
  $("editor-panel").classList.add("hidden");
  $("pdf-view").classList.remove("hidden");
  $("nav-problems").classList.remove("active");
  $("nav-pseudo").classList.remove("active");
  $("nav-pdfs").classList.add("active");
  current = null;
  loadPdfs();
}

$("lang-select").addEventListener("change", (e) => {
  currentLang = e.target.value;
  store.setLang(current.id, currentLang);
  $("results").innerHTML = "";
  initEditor();
  if (current.judge === "browser") renderPreview();
});

$("btn-run").addEventListener("click", runCode);
$("btn-submit").addEventListener("click", submitCode);
$("btn-reset").addEventListener("click", resetCode);
$("btn-format").addEventListener("click", formatCode);
$("preview-reload").addEventListener("click", renderPreview);
$("quiz-submit").addEventListener("click", submitQuiz);
$("quiz-clear").addEventListener("click", clearQuiz);

/* ================================================================== */
/* AUTH UI WIRING */
/* ================================================================== */

$("btn-login").addEventListener("click", (e) => {
  e.preventDefault();
  openAuthModal(false);
});

$("btn-logout").addEventListener("click", (e) => {
  e.preventDefault();
  auth.logout().then(() => {
    userSolved = {};
    userSubmissions = [];
    updateUserMenu();
    renderList();
  });
});

$("auth-toggle-link").addEventListener("click", (e) => {
  e.preventDefault();
  const mode = $("auth-form").dataset.mode;
  openAuthModal(mode !== "register");
});

$("auth-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const email = $("auth-email").value.trim();
  const password = $("auth-password").value;
  const username = $("auth-username").value.trim();
  const isRegister = $("auth-form").dataset.mode === "register";
  const errorEl = $("auth-error");

  if (!email || !password) {
    errorEl.textContent = "Please fill in all fields";
    errorEl.classList.remove("hidden");
    return;
  }

  const success = isRegister
    ? await auth.register(username, email, password)
    : await auth.login(email, password);

  if (success) {
    closeAuthModal();
    await loadUserProgress();
    updateUserMenu();
    renderList();
  } else {
    errorEl.textContent = isRegister ? "Registration failed" : "Login failed";
    errorEl.classList.remove("hidden");
  }
});

$("auth-modal").addEventListener("click", (e) => {
  if (e.target === $("auth-modal")) closeAuthModal();
});

/* INITIALIZE */
(async () => {
  await auth.checkAuth();
  updateUserMenu();
  if (currentUser) {
    await loadUserProgress();
  }
  loadProblems();
})();
