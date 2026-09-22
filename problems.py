"""
Problem definitions for the practice platform.
Each problem carries its description (HTML), boilerplates, and test cases.
Server-side judged problems (java/cpp/sql) include per-database reference solutions;
browser-judged problems (javascript DOM) define test steps interpreted by the frontend.
Problems 4-15 (curated from the KN Academy course) live in problems_extra.py.
"""

from problems_extra import NEW_PROBLEMS, QUIZ_PROBLEMS, PDF_QUIZ_PROBLEMS
from problems_extra_pdfbanks import PDF_BANK_QUIZ_PROBLEMS
from problems_pseudocode import PSEUDOCODE_QUIZ
from problems_2026 import CODE_2026_PROBLEMS, WEB_2026_PROBLEMS, QUIZ_WEB_MCQ_2026, QUIZ_SQL_2026
from problems_accenture_coding_pdf import ACCENTURE_CODING_PDF_PROBLEMS
from practice_sets import PRACTICE_SETS
from problems_webdev_exam import WEBDEV_EXAM_PROBLEMS
from problems_sql_exam import SQL_EXAM_PROBLEMS
from problems_dom_practice import DOM_PRACTICE_PROBLEMS

def _db(name, hidden, schema, seed, reference_query):
    return {
        "name": name,
        "hidden": hidden,
        "schema": schema,
        "seed": seed,
        "reference_query": reference_query,
    }


PROBLEMS = [
    # ------------------------------------------------------------------ #
    # 1. Check if Every Row and Column Contains All Numbers
    # ------------------------------------------------------------------ #
    {
        "id": 1,
        "slug": "check-valid-matrix",
        "title": "Check if Every Row and Column Contains All Numbers",
        "difficulty": "Easy",
        "topics": ["Arrays", "Hash Table", "Matrix"],
        "judge": "server",
        "languages": ["java", "cpp", "python"],
        "description": """
<p>An <code>n x n</code> matrix is <b>valid</b> if every row and every column contains all the integers
from <code>1</code> to <code>n</code> (inclusive).</p>
<p>Given an <code>n x n</code> integer matrix, print <code>true</code> if the matrix is valid,
otherwise print <code>false</code>.</p>
<h3>Input format:</h3>
<p>First line: <code>n</code>. Then <code>n</code> lines, each with <code>n</code> space-separated integers.</p>
<h3>Example 1:</h3>
<pre>Input:            Output:
3                 true
1 2 3
3 1 2
2 3 1</pre>
<p>Explanation: n = 3. Every row and column contains the numbers 1, 2, and 3.</p>
<h3>Example 2:</h3>
<pre>Input:            Output:
3                 false
1 1 1
1 2 3
1 2 3</pre>
<p>Explanation: The first row does not contain the numbers 2 and 3.</p>
<h3>Constraints:</h3>
<ul>
  <li><code>1 &lt;= n &lt;= 100</code></li>
  <li><code>1 &lt;= matrix[i][j] &lt;= n</code></li>
</ul>
""",
        "hint": "For a row (or column) to contain every number from 1 to n exactly once, the set of values "
                 "in it must have size n, and every value must be within [1, n]. Try using a set per row "
                 "and per column, or a frequency table.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] matrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }

        // TODO: check every row and column contains 1..n exactly once
        boolean valid = true;

        System.out.println(valid);
    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<vector<int>> matrix(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> matrix[i][j];

    // TODO: check every row and column contains 1..n exactly once
    bool valid = true;

    cout << (valid ? "true" : "false") << endl;
    return 0;
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\nmatrix = [[read_int() for _ in range(n)] for _ in range(n)]\n\n# TODO: check every row and column contains 1..n exactly once\nvalid = True\n\nprint(str(valid).lower())",
        },
        "tests": [
            {"input": "3\n1 2 3\n3 1 2\n2 3 1", "expected": "true", "hidden": False},
            {"input": "3\n1 1 1\n1 2 3\n1 2 3", "expected": "false", "hidden": False},
            {"input": "1\n1", "expected": "true", "hidden": True},
            {"input": "2\n1 2\n2 1", "expected": "true", "hidden": True},
            {"input": "2\n1 2\n1 2", "expected": "false", "hidden": True},
            {"input": "3\n1 2 3\n2 3 1\n1 2 3", "expected": "false", "hidden": True},
            {"input": "4\n1 2 3 4\n2 3 4 1\n3 4 1 2\n4 1 2 3", "expected": "true", "hidden": True},
            {"input": "4\n1 2 3 4\n1 2 3 4\n1 2 3 4\n1 2 3 4", "expected": "false", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 2. High-Value Completed Orders in USA (2025)
    # ------------------------------------------------------------------ #
    {
        "id": 2,
        "slug": "high-value-orders-usa",
        "title": "High-Value Completed Orders in USA (2025)",
        "difficulty": "Medium",
        "topics": ["Database", "SQL"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: Customers</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| customer_name | varchar |
| country_id    | int     |
+---------------+---------+</pre>
<p><code>customer_id</code> is the unique identifier for this table.<br>
<code>country_id</code> is a foreign key referencing the <code>Countries</code> table.</p>

<h3>Table: Countries</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| country_id    | int     |
| country_name  | varchar |
+---------------+---------+</pre>
<p><code>country_id</code> is the unique identifier for this table.</p>

<h3>Table: Orders</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| customer_id   | int     |
| status_id     | int     |
| order_date    | date    |
+---------------+---------+</pre>
<p><code>order_id</code> is the unique identifier for this table.<br>
<code>customer_id</code> references <code>Customers</code>, and <code>status_id</code> references
<code>Order_Status</code>.</p>

<h3>Table: Order_Status</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| status_id     | int     |
| status_name   | varchar |
+---------------+---------+</pre>
<p><code>status_id</code> is the unique identifier for this table.</p>

<h3>Table: Order_Items</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| quantity      | int     |
| unit_price    | decimal |
+---------------+---------+</pre>
<p>Each row stores one line item of an order. An order's amount is
<code>quantity * unit_price</code> summed over all its items.</p>

<h3>Problem:</h3>
<p>Write a solution to report the <b>name</b>, the <b>number of completed orders</b>, and the
<b>total amount spent</b> for each customer satisfying the following conditions:</p>
<ul>
  <li>The customer resides in <code>'USA'</code>.</li>
  <li>The order status is <code>'Completed'</code>.</li>
  <li>The order was placed in the year <code>2025</code>.</li>
  <li>The total amount spent across all qualifying completed orders <b>exceeds</b> <code>$1000</code>.</li>
</ul>
<p>Return the result table ordered by <code>total_spent</code> in <b>descending</b> order.
Name your output columns <code>customer_name</code>, <code>total_orders</code>, <code>total_spent</code>.</p>

<h3>Example Output:</h3>
<pre>+---------------+--------------+-------------+
| customer_name | total_orders | total_spent |
+---------------+--------------+-------------+
| Alice Smith   | 3            | 2450.00     |
| Bob Johnson   | 2            | 1120.50     |
+---------------+--------------+-------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b> (use <code>strftime('%Y', order_date)</code> for the year if needed).</li>
  <li>An order counts toward a customer only once even if it has multiple items — use
      <code>COUNT(DISTINCT order_id)</code>.</li>
</ul>
""",
        "hint": "Join all five tables, filter in the WHERE clause (country, status, year), aggregate with "
                 "GROUP BY customer, then filter the aggregated total with HAVING (not WHERE). Watch out: "
                 "an order with multiple items appears multiple times in the join — count orders with "
                 "COUNT(DISTINCT order_id).",
        "boilerplate": {
            "sql": """-- Write your SQLite query below
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY""",
        },
        "tests": [],  # SQL judged against databases below
        "samples": [0],
        "databases": [
            {
                "name": "Sample database",
                "hidden": False,
                "schema": """
CREATE TABLE Customers (customer_id INTEGER PRIMARY KEY, customer_name TEXT, country_id INTEGER);
CREATE TABLE Countries (country_id INTEGER PRIMARY KEY, country_name TEXT);
CREATE TABLE Orders (order_id INTEGER PRIMARY KEY, customer_id INTEGER, status_id INTEGER, order_date TEXT);
CREATE TABLE Order_Status (status_id INTEGER PRIMARY KEY, status_name TEXT);
CREATE TABLE Order_Items (order_id INTEGER, quantity INTEGER, unit_price REAL);
""",
                "seed": {
                    "Countries": [
                        (1, "USA"), (2, "Canada"), (3, "UK"),
                    ],
                    "Customers": [
                        (1, "Alice Smith", 1),
                        (2, "Bob Johnson", 1),
                        (3, "Carol White", 1),
                        (4, "David Brown", 2),
                        (5, "Emma Davis", 1),
                    ],
                    "Order_Status": [
                        (1, "Completed"), (2, "Processing"), (3, "Cancelled"),
                    ],
                    "Orders": [
                        (101, 1, 1, "2025-01-15"),
                        (102, 1, 1, "2025-03-20"),
                        (103, 1, 1, "2025-06-05"),
                        (104, 2, 1, "2025-02-10"),
                        (105, 2, 1, "2025-08-30"),
                        (106, 3, 1, "2025-04-12"),
                        (107, 4, 1, "2025-05-01"),
                        (108, 5, 2, "2025-07-19"),
                        (109, 1, 2, "2025-09-09"),
                        (110, 2, 1, "2024-12-31"),
                    ],
                    "Order_Items": [
                        (101, 2, 300.00),   # 600.00
                        (102, 1, 850.00),   # 850.00   -> Alice: 2450.00 (3 orders)
                        (103, 2, 500.00),   # 1000.00
                        (104, 3, 150.50),   # 451.50
                        (105, 1, 669.00),   # 669.00   -> Bob: 1120.50 (2 orders)
                        (106, 3, 300.00),   # 900.00   -> Carol: below 1000, excluded
                        (107, 5, 1000.00),  # 5000.00  -> David: Canada, excluded
                        (108, 2, 400.00),   # 800.00   -> Emma: Processing, excluded
                        (109, 1, 700.00),   #          -> Processing status, excluded
                        (110, 4, 250.00),   #          -> year 2024, excluded
                    ],
                },
                "reference_query": """
SELECT cu.customer_name AS customer_name,
       COUNT(DISTINCT o.order_id) AS total_orders,
       SUM(oi.quantity * oi.unit_price) AS total_spent
FROM Customers cu
JOIN Countries co ON cu.country_id = co.country_id
JOIN Orders o ON o.customer_id = cu.customer_id
JOIN Order_Status s ON o.status_id = s.status_id
JOIN Order_Items oi ON oi.order_id = o.order_id
WHERE co.country_name = 'USA'
  AND s.status_name = 'Completed'
  AND CAST(strftime('%Y', o.order_date) AS INTEGER) = 2025
GROUP BY cu.customer_id, cu.customer_name
HAVING SUM(oi.quantity * oi.unit_price) > 1000
ORDER BY total_spent DESC
""",
            },
            {
                "name": "Hidden database",
                "hidden": True,
                "schema": """
CREATE TABLE Customers (customer_id INTEGER PRIMARY KEY, customer_name TEXT, country_id INTEGER);
CREATE TABLE Countries (country_id INTEGER PRIMARY KEY, country_name TEXT);
CREATE TABLE Orders (order_id INTEGER PRIMARY KEY, customer_id INTEGER, status_id INTEGER, order_date TEXT);
CREATE TABLE Order_Status (status_id INTEGER PRIMARY KEY, status_name TEXT);
CREATE TABLE Order_Items (order_id INTEGER, quantity INTEGER, unit_price REAL);
""",
                "seed": {
                    "Countries": [
                        (1, "USA"), (2, "Canada"), (3, "UK"),
                    ],
                    "Customers": [
                        (11, "Frank Moore", 1),
                        (12, "Grace Lee", 1),
                        (13, "Henry Walker", 1),
                        (14, "Ivy Clark", 3),
                        (15, "Jack Hall", 1),
                        (16, "Karen Young", 1),
                    ],
                    "Order_Status": [
                        (1, "Completed"), (2, "Processing"), (3, "Cancelled"),
                    ],
                    "Orders": [
                        (201, 11, 1, "2025-02-01"),   # Frank: exactly 1000.00 -> excluded (not >)
                        (202, 11, 1, "2025-06-15"),
                        (203, 12, 1, "2025-03-03"),   # Grace: 3300.00
                        (204, 12, 1, "2025-07-07"),
                        (205, 13, 1, "2025-01-20"),   # Henry: 1500.00
                        (206, 14, 1, "2025-05-05"),   # Ivy: UK -> excluded
                        (207, 15, 3, "2025-04-04"),   # Jack: only cancelled -> excluded
                        (208, 16, 1, "2024-08-08"),   # Karen: 2024 -> excluded
                        (209, 16, 1, "2025-10-01"),   # Karen: 2025 completed 2200.00
                    ],
                    "Order_Items": [
                        (201, 1, 500.00),   # 500.00
                        (202, 1, 500.00),   # 500.00 -> Frank total 1000.00, excluded
                        (203, 2, 900.00),   # 1800.00
                        (204, 3, 500.00),   # 1500.00 -> Grace total 3300.00
                        (205, 3, 500.00),   # 1500.00 -> Henry total 1500.00
                        (206, 4, 900.00),   # 3600.00 -> UK, excluded
                        (207, 2, 800.00),   # 1600.00 -> cancelled, excluded
                        (208, 4, 300.00),   # 1200.00 -> 2024, excluded
                        (209, 2, 1100.00),  # 2200.00 -> Karen total 2200.00
                    ],
                },
                "reference_query": """
SELECT cu.customer_name AS customer_name,
       COUNT(DISTINCT o.order_id) AS total_orders,
       SUM(oi.quantity * oi.unit_price) AS total_spent
FROM Customers cu
JOIN Countries co ON cu.country_id = co.country_id
JOIN Orders o ON o.customer_id = cu.customer_id
JOIN Order_Status s ON o.status_id = s.status_id
JOIN Order_Items oi ON oi.order_id = o.order_id
WHERE co.country_name = 'USA'
  AND s.status_name = 'Completed'
  AND CAST(strftime('%Y', o.order_date) AS INTEGER) = 2025
GROUP BY cu.customer_id, cu.customer_name
HAVING SUM(oi.quantity * oi.unit_price) > 1000
ORDER BY total_spent DESC
""",
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # 3. Bounded Counter with Status Message
    # ------------------------------------------------------------------ #
    {
        "id": 3,
        "slug": "bounded-counter",
        "title": "Bounded Counter with Status Message",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Implement the behavior for an interactive counter with the following HTML layout:</p>
<pre>&lt;div class="counter-container"&gt;
  &lt;h1 id="count"&gt;0&lt;/h1&gt;
  &lt;div class="btn-group"&gt;
    &lt;button id="dec-btn"&gt;-&lt;/button&gt;
    &lt;button id="inc-btn"&gt;+&lt;/button&gt;
  &lt;/div&gt;
  &lt;p id="status-msg"&gt;&lt;/p&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript to fulfill the following specifications:</p>
<ul>
  <li><b>Upper Bound:</b> Clicking <code>#inc-btn</code> increments the counter value displayed in
      <code>#count</code> by 1, up to a maximum value of <code>10</code>.</li>
  <li><b>Lower Bound:</b> Clicking <code>#dec-btn</code> decrements the counter value displayed in
      <code>#count</code> by 1, down to a minimum value of <code>0</code>.</li>
  <li><b>Status Message:</b>
    <ul>
      <li>When the count reaches <code>10</code>, <code>#status-msg</code> must display
          <code>"Maximum limit reached!"</code>.</li>
      <li>When the count reaches <code>0</code>, <code>#status-msg</code> must display
          <code>"Minimum limit reached!"</code>.</li>
      <li>When the count is strictly between 1 and 9, <code>#status-msg</code> must be cleared
          (<code>""</code>).</li>
    </ul>
  </li>
  <li><b>Initial State:</b> On initial load, the counter displays <code>0</code> and
      <code>#status-msg</code> displays <code>"Minimum limit reached!"</code>.</li>
</ul>
<p>Use the <b>Preview</b> tab to interact with your counter live while you code — the preview
re-renders automatically as you type. Submitting runs automated tests that simulate button clicks
in a fresh page.</p>
""",
        "hint": "Read the current value with parseInt(countEl.textContent, 10), clamp it with "
                 "Math.min / Math.max, and update the status message inside a single update() helper "
                 "called after every change and once on initialization.",
        "boilerplate": {
            "javascript": """function initializeCounter() {
  const countEl = document.getElementById('count');
  const incBtn = document.getElementById('inc-btn');
  const decBtn = document.getElementById('dec-btn');
  const statusEl = document.getElementById('status-msg');

  // TODO: wire up the buttons and the status message
}

initializeCounter();
""",
        },
        "tests": [],  # browser-judged; step definitions below are consumed by the frontend
        "samples": [0, 1, 2],
        "browser_html": """<div class="counter-container">
  <h1 id="count">0</h1>
  <div class="btn-group">
    <button id="dec-btn">-</button>
    <button id="inc-btn">+</button>
  </div>
  <p id="status-msg"></p>
</div>""",
        "browser_tests": [
            {
                "name": "Initial state: shows 0 and 'Minimum limit reached!'",
                "hidden": False,
                "steps": [],
                "expect": {"count": "0", "msg": "Minimum limit reached!"},
            },
            {
                "name": "Decrement at 0 stays at the minimum",
                "hidden": False,
                "steps": [{"click": "dec-btn"}],
                "expect": {"count": "0", "msg": "Minimum limit reached!"},
            },
            {
                "name": "Increment works and clears the message",
                "hidden": False,
                "steps": [{"click": "inc-btn"}],
                "expect": {"count": "1", "msg": ""},
            },
            {
                "name": "Increments up to 10 and shows maximum message",
                "hidden": True,
                "steps": [{"click": "inc-btn"} for _ in range(10)],
                "expect": {"count": "10", "msg": "Maximum limit reached!"},
            },
            {
                "name": "Increment at 10 stays clamped",
                "hidden": True,
                "steps": [{"click": "inc-btn"} for _ in range(11)],
                "expect": {"count": "10", "msg": "Maximum limit reached!"},
            },
            {
                "name": "Decrement from 10 clears the message",
                "hidden": True,
                "steps": [{"click": "inc-btn"} for _ in range(10)] + [{"click": "dec-btn"}],
                "expect": {"count": "9", "msg": ""},
            },
            {
                "name": "Full cycle back down to 0",
                "hidden": True,
                "steps": [{"click": "inc-btn"} for _ in range(10)] + [{"click": "dec-btn"} for _ in range(10)],
                "expect": {"count": "0", "msg": "Minimum limit reached!"},
            },
        ],
    },
]

PROBLEMS.append(
    {
        "id": 27,
        "slug": "array-index-transformation-sum",
        "title": "Array Index Transformation Sum (8th Sept Shift 1)",
        "difficulty": "Easy",
        "topics": ["Arrays", "Math"],
        "judge": "server",
        "languages": ["java", "cpp", "python"],
        "description": """<p class="text-muted">Accenture — 8th Sept Shift 1</p>
<p>Given an array of integers <code>nums</code>, perform the following transformation on each
element based on its <b>0-based index</b> <code>i</code>:</p>
<ol>
  <li>Subtract <code>(i % 7) * 3</code> from the element.</li>
  <li>If the original element <code>nums[i]</code> is divisible by 11, add <code>nums[i] / 11</code>
  to the modified value.</li>
</ol>
<p>Return the <b>total sum</b> of all elements in the array after applying these transformations.</p>
<h3>Input Format</h3>
<p>The first line contains an integer <code>n</code> — the number of elements.<br>
The second line contains <code>n</code> space-separated integers <code>nums[0] .. nums[n-1]</code>.</p>
<h3>Output Format</h3>
<p>Print a single integer — the total sum after the transformations.</p>
<h3>Sample Test Case:</h3>
<pre>Input:
5
10 20 30 40 50

Output:
120</pre>
<p class="text-muted">Explanation: modified values are <code>10, 17, 24, 31, 38</code> —
each index i loses <code>(i % 7) * 3</code>; none of the originals is divisible by 11, so the sum
is <code>10+17+24+31+38 = 120</code>.</p>
""",
        "hint": "Walk the array once keeping the 0-based index i. Subtract (i % 7) * 3 from each element, and only if the ORIGINAL nums[i] % 11 == 0 additionally add nums[i] / 11 (integer division). Sum everything. Note the subtraction continues cycling i%7 = 0,1,2,3,4,5,6,0,1,... for i >= 7.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] nums = new long[n];
        for (int i = 0; i < n; i++) nums[i] = sc.nextLong();

        // TODO: apply the transformation and print the total sum
    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];

    // TODO: apply the transformation and print the total sum
    return 0;
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\nnums = [read_int() for _ in range(n)]\n\n# TODO: apply the transformation and print the total sum\nprint(0)",
        },
        "tests": [
            {"input": "5\n10 20 30 40 50", "expected": "120", "hidden": False},
            {"input": "1\n5", "expected": "5", "hidden": False},
            {"input": "10\n10 20 30 40 50 60 70 80 90 100", "expected": "478", "hidden": True},
            {"input": "12\n11 22 33 44 55 66 77 88 99 110 121 132", "expected": "843", "hidden": True},
            {"input": "8\n100 100 100 100 100 100 100 100", "expected": "737", "hidden": True},
            {"input": "9\n-11 0 7 14 21 28 35 42 49", "expected": "118", "hidden": True},
            {"input": "1\n22", "expected": "24", "hidden": True},
        ],
        "samples": [0, 1],
    }
)

PROBLEMS.append(
    {
        "id": 28,
        "slug": "equivalent-prefix-sum",
        "title": "Equivalent Prefix Sum (8th Sept Shift 2)",
        "difficulty": "Medium",
        "topics": ["Math", "Binary Search", "Number Theory"],
        "judge": "server",
        "languages": ["java", "cpp", "python"],
        "description": """<p class="text-muted">Accenture — 8th Sept Shift 2</p>
<p>You are given a target positive integer <code>N</code>.</p>
<p>For any integer <code>X</code>, define its <b>Equivalent Sum</b> <code>EqSum(X)</code> as the
sum of all prefix sub-numbers formed by reading <code>X</code> from left to right. If
<code>X</code> is represented as a string of digits <code>d1 d2 ... dk</code>:</p>
<pre>EqSum(X) = d1 + int(d1 d2) + ... + int(d1 d2 ... dk)</pre>
<p>For example, for <code>X = 112</code>:</p>
<pre>EqSum(112) = 1 + 11 + 112 = 124</pre>
<p><b>Goal:</b> Find the integer <code>X</code> such that <code>EqSum(X) = N</code>. If no such
<code>X</code> exists, print <code>-1</code>.</p>
<h3>Input Format</h3>
<p>A single integer <code>N</code> <span class="text-muted">(1 &le; N &le; 10<sup>18</sup>)</span>.</p>
<h3>Output Format</h3>
<p>Print the unique <code>X</code> with <code>EqSum(X) = N</code>, or <code>-1</code> if none exists.</p>
<h3>Sample Test Cases:</h3>
<pre>Input:  124        Input:  112        Input:  10
Output: 112        Output: 101        Output: -1</pre>
<p class="text-muted">Explanation: <code>EqSum(112) = 1 + 11 + 112 = 124</code>,
<code>EqSum(101) = 1 + 10 + 101 = 112</code>, and no <code>X</code> has
<code>EqSum(X) = 10</code> (since <code>EqSum(9) = 9</code> but <code>EqSum(10) = 11</code>).</p>
""",
        "hint": "EqSum is STRICTLY increasing: EqSum(X) > X and each step adds X's own value, so EqSum(X+1) > EqSum(X). That means at most one X can map to N. Binary search X in [1, N]: compute EqSum(mid) by repeatedly taking prefixes (mid, mid/10, mid/100, ... while > 0) and summing — use 64-bit integers. If EqSum(mid) == N return mid; if smaller, go right; else go left. If the search space empties, print -1.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    // sum of all prefixes of x: x + x/10 + x/100 + ...
    static long eqSum(long x) {
        long s = 0;
        while (x > 0) {
            s += x;
            x /= 10;
        }
        return s;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();

        // TODO: binary search the unique X with eqSum(X) == n, or print -1
    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

// sum of all prefixes of x: x + x/10 + x/100 + ...
long long eqSum(long long x) {
    long long s = 0;
    while (x > 0) {
        s += x;
        x /= 10;
    }
    return s;
}

int main() {
    long long n;
    cin >> n;

    // TODO: binary search the unique X with eqSum(X) == n, or print -1
    return 0;
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\n\n# TODO: binary search the unique X with eqSum(X) == n, or print -1\nprint(-1)",
        },
        "tests": [
            {"input": "124", "expected": "112", "hidden": False},
            {"input": "112", "expected": "101", "hidden": False},
            {"input": "10", "expected": "-1", "hidden": False},
            {"input": "1", "expected": "1", "hidden": True},
            {"input": "11", "expected": "10", "hidden": True},
            {"input": "1107", "expected": "999", "hidden": True},
            {"input": "1108", "expected": "-1", "hidden": True},
            {"input": "1111104", "expected": "999999", "hidden": True},
            {"input": "1000000000000", "expected": "900000000001", "hidden": True},
        ],
        "samples": [0, 1, 2],
    }
)

PROBLEMS.append(
    {
        "id": 3099,
        "slug": "count-squares-ending-in-digit",
        "title": "Count Numbers Whose Square Ends in a Given Digit (20th Sept Exam)",
        "difficulty": "Easy",
        "topics": ["Math", "Loops"],
        "judge": "server",
        "languages": ["java", "cpp", "python"],
        "description": """<p class="text-muted">Accenture — 20th Sept Exam</p>
<p>You are given two integers <code>N</code> and <code>D</code>. For every integer <code>i</code>
from <code>1</code> to <code>N</code>, compute <code>i&sup2;</code> and check whether its
<b>last digit</b> equals <code>D</code>. Print how many values of <code>i</code> satisfy this.</p>
<h3>Example</h3>
<pre>N = 5, D = 9

i     i&sup2;     last digit
1     1     1
2     4     4
3     9     9   &larr; matches D = 9
4     16    6
5     25    5

Count = 1</pre>
<h3>Input Format</h3>
<p>Line 1: two space-separated integers <code>N</code> and <code>D</code>.</p>
<h3>Output Format</h3>
<p>Print a single integer &mdash; the count of values in <code>[1, N]</code> whose square ends in
digit <code>D</code>.</p>
<h3>Constraints</h3>
<ul>
  <li><code>1 &lt;= N &lt;= 10^6</code></li>
  <li><code>0 &lt;= D &lt;= 9</code></li>
</ul>
""",
        "hint": "Loop i from 1 to N, compute i*i % 10, and increment a counter whenever it equals D. "
                 "(The last digit of i^2 only depends on the last digit of i, repeating every 10 values, "
                 "so you could also solve it in O(1) per block of 10 — but a direct loop is simple and "
                 "fast enough here.)",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int d = sc.nextInt();

        // TODO: count how many i in [1, n] have (i*i) % 10 == d
        int count = 0;

        System.out.println(count);
    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n, d;
    cin >> n >> d;

    // TODO: count how many i in [1, n] have (i*i) % 10 == d
    long long count = 0;

    cout << count << endl;
    return 0;
}""", "python": "import sys\n_data = sys.stdin.read().split()\nn = int(_data[0])\nd = int(_data[1])\n\n# TODO: count how many i in [1, n] have (i*i) % 10 == d\ncount = 0\n\nprint(count)",
        },
        "tests": [
            {"input": "5 9", "expected": "1", "hidden": False},
            {"input": "10 6", "expected": "2", "hidden": False},
            {"input": "1 1", "expected": "1", "hidden": True},
            {"input": "1 0", "expected": "0", "hidden": True},
            {"input": "20 4", "expected": "4", "hidden": True},
            {"input": "100 6", "expected": "20", "hidden": True},
            {"input": "50 0", "expected": "5", "hidden": True},
            {"input": "1000 5", "expected": "100", "hidden": True},
        ],
        "samples": [0, 1],
    }
)

PROBLEMS.append(
    {
        "id": 3100,
        "slug": "mountain-trail-elevation",
        "title": "Mountain Trail Elevation (Max Bitonic Subarray Sum) (18th Sept Exam · Slot 1)",
        "difficulty": "Medium",
        "topics": ["Arrays", "Dynamic Programming"],
        "judge": "server",
        "languages": ["java", "cpp", "python"],
        "description": """<p class="text-muted">Accenture &mdash; 17 &amp; 18 Sept Exam, Slot 1</p>
<p>A person is travelling along a mountain trail and records the elevation at each checkpoint in an
array <code>A</code> of size <code>N</code>.</p>
<p>A valid <b>mountain route</b> must follow these strict rules:</p>
<ul>
  <li>Must be a <b>contiguous subarray</b> of checkpoints.</li>
  <li>Elevation must <b>strictly increase</b> while moving toward the peak.</li>
  <li>At one checkpoint, the person reaches the peak.</li>
  <li>After the peak, elevation must <b>strictly decrease</b>.</li>
  <li>Must contain at least <b>3 checkpoints</b> (at least 1 step up and 1 step down).</li>
</ul>
<p>Find the <b>maximum possible sum</b> of elevations in any valid mountain route. If no valid route
exists, print <code>0</code>.</p>
<h3>Example</h3>
<pre>Input:
N = 9
A = [2, 4, 6, 9, 7, 5, 3, 1, 4]

Output:
37</pre>
<p class="text-muted">Explanation: the route <code>[2, 4, 6, 9, 7, 5, 3, 1]</code> strictly increases
to the peak <code>9</code> and then strictly decreases to <code>1</code>. Its sum is
<code>2+4+6+9+7+5+3+1 = 37</code>. The final <code>4</code> breaks the decreasing run, so it cannot
extend this route.</p>
<h3>Input Format</h3>
<p>Line 1: <code>N</code>. Line 2: <code>N</code> space-separated integers <code>A[0] .. A[N-1]</code>.</p>
<h3>Output Format</h3>
<p>Print a single integer &mdash; the maximum mountain-route sum, or <code>0</code> if none exists.</p>
<h3>Constraints</h3>
<ul>
  <li><code>1 &lt;= N &lt;= 10^5</code></li>
  <li><code>-10^9 &lt;= A[i] &lt;= 10^9</code></li>
</ul>
""",
        "hint": "For each index i, compute leftSum[i]/leftLen[i]: the sum and length of the strictly "
                 "increasing run of A ending at i. Compute rightSum[i]/rightLen[i] the same way for the "
                 "strictly decreasing run starting at i. Index i can be a peak only if leftLen[i] >= 2 "
                 "and rightLen[i] >= 2 (a real step up AND a real step down); its route sum is then "
                 "leftSum[i] + rightSum[i] - A[i] (A[i] is counted in both halves). Take the max over "
                 "all valid peaks, or 0 if none exist. This runs in O(N) with two passes.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] a = new long[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextLong();

        // TODO: find the maximum sum over all strictly-increasing-then-strictly-decreasing
        // contiguous subarrays with at least 3 elements; print 0 if none exists
        long best = 0;

        System.out.println(best);
    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    // TODO: find the maximum sum over all strictly-increasing-then-strictly-decreasing
    // contiguous subarrays with at least 3 elements; print 0 if none exists
    long long best = 0;

    cout << best << endl;
    return 0;
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\na = [read_int() for _ in range(n)]\n\n# TODO: find the maximum sum over all strictly-increasing-then-strictly-decreasing\n# contiguous subarrays with at least 3 elements; print 0 if none exists\nbest = 0\n\nprint(best)",
        },
        "tests": [
            {"input": "9\n2 4 6 9 7 5 3 1 4", "expected": "37", "hidden": False},
            {"input": "3\n1 5 2", "expected": "8", "hidden": False},
            {"input": "5\n1 2 3 4 5", "expected": "0", "hidden": True},
            {"input": "5\n5 4 3 2 1", "expected": "0", "hidden": True},
            {"input": "8\n1 3 5 4 2 6 8 7", "expected": "23", "hidden": True},
            {"input": "6\n10 20 30 25 15 5", "expected": "105", "hidden": True},
            {"input": "1\n5", "expected": "0", "hidden": True},
            {"input": "3\n1 2 2", "expected": "0", "hidden": True},
        ],
        "samples": [0, 1],
    }
)

PROBLEMS.append(
    {
        "id": 3101,
        "slug": "robot-energy-peak-route",
        "title": "Robot Energy Peak Route (18th Sept Exam · Slot 2)",
        "difficulty": "Medium",
        "topics": ["Arrays", "Dynamic Programming"],
        "judge": "server",
        "languages": ["java", "cpp", "python"],
        "description": """<p class="text-muted">Accenture &mdash; 17 &amp; 18 Sept Exam, Slot 2</p>
<p>A robot travels through a series of checkpoints where each checkpoint has an associated
<b>energy value</b>, given in an array <code>A</code> of size <code>N</code>.</p>
<p>A valid <b>energy route</b> must follow these rules:</p>
<ul>
  <li>The route consists of <b>consecutive checkpoints</b> (a contiguous subarray).</li>
  <li>Energy values <b>strictly increase</b> while moving toward a peak checkpoint.</li>
  <li>After reaching the highest energy value (the peak), energy values <b>strictly decrease</b>.</li>
  <li>The route must contain at least <b>3 checkpoints</b>.</li>
</ul>
<p>Output the <b>maximum sum</b> of energy values along any valid bitonic energy route. If no valid
route exists, print <code>0</code>.</p>
<p class="text-muted">This is the same shape of problem as the "Mountain Trail Elevation" question
from the same exam, reused here for the second slot with the checkpoints reframed as a robot's
energy readings instead of a hiker's elevations.</p>
<h3>Example</h3>
<pre>Input:
N = 8
A = [1, 3, 5, 4, 2, 6, 8, 7]

Output:
23</pre>
<p class="text-muted">Explanation: the route <code>[1, 3, 5, 4, 2]</code> is valid (peak 5) and sums to 15, but the
route <code>[2, 6, 8, 7]</code> is also valid (peak 8, strictly up from 2 then strictly down to 7)
and sums to <code>2+6+8+7 = 23</code>, which is larger. The two candidate mountains can't be joined
into one longer route because <code>4 &gt; 2</code> breaks the strictly-decreasing run right before
the second climb starts, so 23 is the maximum.</p>
<h3>Input Format</h3>
<p>Line 1: <code>N</code>. Line 2: <code>N</code> space-separated integers <code>A[0] .. A[N-1]</code>.</p>
<h3>Output Format</h3>
<p>Print a single integer &mdash; the maximum energy-route sum, or <code>0</code> if none exists.</p>
<h3>Constraints</h3>
<ul>
  <li><code>1 &lt;= N &lt;= 10^5</code></li>
  <li><code>-10^9 &lt;= A[i] &lt;= 10^9</code></li>
</ul>
""",
        "hint": "For each index i, compute leftSum[i]/leftLen[i]: the sum and length of the strictly "
                 "increasing run of A ending at i. Compute rightSum[i]/rightLen[i] the same way for the "
                 "strictly decreasing run starting at i. Index i can be a peak only if leftLen[i] >= 2 "
                 "and rightLen[i] >= 2; its route sum is then leftSum[i] + rightSum[i] - A[i]. Take the "
                 "max over all valid peaks, or 0 if none exist. O(N) with two passes.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] a = new long[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextLong();

        // TODO: find the maximum sum over all strictly-increasing-then-strictly-decreasing
        // contiguous subarrays with at least 3 elements; print 0 if none exists
        long best = 0;

        System.out.println(best);
    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    // TODO: find the maximum sum over all strictly-increasing-then-strictly-decreasing
    // contiguous subarrays with at least 3 elements; print 0 if none exists
    long long best = 0;

    cout << best << endl;
    return 0;
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\na = [read_int() for _ in range(n)]\n\n# TODO: find the maximum sum over all strictly-increasing-then-strictly-decreasing\n# contiguous subarrays with at least 3 elements; print 0 if none exists\nbest = 0\n\nprint(best)",
        },
        "tests": [
            {"input": "8\n1 3 5 4 2 6 8 7", "expected": "23", "hidden": False},
            {"input": "3\n2 9 4", "expected": "15", "hidden": False},
            {"input": "5\n1 2 3 4 5", "expected": "0", "hidden": True},
            {"input": "6\n10 20 30 25 15 5", "expected": "105", "hidden": True},
            {"input": "1\n7", "expected": "0", "hidden": True},
            {"input": "9\n2 4 6 9 7 5 3 1 4", "expected": "37", "hidden": True},
            {"input": "4\n3 3 3 3", "expected": "0", "hidden": True},
            {"input": "7\n5 10 15 20 18 12 6", "expected": "86", "hidden": True},
        ],
        "samples": [0, 1],
    }
)

PROBLEMS.append(
    {
        "id": 3102,
        "slug": "array-digital-length-operations",
        "title": "Array Digital Length & Digit Operations (18th Sept Exam · Slot 3)",
        "difficulty": "Easy",
        "topics": ["Math", "Strings"],
        "judge": "server",
        "languages": ["java", "cpp", "python"],
        "description": """<p class="text-muted">Accenture &mdash; 17 &amp; 18 Sept Exam, Slot 3</p>
<p>Given an array of integers <code>A</code> of length <code>N</code>, inspect the number of digits
(the <b>digital length</b>) of each element and compute the total described below.</p>
<p>For every element:</p>
<ul>
  <li>If its digital length is <b>even</b>, add the <b>square of the digital length</b> to the
  total.</li>
  <li>If its digital length is <b>odd</b>, add the <b>sum of the individual digits</b> of that
  number to the total.</li>
</ul>
<p>The sign of a number does not count as a digit &mdash; use its absolute value.</p>
<h3>Example</h3>
<pre>Input:
N = 4
A = [12, 345, 7, 8888]

12   -&gt; length 2 (even) -&gt; 2^2        = 4
345  -&gt; length 3 (odd)  -&gt; 3+4+5      = 12
7    -&gt; length 1 (odd)  -&gt; 7          = 7
8888 -&gt; length 4 (even) -&gt; 4^2        = 16

Output:
39</pre>
<h3>Input Format</h3>
<p>Line 1: <code>N</code>. Line 2: <code>N</code> space-separated integers <code>A[0] .. A[N-1]</code>
(may be negative).</p>
<h3>Output Format</h3>
<p>Print a single integer &mdash; the total described above.</p>
<h3>Constraints</h3>
<ul>
  <li><code>1 &lt;= N &lt;= 10^5</code></li>
  <li><code>-10^9 &lt;= A[i] &lt;= 10^9</code></li>
</ul>
""",
        "hint": "For each value, take its absolute value and convert to a string (or repeatedly divide "
                 "by 10) to get its digit count. If that count is even, add count*count. If it's odd, "
                 "add the sum of its individual digits (peel them off with % 10 and / 10, or sum the "
                 "string's characters). Accumulate across the whole array.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] a = new long[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextLong();

        // TODO: for each element, if its digit count is even add (digitCount)^2 to the total,
        // otherwise add the sum of its individual digits. Use Math.abs for negative numbers.
        long total = 0;

        System.out.println(total);
    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<long long> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    // TODO: for each element, if its digit count is even add (digitCount)^2 to the total,
    // otherwise add the sum of its individual digits. Use abs() for negative numbers.
    long long total = 0;

    cout << total << endl;
    return 0;
}""", "python": "import sys\n_data = sys.stdin.read().split()\n_idx = 0\ndef read_int():\n    global _idx\n    val = int(_data[_idx]); _idx += 1\n    return val\n\nn = read_int()\na = [read_int() for _ in range(n)]\n\n# TODO: for each element, if its digit count is even add (digitCount)**2 to the total,\n# otherwise add the sum of its individual digits. Use abs() for negative numbers.\ntotal = 0\n\nprint(total)",
        },
        "tests": [
            {"input": "4\n12 345 7 8888", "expected": "39", "hidden": False},
            {"input": "3\n9 10 100", "expected": "14", "hidden": False},
            {"input": "1\n0", "expected": "0", "hidden": True},
            {"input": "2\n-45 100000", "expected": "40", "hidden": True},
            {"input": "5\n1 22 333 4444 55555", "expected": "55", "hidden": True},
            {"input": "1\n999999999", "expected": "81", "hidden": True},
        ],
        "samples": [0, 1],
    }
)

PROBLEMS.extend(NEW_PROBLEMS)
PROBLEMS.extend(QUIZ_PROBLEMS)
PROBLEMS.extend(PDF_QUIZ_PROBLEMS)
PROBLEMS.extend(PDF_BANK_QUIZ_PROBLEMS)
PROBLEMS.append(PSEUDOCODE_QUIZ)
PROBLEMS.extend(CODE_2026_PROBLEMS)
PROBLEMS.extend(WEB_2026_PROBLEMS)
PROBLEMS.append(QUIZ_WEB_MCQ_2026)
PROBLEMS.append(QUIZ_SQL_2026)
PROBLEMS.extend(ACCENTURE_CODING_PDF_PROBLEMS)
PROBLEMS.extend(PRACTICE_SETS)
PROBLEMS.extend(WEBDEV_EXAM_PROBLEMS)
PROBLEMS.extend(SQL_EXAM_PROBLEMS)
PROBLEMS.extend(DOM_PRACTICE_PROBLEMS)
# ------------------------------------------------------------------ #
# Custom: add two SQL problems from user attachments (movie rating/watch queries)
# ------------------------------------------------------------------ #
PROBLEMS.extend([
    {
        "id": 1001,
        "slug": "movie-watch-details",
        "title": "Movie Watch Details (Genre / Age / Rating / Duration)",
        "difficulty": "Easy",
        "topics": ["Database", "SQL"],
        "judge": "server",
        "languages": ["sql"],
                "description": """
<h3>Tables</h3>
<pre>Movies(movie_id INTEGER PRIMARY KEY, movie_name TEXT, genre TEXT)
Users(user_id INTEGER PRIMARY KEY, user_name TEXT, age INTEGER)
WatchHistory(watch_id INTEGER PRIMARY KEY, user_id INTEGER, movie_id INTEGER, minutes_watched INTEGER)
Ratings(rating_id INTEGER PRIMARY KEY, user_id INTEGER, movie_id INTEGER, rating REAL)</pre>
<p>Write an SQL query to display the <b>movie_name</b>, <b>genre</b>, <b>user_name</b> and <b>rating</b>
for movies watched by users where:</p>
<ul>
    <li>the movie's genre is <code>Action</code></li>
    <li>the user's age is greater than <code>25</code></li>
    <li>the rating is <code>&gt;= 4.0</code></li>
    <li>the movie was watched for more than <code>60</code> minutes</li>
</ul>
<h3>Expected Output (sample)</h3>
<pre>movie_name | genre  | user_name | rating
Fast Chase | Action | Alice     | 4.5
Night Raid  | Action | Carol     | 4.0</pre>
""",
        "hint": "Join Movies, Ratings, Users and WatchHistory. Filter by genre, age, rating and minutes_watched.",
        "boilerplate": {"sql": "-- Write your SQLite query below\nSELECT"},
        "tests": [],
        "samples": [0],
        "databases": [
            _db(
                "Sample database", False,
                """
CREATE TABLE Movies (movie_id INTEGER PRIMARY KEY, movie_name TEXT, genre TEXT);
CREATE TABLE Users (user_id INTEGER PRIMARY KEY, user_name TEXT, age INTEGER);
CREATE TABLE WatchHistory (watch_id INTEGER PRIMARY KEY, user_id INTEGER, movie_id INTEGER, minutes_watched INTEGER);
CREATE TABLE Ratings (rating_id INTEGER PRIMARY KEY, user_id INTEGER, movie_id INTEGER, rating REAL);
""",
                {
                    "Movies": [
                        (1, "Fast Chase", "Action"),
                        (2, "Slow Drama", "Drama"),
                        (3, "Night Raid", "Action"),
                    ],
                    "Users": [
                        (1, "Alice", 30),
                        (2, "Bob", 24),
                        (3, "Carol", 40),
                    ],
                    "WatchHistory": [
                        (1, 1, 1, 120),
                        (2, 2, 1, 55),
                        (3, 3, 3, 75),
                        (4, 1, 2, 90),
                    ],
                    "Ratings": [
                        (1, 1, 1, 4.5),
                        (2, 2, 1, 3.5),
                        (3, 3, 3, 4.0),
                        (4, 1, 2, 4.2),
                    ],
                },
                """
SELECT m.movie_name AS movie_name, m.genre AS genre, u.user_name AS user_name, r.rating AS rating
FROM Movies m
JOIN Ratings r ON r.movie_id = m.movie_id
JOIN Users u ON u.user_id = r.user_id
JOIN WatchHistory w ON w.user_id = u.user_id AND w.movie_id = m.movie_id
WHERE m.genre = 'Action'
  AND u.age > 25
  AND r.rating >= 4.0
  AND w.minutes_watched > 60
ORDER BY m.movie_name, u.user_name
""",
            ),
            _db(
                "Hidden database", True,
                """
CREATE TABLE Movies (movie_id INTEGER PRIMARY KEY, movie_name TEXT, genre TEXT);
CREATE TABLE Users (user_id INTEGER PRIMARY KEY, user_name TEXT, age INTEGER);
CREATE TABLE WatchHistory (watch_id INTEGER PRIMARY KEY, user_id INTEGER, movie_id INTEGER, minutes_watched INTEGER);
CREATE TABLE Ratings (rating_id INTEGER PRIMARY KEY, user_id INTEGER, movie_id INTEGER, rating REAL);
""",
                {
                    "Movies": [
                        (11, "Explosive Run", "Action"),
                        (12, "Quiet Night", "Thriller"),
                        (13, "Family Tales", "Drama"),
                    ],
                    "Users": [
                        (21, "Dave", 28),
                        (22, "Eve", 26),
                        (23, "Frank", 22),
                    ],
                    "WatchHistory": [
                        (11, 21, 11, 80),
                        (12, 22, 11, 65),
                        (13, 23, 12, 120),
                    ],
                    "Ratings": [
                        (11, 21, 11, 4.2),
                        (12, 22, 11, 3.9),
                        (13, 23, 12, 4.8),
                    ],
                },
                """
SELECT m.movie_name AS movie_name, m.genre AS genre, u.user_name AS user_name, r.rating AS rating
FROM Movies m
JOIN Ratings r ON r.movie_id = m.movie_id
JOIN Users u ON u.user_id = r.user_id
JOIN WatchHistory w ON w.user_id = u.user_id AND w.movie_id = m.movie_id
WHERE m.genre = 'Action'
  AND u.age > 25
  AND r.rating >= 4.0
  AND w.minutes_watched > 60
ORDER BY m.movie_name, u.user_name
""",
            ),
        ],
    },

    {
        "id": 1002,
        "slug": "movie-watch-aggregates",
        "title": "Movie Watch Aggregates (Count & Total Minutes)",
        "difficulty": "Easy",
        "topics": ["Database", "SQL"],
        "judge": "server",
        "languages": ["sql"],
                "description": """
<h3>Tables</h3>
<pre>Movies(movie_id INTEGER PRIMARY KEY, movie_name TEXT, genre TEXT)
WatchHistory(watch_id INTEGER PRIMARY KEY, user_id INTEGER, movie_id INTEGER, minutes_watched INTEGER)</pre>
<p>Write an SQL query to find the total number of times each movie was watched and the total watch minutes for that movie.</p>
<p>Display only movies where:</p>
<ul>
    <li>The movie belongs to the <code>Action</code> or <code>Thriller</code> genre.</li>
    <li>The movie was watched more than <code>5</code> times.</li>
    <li>The total watch time is greater than <code>500</code> minutes.</li>
</ul>
<h3>Expected Output (sample)</h3>
<pre>movie_name  | watch_count | total_minutes
Thrill Ride | 8           | 825
Fast Chase  | 6           | 520</pre>
""",
        "hint": "Aggregate WatchHistory grouped by movie_id, join Movies for genre, filter in HAVING for counts and sums.",
        "boilerplate": {"sql": "-- Write your SQLite query below\nSELECT"},
        "tests": [],
        "samples": [0],
        "databases": [
            _db(
                "Sample database", False,
                """
CREATE TABLE Movies (movie_id INTEGER PRIMARY KEY, movie_name TEXT, genre TEXT);
CREATE TABLE WatchHistory (watch_id INTEGER PRIMARY KEY, user_id INTEGER, movie_id INTEGER, minutes_watched INTEGER);
""",
                {
                    "Movies": [
                        (1, "Fast Chase", "Action"),
                        (2, "Night Raid", "Action"),
                        (3, "Thrill Ride", "Thriller"),
                        (4, "Family Drama", "Drama"),
                    ],
                    "WatchHistory": [
                        (1, 1, 1, 120),(2,2,1,90),(3,3,1,60),(4,4,1,80),(5,5,1,70),(6,6,1,100),
                        (7,1,2,30),(8,2,2,40),(9,3,2,35),(10,4,2,25),(11,5,2,50),
                        (12,1,3,120),(13,2,3,110),(14,3,3,100),(15,4,3,90),(16,5,3,95),(17,6,3,105),(18,7,3,125),(19,8,3,80)
                    ],
                },
                """
SELECT m.movie_name AS movie_name,
       COUNT(*) AS watch_count,
       SUM(w.minutes_watched) AS total_minutes
FROM Movies m
JOIN WatchHistory w ON w.movie_id = m.movie_id
WHERE m.genre IN ('Action', 'Thriller')
GROUP BY m.movie_id, m.movie_name
HAVING COUNT(*) > 5 AND SUM(w.minutes_watched) > 500
ORDER BY total_minutes DESC
""",
            ),
            _db(
                "Hidden database", True,
                """
CREATE TABLE Movies (movie_id INTEGER PRIMARY KEY, movie_name TEXT, genre TEXT);
CREATE TABLE WatchHistory (watch_id INTEGER PRIMARY KEY, user_id INTEGER, movie_id INTEGER, minutes_watched INTEGER);
""",
                {
                    "Movies": [
                        (11, "Explosive Run", "Action"),
                        (12, "Dark Alley", "Thriller"),
                        (13, "Slow Story", "Drama"),
                    ],
                    "WatchHistory": [
                        (11,1,11,60),(12,2,11,70),(13,3,11,90),(14,4,11,80),(15,5,11,75),(16,6,11,95),(17,7,11,85),
                        (18,1,12,90),(19,2,12,60),(20,3,12,55),(21,4,12,80),(22,5,12,75),(23,6,12,65),
                    ],
                },
                """
SELECT m.movie_name AS movie_name,
       COUNT(*) AS watch_count,
       SUM(w.minutes_watched) AS total_minutes
FROM Movies m
JOIN WatchHistory w ON w.movie_id = m.movie_id
WHERE m.genre IN ('Action', 'Thriller')
GROUP BY m.movie_id, m.movie_name
HAVING COUNT(*) > 5 AND SUM(w.minutes_watched) > 500
ORDER BY total_minutes DESC
""",
            ),
        ],
    },
])
PROBLEMS.sort(key=lambda p: p["id"])

# Several MCQ banks were transcribed with the answer nearly always in
# position A, so the options get a deterministic reshuffle at load time.
from quiz_shuffle import shuffle_quiz_options  # noqa: E402

shuffle_quiz_options(PROBLEMS)


