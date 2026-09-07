"""
Problems 4-15: curated from KN Academy "Accenture Mock Test Series" course
(see extracted/curated-questions.md for sources and scrape details).
Merged into problems.PROBLEMS by __init__ wiring at the bottom of problems.py.
"""

def _db(name, hidden, schema, seed, reference_query):
    return {
        "name": name,
        "hidden": hidden,
        "schema": schema,
        "seed": seed,
        "reference_query": reference_query,
    }


NEW_PROBLEMS = [
    # ------------------------------------------------------------------ #
    # 4. Prime Hideouts (Coding Mock Test - 14) - real hidden test cases
    # ------------------------------------------------------------------ #
    {
        "id": 4,
        "slug": "prime-hideouts",
        "title": "Prime Hideouts",
        "difficulty": "Easy",
        "topics": ["Math", "Number Theory", "Prime Sieve"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p>Detective Reva is on a high-profile case. The secret hideouts of the suspects are numbered from
<code>L</code> to <code>R</code>. According to a tip, only those at <b>prime-numbered</b> addresses are
suspicious. To narrow her search, she needs a program that lists all prime numbers between two given
limits <code>L</code> and <code>R</code> (inclusive).</p>
<p>If there are no prime numbers in the range, print <code>No primes found</code>.</p>
<h3>Sample Test Case:</h3>
<pre>Input:
10
20

Output:
11
13
17
19</pre>
<h3>Constraints:</h3>
<ul>
  <li><code>1 &lt;= L &lt;= R &lt;= 10^6</code></li>
</ul>
<p><b>Input format:</b> two lines, first <code>L</code> then <code>R</code>.<br>
<b>Output format:</b> one prime per line, or the single line <code>No primes found</code>.</p>
""",
        "hint": "Trial division per number is fine for R up to 10^6 if you only test divisors up to "
                 "sqrt(n). A Sieve of Eratosthenes up to R is even faster. Remember 1 is not prime.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int lo = sc.nextInt();
        int hi = sc.nextInt();

        // TODO: print every prime in [lo, hi], one per line,
        // or "No primes found" if there are none.
    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    int lo, hi;
    cin >> lo >> hi;

    // TODO: print every prime in [lo, hi], one per line,
    // or "No primes found" if there are none.
    return 0;
}""",
        },
        "tests": [
            {"input": "1\n10", "expected": "2\n3\n5\n7", "hidden": False},
            {"input": "10\n20", "expected": "11\n13\n17\n19", "hidden": False},
            {"input": "22\n29", "expected": "23\n29", "hidden": True},
            {"input": "50\n55", "expected": "53", "hidden": True},
            {"input": "8\n10", "expected": "No primes found", "hidden": True},
            {"input": "97\n100", "expected": "97", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 5. Armstrong Number (Coding Mock Test - 15) - real hidden test cases
    # ------------------------------------------------------------------ #
    {
        "id": 5,
        "slug": "armstrong-number",
        "title": "Armstrong Number",
        "difficulty": "Easy",
        "topics": ["Math", "Number Theory"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p>In the year 3025, astronauts aboard the spaceship Voyager Armstrong are scanning asteroid belts.
Each asteroid has an identification number. Their onboard AI detects <b>Armstrong numbers</b> to mark
them as safe zones.</p>
<p>Write a program for the AI that will identify if a given number is an Armstrong number or not.</p>
<p>An <b>Armstrong number</b> is a number equal to the sum of its own digits each raised to the power
of the number of digits (e.g. <code>153 = 1^3 + 5^3 + 3^3</code>).</p>
<p>If it is not an Armstrong number print <code>Not an Armstrong Number</code>, otherwise print
<code>Armstrong Number</code>.</p>
<h3>Sample Test Case:</h3>
<pre>Input:
153

Output:
Armstrong Number</pre>
""",
        "hint": "Count the digits first, then sum each digit raised to that power and compare with the "
                 "original number. Watch out: single-digit numbers (0-9) are Armstrong numbers.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();

        // TODO: print "Armstrong Number" or "Not an Armstrong Number"
    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n;
    cin >> n;

    // TODO: print "Armstrong Number" or "Not an Armstrong Number"
    return 0;
}""",
        },
        "tests": [
            {"input": "153", "expected": "Armstrong Number", "hidden": False},
            {"input": "370", "expected": "Armstrong Number", "hidden": True},
            {"input": "371", "expected": "Armstrong Number", "hidden": True},
            {"input": "9474", "expected": "Armstrong Number", "hidden": True},
            {"input": "100", "expected": "Not an Armstrong Number", "hidden": True},
            {"input": "407", "expected": "Armstrong Number", "hidden": True},
            {"input": "7", "expected": "Armstrong Number", "hidden": True},
        ],
        "samples": [0],
    },

    # ------------------------------------------------------------------ #
    # 6. Vowel Counter (Coding Mock Test - 16) - real hidden test cases
    # ------------------------------------------------------------------ #
    {
        "id": 6,
        "slug": "vowel-counter",
        "title": "Vowel Counter",
        "difficulty": "Easy",
        "topics": ["Strings", "Counting"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p>In a city-wide Spell Bee Championship, students are given words and are scored based on the number
of vowels in their word. The teacher wants to automate scoring by writing a program that counts how
many vowels are present in a given word.</p>
<p>As the school's coding champ, your task is to write a function that counts the number of vowels
(<code>a, e, i, o, u</code>) in a given lowercase English word.</p>
<h3>Sample Test Case:</h3>
<pre>Input:
education

Output:
5</pre>
""",
        "hint": "Iterate over the characters and check membership in the set {a, e, i, o, u}. "
                 "The word is guaranteed lowercase, so no case handling is needed.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next();

        // TODO: print the number of vowels in the word
    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    string word;
    cin >> word;

    // TODO: print the number of vowels in the word
    return 0;
}""",
        },
        "tests": [
            {"input": "education", "expected": "5", "hidden": False},
            {"input": "apple", "expected": "2", "hidden": True},
            {"input": "rhythm", "expected": "0", "hidden": True},
            {"input": "umbrella", "expected": "3", "hidden": True},
            {"input": "aeiou", "expected": "5", "hidden": True},
            {"input": "quizmaster", "expected": "4", "hidden": True},
        ],
        "samples": [0],
    },

    # ------------------------------------------------------------------ #
    # 7. Remove Adjacent Duplicates (Coding 1 Accenture) - real hidden cases
    # ------------------------------------------------------------------ #
    {
        "id": 7,
        "slug": "remove-adjacent-duplicates",
        "title": "Remove Adjacent Duplicates",
        "difficulty": "Easy",
        "topics": ["Strings", "Stack"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p>Given a string, repeatedly remove two adjacent identical characters until no such pair remains.
Return the resulting string.</p>
<h3>Example:</h3>
<pre>Input: abbaca
Process: abbaca &rarr; aaca &rarr; ca
Output: ca</pre>
<p>Removal can cascade: after removing <code>bb</code> the two <code>a</code>s become adjacent and
are removed too.</p>
""",
        "hint": "Use a stack (or build the answer in a char array): push each character, and if it "
                 "equals the top of the stack, pop instead of pushing. The stack contents at the end "
                 "are the answer.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        // TODO: repeatedly remove pairs of adjacent equal characters, print result
    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;

    // TODO: repeatedly remove pairs of adjacent equal characters, print result
    return 0;
}""",
        },
        "tests": [
            {"input": "abbaca", "expected": "ca", "hidden": False},
            {"input": "aabcac", "expected": "bcac", "hidden": True},
            {"input": "abaab", "expected": "a", "hidden": True},
            {"input": "azxxzy", "expected": "ay", "hidden": True},
            {"input": "abba", "expected": "", "hidden": True},
            {"input": "abcde", "expected": "abcde", "hidden": True},
        ],
        "samples": [0],
    },

    # ------------------------------------------------------------------ #
    # 8. Maximum Plane Regions (PYQ PDF #3)
    # ------------------------------------------------------------------ #
    {
        "id": 8,
        "slug": "maximum-plane-regions",
        "title": "Maximum Plane Regions",
        "difficulty": "Easy",
        "topics": ["Math", "Combinatorics"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p>Mr. Professor is a great scientist, but he is not able to find a solution to one problem.</p>
<p>There are <code>N</code> straight lines that are not parallel, and no three lines go through the
same point. The lines divide the plane into <code>M</code> regions. Write a function to find out the
<b>maximum</b> number of such regions he can get on the plane.</p>
<h3>Input Specification:</h3>
<p><code>input1</code>: An integer N representing the number of straight lines
(<code>0 &lt;= N &lt;= 100</code>)</p>
<h3>Output Specification:</h3>
<p>Return the maximum number of regions.</p>
<h3>Sample:</h3>
<pre>Input: 3
Output: 7</pre>
<p>(3 lines in general position cut the plane into 7 regions.)</p>
""",
        "hint": "Each new line in general position crosses all previous lines and adds one region per "
                 "crossing plus one. Summing gives N(N+1)/2 + 1. Don't forget N = 0 returns 1.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: print the maximum number of regions
    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    // TODO: print the maximum number of regions
    return 0;
}""",
        },
        "tests": [
            {"input": "3", "expected": "7", "hidden": False},
            {"input": "0", "expected": "1", "hidden": True},
            {"input": "1", "expected": "2", "hidden": True},
            {"input": "2", "expected": "4", "hidden": True},
            {"input": "100", "expected": "5051", "hidden": True},
        ],
        "samples": [0],
    },

    # ------------------------------------------------------------------ #
    # 9. Climbing Stairs (PYQ PDF #9)
    # ------------------------------------------------------------------ #
    {
        "id": 9,
        "slug": "climbing-stairs",
        "title": "Climbing Stairs",
        "difficulty": "Easy",
        "topics": ["Dynamic Programming", "Math"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p>You are climbing a staircase. It takes <code>n</code> steps to reach the top.</p>
<p>Each time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways
can you climb to the top?</p>
<h3>Sample Test Case:</h3>
<pre>Input: 3
Output: 3
Explanation: 1+1+1, 1+2, 2+1</pre>
<h3>Constraints:</h3>
<ul>
  <li><code>1 &lt;= n &lt;= 45</code></li>
</ul>
""",
        "hint": "ways(n) = ways(n-1) + ways(n-2) — the Fibonacci recurrence. Use two rolling "
                 "variables; recursion without memoisation will be too slow for n = 45.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: print the number of distinct ways to climb n stairs
    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    // TODO: print the number of distinct ways to climb n stairs
    return 0;
}""",
        },
        "tests": [
            {"input": "3", "expected": "3", "hidden": False},
            {"input": "1", "expected": "1", "hidden": True},
            {"input": "2", "expected": "2", "hidden": True},
            {"input": "10", "expected": "89", "hidden": True},
            {"input": "45", "expected": "1836311903", "hidden": True},
        ],
        "samples": [0],
    },

    # ------------------------------------------------------------------ #
    # 10. Sum of Binary Digits (PYQ PDF #17, Hirepro 2023)
    # ------------------------------------------------------------------ #
    {
        "id": 10,
        "slug": "sum-of-binary-digits",
        "title": "Sum of Binary Digits",
        "difficulty": "Easy",
        "topics": ["Math", "Bit Manipulation"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p>You are given a number N. Convert the number to its binary form and print the <b>sum of its binary
digits</b> (i.e. the number of <code>1</code> bits plus zero contributions from <code>0</code> bits —
equivalently, just count the <code>1</code> bits).</p>
<h3>Sample Test Case:</h3>
<pre>Input: 15
Output: 4
Explanation: Binary of 15 is 1111, so the sum is 4.</pre>
""",
        "hint": "Repeatedly take n % 2 (or n & 1) and add to a running sum, then divide (or shift) "
                 "n by 2 until n is 0.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: print the sum of digits of n in binary
    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    // TODO: print the sum of digits of n in binary
    return 0;
}""",
        },
        "tests": [
            {"input": "15", "expected": "4", "hidden": False},
            {"input": "0", "expected": "0", "hidden": True},
            {"input": "1", "expected": "1", "hidden": True},
            {"input": "16", "expected": "1", "hidden": True},
            {"input": "255", "expected": "8", "hidden": True},
            {"input": "1023", "expected": "10", "hidden": True},
        ],
        "samples": [0],
    },

    # ------------------------------------------------------------------ #
    # 11. First-Last Combination Frequency (11 Oct 2025 coding set)
    # ------------------------------------------------------------------ #
    {
        "id": 11,
        "slug": "first-last-combination-frequency",
        "title": "Most Frequent First-Last Combination",
        "difficulty": "Medium",
        "topics": ["Strings", "Hash Table", "Counting"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p>Given a string (may contain multiple spaces), find the <b>first+last character combination</b> of
each word. Then return the combination(s) with the <b>highest frequency</b>, maintaining the original
order of appearance.</p>
<h3>Sample Test Case:</h3>
<pre>Input: aaa human      achinh ae add  ad  admind

Output: ad</pre>
<p>Explanation: the words are <code>aaa aa, human hn, achinh ah, ae ae, add ad, ad ad, admind ad</code>
— wait, carefully: <code>aaa&rarr;aa</code>, <code>human&rarr;hn</code>, <code>achinh&rarr;ah</code>,
<code>ae&rarr;ae</code>, <code>add&rarr;ad</code>, <code>ad&rarr;ad</code>,
<code>admind&rarr;ad</code>. <code>ad</code> appears 3 times, more than any other combination.</p>
<h3>Notes:</h3>
<ul>
  <li>Words are separated by one <b>or more</b> spaces.</li>
  <li>For a single-character word the first and last character are the same character.</li>
  <li>Print each winning combination on its own line, in order of first appearance.</li>
</ul>
""",
        "hint": "Split on \\\\s+ (regex) after trimming, build a frequency map that preserves insertion "
                 "order (LinkedHashMap in Java), find the max frequency, then print every combination "
                 "with that frequency in insertion order.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().trim();

        // TODO: print the most frequent first+last combination(s), one per line
    }
}""",
            "cpp": """#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    getline(cin, s);

    // TODO: print the most frequent first+last combination(s), one per line
    return 0;
}""",
        },
        "tests": [
            {"input": "aaa human      achinh ae add  ad  admind ",
             "expected": "ad", "hidden": False},
            {"input": "a b c d",
             "expected": "aa\nbb\ncc\ndd", "hidden": False},
            {"input": "hello egg olive era",
             "expected": "ho\neg\noe\nea", "hidden": True},
            {"input": "cat cot dog dot dot",
             "expected": "ct\ndt", "hidden": True},
            {"input": "single",
             "expected": "se", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 12. Departments Above Average Salary (SQL Query 1 article)
    # ------------------------------------------------------------------ #
    {
        "id": 12,
        "slug": "departments-above-average-salary",
        "title": "Departments Above Average Salary",
        "difficulty": "Medium",
        "topics": ["Database", "SQL"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: Employees</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| emp_id        | int     |
| emp_name      | varchar |
| department_id | int     |
| salary        | int     |
+---------------+---------+</pre>
<p><code>emp_id</code> is the primary key.</p>

<h3>Table: Departments</h3>
<pre>+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| department_id  | int     |
| department_name| varchar |
+----------------+---------+</pre>
<p><code>department_id</code> is the primary key.</p>

<h3>Problem:</h3>
<p>Write a SQL query to display the <b>names of departments</b> where the <b>average salary</b> of
employees is <b>greater than the overall average salary</b> of all employees.</p>
<p>Name the output column <code>department_name</code>. Order the result by
<code>department_name</code> ascending.</p>

<h3>Sample:</h3>
<p>With the sample data, the overall average salary is
<code>(60000+80000+70000+40000+90000)/5 = 68000</code>.
Department 10 (HR) averages 70000 and department 30 (Finance) averages 90000 — both exceed 68000.
Department 20 (IT) averages 55000 and is excluded.</p>
<pre>+-----------------+
| department_name |
+-----------------+
| Finance         |
| HR              |
+-----------------+</pre>
""",
        "hint": "Compute the overall average in a scalar subquery, group employees by department, use "
                 "HAVING to keep departments whose AVG(salary) exceeds it, then join to Departments "
                 "for the name.",
        "boilerplate": {
            "sql": """-- Write your SQLite query below
SELECT
FROM
GROUP BY
HAVING""",
        },
        "tests": [],  # SQL judged against databases below
        "samples": [0],
        "databases": [
            _db(
                "Sample database",
                False,
                """
CREATE TABLE Employees (emp_id INTEGER PRIMARY KEY, emp_name TEXT, department_id INTEGER, salary INTEGER);
CREATE TABLE Departments (department_id INTEGER PRIMARY KEY, department_name TEXT);
""",
                {
                    "Employees": [
                        (1, "John", 10, 60000),
                        (2, "Alice", 10, 80000),
                        (3, "Bob", 20, 70000),
                        (4, "Mike", 20, 40000),
                        (5, "Carol", 30, 90000),
                    ],
                    "Departments": [
                        (10, "HR"), (20, "IT"), (30, "Finance"),
                    ],
                },
                """
SELECT d.department_name AS department_name
FROM Employees e
JOIN Departments d ON e.department_id = d.department_id
GROUP BY e.department_id, d.department_name
HAVING AVG(e.salary) > (SELECT AVG(salary) FROM Employees)
ORDER BY department_name ASC
""",
            ),
            _db(
                "Hidden database",
                True,
                """
CREATE TABLE Employees (emp_id INTEGER PRIMARY KEY, emp_name TEXT, department_id INTEGER, salary INTEGER);
CREATE TABLE Departments (department_id INTEGER PRIMARY KEY, department_name TEXT);
""",
                {
                    "Employees": [
                        (1, "Ravi", 1, 50000),
                        (2, "Priya", 1, 70000),
                        (3, "Amit", 2, 45000),
                        (4, "Neha", 2, 55000),
                        (5, "Karan", 3, 120000),
                        (6, "Sara", 3, 100000),
                        (7, "Mohan", 4, 48000),
                        (8, "Isha", 4, 52000),
                    ],
                    "Departments": [
                        (1, "Engineering"), (2, "Support"), (3, "Executive"), (4, "Operations"),
                    ],
                },
                """
SELECT d.department_name AS department_name
FROM Employees e
JOIN Departments d ON e.department_id = d.department_id
GROUP BY e.department_id, d.department_name
HAVING AVG(e.salary) > (SELECT AVG(salary) FROM Employees)
ORDER BY department_name ASC
""",
            ),
        ],
    },

    # ------------------------------------------------------------------ #
    # 13. Highest Paid Employee per Department (SQL Query 2 article)
    # ------------------------------------------------------------------ #
    {
        "id": 13,
        "slug": "highest-paid-per-department",
        "title": "Highest Paid Employee per Department",
        "difficulty": "Medium",
        "topics": ["Database", "SQL"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<h3>Table: Employees</h3>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| emp_id        | int     |
| name          | varchar |
| department    | varchar |
| salary        | int     |
+---------------+---------+</pre>
<p><code>emp_id</code> is the primary key.</p>

<h3>Problem:</h3>
<p>Write a SQL query to display the <b>highest paid employee(s) in each department</b>.</p>
<p>Return the columns <code>department</code>, <code>name</code>, <code>salary</code>. Order the
result by <code>department</code> ascending, then <code>name</code> ascending. If several employees
tie for the top salary in a department, list all of them.</p>

<h3>Sample:</h3>
<pre>+------------+-------+--------+
| department | name  | salary |
+------------+-------+--------+
| Finance    | Eva   | 60000  |
| HR         | Alice | 50000  |
| IT         | Frank | 72000  |
+------------+-------+--------+</pre>
""",
        "hint": "A correlated subquery works well: keep only rows where salary equals "
                 "(SELECT MAX(salary) FROM Employees e2 WHERE e2.department = e1.department). "
                 "SQLite also supports window functions if you prefer MAX() OVER (PARTITION BY ...).",
        "boilerplate": {
            "sql": """-- Write your SQLite query below
SELECT
FROM
WHERE""",
        },
        "tests": [],  # SQL judged against databases below
        "samples": [0],
        "databases": [
            _db(
                "Sample database",
                False,
                """
CREATE TABLE Employees (emp_id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary INTEGER);
""",
                {
                    "Employees": [
                        (1, "Alice", "HR", 50000),
                        (2, "Bob", "IT", 70000),
                        (3, "Carol", "IT", 65000),
                        (4, "David", "HR", 48000),
                        (5, "Eva", "Finance", 60000),
                        (6, "Frank", "IT", 72000),
                        (7, "Grace", "Finance", 58000),
                    ],
                },
                """
SELECT e.department AS department, e.name AS name, e.salary AS salary
FROM Employees e
WHERE e.salary = (SELECT MAX(e2.salary) FROM Employees e2 WHERE e2.department = e.department)
ORDER BY e.department ASC, e.name ASC
""",
            ),
            _db(
                "Hidden database",
                True,
                """
CREATE TABLE Employees (emp_id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary INTEGER);
""",
                {
                    "Employees": [
                        (1, "Vikram", "Sales", 40000),
                        (2, "Anita", "Sales", 61000),
                        (3, "Rahul", "Sales", 61000),
                        (4, "Meena", "Admin", 35000),
                        (5, "Arjun", "Admin", 42000),
                        (6, "Divya", "Legal", 90000),
                    ],
                },
                """
SELECT e.department AS department, e.name AS name, e.salary AS salary
FROM Employees e
WHERE e.salary = (SELECT MAX(e2.salary) FROM Employees e2 WHERE e2.department = e.department)
ORDER BY e.department ASC, e.name ASC
""",
            ),
        ],
    },

    # ------------------------------------------------------------------ #
    # 14. Password Strength & Match Evaluator (Coding Assessment Full 2 §3)
    # ------------------------------------------------------------------ #
    {
        "id": 14,
        "slug": "password-strength-evaluator",
        "title": "Password Strength & Match Evaluator",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "Events"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Implement real-time validation for a sign-up form with the following HTML:</p>
<pre>&lt;label for="pass"&gt;Password (Min 8 chars):&lt;/label&gt;
&lt;input type="password" id="pass" placeholder="Enter password"&gt;
&lt;label for="confirm-pass"&gt;Confirm Password:&lt;/label&gt;
&lt;input type="password" id="confirm-pass" placeholder="Confirm password"&gt;
&lt;p id="feedback-msg"&gt;&lt;/p&gt;</pre>
<p>Write JavaScript to fulfill the following specifications:</p>
<ul>
  <li><b>Real-time:</b> validation must run on every <code>input</code> event of either field.</li>
  <li><b>Length rule:</b> the password must be at least <code>8</code> characters long.</li>
  <li><b>Match rule:</b> the Password and Confirm Password fields must be equal.</li>
  <li><b>Success:</b> when both rules pass, <code>#feedback-msg</code> shows
      <code>Passwords Match</code> with <code>style.color</code> set to <code>green</code>.</li>
  <li><b>Failure:</b> otherwise it shows <code>Passwords do not match or too short</code> with
      <code>style.color</code> set to <code>red</code>.</li>
  <li><b>Initial state:</b> on load (both fields empty) the message must show the failure state.</li>
</ul>
<p>Use the <b>Preview</b> tab to try the form live. Submitting runs automated tests that type into
the fields in a fresh page.</p>
""",
        "hint": "Attach the same validate() function to the 'input' event of both fields. Inside, "
                 "read .value of both inputs, check val1.length >= 8 && val1 === val2, and set "
                 "msg.textContent plus msg.style.color accordingly. Call validate() once on load.",
        "boilerplate": {
            "javascript": """function initializePasswordForm() {
  const passInput = document.getElementById('pass');
  const confirmInput = document.getElementById('confirm-pass');
  const msg = document.getElementById('feedback-msg');

  // TODO: validate on input events and on initial load
}

initializePasswordForm();
""",
        },
        "tests": [],
        "samples": [],
        "browser_html": """<label for="pass">Password (Min 8 chars):</label>
<input type="password" id="pass" placeholder="Enter password">
<label for="confirm-pass">Confirm Password:</label>
<input type="password" id="confirm-pass" placeholder="Confirm password">
<p id="feedback-msg"></p>""",
        "browser_tests": [
            {
                "name": "Initial state shows failure message",
                "hidden": False,
                "steps": [],
                "expect": {"msg": "Passwords do not match or too short", "color": "red"},
            },
            {
                "name": "Too-short matching passwords fail",
                "hidden": False,
                "steps": [
                    {"type": "pass", "value": "abc12"},
                    {"type": "confirm-pass", "value": "abc12"},
                ],
                "expect": {"msg": "Passwords do not match or too short", "color": "red"},
            },
            {
                "name": "Valid 8-char matching passwords pass",
                "hidden": False,
                "steps": [
                    {"type": "pass", "value": "hunter2boogaloo"},
                    {"type": "confirm-pass", "value": "hunter2boogaloo"},
                ],
                "expect": {"msg": "Passwords Match", "color": "green"},
            },
            {
                "name": "Mismatched long passwords fail",
                "hidden": True,
                "steps": [
                    {"type": "pass", "value": "longenough123"},
                    {"type": "confirm-pass", "value": "longenough124"},
                ],
                "expect": {"msg": "Passwords do not match or too short", "color": "red"},
            },
            {
                "name": "Exactly 8 characters passes",
                "hidden": True,
                "steps": [
                    {"type": "pass", "value": "12345678"},
                    {"type": "confirm-pass", "value": "12345678"},
                ],
                "expect": {"msg": "Passwords Match", "color": "green"},
            },
            {
                "name": "Fixing confirm field recovers to green",
                "hidden": True,
                "steps": [
                    {"type": "pass", "value": "correcthorse"},
                    {"type": "confirm-pass", "value": "wrong"},
                    {"type": "confirm-pass", "value": "correcthorse"},
                ],
                "expect": {"msg": "Passwords Match", "color": "green"},
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # 15. Product Search Filter (PYQ Recent Set PDF)
    # ------------------------------------------------------------------ #
    {
        "id": 15,
        "slug": "product-search-filter",
        "title": "Product Search Filter",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "CSS"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Build a dynamic search filter for a product list. The page contains:</p>
<pre>&lt;input type="text" id="search-input" placeholder="Search products..."&gt;
&lt;ul class="product"&gt;
  &lt;li data-name="banana"&gt;Banana&lt;/li&gt;
  &lt;li data-name="orange"&gt;Orange&lt;/li&gt;
  &lt;li data-name="pineapple"&gt;Pineapple&lt;/li&gt;
  &lt;li data-name="pomegranate"&gt;Pomegranate&lt;/li&gt;
  &lt;li data-name="mango"&gt;Mango&lt;/li&gt;
&lt;/ul&gt;</pre>
<p>Write the CSS and JavaScript to fulfill the following objectives:</p>
<ul>
  <li><b>CSS:</b> set the font size of the list items to <code>25px</code>
      (use a <code>.product li</code> rule — this is pre-filled for you).</li>
  <li><b>Initial value:</b> set the search input's value to <code>"nana"</code> on load.</li>
  <li><b>Filter rule:</b> a product is displayed if the current search value (lowercased) is a
      substring of its <code>data-name</code> attribute (lowercased); otherwise hide it by setting
      <code>style.display = "none"</code>. Displayed items must have
      <code>style.display = ""</code>.</li>
  <li><b>Real-time:</b> re-filter on every <code>input</code> event, and also apply the filter once
      on load (so the initial <code>"nana"</code> value takes effect).</li>
</ul>
<p>Use the <b>Preview</b> tab to try the filter live. Submitting runs automated tests that type into
the search box in a fresh page and check which items are visible.</p>
""",
        "hint": "After setting searchInput.value = 'nana', write one filter() that loops over "
                 "document.querySelectorAll('.product li'), reads getAttribute('data-name') and "
                 "input.value both lowercased, and toggles item.style.display between '' and 'none'. "
                 "Wire it to the input event and call it once.",
        "boilerplate": {
            "javascript": """function initializeSearchFilter() {
  const searchInput = document.getElementById('search-input');
  const productList = document.querySelectorAll('.product li');

  // TODO: set the initial search value to "nana",
  //       filter items on every input event, and filter once on load.
}

initializeSearchFilter();
""",
        },
        "tests": [],
        "samples": [],
        "browser_html": """<input type="text" id="search-input" placeholder="Search products...">
<ul class="product">
  <li data-name="banana">Banana</li>
  <li data-name="orange">Orange</li>
  <li data-name="pineapple">Pineapple</li>
  <li data-name="pomegranate">Pomegranate</li>
  <li data-name="mango">Mango</li>
</ul>""",
        "browser_style": """.product li { font-size: 25px; }""",
        "browser_tests": [
            {
                "name": "Initial value 'nana' shows only Banana",
                "hidden": False,
                "steps": [],
                "expect": {"visible": ["Banana"], "hidden": ["Orange", "Pineapple", "Pomegranate", "Mango"]},
            },
            {
                "name": "Empty search shows every product",
                "hidden": False,
                "steps": [{"type": "search-input", "value": ""}],
                "expect": {"visible": ["Banana", "Orange", "Pineapple", "Pomegranate", "Mango"], "hidden": []},
            },
            {
                "name": "Substring 'an' matches Banana, Orange, Mango, Pomegranate",
                "hidden": True,
                "steps": [{"type": "search-input", "value": "an"}],
                "expect": {"visible": ["Banana", "Orange", "Mango", "Pomegranate"], "hidden": ["Pineapple"]},
            },
            {
                "name": "Prefix 'pom' matches only Pomegranate",
                "hidden": True,
                "steps": [{"type": "search-input", "value": "pom"}],
                "expect": {"visible": ["Pomegranate"], "hidden": ["Banana", "Orange", "Pineapple", "Mango"]},
            },
            {
                "name": "No match hides everything",
                "hidden": True,
                "steps": [{"type": "search-input", "value": "zzz"}],
                "expect": {"visible": [], "hidden": ["Banana", "Orange", "Pineapple", "Pomegranate", "Mango"]},
            },
            {
                "name": "Full word 'mango' matches case-insensitively",
                "hidden": True,
                "steps": [{"type": "search-input", "value": "MANGO"}],
                "expect": {"visible": ["Mango"], "hidden": ["Banana", "Orange", "Pineapple", "Pomegranate"]},
            },
        ],
    },
]
