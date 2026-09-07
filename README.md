# PracticeCode — LeetCode-style Practice Platform

A self-contained practice platform for three problems, with real compilation, real SQL
execution, a live DOM preview, and LeetCode-style judging (Run on samples, Submit on
samples + hidden tests).

## Run it

```bash
cd practice-platform
python3 app.py
```

Then open **http://localhost:5000** (requires `flask`, plus `javac` and `g++` on PATH
for problem 1).

## The problems

| # | Title | Difficulty | Judging |
|---|-------|-----------|---------|
| 1 | Check if Every Row and Column Contains All Numbers | Easy | `javac` / `g++` compile & run against 2 sample + 5 hidden matrices |
| 2 | High-Value Completed Orders in USA (2025) | Medium | Query runs on a real SQLite database — sample dataset on Run, sample + hidden dataset on Submit (hidden dataset includes edge cases: exactly-$1000 total, wrong country/status/year) |
| 3 | Bounded Counter with Status Message | Easy | Live interactive preview (re-renders as you type) + automated tests that simulate button clicks in a fresh page (3 visible + 4 hidden) |

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
- Problem 2 has a Schema & Data tab showing the exact rows your query runs against
- Problem 3 has a Live Preview tab where the counter is fully clickable, plus
  automated click-simulation tests on Submit
- Keyboard shortcut: `Ctrl+Enter` to Run

## Layout

```
app.py               Flask server + judges (Java, C++, SQLite)
problems.py          Problem data: descriptions, boilerplates, tests, SQL datasets
templates/index.html SPA shell
static/app.js        Frontend logic, editor, browser-side JS judge, live preview
static/style.css     Dark LeetCode-style theme
static/vendor/       CodeMirror assets (bundled locally, no CDN needed)
```
