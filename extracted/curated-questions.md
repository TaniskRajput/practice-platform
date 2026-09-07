# Curated Questions from KN Academy "Accenture Mock Test Series"

Source session: sess_6b1059da (continuation). Course: `knacademycourses.graphy.com`
course id `677fe6f13aefc560aacf5a59`.

## What was collected

| Artifact | File | Contents |
|---|---|---|
| Full course tree (20 sections, 182 items) | `extracted/course-structure.json` | every section/item with graphy `data-id` + type |
| Web/JS/SQL article bodies | `extracted/web-articles.json` | 14 articles incl. JS Function 1-3, HTML CSS, SQL Trigger, Coding Assessment Full 1/2, 8 Jan Solution, Full Paper JSON |
| Code-player items w/ hidden test cases | `extracted/code-items-full.json` | Coding 1, Mock 14/15/16 - real stdin/stdout test cases incl. hidden |
| Raw code items (truncated) | `extracted/code-items.json` | earlier partial scrape |
| SQL mock questions | `extracted/sql-mock-1.json`, `sql-mock-2.json` | 15+15 questions (mostly MCQ) |
| SQL article schemas | `extracted/sql-articles.json` | SQL - 1, SQL Query 1/2 |
| PDF direct URLs + per-PDF passwords | `extracted/pdf-urls.json`, `pdf-creds.json`, `pdf-passwords.json` | Graphy encrypts PDFs (AESV2, password = AES-decrypt of `preview/url` `p` field via `parseJData`) |
| Decrypted PDF text | `extracted/downloaded/*.txt` | 11 PDFs incl. 367-page Previous Years Coding |

## Access pattern (for future re-scrapes)

- Article content: `GET /s/courses/{cid}/articles/{aid}/get` → parse `#articleHtml` (works with session cookies only).
- Code item + hidden test cases: `GET /t/api/content/courses/{cid}/codes/{aid}/get/report?userId={uid}`
  with header `Authorization: <localStorage.microserviceAuthToken>` (Basic ...).
- PDF file URL + password: `GET /s/courses/{cid}/pdfs/{aid}/preview/url` → `{url, p}`;
  password = `parseJData(p)`: `p[32:len-32]` = base64 ciphertext, `p[len-32:]` = hex AES-128 key,
  `p[0:32]` = hex IV, AES-CBC/PKCS7 → UTF-8 UUID password.
- PDF direct: `https://d2a5xnk4s7n8a6.cloudfront.net/w/o/{org}/v/{aid}/u/{uid}/p/assets/pdfs/.../file.pdf`.

## User instructions

- Skip MCQs / mock tests that are MCQ-only (Pseudo, Networking, OS, Cyber, OOPS, Cloud,
  Security, MS Office, Cognitive, English, Live Tests).
- Focus: core coding (DSA), SQL, web-based (JS/HTML) questions.

## Curated additions to practice-platform

### DSA / core coding (stdin/stdout, java+cpp) - source: code items + Previous Years PDF
1. **Prime Hideouts (Coding Mock 14)** - primes in [L, R]; `No primes found` if none.
   5 real test cases incl. hidden (from API). `1\n10 → 2\n3\n5\n7`, `8\n10 → No primes found`.
2. **Armstrong Number (Coding Mock 15)** - classify N. `370/371/9474/407 → Armstrong Number`, `100 → Not an Armstrong Number`.
3. **Vowel Counter (Coding Mock 16)** - count vowels in lowercase word. `education → 5`.
4. **Remove Adjacent Duplicates (Coding 1 Accenture)** - `abbaca → ca`; real hidden cases.
5. **Maximum Plane Regions (PYQ PDF #3)** - N lines → max regions = N(N+1)/2 + 1.
6. **Climbing Stairs (PYQ PDF #9)** - classic DP.
7. **Sum of Binary Digits (PYQ PDF #17 Hirepro 2023)** - popcount.
8. **First-Last Combination Frequency (11 Oct 2025 set)** - most frequent first+last char pair,
   insertion order.

### SQL (schema-per-problem support added to app.py)
9. **Departments Above Average Salary (SQL Query 1 article)** - Employees/Departments;
   departments whose avg salary > overall avg.
10. **Highest Paid Employee per Department (SQL Query 2 article)** - window-free classic.
11. **E-Commerce High-Value Customers (Coding Assessment Full 1 §2)** - same family as existing
    problem 2 but 6-table schema with Products; reference solution from article.

### Web / JS (browser judge)
12. **Password Strength & Match Evaluator (Coding Assessment Full 2 §3)** - live validation,
    `#feedback-msg` green/red.
13. **Product Search Filter (PYQ Recent Set PDF)** - filter `<li data-name>` by input, initial
    value "nana", font-size 25px.

## Skipped (per user instruction / not coding-actable)
- SQL Mock-1/2 items: presented as MCQs (pick the correct query) - skipped.
- Pseudocode/Technical/OOPS/Cloud/etc. mocks: MCQ-only.
- JS Function 1-3 & HTML CSS articles: MCQ answer-reveal sets - skipped (kept in
  web-articles.json for reference).
- Accenture Code MCQ, Paper Solution, Technical All Questions Set: MCQ/PDF-only.
- Web Based Questions lab (10 mini-projects): captured in web-articles.json; too
  scaffold-heavy for automated browser tests - candidates for future manual addition.
