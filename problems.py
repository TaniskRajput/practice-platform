"""
Problem definitions for the practice platform.
Each problem carries its description (HTML), boilerplates, and test cases.
Server-side judged problems (java/cpp/sql) include reference solutions;
browser-judged problems (javascript DOM) define test steps interpreted by the frontend.
"""

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
        "languages": ["java", "cpp"],
        "description": """
<p>An <code>n x n</code> matrix is <b>valid</b> if every row and every column contains all the integers
from <code>1</code> to <code>n</code> (inclusive).</p>
<p>Given an <code>n x n</code> integer matrix <code>matrix</code>, return <code>true</code> if the matrix
is valid. Otherwise, return <code>false</code>.</p>
<h3>Example 1:</h3>
<pre>Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3. Every row and column contains the numbers 1, 2, and 3.</pre>
<h3>Example 2:</h3>
<pre>Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3. The first row does not contain the numbers 2 and 3.</pre>
<h3>Constraints:</h3>
<ul>
  <li><code>n == matrix.length == matrix[i].length</code></li>
  <li><code>1 &lt;= n &lt;= 100</code></li>
  <li><code>1 &lt;= matrix[i][j] &lt;= n</code></li>
</ul>
""",
        "hint": "For a row (or column) to contain every number from 1 to n exactly once, the set of values "
                 "in it must have size n, and every value must be within [1, n]. Try using a set per row "
                 "and per column, or a frequency table.",
        "boilerplate": {
            "java": """class Solution {
    public boolean checkValid(int[][] matrix) {

    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool checkValid(vector<vector<int>>& matrix) {

    }
};""",
        },
        "tests": [
            {"input": "[[1,2,3],[3,1,2],[2,3,1]]", "expected": "true", "hidden": False},
            {"input": "[[1,1,1],[1,2,3],[1,2,3]]", "expected": "false", "hidden": False},
            {"input": "[[1]]", "expected": "true", "hidden": True},
            {"input": "[[1,2],[2,1]]", "expected": "true", "hidden": True},
            {"input": "[[1,2],[1,2]]", "expected": "false", "hidden": True},
            {"input": "[[1,2,3],[2,3,1],[1,2,3]]", "expected": "false", "hidden": True},
            {"input": "[[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,1,2,3]]", "expected": "true", "hidden": True},
        ],
        "samples": [0, 1],
        "function_name": "checkValid",
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
            },
            {
                "name": "Hidden database",
                "hidden": True,
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
            },
        ],
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

SCHEMA_SQL = """
CREATE TABLE Customers (customer_id INTEGER PRIMARY KEY, customer_name TEXT, country_id INTEGER);
CREATE TABLE Countries (country_id INTEGER PRIMARY KEY, country_name TEXT);
CREATE TABLE Orders (order_id INTEGER PRIMARY KEY, customer_id INTEGER, status_id INTEGER, order_date TEXT);
CREATE TABLE Order_Status (status_id INTEGER PRIMARY KEY, status_name TEXT);
CREATE TABLE Order_Items (order_id INTEGER, quantity INTEGER, unit_price REAL);
"""

