/* PracticeCode frontend */

const CM_MODES = {
  java: "text/x-java",
  cpp: "text/x-c++src",
  sql: "text/x-sql",
  javascript: "javascript",
  python: "text/x-python",
};
const LANG_LABELS = {
  java: "Java",
  cpp: "C++",
  sql: "MySQL-ish (SQLite)",
  javascript: "JavaScript",
  python: "Python 3",
};

let problems = [];
let pdfs = [];
let current = null; // full problem payload
let editor = null;
let currentLang = null;
let previewTimer = null;
let judgePending = null; // {resolve} for browser judge
let currentUser = null; // {id, username, email} or null
let lastQuizResult = null; // {pid, data} — backs the submission review page
let reviewContext = null; // {mode:"quiz"|"practice", pid, attemptNo, createdAt}
let quizTimerHandle = null;
let quizTimerPid = null;
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

async function syncLocalProgressToServer() {
  if (!currentUser) return;
  const flagKey = `pc_synced_${currentUser.user_id}`;
  if (localStorage.getItem(flagKey)) return;

  let solved;
  try {
    solved = JSON.parse(localStorage.getItem("pc_solved") || "{}");
  } catch {
    solved = {};
  }
  const pids = Object.keys(solved).filter((pid) => solved[pid]);
  if (!pids.length) {
    localStorage.setItem(flagKey, "1");
    return;
  }

  const problems = pids.map((pid) => {
    const lang = localStorage.getItem(`pc_lang_${pid}`) || "";
    const code = lang
      ? localStorage.getItem(`pc_code_${pid}_${lang}`) || ""
      : "";
    return { problem_id: +pid, language: lang, code };
  });

  try {
    await fetch("/api/user/import-local-progress", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ problems }),
    });
    localStorage.setItem(flagKey, "1");
  } catch (e) {
    console.error("Failed to sync local progress:", e);
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

  /* Best practice-set score seen in this browser, used for the card badge.
     Server-side history is authoritative but this keeps the list instant. */
  bestPractice(pid) {
    try {
      const raw = localStorage.getItem(`pc_best_${pid}`);
      return raw ? JSON.parse(raw) : null;
    } catch {
      return null;
    }
  },

  setBestPractice(pid, score) {
    const prev = this.bestPractice(pid);
    if (prev && prev.score >= score) return;
    localStorage.setItem(`pc_best_${pid}`, JSON.stringify({ score }));
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

const SECTION_ORDER = ["SQL", "Web", "Coding", "Accenture Coding (Important)", "General MCQs", "Pseudocode"];
const SECTION_LABELS = { "General MCQs": "MCQs", "Accenture Coding (Important)": "⭐ Accenture Coding — Important" };

function renderRow(p, solved, num) {
  const diffClass = p.difficulty.toLowerCase();
  const topics = p.topics
    .map((t) => `<span class="topic-chip">${t}</span>`)
    .join("");
  return `<tr data-id="${p.id}">
      <td>${solved[p.id] ? '<span class="check">&#10003;</span>' : '<span class="check" style="color:var(--text-dim)">&mdash;</span>'}</td>
      <td style="color:var(--text-dim)">${num}</td>
      <td><b>${p.title}</b></td>
      <td><span class="diff ${diffClass}">${p.difficulty}</span></td>
      <td>${topics}</td>
    </tr>`;
}

function sectionHeaderRow(name) {
  const label = SECTION_LABELS[name] || name;
  return `<tr class="list-section-row"><td colspan="5" class="list-section">${label}</td></tr>`;
}

function renderList() {
  const solved = store.getSolved();
  const shown = problems.filter(
    (p) => listFilter === "all" || p.judge === "quiz",
  );
  let html = "";

  if (listFilter === "all") {
    // Group into SQL / Web / Coding / MCQs / Pseudocode sections instead of
    // one flat list, using the "section" field the backend already computes.
    const bySection = {};
    shown.forEach((p) => {
      const sec = p.section || "General MCQs";
      (bySection[sec] = bySection[sec] || []).push(p);
    });
    SECTION_ORDER.forEach((sec) => {
      const list = bySection[sec];
      if (!list || !list.length) return;
      html += sectionHeaderRow(sec);
      list.forEach((p, i) => {
        html += renderRow(p, solved, i + 1);
      });
    });
  } else {
    shown.forEach((p, i) => {
      if (i === 0) html += sectionHeaderRow("Pseudocode Quizzes");
      html += renderRow(p, solved, i + 1);
    });
  }

  $("problem-rows").innerHTML = html;
  document.querySelectorAll("#problem-rows tr[data-id]").forEach((tr) => {
    tr.addEventListener("click", () => openProblem(+tr.dataset.id));
  });
  $("solved-counter").innerHTML =
    `Solved <b>${store.solvedCount()}</b>/${problems.length}`;
}

/* ---------------- Problem view ---------------- */
async function openProblem(pid) {
  const res = await fetch(`/api/problems/${pid}`);
  current = await res.json();
  setRoute(`#p=${pid}`);

  $("list-view").classList.add("hidden");
  $("problem-view").classList.remove("hidden");
  $("review-view").classList.add("hidden");
  $("practice-view").classList.add("hidden");
  $("dom-practice-view").classList.add("hidden");
  $("attempts-view").classList.add("hidden");
  $("mock-view").classList.add("hidden");
  $("mock-summary-view").classList.add("hidden");
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
  // a quiz opened earlier swaps these panels, so restore them here
  $("editor-panel-quiz").classList.add("hidden");
  $("editor-panel").classList.remove("hidden");

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

  // If a mock test is running and this Submit was for one of its parts,
  // record the result so the floating bar and final summary reflect it.
  if (mockSession && mockSession.parts.some((p) => p.pid === current.id)) {
    mockSession.results[current.id] = { passed, detail };
    saveMockSession();
    renderMockBar();
  }

  // Also send to server if logged in
  if (currentUser) {
    fetch("/api/record-submission", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        problem_id: current.id,
        language: currentLang,
        code: editor ? editor.getValue() : "",
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
          if (prop === 'text') return el.textContent.trim();
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
          } else if (s.starClick !== undefined) {
            var starEls = document.querySelectorAll('.rating-stars .star');
            if (starEls[s.starClick - 1]) starEls[s.starClick - 1].click();
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
          if (e.stars !== undefined) {
            var starCount = document.querySelectorAll('.rating-stars .star').length;
            ok = ok && (starCount === e.stars);
            parts.push('stars = ' + starCount + ' (expected ' + e.stars + ')');
          }
          if (e.filled !== undefined) {
            var filledCount = document.querySelectorAll('.rating-stars .star.filled').length;
            ok = ok && (filledCount === e.filled);
            parts.push('filled stars = ' + filledCount + ' (expected ' + e.filled + ')');
          }
          if (e.starColor !== undefined) {
            var colorEls = document.querySelectorAll('.rating-stars .star');
            var colorEl = colorEls[e.starColor.index - 1];
            var starCol = colorEl ? getComputedStyle(colorEl).color : '(missing)';
            ok = ok && (starCol === e.starColor.value);
            parts.push('star ' + e.starColor.index + ' color = ' + starCol +
              ' (expected ' + e.starColor.value + ')');
          }
          if (e.exists !== undefined) {
            var exEl = document.querySelector(e.exists.selector);
            var present = !!exEl;
            ok = ok && (present === e.exists.value);
            parts.push('exists ' + e.exists.selector + ' = ' + present +
              ' (expected ' + e.exists.value + ')');
            if (present && e.exists.text !== undefined) {
              var exText = exEl.textContent.trim();
              ok = ok && (exText === e.exists.text);
              parts.push('its text = "' + exText + '" (expected "' + e.exists.text + '")');
            }
          }
          if (e.css !== undefined) {
            var cssEl = document.querySelector(e.css.selector);
            var cssVal = cssEl ? getComputedStyle(cssEl)[e.css.property] : '(missing)';
            ok = ok && (cssVal === e.css.value);
            parts.push(e.css.selector + ' ' + e.css.property + ' = ' + cssVal +
              ' (expected ' + e.css.value + ')');
          }
          if (e.html !== undefined) {
            var htmlEl = document.getElementById(e.html.id);
            var hv = htmlEl ? htmlEl.innerHTML.trim() : '(missing)';
            ok = ok && (hv === e.html.value);
            parts.push('#' + e.html.id + ' innerHTML = "' + hv + '" (expected "' + e.html.value + '")');
          }
          if (e.attr !== undefined) {
            var attrEl = document.querySelector(e.attr.selector);
            var av = attrEl ? attrEl.getAttribute(e.attr.name) : null;
            av = av === null ? 'null' : av;
            ok = ok && (av === e.attr.value);
            parts.push(e.attr.selector + ' [' + e.attr.name + '] = ' + av +
              ' (expected ' + e.attr.value + ')');
          }
          if (e.elemCount !== undefined) {
            var ecCount = document.querySelectorAll(e.elemCount.selector).length;
            ok = ok && (ecCount === e.elemCount.value);
            parts.push('count of ' + e.elemCount.selector + ' = ' + ecCount +
              ' (expected ' + e.elemCount.value + ')');
          }
          if (e.hasClass !== undefined) {
            var hcEl = document.querySelector(e.hasClass.selector);
            var hasIt = hcEl ? hcEl.classList.contains(e.hasClass.class) : false;
            ok = ok && (hasIt === e.hasClass.value);
            parts.push(e.hasClass.selector + ' has class "' + e.hasClass.class + '" = ' + hasIt +
              ' (expected ' + e.hasClass.value + ')');
          }
          if (e.visibleList !== undefined) {
            var vlVis = [];
            var vlHid = [];
            document.querySelectorAll(e.visibleList.selector).forEach(function (el) {
              (getComputedStyle(el).display === 'none' ? vlHid : vlVis).push(el.textContent.trim());
            });
            var vlSame = vlVis.length === e.visibleList.visible.length &&
              e.visibleList.visible.every(function (x) { return vlVis.indexOf(x) !== -1; }) &&
              vlHid.length === e.visibleList.hidden.length &&
              e.visibleList.hidden.every(function (x) { return vlHid.indexOf(x) !== -1; });
            ok = ok && vlSame;
            parts.push('visible = [' + vlVis.join(', ') + '] (expected [' + e.visibleList.visible.join(', ') + '])');
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
            if (t.expect.stars !== undefined) expectedParts.push('stars = ' + t.expect.stars);
            if (t.expect.filled !== undefined) expectedParts.push('filled stars = ' + t.expect.filled);
            if (t.expect.starColor !== undefined) expectedParts.push('star ' + t.expect.starColor.index + ' color = ' + t.expect.starColor.value);
            if (t.expect.exists !== undefined) expectedParts.push('exists ' + t.expect.exists.selector + ' = ' + t.expect.exists.value + (t.expect.exists.text !== undefined ? ' text = "' + t.expect.exists.text + '"' : ''));
            if (t.expect.css !== undefined) expectedParts.push(t.expect.css.selector + ' ' + t.expect.css.property + ' = ' + t.expect.css.value);
            if (t.expect.html !== undefined) expectedParts.push('#' + t.expect.html.id + ' innerHTML = "' + t.expect.html.value + '"');
            if (t.expect.attr !== undefined) expectedParts.push(t.expect.attr.selector + ' [' + t.expect.attr.name + '] = ' + t.expect.attr.value);
            if (t.expect.elemCount !== undefined) expectedParts.push('count of ' + t.expect.elemCount.selector + ' = ' + t.expect.elemCount.value);
            if (t.expect.hasClass !== undefined) expectedParts.push(t.expect.hasClass.selector + ' has class "' + t.expect.hasClass.class + '" = ' + t.expect.hasClass.value);
            if (t.expect.visibleList !== undefined) expectedParts.push('visible = [' + t.expect.visibleList.visible.join(', ') + ']');
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
    return JSON.parse(localStorage.getItem(`pc_quiz3_${current.id}`) || "[]");
  } catch {
    return [];
  }
}
function saveQuizSelections(sel) {
  localStorage.setItem(`pc_quiz3_${current.id}`, JSON.stringify(sel));
}

/* Practice Set exam timer — 20 min for most sets, 25 min for pseudocode sets
   (server decides the minutes via `timerMin`; missing/0 means untimed). The
   start time is persisted in localStorage so refreshing the page doesn't
   grant extra time; "Clear Answers" is the only thing that resets it. */
function quizTimerKey(pid) {
  return `pc_quiz_timer_${pid}`;
}

function stopQuizTimer() {
  if (quizTimerHandle) {
    clearInterval(quizTimerHandle);
    quizTimerHandle = null;
  }
  quizTimerPid = null;
}

function startQuizTimer(p) {
  stopQuizTimer();
  const timerEl = $("quiz-timer");
  if (!p.timerMin) {
    timerEl.classList.add("hidden");
    return;
  }
  const key = quizTimerKey(p.id);
  let startedAt = +localStorage.getItem(key);
  if (!startedAt) {
    startedAt = Date.now();
    localStorage.setItem(key, String(startedAt));
  }
  const durationMs = p.timerMin * 60000;
  timerEl.classList.remove("hidden");
  quizTimerPid = p.id;
  const tick = () => {
    // the user navigated to a different problem/view — stop ticking a timer
    // for a quiz that isn't the one on screen anymore
    if (!current || current.id !== p.id || quizTimerPid !== p.id) {
      stopQuizTimer();
      return;
    }
    const remaining = startedAt + durationMs - Date.now();
    renderQuizTimer(remaining);
    if (remaining <= 0) {
      stopQuizTimer();
      doSubmitQuiz(true);
    }
  };
  quizTimerHandle = setInterval(tick, 1000);
  tick();
}

function renderQuizTimer(remaining) {
  const mins = Math.max(0, Math.floor(remaining / 60000));
  const secs = Math.max(0, Math.floor((remaining % 60000) / 1000));
  const timerEl = $("quiz-timer");
  timerEl.textContent = `${String(mins).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;
  timerEl.classList.toggle("low", remaining < 5 * 60000);
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
  $("review-view").classList.add("hidden");
  $("practice-view").classList.add("hidden");
  $("dom-practice-view").classList.add("hidden");
  $("attempts-view").classList.add("hidden");
  $("mock-view").classList.add("hidden");
  $("mock-summary-view").classList.add("hidden");
  $("quiz-results").innerHTML = "";
  // the review button only means something once this quiz has been graded
  $("quiz-review").classList.toggle(
    "hidden",
    !lastQuizResult || lastQuizResult.pid !== current.id,
  );

  const saved = quizSelections();
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
  startQuizTimer(current);
}

function updateQuizProgress() {
  const sel = quizSelections();
  const answered = current.questions.filter(
    (q) => sel[q.n - 1] !== undefined && sel[q.n - 1] !== null,
  ).length;
  const total = current.questions.length;
  $("quiz-progress").textContent = `${answered}/${total} answered`;
  // Partial submissions are allowed: on 100+ question banks, requiring every
  // answer before enabling Submit made the button look broken.
  $("quiz-submit").disabled = answered === 0;
  $("quiz-submit").title =
    answered === 0
      ? "Answer at least one question to submit"
      : answered < total
        ? `${total - answered} unanswered — you can still submit`
        : "";
}

function clearQuiz() {
  if (!confirm("Clear all selected answers for this quiz?")) return;
  saveQuizSelections([]);
  // "Clear Answers" is the explicit restart action, so the exam clock
  // restarts too rather than keeping whatever time had already elapsed.
  localStorage.removeItem(quizTimerKey(current.id));
  renderQuiz();
}

async function submitQuiz() {
  await doSubmitQuiz(false);
}

async function doSubmitQuiz(force) {
  const sel = quizSelections();
  const unanswered = current.questions.filter(
    (q) => sel[q.n - 1] === undefined || sel[q.n - 1] === null,
  ).length;
  if (
    !force &&
    unanswered > 0 &&
    !confirm(
      `${unanswered} question${unanswered === 1 ? "" : "s"} unanswered. Submit anyway?`,
    )
  ) {
    return;
  }
  stopQuizTimer();
  setButtonsBusy(true);
  $("quiz-results").innerHTML =
    `<div class="results-header"><span class="verdict pending">Grading…</span></div>`;
  try {
    const practice = isPracticeSet(current);
    const data = practice
      ? await submitPracticeAttempt(current.id, sel)
      : await gradeQuiz(current.id, sel);
    renderQuizResults(data);
  } catch (e) {
    $("quiz-results").innerHTML =
      `<div class="results-header"><span class="verdict wa">Error</span></div><pre class="error-pre">${escapeHtml(String(e))}</pre>`;
  } finally {
    setButtonsBusy(false);
  }
}

async function gradeQuiz(pid, answers) {
  const res = await fetch("/api/quiz/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ problem_id: pid, answers }),
  });
  return res.json();
}

/* Practice sets persist every attempt — server-side when logged in, in the
   browser otherwise — so the attempt history page can reopen any of them. */
async function submitPracticeAttempt(pid, answers) {
  const res = await fetch("/api/practice/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ problem_id: pid, answers }),
  });
  const data = await res.json();
  if (!data.error) {
    if (!data.attemptId) saveLocalAttempt(pid, answers, data);
    store.setBestPractice(pid, data.score);
  }
  return data;
}

function renderQuizResults(data) {
  if (data.error) {
    $("quiz-results").innerHTML =
      `<div class="results-header"><span class="verdict wa">Error</span></div><pre class="error-pre">${escapeHtml(data.error)}</pre>`;
    return;
  }
  lastQuizResult = { pid: current.id, data };
  const box = renderQuizScorecard(data);
  recordSubmission(data.passed, `${data.correct}/${data.total} correct`, true);
  box.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

function renderQuizScorecard(data) {
  const practice = isPracticeSet(current);
  $("quiz-review").classList.toggle("hidden", practice);
  const wrong = data.results.filter((r) => !r.passed && r.picked != null).length;
  const skipped = data.results.filter((r) => r.picked == null).length;
  const box = $("quiz-results");
  // Practice sets route through their own attempt history; the original quiz
  // banks jump straight into the review page as before.
  const cta = practice
    ? `<button class="btn btn-review" id="quiz-results-review">View Result</button>`
    : `<button class="btn btn-review" id="quiz-results-review">
         View Submission — answers &amp; explanations
       </button>`;
  box.innerHTML = `<div class="results-header">
      <span class="verdict ${data.passed ? "ac" : "wa"}">${data.correct === data.total ? "Perfect Score" : practice ? "Submitted" : "Quiz Graded"}</span>
      <span style="color:var(--text-dim);font-weight:400">${data.correct}/${data.total} correct (${data.score}%)</span>
    </div>
    <div class="quiz-scorecard">
      <div class="score-tiles">
        <div class="score-tile ok"><b>${data.correct}</b><span>Correct</span></div>
        <div class="score-tile bad"><b>${wrong}</b><span>Wrong</span></div>
        <div class="score-tile skip"><b>${skipped}</b><span>Skipped</span></div>
        <div class="score-tile"><b>${data.score}%</b><span>Score</span></div>
      </div>
      ${cta}
    </div>`;
  $("quiz-results-review").addEventListener(
    "click",
    practice ? () => openAttempts(current.id) : showQuizReview,
  );
  return box;
}

/* ---------------- Quiz submission review page ---------------- */
const LETTERS = ["A", "B", "C", "D", "E", "F"];

function reviewState(r) {
  if (r.passed) return "ok";
  return r.picked == null ? "skip" : "bad";
}

async function showQuizReview() {
  if (!current || !lastQuizResult || lastQuizResult.pid !== current.id) return;
  reviewContext = null;
  setRoute(`#review=${current.id}`);
  renderQuizReview();
}

// Entry point for a cold #review=<id> load (refresh, bookmark, back button):
// the saved selections in localStorage are re-graded so the page still works.
async function openQuizReview(pid) {
  if (!current || current.id !== pid) {
    const res = await fetch(`/api/problems/${pid}`);
    current = await res.json();
    if (current.judge !== "quiz") return showList();
    renderQuiz();
  }
  if (!lastQuizResult || lastQuizResult.pid !== pid) {
    const data = await gradeQuiz(pid, quizSelections());
    if (data.error) return showList();
    lastQuizResult = { pid, data };
    $("quiz-review").classList.remove("hidden");
  }
  setRoute(`#review=${pid}`);
  renderQuizReview();
}

function renderQuizReview() {
  const { data } = lastQuizResult;
  $("problem-view").classList.add("hidden");
  $("list-view").classList.add("hidden");
  $("pdf-view").classList.add("hidden");
  $("practice-view").classList.add("hidden");
  $("dom-practice-view").classList.add("hidden");
  $("attempts-view").classList.add("hidden");
  $("mock-view").classList.add("hidden");
  $("mock-summary-view").classList.add("hidden");
  $("review-view").classList.remove("hidden");

  const practice = reviewContext && reviewContext.mode === "practice";
  $("review-title").textContent = practice
    ? `${current.title} — Attempt ${reviewContext.attemptNo}`
    : current.title;
  $("review-back").textContent = practice
    ? "← All attempts"
    : "← Back to quiz";
  const wrong = data.results.filter((r) => reviewState(r) === "bad").length;
  const skipped = data.results.filter((r) => reviewState(r) === "skip").length;
  const when =
    practice && reviewContext.createdAt
      ? ` · ${new Date(reviewContext.createdAt).toLocaleString()}`
      : "";
  $("review-score").innerHTML = `
    <span class="verdict ${data.passed ? "ac" : "wa"}">${data.score}%</span>
    <span class="review-score-line">${data.correct}/${data.total} correct
      · ${wrong} wrong · ${skipped} skipped${escapeHtml(when)}</span>`;

  $("review-grid").innerHTML = data.results
    .map(
      (r) =>
        `<button class="rnum ${reviewState(r)}" data-n="${r.n}" title="Question ${r.n}">${r.n}</button>`,
    )
    .join("");

  const focus = data.focusAreas || [];
  $("review-focus").innerHTML = focus.length
    ? `<div class="review-side-title">Areas to focus on</div>` +
      focus
        .map(
          (f) =>
            `<div class="focus-row"><span>${escapeHtml(f.topic)}</span>
               <b>${f.wrong}/${f.total} wrong</b></div>`,
        )
        .join("")
    : "";

  $("review-list").innerHTML = data.results
    .map((r) => {
      const q = current.questions[r.n - 1];
      const state = reviewState(r);
      const opts = q.options
        .map((o, oi) => {
          const isRight = oi === r.answer;
          const isPicked = oi === r.picked;
          const cls = isRight ? "right" : isPicked ? "wrong" : "";
          const tag = isRight
            ? '<span class="opt-tag right">Correct answer</span>'
            : isPicked
              ? '<span class="opt-tag wrong">Your answer</span>'
              : "";
          return `<div class="ropt ${cls}">
              <span class="quiz-letter">${LETTERS[oi]}</span>
              <span class="ropt-text">${escapeHtml(o)}</span>${tag}
            </div>`;
        })
        .join("");
      const why = r.explanation
        ? `<div class="why"><span class="why-label">Why</span>
             <div class="why-text">${escapeHtml(r.explanation)}</div></div>`
        : `<div class="why muted"><span class="why-label">Why</span>
             <div class="why-text">Explanation coming soon for this question.</div></div>`;
      const topic = r.topic
        ? `<span class="rq-topic">${escapeHtml(r.topic)}</span>`
        : "";
      const label =
        state === "ok" ? "Correct" : state === "skip" ? "Skipped" : "Wrong";
      return `<article class="rq collapsed" id="rq-${r.n}" data-state="${state}">
          <button class="rq-head" data-n="${r.n}">
            <span class="rnum ${state}">${r.n}</span>
            <span class="rq-q">${q.q}</span>
            ${topic}
            <span class="rq-flag ${state}">${label}</span>
          </button>
          <div class="rq-body">${opts}${why}</div>
        </article>`;
    })
    .join("");

  $("review-grid")
    .querySelectorAll(".rnum")
    .forEach((b) =>
      b.addEventListener("click", () => openReviewQuestion(+b.dataset.n)),
    );
  $("review-list")
    .querySelectorAll(".rq-head")
    .forEach((h) =>
      h.addEventListener("click", () =>
        h.parentElement.classList.toggle("collapsed"),
      ),
    );
  setReviewFilter("all");
  window.scrollTo({ top: 0 });
}

function openReviewQuestion(n) {
  const card = $(`rq-${n}`);
  if (!card) return;
  // a filter can have the target hidden — clicking a number always wins
  if (card.classList.contains("filtered")) setReviewFilter("all");
  card.classList.remove("collapsed");
  card.scrollIntoView({ behavior: "smooth", block: "center" });
  card.classList.add("flash");
  setTimeout(() => card.classList.remove("flash"), 1200);
}

function setReviewFilter(filter) {
  document
    .querySelectorAll(".review-filters .chip")
    .forEach((c) => c.classList.toggle("active", c.dataset.filter === filter));
  $("review-list")
    .querySelectorAll(".rq")
    .forEach((card) => {
      const state = card.dataset.state;
      const show =
        filter === "all" ||
        (filter === "wrong" && state === "bad") ||
        (filter === "skipped" && state === "skip");
      card.classList.toggle("filtered", !show);
    });
}

function setAllReviewCards(collapsed) {
  $("review-list")
    .querySelectorAll(".rq")
    .forEach((c) => c.classList.toggle("collapsed", collapsed));
}

function backToQuiz() {
  // From a practice attempt, "back" belongs to the attempt history, not the quiz
  if (reviewContext && reviewContext.mode === "practice") {
    const pid = reviewContext.pid;
    reviewContext = null;
    return openAttempts(pid);
  }
  $("review-view").classList.add("hidden");
  $("practice-view").classList.add("hidden");
  $("dom-practice-view").classList.add("hidden");
  $("attempts-view").classList.add("hidden");
  $("mock-view").classList.add("hidden");
  $("mock-summary-view").classList.add("hidden");
  setRoute(`#p=${current.id}`);
  renderQuiz();
  if (lastQuizResult && lastQuizResult.pid === current.id) {
    renderQuizScorecard(lastQuizResult.data).scrollIntoView({ block: "nearest" });
  }
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

/* ---------------- URL routing (reload stays on the same page) ---------------- */
let applyingRoute = false;

function setRoute(hash) {
  if ((location.hash || "") === hash) return;
  applyingRoute = true;
  location.hash = hash;
}

async function applyRoute() {
  const hash = location.hash || "";
  const m = hash.match(/^#p=(\d+)$/);
  if (m) {
    const pid = +m[1];
    if (!current || current.id !== pid) await openProblem(pid);
    return;
  }
  const rev = hash.match(/^#review=(\d+)$/);
  if (rev) {
    reviewContext = null;
    await openQuizReview(+rev[1]);
    return;
  }
  if (hash === "#practice") {
    showPractice();
    return;
  }
  if (hash === "#domjs") {
    showDomPractice();
    return;
  }
  if (hash === "#mock") {
    showMock();
    return;
  }
  const att = hash.match(/^#attempts=(\d+)$/);
  if (att) {
    await openAttempts(+att[1]);
    return;
  }
  const one = hash.match(/^#attempt=(\d+):(.+)$/);
  if (one) {
    const pid = +one[1];
    const attempts = await fetchAttempts(pid);
    const found = attempts.find((a) => String(a.id) === one[2]);
    await openAttemptDetail(pid, one[2], found ? found.n : 1);
    return;
  }
  if (hash === "#pseudo") {
    showPseudocode();
    return;
  }
  if (hash === "#pdfs") {
    showPdfs();
    return;
  }
  showList();
}

window.addEventListener("hashchange", () => {
  if (applyingRoute) {
    applyingRoute = false;
    return;
  }
  applyRoute();
});

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
  setRoute("");
  listFilter = "all";
  $("problem-view").classList.add("hidden");
  $("pdf-view").classList.add("hidden");
  $("list-view").classList.remove("hidden");
  $("editor-panel-quiz").classList.add("hidden");
  $("review-view").classList.add("hidden");
  $("practice-view").classList.add("hidden");
  $("dom-practice-view").classList.add("hidden");
  $("attempts-view").classList.add("hidden");
  $("mock-view").classList.add("hidden");
  $("mock-summary-view").classList.add("hidden");
  $("editor-panel").classList.remove("hidden");
  document.querySelector("#list-view .page-title").textContent = "Problems";
  $("nav-problems").classList.add("active");
  $("nav-pseudo").classList.remove("active");
  $("nav-pdfs").classList.remove("active");
  $("nav-domjs").classList.remove("active");
  current = null;
  renderList();
}

function showPseudocode() {
  setRoute("#pseudo");
  listFilter = "pseudo";
  $("problem-view").classList.add("hidden");
  $("pdf-view").classList.add("hidden");
  $("list-view").classList.remove("hidden");
  $("editor-panel-quiz").classList.add("hidden");
  $("review-view").classList.add("hidden");
  $("practice-view").classList.add("hidden");
  $("dom-practice-view").classList.add("hidden");
  $("attempts-view").classList.add("hidden");
  $("mock-view").classList.add("hidden");
  $("mock-summary-view").classList.add("hidden");
  $("editor-panel").classList.remove("hidden");
  document.querySelector("#list-view .page-title").textContent = "Pseudocode";
  $("nav-problems").classList.remove("active");
  $("nav-pseudo").classList.add("active");
  $("nav-pdfs").classList.remove("active");
  $("nav-domjs").classList.remove("active");
  current = null;
  renderList();
}

function showPdfs() {
  setRoute("#pdfs");
  listFilter = "all";
  $("problem-view").classList.add("hidden");
  $("list-view").classList.add("hidden");
  $("editor-panel-quiz").classList.add("hidden");
  $("review-view").classList.add("hidden");
  $("practice-view").classList.add("hidden");
  $("dom-practice-view").classList.add("hidden");
  $("attempts-view").classList.add("hidden");
  $("mock-view").classList.add("hidden");
  $("mock-summary-view").classList.add("hidden");
  $("editor-panel").classList.add("hidden");
  $("pdf-view").classList.remove("hidden");
  $("nav-problems").classList.remove("active");
  $("nav-pseudo").classList.remove("active");
  $("nav-pdfs").classList.add("active");
  $("nav-domjs").classList.remove("active");
  current = null;
  loadPdfs();
}

/* ---------------- Practice Sets ---------------- */
function isPracticeSet(p) {
  return !!p && (p.section === "Practice Sets" ||
    (p.topics || []).includes("Practice Set"));
}

function showPractice() {
  setRoute("#practice");
  $("problem-view").classList.add("hidden");
  $("list-view").classList.add("hidden");
  $("pdf-view").classList.add("hidden");
  $("editor-panel-quiz").classList.add("hidden");
  $("review-view").classList.add("hidden");
  $("attempts-view").classList.add("hidden");
  $("mock-view").classList.add("hidden");
  $("mock-summary-view").classList.add("hidden");
  $("dom-practice-view").classList.add("hidden");
  $("practice-view").classList.remove("hidden");
  $("nav-problems").classList.remove("active");
  $("nav-pseudo").classList.remove("active");
  $("nav-pdfs").classList.remove("active");
  $("nav-practice").classList.add("active");
  $("nav-domjs").classList.remove("active");
  current = null;
  renderPracticeSets();
}

function renderPracticeSets() {
  const sets = problems.filter(isPracticeSet);
  if (!sets.length) {
    $("practice-groups").innerHTML =
      `<p style="color:var(--text-dim)">No practice sets available yet.</p>`;
    return;
  }
  // group by the second topic tag, which names the practice topic
  const byTopic = {};
  sets.forEach((p) => {
    const topic = (p.topics || []).filter((t) => t !== "Practice Set")[0] || "Other";
    (byTopic[topic] = byTopic[topic] || []).push(p);
  });
  const solved = store.getSolved();
  $("practice-groups").innerHTML = Object.keys(byTopic)
    .map((topic) => {
      const cards = byTopic[topic]
        .map((p) => {
          const best = store.bestPractice(p.id);
          const badge = best
            ? `<span class="pset-best">Best ${best.score}%</span>`
            : `<span class="pset-new">Not attempted</span>`;
          return `<div class="pset-card" data-id="${p.id}">
            <div class="pset-card-top">
              <span class="pset-count">20 questions</span>${badge}
            </div>
            <div class="pset-title">${escapeHtml(p.title)}</div>
            <div class="pset-meta">${escapeHtml(p.difficulty)} · situational</div>
          </div>`;
        })
        .join("");
      return `<div class="pset-group">
          <div class="pset-group-title">${escapeHtml(topic)}</div>
          <div class="pset-grid">${cards}</div>
        </div>`;
    })
    .join("");
  document.querySelectorAll("#practice-groups .pset-card").forEach((el) => {
    el.addEventListener("click", () => openProblem(+el.dataset.id));
  });
}

/* ---------------- JS DOM Practice ---------------- */
// Curriculum order — deliberately NOT alphabetical, each chunk builds on the last.
const DOM_CHUNK_ORDER = [
  "Selecting & Reading Elements",
  "Changing Text & Attributes",
  "Styling with Classes",
  "Handling Events",
  "Creating & Removing Elements",
  "DOM Traversal",
  "Working with Forms",
  "Mini Projects",
];

function isDomPractice(p) {
  return !!p && (p.section === "JS DOM Practice" ||
    (p.topics || []).includes("JS DOM Practice"));
}

function showDomPractice() {
  setRoute("#domjs");
  $("problem-view").classList.add("hidden");
  $("list-view").classList.add("hidden");
  $("pdf-view").classList.add("hidden");
  $("editor-panel-quiz").classList.add("hidden");
  $("review-view").classList.add("hidden");
  $("practice-view").classList.add("hidden");
  $("attempts-view").classList.add("hidden");
  $("mock-view").classList.add("hidden");
  $("mock-summary-view").classList.add("hidden");
  $("dom-practice-view").classList.remove("hidden");
  $("nav-problems").classList.remove("active");
  $("nav-pseudo").classList.remove("active");
  $("nav-pdfs").classList.remove("active");
  $("nav-practice").classList.remove("active");
  $("nav-domjs").classList.add("active");
  current = null;
  renderDomPracticeGroups();
}

function renderDomPracticeGroups() {
  const exercises = problems.filter(isDomPractice);
  if (!exercises.length) {
    $("dom-practice-groups").innerHTML =
      `<p style="color:var(--text-dim)">No DOM practice exercises available yet.</p>`;
    return;
  }
  // group by the chunk tag (the topic after "JS DOM Practice"), in curriculum order
  const byChunk = {};
  exercises.forEach((p) => {
    const chunk = (p.topics || []).find((t) =>
      t !== "JavaScript" && t !== "DOM Manipulation" && t !== "JS DOM Practice",
    ) || "Other";
    (byChunk[chunk] = byChunk[chunk] || []).push(p);
  });
  const chunkNames = [
    ...DOM_CHUNK_ORDER.filter((c) => byChunk[c]),
    ...Object.keys(byChunk).filter((c) => !DOM_CHUNK_ORDER.includes(c)),
  ];
  const solved = store.getSolved();
  $("dom-practice-groups").innerHTML = chunkNames
    .map((chunk, i) => {
      const cards = byChunk[chunk]
        .map((p) => {
          const isSolved = !!solved[p.id];
          const badge = isSolved
            ? `<span class="pset-best">Solved &#10003;</span>`
            : `<span class="pset-new">Not attempted</span>`;
          return `<div class="pset-card" data-id="${p.id}">
            <div class="pset-card-top">
              <span class="pset-count">${escapeHtml(p.difficulty)}</span>${badge}
            </div>
            <div class="pset-title">${escapeHtml(p.title)}</div>
            <div class="pset-meta">JavaScript &middot; DOM</div>
          </div>`;
        })
        .join("");
      return `<div class="pset-group">
          <div class="pset-group-title">Chunk ${i + 1}: ${escapeHtml(chunk)}</div>
          <div class="pset-grid">${cards}</div>
        </div>`;
    })
    .join("");
  document.querySelectorAll("#dom-practice-groups .pset-card").forEach((el) => {
    el.addEventListener("click", () => openProblem(+el.dataset.id));
  });
}

/* Guest attempt history lives in the browser; logged-in history lives in the
   DB so it follows the account across devices. */
function localAttempts(pid) {
  try {
    return JSON.parse(localStorage.getItem(`pc_attempts_${pid}`) || "[]");
  } catch {
    return [];
  }
}

function saveLocalAttempt(pid, answers, data) {
  const list = localAttempts(pid);
  list.push({
    id: `local-${Date.now()}`,
    answers,
    correct: data.correct,
    total: data.total,
    score: data.score,
    createdAt: new Date().toISOString(),
  });
  localStorage.setItem(`pc_attempts_${pid}`, JSON.stringify(list));
  return list.length;
}

async function fetchAttempts(pid) {
  if (currentUser) {
    const res = await fetch(`/api/practice/attempts/${pid}`);
    if (res.ok) return (await res.json()).attempts;
  }
  return localAttempts(pid).map((a, i) => ({ ...a, n: i + 1 }));
}

async function openAttempts(pid) {
  const p = problems.find((x) => x.id === pid);
  if (!current || current.id !== pid) {
    const res = await fetch(`/api/problems/${pid}`);
    current = await res.json();
  }
  setRoute(`#attempts=${pid}`);
  $("problem-view").classList.add("hidden");
  $("list-view").classList.add("hidden");
  $("pdf-view").classList.add("hidden");
  $("practice-view").classList.add("hidden");
  $("dom-practice-view").classList.add("hidden");
  $("review-view").classList.add("hidden");
  $("attempts-view").classList.remove("hidden");

  $("attempts-title").textContent = (p && p.title) || current.title;
  const attempts = await fetchAttempts(pid);
  $("attempts-intro").textContent = attempts.length
    ? `${attempts.length} attempt${attempts.length === 1 ? "" : "s"} — click one to see its marks, answers and explanations.`
    : "No attempts yet. Take the set and submit it to build your history here.";
  if (!currentUser) {
    $("attempts-intro").textContent +=
      " (Not logged in — this history is saved in this browser only.)";
  }

  $("attempts-list").innerHTML = attempts
    .slice()
    .reverse()
    .map((a) => {
      const when = new Date(a.createdAt).toLocaleString();
      const cls = a.score >= 70 ? "good" : a.score >= 50 ? "mid" : "low";
      return `<div class="attempt-row" data-id="${a.id}" data-n="${a.n}">
          <div class="attempt-n">Attempt ${a.n}</div>
          <div class="attempt-when">${escapeHtml(when)}</div>
          <div class="attempt-score ${cls}">${a.correct}/${a.total} · ${a.score}%</div>
          <div class="attempt-go">View →</div>
        </div>`;
    })
    .join("");

  document.querySelectorAll("#attempts-list .attempt-row").forEach((row) => {
    row.addEventListener("click", () =>
      openAttemptDetail(pid, row.dataset.id, +row.dataset.n),
    );
  });
}

async function openAttemptDetail(pid, attemptId, attemptNo) {
  if (!current || current.id !== pid) {
    const res = await fetch(`/api/problems/${pid}`);
    current = await res.json();
  }
  let data;
  if (String(attemptId).startsWith("local-")) {
    const stored = localAttempts(pid).find((a) => a.id === attemptId);
    if (!stored) return;
    data = await gradeQuiz(pid, stored.answers);
    data.createdAt = stored.createdAt;
  } else {
    const res = await fetch(`/api/practice/attempt/${attemptId}`);
    if (!res.ok) return;
    data = await res.json();
  }
  lastQuizResult = { pid, data };
  reviewContext = {
    mode: "practice",
    pid,
    attemptNo,
    createdAt: data.createdAt,
  };
  setRoute(`#attempt=${pid}:${attemptId}`);
  renderQuizReview();
}

/* ================================================================== */
/* MOCK TEST — timed, 3-part coding round (Coding + SQL + Web Dev)     */
/* ================================================================== */

const MOCK_TESTS = [
  {
    id: "mock-1",
    title: "Coding Round Mock #1 — 60 Minutes",
    desc: "One coding problem, one SQL join, one JavaScript/DOM task — the same 3-part shape "
      + "as the real Accenture coding round, built entirely from real reported exam questions. "
      + "Work through all three under one 60-minute clock, then submit each with the normal "
      + "Submit button before time runs out.",
    durationMin: 60,
    parts: [
      { pid: 27, label: "Coding" },
      { pid: 4018, label: "SQL" },
      { pid: 4016, label: "Web Dev" },
    ],
  },
  {
    id: "mock-2",
    title: "Coding Round Mock #2 — 60 Minutes",
    desc: "Coding: 8th Sept Shift 2 reported question (binary-search on a digit-sum prefix "
      + "series). SQL: a 3-table join with a location filter, the same 'join + WHERE' shape as "
      + "the reported SQL question. Web Dev: a dark/light theme toggle with persisted state.",
    durationMin: 60,
    parts: [
      { pid: 28, label: "Coding" },
      { pid: 3078, label: "SQL" },
      { pid: 50, label: "Web Dev" },
    ],
  },
  {
    id: "mock-3",
    title: "Coding Round Mock #3 — 60 Minutes",
    desc: "Coding: the 20th Sept reported question (count squares ending in a given digit) — "
      + "a plain loop, on the easier end of the coding round. SQL: a salary-threshold join "
      + "across 3 tables. Web Dev: real-time password strength and confirm-match validation.",
    durationMin: 60,
    parts: [
      { pid: 3099, label: "Coding" },
      { pid: 3070, label: "SQL" },
      { pid: 14, label: "Web Dev" },
    ],
  },
  {
    id: "mock-4",
    title: "Coding Round Mock #4 — 60 Minutes",
    desc: "Coding: 18th Sept Slot 3 reported question (even/odd digit-length rules on an "
      + "array) — the one with the visible optimal solution in the source. SQL: a join filtered "
      + "on a name pattern and a numeric flight-code pattern. Web Dev: a live search/filter list.",
    durationMin: 60,
    parts: [
      { pid: 3102, label: "Coding" },
      { pid: 3086, label: "SQL" },
      { pid: 15, label: "Web Dev" },
    ],
  },
  {
    id: "mock-5",
    title: "Coding Round Mock #5 — 60 Minutes",
    desc: "Coding: 18th Sept Slot 1 reported question (max bitonic subarray sum) — the hardest "
      + "of the five mocks, O(N) two-pass DP. SQL: a join filtered on status plus a plate-number "
      + "pattern. Web Dev: a bounded counter with clamped limits and a status message.",
    durationMin: 60,
    parts: [
      { pid: 3100, label: "Coding" },
      { pid: 3094, label: "SQL" },
      { pid: 3, label: "Web Dev" },
    ],
  },
];

let mockSession = null; // {mockId, parts, startedAt, durationMs, results:{pid:{passed,detail}}}
let mockTickHandle = null;

function loadMockSession() {
  try {
    return JSON.parse(localStorage.getItem("pc_mock_session") || "null");
  } catch {
    return null;
  }
}
function saveMockSession() {
  if (mockSession) localStorage.setItem("pc_mock_session", JSON.stringify(mockSession));
  else localStorage.removeItem("pc_mock_session");
}
function mockHistory() {
  try {
    return JSON.parse(localStorage.getItem("pc_mock_history") || "[]");
  } catch {
    return [];
  }
}
function saveMockHistory(list) {
  localStorage.setItem("pc_mock_history", JSON.stringify(list));
}

function showMock() {
  setRoute("#mock");
  $("problem-view").classList.add("hidden");
  $("list-view").classList.add("hidden");
  $("pdf-view").classList.add("hidden");
  $("practice-view").classList.add("hidden");
  $("dom-practice-view").classList.add("hidden");
  $("review-view").classList.add("hidden");
  $("attempts-view").classList.add("hidden");
  $("mock-summary-view").classList.add("hidden");
  $("mock-view").classList.remove("hidden");
  $("nav-problems").classList.remove("active");
  $("nav-pseudo").classList.remove("active");
  $("nav-pdfs").classList.remove("active");
  $("nav-practice").classList.remove("active");
  $("nav-domjs").classList.remove("active");
  $("nav-mock").classList.add("active");
  current = null;
  renderMockList();
}

function renderMockList() {
  $("mock-list").innerHTML = MOCK_TESTS.map((m) => {
    const inProgress = mockSession && mockSession.mockId === m.id;
    const btnLabel = inProgress ? "Resume" : "Start Mock";
    return `<div class="mock-card">
        <div class="mock-card-title">${escapeHtml(m.title)}</div>
        <div class="mock-card-desc">${escapeHtml(m.desc)}</div>
        <div class="mock-card-parts">
          ${m.parts.map((p, i) => `<span class="mock-part-chip">Part ${i + 1} · ${escapeHtml(p.label)}</span>`).join("")}
        </div>
        <button class="btn btn-submit" data-mock="${m.id}">${btnLabel}</button>
      </div>`;
  }).join("");
  document.querySelectorAll("#mock-list [data-mock]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const m = MOCK_TESTS.find((x) => x.id === btn.dataset.mock);
      if (mockSession && mockSession.mockId === m.id) resumeMock();
      else startMock(m);
    });
  });

  const hist = mockHistory().slice().reverse();
  $("mock-history").innerHTML = hist.length
    ? hist.map((h, i) => {
        const m = MOCK_TESTS.find((x) => x.id === h.mockId);
        const passed = Object.values(h.results).filter((r) => r && r.passed).length;
        const total = m ? m.parts.length : Object.keys(h.results).length;
        const mins = Math.round(h.elapsedMs / 60000);
        return `<div class="mock-history-row" data-idx="${hist.length - 1 - i}">
            <div>
              <div>${escapeHtml((m && m.title) || h.mockId)}</div>
              <div class="mock-history-when">${new Date(h.finishedAt).toLocaleString()} · ${mins} min used</div>
            </div>
            <div class="mock-history-score">${passed}/${total} passed</div>
            <div class="mock-history-when">View →</div>
          </div>`;
      }).join("")
    : `<p style="color:var(--text-dim);font-size:13px">No mock attempts yet.</p>`;
  document.querySelectorAll("#mock-history [data-idx]").forEach((row) => {
    row.addEventListener("click", () => renderMockSummary(mockHistory()[+row.dataset.idx]));
  });
}

function startMock(m) {
  mockSession = {
    mockId: m.id,
    parts: m.parts,
    startedAt: Date.now(),
    durationMs: m.durationMin * 60000,
    current: 0,
    results: {},
  };
  saveMockSession();
  resumeMock();
}

function resumeMock() {
  if (!mockSession) return;
  startMockTicker();
  mockGoToPart(mockSession.current || 0);
}

async function mockGoToPart(index) {
  if (!mockSession) return;
  mockSession.current = index;
  saveMockSession();
  const part = mockSession.parts[index];
  await openProblem(part.pid);
  renderMockBar();
}

function startMockTicker() {
  $("mock-bar").classList.remove("hidden");
  if (mockTickHandle) clearInterval(mockTickHandle);
  mockTickHandle = setInterval(tickMockTimer, 1000);
  tickMockTimer();
}

function tickMockTimer() {
  if (!mockSession) return;
  const remaining = mockSession.startedAt + mockSession.durationMs - Date.now();
  if (remaining <= 0) {
    finishMock();
    return;
  }
  renderMockBar(remaining);
}

function renderMockBar(remainingOverride) {
  if (!mockSession) return;
  const m = MOCK_TESTS.find((x) => x.id === mockSession.mockId);
  const remaining = remainingOverride != null
    ? remainingOverride
    : mockSession.startedAt + mockSession.durationMs - Date.now();
  const mins = Math.max(0, Math.floor(remaining / 60000));
  const secs = Math.max(0, Math.floor((remaining % 60000) / 1000));
  const timerEl = $("mock-bar-timer");
  timerEl.textContent = `${String(mins).padStart(2, "0")}:${String(secs).padStart(2, "0")}`;
  timerEl.classList.toggle("low", remaining < 5 * 60000);
  $("mock-bar-label").textContent = (m && m.title) || "Mock Test";
  $("mock-bar-parts").innerHTML = mockSession.parts
    .map((p, i) => {
      const r = mockSession.results[p.pid];
      // "active" (which part is open) and "done-pass"/"done-fail" (whether it's been
      // submitted successfully) are independent — a part can be both at once, so the
      // status is encoded in the icon rather than relying on a single mutually
      // exclusive CSS class to convey both facts.
      const activeClass = i === mockSession.current ? "active" : "";
      const doneClass = r ? (r.passed ? "done-pass" : "done-fail") : "";
      const icon = r ? (r.passed ? " ✓" : " ✗") : "";
      return `<button class="mock-part-btn ${activeClass} ${doneClass}" data-i="${i}">${i + 1}. ${escapeHtml(p.label)}${icon}</button>`;
    })
    .join("");
  $("mock-bar-parts").querySelectorAll("[data-i]").forEach((btn) => {
    btn.addEventListener("click", () => mockGoToPart(+btn.dataset.i));
  });
}

function finishMock() {
  if (!mockSession) return;
  if (mockTickHandle) clearInterval(mockTickHandle);
  mockTickHandle = null;
  $("mock-bar").classList.add("hidden");

  const record = {
    mockId: mockSession.mockId,
    startedAt: mockSession.startedAt,
    finishedAt: Date.now(),
    elapsedMs: Date.now() - mockSession.startedAt,
    results: mockSession.results,
  };
  const hist = mockHistory();
  hist.push(record);
  saveMockHistory(hist);

  mockSession = null;
  saveMockSession();
  setRoute("#mock");
  renderMockSummary(record);
}

function renderMockSummary(record) {
  $("problem-view").classList.add("hidden");
  $("list-view").classList.add("hidden");
  $("pdf-view").classList.add("hidden");
  $("practice-view").classList.add("hidden");
  $("dom-practice-view").classList.add("hidden");
  $("review-view").classList.add("hidden");
  $("attempts-view").classList.add("hidden");
  $("mock-view").classList.add("hidden");
  $("mock-summary-view").classList.remove("hidden");

  const m = MOCK_TESTS.find((x) => x.id === record.mockId);
  $("mock-summary-title").textContent = (m && m.title) || "Mock Test Result";
  const mins = Math.round(record.elapsedMs / 60000);
  const parts = (m && m.parts) || Object.keys(record.results).map((pid) => ({ pid: +pid, label: "Part" }));
  const passedCount = parts.filter((p) => record.results[p.pid] && record.results[p.pid].passed).length;

  $("mock-summary-body").innerHTML = `
    <p style="color:var(--text-dim);margin-bottom:18px">
      Finished ${new Date(record.finishedAt).toLocaleString()} · ${mins} minute${mins === 1 ? "" : "s"} used ·
      <b style="color:var(--text)">${passedCount}/${parts.length} parts passed</b>
    </p>
    <div class="mock-summary-tiles">
      ${parts.map((p, i) => {
        const r = record.results[p.pid];
        const status = !r ? "skip" : r.passed ? "pass" : "fail";
        const statusText = !r ? "Not attempted" : r.passed ? "Passed" : `Failed — ${escapeHtml(r.detail || "")}`;
        return `<div class="mock-summary-tile ${status}">
            <div class="mock-summary-part-label">Part ${i + 1}</div>
            <div class="mock-summary-part-title">${escapeHtml(p.label)}</div>
            <div class="mock-summary-part-status ${status}">${statusText}</div>
            <button class="btn btn-ghost btn-small" style="margin-top:10px" data-reopen="${p.pid}">Reopen</button>
          </div>`;
      }).join("")}
    </div>
    <button class="btn btn-submit" id="mock-retake">Start a fresh attempt</button>
  `;
  $("mock-summary-body").querySelectorAll("[data-reopen]").forEach((btn) => {
    btn.addEventListener("click", () => openProblem(+btn.dataset.reopen));
  });
  const retakeBtn = $("mock-retake");
  if (retakeBtn && m) {
    retakeBtn.addEventListener("click", () => startMock(m));
  }
}

$("mock-bar-finish").addEventListener("click", () => {
  if (confirm("Finish the mock now? You won't be able to submit further answers for it afterward.")) {
    finishMock();
  }
});
$("mock-summary-back").addEventListener("click", (e) => {
  e.preventDefault();
  showMock();
});
$("nav-mock").addEventListener("click", (e) => {
  e.preventDefault();
  showMock();
});

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
$("quiz-review").addEventListener("click", showQuizReview);
$("review-back").addEventListener("click", (e) => {
  e.preventDefault();
  backToQuiz();
});
$("nav-practice").addEventListener("click", (e) => {
  e.preventDefault();
  showPractice();
});
$("nav-domjs").addEventListener("click", (e) => {
  e.preventDefault();
  showDomPractice();
});
$("attempts-back").addEventListener("click", (e) => {
  e.preventDefault();
  showPractice();
});
$("review-expand").addEventListener("click", () => setAllReviewCards(false));
$("review-collapse").addEventListener("click", () => setAllReviewCards(true));
document.querySelectorAll(".review-filters .chip").forEach((chip) =>
  chip.addEventListener("click", () => setReviewFilter(chip.dataset.filter)),
);

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
    await syncLocalProgressToServer();
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
    await syncLocalProgressToServer();
    await loadUserProgress();
  }
  await loadProblems();

  // Resume an in-progress mock test if the browser was closed/refreshed
  // mid-session, as long as its 60-minute window hasn't already expired.
  const savedMock = loadMockSession();
  if (savedMock) {
    const remaining = savedMock.startedAt + savedMock.durationMs - Date.now();
    if (remaining > 0) {
      mockSession = savedMock;
      startMockTicker();
    } else {
      mockSession = savedMock;
      finishMock();
    }
  }

  await applyRoute();
})();
