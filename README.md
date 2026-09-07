# PracticeCode — LeetCode-style Practice Platform

A self-contained practice platform with real compilation, real SQL execution, a live
DOM preview, and LeetCode-style judging (Run on samples, Submit on samples + hidden
tests). Originally built around 3 problems, now expanded to **15 problems** — 12 of
them curated from the KN Academy "Accenture Mock Test Series" course.

## Run it

```bash
cd practice-platform
python3 app.py
```

Then open **http://localhost:5000** (requires `flask`, plus `javac` and `g++` on PATH
for the coding problems).

## The problems

| # | Title | Difficulty | Judging |
|---|-------|-----------|---------|
| 1 | Check if Every Row and Column Contains All Numbers | Easy | `javac` / `g++` compile & run, stdin/stdout, 2 sample + 6 hidden tests |
| 2 | High-Value Completed Orders in USA (2025) | Medium | Query runs on a real SQLite database — sample dataset on Run, sample + hidden dataset on Submit |
| 3 | Bounded Counter with Status Message | Easy | Live interactive preview + automated tests that simulate button clicks in a fresh page (3 visible + 4 hidden) |
| 4 | Prime Hideouts | Easy | stdin/stdout — primes in [L, R] or `No primes found` (real hidden cases from the course) |
| 5 | Armstrong Number | Easy | stdin/stdout classification (real hidden cases: 370, 371, 9474, 407, 100, 7) |
| 6 | Vowel Counter | Easy | stdin/stdout counting (real hidden cases) |
| 7 | Remove Adjacent Duplicates | Easy | stdin/stdout stack problem (`abbaca → ca`; real hidden cases) |
| 8 | Maximum Plane Regions | Easy | stdin/stdout math (`N(N+1)/2 + 1`) |
| 9 | Climbing Stairs | Easy | stdin/stdout DP |
| 10 | Sum of Binary Digits | Easy | stdin/stdout popcount |
| 11 | Most Frequent First-Last Combination | Medium | stdin/stdout hashing with insertion-order tie handling |
| 12 | Departments Above Average Salary | Medium | SQL judged against per-problem SQLite schema + hidden dataset |
| 13 | Highest Paid Employee per Department | Medium | SQL judged against per-problem SQLite schema + hidden dataset (ties included) |
| 14 | Password Strength & Match Evaluator | Easy | Browser judge: types into both fields, checks `#feedback-msg` text + color |
| 15 | Product Search Filter | Easy | Browser judge: types into the search box, checks which `<li data-name>` items are visible/hidden |

Problems 4–15 were curated from the KN Academy course — see
`extracted/curated-questions.md` for the source of each one and what was skipped.

## Features

- LeetCode-style problem list with difficulty badges, topic chips, and solved checkmarks
- Full problem descriptions with examples, constraints, schema tables, and a hint tab
- CodeMirror editor (syntax highlighting for Java, C++, SQL, JavaScript)
- **Run** executes visible sample tests; **Submit** runs hidden tests and records a
  submission history (Submissions tab), persisting solved state and code per
  problem/language in `localStorage`
- Compile errors, runtime errors, and timeouts are surfaced verbatim
- **Auto-Structure** button: one-click code formatting for every language —
  brace-aware re-indentation for Java/C++/JavaScript (for-loops, `} else {`,
  arrow callbacks, do-while, comments, and string literals are handled) and a
  keyword formatter for SQL (clauses on their own lines, one column per line,
  subquery indentation, literals preserved)
- SQL problems have a Schema & Data tab showing the exact rows your query runs
  against (column headers are parsed from each problem's own schema)
- Web problems have a Live Preview tab where the page is fully interactive while
  you code, plus automated interaction tests on Submit
- Java judge accepts any public class name (the file is renamed to match);
  each test case runs in its own process so a crash can't corrupt later cases
- Keyboard shortcut: `Ctrl+Enter` to Run

## Layout

```
app.py               Flask server + judges (Java, C++, SQLite, browser-DOM dispatch)
problems.py          Problems 1–3 + merge of the curated set
problems_extra.py    Problems 4–15 (curated from the KN Academy course)
extracted/           Raw scraped course content + curated-questions.md provenance doc
templates/index.html SPA shell
static/app.js        Frontend logic, editor, browser-side JS judge, live preview
static/style.css     Dark LeetCode-style theme
static/vendor/       CodeMirror assets (bundled locally, no CDN needed)
```
