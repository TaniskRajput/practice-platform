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


# ============================================================ #
# MCQ quizzes (16-20): Web Mock 1-3 + SQL Mock 1-2, scraped     #
# from the KN Academy course (extracted/mcq-quizzes.json).      #
# ============================================================ #

QUIZ_PROBLEMS = [
    # ------------------------------------------------------------------ #
    # 16. Web Mock-1 (HTML/CSS/JS)
    # ------------------------------------------------------------------ #
    {
        "id": 16,
        "slug": "web-mock-1",
        "title": "Web Mock-1 (HTML/CSS/JS)",
        "difficulty": "Easy",
        "topics": "HTML · CSS · JavaScript".split(" · "),
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p>20 MCQs straight from the KN Academy Web Mock-1 — pick the correct option for each and submit to get graded.</p>
<p>Select an option for every question, then press <b>Submit</b>. Correct answers
turn green; wrong picks show the right one. Your score out of 20 is shown at the end.</p>
""",
        "hint": "The mock platform grades instantly per question — here you pick everything first, "
                "then submit to see the full answer key. Re-attempt any time; nothing is saved as wrong.",
        "boilerplate": {},
        "samples": [],
        "questions": [
        {
                "q": "Which of the following colors contain equal amounts of RBG?",
                "options": [
                        "White",
                        "Gray",
                        "Black",
                        "All of the above"
                ],
                "answer": 3
        },
        {
                "q": "Which of the following is a valid way to integrate CSS into a webpage?",
                "options": [
                        "Inline",
                        "External",
                        "Internal",
                        "All of the above"
                ],
                "answer": 3
        },
        {
                "q": "Which CSS property is used to change the text color of an element?",
                "options": [
                        "text-color",
                        "color",
                        "font-color",
                        "background-color"
                ],
                "answer": 1
        },
        {
                "q": "What will be the output of the following code snippet?",
                "options": [
                        "{first: 20, second: 30}",
                        "{first: 50, second: 30}",
                        "{first: 20, second: 30, first: 50}",
                        "Syntax Error"
                ],
                "answer": 1
        },
        {
                "q": "Which of the following is not a difference between HTML and XHTML?",
                "options": [
                        "Charset in both html and xhtml is “text/html”",
                        "Tags and attributes are case-insensitive in HTML but not in XHTML",
                        "Special characters must be escaped using character entities in XHTML unlike HTML",
                        "Charset in html is “text/html” where as in xhtml it is “application/xml+xhtml”"
                ],
                "answer": 0
        },
        {
                "q": "Which of the following is a correct syntax to display “Hello World” in an alert box using JavaScript?",
                "options": [
                        "alertBox(&#x27;Hello World&#x27;);",
                        "alert(&#x27;Hello World&#x27;);",
                        "msgAlert(&#x27;Hello World&#x27;);",
                        "displayAlert(&#x27;Hello World&#x27;);"
                ],
                "answer": 1
        },
        {
                "q": "What does the undefined value in JavaScript represent?",
                "options": [
                        "An unassigned variable",
                        "A null value",
                        "A logical false",
                        "An error condition"
                ],
                "answer": 0
        },
        {
                "q": "What is the &lt;select&gt; tag used for?",
                "options": [
                        "Creates a combo box.",
                        "Select some attributes and change their style.",
                        "Change text font.",
                        "None of the above."
                ],
                "answer": 0
        },
        {
                "q": "Which of the following are examples of block-level elements in HTML?",
                "options": [
                        "&lt;div&gt;",
                        "&lt;p&gt;",
                        "&lt;h1&gt;",
                        "All of the above"
                ],
                "answer": 3
        },
        {
                "q": "Which selector is used to target an element based on its id?",
                "options": [
                        "#id",
                        ".id",
                        "*id",
                        "id"
                ],
                "answer": 0
        },
        {
                "q": "How do you select elements with the class name &quot;example&quot;?",
                "options": [
                        ".example",
                        "#example",
                        "example",
                        "*example"
                ],
                "answer": 0
        },
        {
                "q": "What will be the output of the following code snippet?",
                "options": [
                        "Object",
                        "Number",
                        "String",
                        "None of the above"
                ],
                "answer": 1
        },
        {
                "q": "What is DOM in HTML?",
                "options": [
                        "Language dependent application programming",
                        "Hierarchy of objects in ASP.NET",
                        "Application programming interface",
                        "Convention for representing and interacting with objects in html documents"
                ],
                "answer": 3
        },
        {
                "q": "Which element is used to get highlighted text in HTML5?",
                "options": [
                        "&lt;u&gt;",
                        "&lt;mark&gt;",
                        "&lt;highlight&gt;",
                        "&lt;b&gt;"
                ],
                "answer": 1
        },
        {
                "q": "Which operator is used to check both the value and the type of a variable in JavaScript?",
                "options": [
                        "==",
                        "===",
                        "!=",
                        "!=="
                ],
                "answer": 1
        },
        {
                "q": "What is the output of the following code snippet? let x = &#x27;Hello&#x27;; let y = &#x27;World&#x27;; console.log(x + &#x27; &#x27; + y);",
                "options": [
                        "HelloWorld",
                        "&#x27;Hello World&#x27;",
                        "&#x27;Hello&#x27; &#x27;World&#x27;",
                        "Hello World"
                ],
                "answer": 1
        },
        {
                "q": "How do you define a function in JavaScript?",
                "options": [
                        "function = myFunc() {}",
                        "function: myFunc() {}",
                        "function myFunc() {}",
                        "myFunc() = function {}"
                ],
                "answer": 2
        },
        {
                "q": "What is meant by an empty tag in HTML?",
                "options": [
                        "There is no such concept of an empty tag in HTML",
                        "An empty tag does not require a closing tag",
                        "An empty tag cannot have any content within it",
                        "None of the above"
                ],
                "answer": 1
        },
        {
                "q": "Which of the following properties is used to change the font of text?",
                "options": [
                        "font-family",
                        "font-size",
                        "text-align",
                        "None of the above"
                ],
                "answer": 0
        },
        {
                "q": "Identify the error in the CSS code: .class { color: blue; font-weight; bold; }",
                "options": [
                        "Syntax error in property declaration",
                        "Missing class name",
                        "Incorrect property value",
                        "No error"
                ],
                "answer": 0
        }
],
    },

    # ------------------------------------------------------------------ #
    # 17. Web Mock-2 (HTML/CSS/JS)
    # ------------------------------------------------------------------ #
    {
        "id": 17,
        "slug": "web-mock-2",
        "title": "Web Mock-2 (HTML/CSS/JS)",
        "difficulty": "Easy",
        "topics": "HTML · CSS · JavaScript".split(" · "),
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p>20 MCQs straight from the KN Academy Web Mock-2 — pick the correct option for each and submit to get graded.</p>
<p>Select an option for every question, then press <b>Submit</b>. Correct answers
turn green; wrong picks show the right one. Your score out of 20 is shown at the end.</p>
""",
        "hint": "The mock platform grades instantly per question — here you pick everything first, "
                "then submit to see the full answer key. Re-attempt any time; nothing is saved as wrong.",
        "boilerplate": {},
        "samples": [],
        "questions": [
        {
                "q": "What components make up the CSS Box Model?",
                "options": [
                        "Content, Padding, Border, Margin",
                        "Padding, Margin, Border, Shadow",
                        "Content, Margin, Border, Outline",
                        "Content, Padding, Shadow, Margin"
                ],
                "answer": 0
        },
        {
                "q": "Which CSS property is used to control the outer space around an element?",
                "options": [
                        "Padding",
                        "Margin",
                        "Border",
                        "Content"
                ],
                "answer": 1
        },
        {
                "q": "What will be the output of the following code snippet?",
                "options": [
                        "8",
                        "7",
                        "0",
                        "1"
                ],
                "answer": 1
        },
        {
                "q": "What will be the output of the following code snippet?",
                "options": [
                        "0 1 2",
                        "0 undefined undefined",
                        "undefined undefined undefined",
                        "None of the above"
                ],
                "answer": 2
        },
        {
                "q": "What will be the output of the following code snippet?",
                "options": [
                        "[111, 44, 1, 22]",
                        "[44,1,22,111]",
                        "[111,44,22,1]",
                        "[1,22,111,44]"
                ],
                "answer": 0
        },
        {
                "q": "HTML is a subset of ___________",
                "options": [
                        "SGMT",
                        "SGML",
                        "SGME",
                        "XHTML"
                ],
                "answer": 1
        },
        {
                "q": "Which of the following HTML code will make an image clickable?",
                "options": [
                        "&lt;a href=&quot;https://www.knacademy.com/&quot;&gt;KN Academy Home Page&lt;/a&gt;",
                        "&lt;img src=&quot;https://www.knacademy.com/knacademy-logo&quot;&gt; &lt;a href=&quot;https://www.knacademy.com/&quot;&gt;KN Academy Home Page&lt;/a&gt; &lt;/img&gt;",
                        "&lt;a href=&quot;https://www.knacademy.com/&quot;&gt;KN Academy Home Page&lt;/a&gt; &lt;img src=&quot;https://www.knacademy.com/knacademy-logo&quot; /&gt;",
                        "&lt;a href=&quot;https://www.knacademy.com/&quot;&gt;&lt;img src=&quot;https://www.knacademy.com/knacademy-logo&quot; /&gt;&lt;/a&gt;"
                ],
                "answer": 3
        },
        {
                "q": "Which HTML element is used for short quote?",
                "options": [
                        "&lt;em&gt;",
                        "&lt;abbr&gt;",
                        "&lt;q&gt;",
                        "&lt;blockquote&gt;"
                ],
                "answer": 2
        },
        {
                "q": "[Image question] What is the output of the JavaScript code shown? An array of 3 elements has a new element pushed onto it (see images/web-mock-2-q9.png). console.log(arr.length) after push.",
                "options": [
                        "3",
                        "4",
                        "5",
                        "Error"
                ],
                "answer": 1
        },
        {
                "q": "[Image question] What is the flaw in the JavaScript function shown? A pow(x, n) style function is defined without a default for the exponent parameter (see images/web-mock-2-q10.png).",
                "options": [
                        "It doesn&#x27;t handle the case when exponent is not provided",
                        "It returns the wrong value",
                        "It causes an infinite loop",
                        "Syntax error"
                ],
                "answer": 0
        },
        {
                "q": "Which property allows an image link to show a text label?",
                "options": [
                        "alt",
                        "str",
                        "alternative",
                        "None of the above"
                ],
                "answer": 0
        },
        {
                "q": "How is black color represented in terms of RGB values?",
                "options": [
                        "RCB(0, 0, 0)",
                        "RCB(100, 100, 100)",
                        "RCB(100, 100, 0)",
                        "RCB(100, 0, 0)"
                ],
                "answer": 0
        },
        {
                "q": "The default value of the BORDER attribute is?",
                "options": [
                        "1pixel",
                        "2pixel",
                        "4pixel",
                        "8pixel"
                ],
                "answer": 0
        },
        {
                "q": "What are the types of unordered lists in HTML?",
                "options": [
                        "Circle,square,disc",
                        "Triangle,square,disc",
                        "Triangle,circle,disc",
                        "All of the above"
                ],
                "answer": 0
        },
        {
                "q": "What are those objects called which are used for storing data on the client provided by the HTML local storage?",
                "options": [
                        "Windows.localStorage",
                        "Windows.sessionStorage",
                        "Both A and B",
                        "None of the above"
                ],
                "answer": 2
        },
        {
                "q": "What does the Alpha value in RGBA represent?",
                "options": [
                        "Opacity value for a color",
                        "The shade of a color",
                        "Both A and B",
                        "None of the above"
                ],
                "answer": 0
        },
        {
                "q": "What does the Alpha value of 0.0 represent?",
                "options": [
                        "Fully Opaque",
                        "Fully Transparent",
                        "50% Transparent",
                        "None of the above"
                ],
                "answer": 1
        },
        {
                "q": "How does setting &#x27;margin: auto;&#x27; affect an element?",
                "options": [
                        "Centers the element horizontally",
                        "Increases the element&#x27;s height",
                        "Adds automatic padding",
                        "Does nothing specific"
                ],
                "answer": 0
        },
        {
                "q": "What will be the output of the following code snippet?",
                "options": [
                        "-Infinity Infinity",
                        "Infinity -Infinity",
                        "Infinity Infinity",
                        "-Infinity -Infinity"
                ],
                "answer": 0
        },
        {
                "q": "What will be the output of the following code snippet?",
                "options": [
                        "11 NaN NaN",
                        "11 NaN [object Object]",
                        "11 Hello6 [object Object]6",
                        "None of the above"
                ],
                "answer": 2
        }
],
    },

    # ------------------------------------------------------------------ #
    # 18. Web Mock-3 (HTML/CSS/JS)
    # ------------------------------------------------------------------ #
    {
        "id": 18,
        "slug": "web-mock-3",
        "title": "Web Mock-3 (HTML/CSS/JS)",
        "difficulty": "Easy",
        "topics": "HTML · CSS · JavaScript".split(" · "),
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p>20 MCQs straight from the KN Academy Web Mock-3 — pick the correct option for each and submit to get graded.</p>
<p>Select an option for every question, then press <b>Submit</b>. Correct answers
turn green; wrong picks show the right one. Your score out of 20 is shown at the end.</p>
""",
        "hint": "The mock platform grades instantly per question — here you pick everything first, "
                "then submit to see the full answer key. Re-attempt any time; nothing is saved as wrong.",
        "boilerplate": {},
        "samples": [],
        "questions": [
        {
                "q": "What is the work of &lt;address&gt; element in HTML5?",
                "options": [
                        "contains IP address",
                        "contains home address",
                        "contains url",
                        "contains contact details for author"
                ],
                "answer": 3
        },
        {
                "q": "An element has width: 100px; padding: 15px; border: 5px solid black;. What is its total width if box-sizing: content-box;?",
                "options": [
                        "100px",
                        "115px",
                        "130px",
                        "140px"
                ],
                "answer": 3
        },
        {
                "q": "Identify the issue: div { width: 100%; padding: 20px; } without using box-sizing: border-box;",
                "options": [
                        "The div will be wider than its parent",
                        "The div&#x27;s width is too small",
                        "No issue",
                        "The padding is ignored"
                ],
                "answer": 0
        },
        {
                "q": "What will be the output of the following code snippet? [See image: images/web-mock-3-q4.png]",
                "options": [
                        "NaN",
                        "Number",
                        "Object",
                        "Array"
                ],
                "answer": 2
        },
        {
                "q": "What will be the output of the following code snippet? [See image: images/web-mock-3-q5.png]",
                "options": [
                        "3",
                        "0",
                        "Error",
                        "5"
                ],
                "answer": 3
        },
        {
                "q": "How do you find the length of an array in JavaScript?",
                "options": [
                        "array.size()",
                        "array.length",
                        "array.count()",
                        "length(array)"
                ],
                "answer": 1
        },
        {
                "q": "In JavaScript, how can you check if a variable is an array?",
                "options": [
                        "typeof variable",
                        "variable.isArray()",
                        "Array.isArray(variable)",
                        "variable instanceof Array"
                ],
                "answer": 2
        },
        {
                "q": "[Image question] What is the output of the JavaScript function shown? The function takes a number and returns its cube (num * num * num) (see images/web-mock-3-q8.png).",
                "options": [
                        "[1, 2, 3, 4]",
                        "[10, 20, 30, 40]",
                        "[0.1, 0.2, 0.3, 0.4]",
                        "Error"
                ],
                "answer": 0
        },
        {
                "q": "What will be the output of this code snippet? let numbers = [1, 2, 3]; numbers[10] = 11; console.log(numbers.length);",
                "options": [
                        "3",
                        "4",
                        "11",
                        "10"
                ],
                "answer": 2
        },
        {
                "q": "Output of the below Js code snippet: [See image: images/web-mock-3-q10.png]",
                "options": [
                        "44",
                        "8",
                        "4",
                        "Error"
                ],
                "answer": 0
        },
        {
                "q": "What CSS property allows an element to expand in proportion to its sibling elements in a flex container?",
                "options": [
                        "flex-grow",
                        "flex-wrap",
                        "align-content",
                        "justify-content"
                ],
                "answer": 0
        },
        {
                "q": "What does the CSS box-shadow property do?",
                "options": [
                        "Adds a shadow inside the border of an element.",
                        "Adds a shadow outside the border of an element.",
                        "Increases the width of the border.",
                        "Controls the visibility of the element."
                ],
                "answer": 1
        },
        {
                "q": "What is the correct syntax of web address?",
                "options": [
                        "port://domain.filenmae:path/scheme/prefix",
                        "prefix://scheme.port:domain/filename/path",
                        "path://prefix.port:domain/filename/scheme",
                        "scheme://prefix.domain:port/path/filename"
                ],
                "answer": 3
        },
        {
                "q": "Which attribute is not essential under &lt;iframe&gt;?",
                "options": [
                        "frameborder",
                        "width",
                        "height",
                        "src"
                ],
                "answer": 0
        },
        {
                "q": "Which property aligns a flex item in the center of its container along the main axis?",
                "options": [
                        "align-self: center",
                        "justify-self: center",
                        "justify-content: center",
                        "align-items: center"
                ],
                "answer": 2
        },
        {
                "q": "What will be the output of the following code snippet? [See image: images/web-mock-3-q16.png]",
                "options": [
                        "4 10 18",
                        "1 2 3",
                        "1 4 7",
                        "None of the above"
                ],
                "answer": 0
        },
        {
                "q": "What will be the output of the following code snippet? [See image: images/web-mock-3-q17.png]",
                "options": [
                        "1 2 3 4",
                        "2 3 4 1",
                        "2 4 3 1",
                        "4 3 2 1"
                ],
                "answer": 2
        },
        {
                "q": "How do you create a new object in JavaScript?",
                "options": [
                        "Object.create()",
                        "new Object()",
                        "Both A and B",
                        "Neither A nor B"
                ],
                "answer": 2
        },
        {
                "q": "Given the following code, what is printed to the console? let obj1 = { a: 1 }; let obj2 = { a: 1 }; console.log(obj1 === obj2);",
                "options": [
                        "true",
                        "false",
                        "null",
                        "Error"
                ],
                "answer": 1
        },
        {
                "q": "Which of the following values of the position property will position an element relative to its nearest positioned ancestor?",
                "options": [
                        "absolute",
                        "relative",
                        "fixed",
                        "static"
                ],
                "answer": 0
        }
],
    },

    # ------------------------------------------------------------------ #
    # 19. SQL Mock-1
    # ------------------------------------------------------------------ #
    {
        "id": 19,
        "slug": "sql-mock-1",
        "title": "SQL Mock-1",
        "difficulty": "Easy",
        "topics": "SQL · Queries".split(" · "),
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p>15 SQL MCQs from the KN Academy SQL Mock-1 live test — choose the query that does what the question asks.</p>
<p>Select an option for every question, then press <b>Submit</b>. Correct answers
turn green; wrong picks show the right one. Your score out of 15 is shown at the end.</p>
""",
        "hint": "The mock platform grades instantly per question — here you pick everything first, "
                "then submit to see the full answer key. Re-attempt any time; nothing is saved as wrong.",
        "boilerplate": {},
        "samples": [],
        "questions": [
        {
                "q": "Retrieve all products priced above the average price.",
                "options": [
                        "SELECT * FROM Products WHERE Price &gt;= (SELECT AVG(Price) FROM Products);",
                        "SELECT * FROM Products WHERE Price &gt; (SELECT AVG(Price) FROM Products);",
                        "SELECT * FROM Products WHERE Price &gt; (SELECT AVERAGE(Price) FROM Products);",
                        "SELECT * FROM Products WHERE Price &gt; SELECT AVG(Price);"
                ],
                "answer": 1
        },
        {
                "q": "Display products in the Furniture category, ordered by price descending.",
                "options": [
                        "SELECT * FROM Products WHERE Category = &#x27;Furniture&#x27; ORDER BY Price;",
                        "SELECT * FROM Products WHERE Category == &#x27;Furniture&#x27; ORDER BY Price DESC;",
                        "SELECT * FROM Products WHERE Category = &#x27;Furniture&#x27; ORDER BY Price DESC;",
                        "SELECT * FROM Products WHERE Category = &#x27;Furniture&#x27; ORDER BY DESC;"
                ],
                "answer": 2
        },
        {
                "q": "Show products whose names contain the word &quot;Table.&quot;",
                "options": [
                        "SELECT * FROM Products WHERE Product_Name LIKE &#x27;%Table%&#x27;;",
                        "SELECT * FROM Products WHERE Product_Name LIKE &#x27;Table%&#x27;;",
                        "SELECT * FROM Products WHERE Product_Name LIKE &#x27;%Table_&#x27;;",
                        "SELECT * FROM Products WHERE Product_Name = &#x27;%Table%&#x27;;"
                ],
                "answer": 0
        },
        {
                "q": "Show products with prices within 20% of the maximum price.",
                "options": [
                        "SELECT * FROM Products WHERE Price &gt;= 0.2 * (SELECT MAX(Price) FROM Products);",
                        "SELECT * FROM Products WHERE Price &gt;= 0.8 * SELECT MAX(Price);",
                        "SELECT * FROM Products WHERE Price &gt; 0.8 * (SELECT MAX(Price) FROM Products);",
                        "SELECT * FROM Products WHERE Price &gt;= 0.8 * (SELECT MAX(Price) FROM Products);"
                ],
                "answer": 3
        },
        {
                "q": "Find products priced as a multiple of 5000.",
                "options": [
                        "SELECT * FROM Products WHERE Price / 5000 = 0;",
                        "SELECT * FROM Products WHERE Price % 5000 = 0;",
                        "SELECT * FROM Products WHERE Price % 5000 == 0;",
                        "SELECT * FROM Products WHERE Price % 5000 equal to 0;"
                ],
                "answer": 1
        },
        {
                "q": "Write a SQL query to fetch &quot;FIRST_NAME&quot; from the Student table in upper case and use ALIAS name as STUDENT_NAME.",
                "options": [
                        "SELECT upper(FIRST_NAME) as STUDENT_NAME from Student;",
                        "SELECT FIRST_NAME as STUDENT_NAME from Student;",
                        "SELECT upper(FIRST_NAME)from Student;",
                        "SELECT upper(FIRSTNAME) as STUDENT_NAME from Student;"
                ],
                "answer": 0
        },
        {
                "q": "Write a SQL query to fetch unique values of MAJOR Subjects from Student table.",
                "options": [
                        "SELECT MAJOR from STUDENT;",
                        "SELECT DISTINCT MAJOR from STUDENT ORDER BY MAJOR;",
                        "SELECT DISTINCT MAJOR from STUDENT;",
                        "None of the above"
                ],
                "answer": 2
        },
        {
                "q": "Write a SQL query that fetches the unique values of MAJOR Subjects from Student table and print its length.",
                "options": [
                        "SELECT MAJOR,LENGTH(MAJOR) FROM Student GROUP BY(MAJOR);",
                        "SELECT MAJOR,LENGTH(MAJOR) FROM Student ORDER BY(MAJOR);",
                        "SELECT MAJOR,LENGTH(MAJOR) FROM Student;",
                        "None of the above"
                ],
                "answer": 0
        },
        {
                "q": "Write a SQL query to print FIRST_NAME from the Student table after replacing &#x27;a&#x27; with &#x27;A&#x27;.",
                "options": [
                        "SELECT REPLACE(&#x27;a&#x27;, &#x27;A&#x27;) FROM Student;",
                        "SELECT REPLACE(FIRST_NAME, &#x27;A&#x27;, &#x27;a&#x27;) FROM Student;",
                        "SELECT REPLACE(FIRST_NAME, &#x27;a&#x27;, &#x27;A&#x27;) FROM Student;",
                        "None of the above"
                ],
                "answer": 2
        },
        {
                "q": "Write an SQL query to fetch the count of Students having Major Subject ‘Computer Science’",
                "options": [
                        "SELECT Major, COUNT(*) as TOTAL_COUNT FROM Student WHERE MAJOR = &#x27;Computer Science&#x27;;",
                        "SELECT Major, COUNT(*) as TOTAL_COUNT FROM Student WHERE MAJOR ==&#x27;Computer Science&#x27;;",
                        "SELECT Major FROM Student WHERE MAJOR = &#x27;Computer Science&#x27;;",
                        "None of the above"
                ],
                "answer": 0
        },
        {
                "q": "Identify the error in &quot;SELECT Name, NULLIF(Age, 30) FROM Employees WHERE Age IS NOT NULL;&quot;",
                "options": [
                        "Change &#x27;NULLIF&#x27; to &#x27;ISNULL&#x27;",
                        "Replace &#x27;Age, 30&#x27; with &#x27;Age, 0&#x27;",
                        "Remove &#x27;WHERE Age IS NOT NULL&#x27;",
                        "No error"
                ],
                "answer": 2
        },
        {
                "q": "What is the main use of the CASE statement in SQL?",
                "options": [
                        "To execute a sequence of commands",
                        "To handle errors",
                        "To perform if-then-else type logic",
                        "To loop through records"
                ],
                "answer": 2
        },
        {
                "q": "What needs to be corrected in &quot;SELECT CURRENT_DATE FROM Employees;&quot;?",
                "options": [
                        "Replace &#x27;CURRENT_DATE&#x27; with &#x27;GETDATE()&#x27;",
                        "Remove &#x27;FROM Employees&#x27;",
                        "Add &#x27;AS Today&#x27;",
                        "No error"
                ],
                "answer": 1
        },
        {
                "q": "In &quot;SELECT Name, AGE(BirthDate) AS Age FROM Customers;&quot;, what needs correction?",
                "options": [
                        "AGE",
                        "AS Age",
                        "BirthDate",
                        "No error"
                ],
                "answer": 0
        },
        {
                "q": "What needs to be corrected in &quot;SELECT CONCAT(FirstName, &#x27; &#x27;, LastName) FROM Employees;&quot;?",
                "options": [
                        "Change &#x27;CONCAT&#x27; to &#x27;CONCATENATE&#x27;",
                        "Replace &#x27;,&#x27; with &#x27;+&#x27;",
                        "Add &#x27;AS FullName&#x27; for clarity",
                        "No error"
                ],
                "answer": 2
        }
],
    },

    # ------------------------------------------------------------------ #
    # 20. SQL Mock-2
    # ------------------------------------------------------------------ #
    {
        "id": 20,
        "slug": "sql-mock-2",
        "title": "SQL Mock-2",
        "difficulty": "Easy",
        "topics": "SQL · Queries".split(" · "),
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p>15 SQL MCQs from the KN Academy SQL Mock-2 live test — choose the query that does what the question asks.</p>
<p>Select an option for every question, then press <b>Submit</b>. Correct answers
turn green; wrong picks show the right one. Your score out of 15 is shown at the end.</p>
""",
        "hint": "The mock platform grades instantly per question — here you pick everything first, "
                "then submit to see the full answer key. Re-attempt any time; nothing is saved as wrong.",
        "boilerplate": {},
        "samples": [],
        "questions": [
        {
                "q": "Display the details of students who have received scholarships, including their names, scholarship amounts, and scholarship dates.",
                "options": [
                        "SELECT Student.FIRST_NAME, Student.LAST_NAME, Scholarship.SCHOLARSHIP_AMOUNT, Scholarship.SCHOLARSHIP_DATE FROM Student INNER JOIN Student ON Student.STUDENT_ID = Scholarship.STUDENT_REF_ID;",
                        "SELECT Student.FIRST_NAME, Student.LAST_NAME, Scholarship.SCHOLARSHIP_AMOUNT, Scholarship.SCHOLARSHIP_DATE FROM Student INNER JOIN Scholarship ON Student.STUDENT_ID = Scholarship.STUDENT_REF_ID;",
                        "SELECT Student.FIRST_NAME, Student.LAST_NAME, Scholarship.SCHOLARSHIP_AMOUNT, FROM Student INNER JOIN Scholarship ON Student.STUDENT_ID = Scholarship.STUDENT_REF_ID;",
                        "None of the above"
                ],
                "answer": 1
        },
        {
                "q": "List all students and their scholarship amounts if they have received any. If a student has not received a scholarship, display NULL for the scholarship details.",
                "options": [
                        "SELECT Student.FIRST_NAME, Student.LAST_NAME, Scholarship.SCHOLARSHIP_AMOUNT, Scholarship.SCHOLARSHIP_DATE FROM Student JOIN Scholarship ON Student.STUDENT_ID = Scholarship.STUDENT_REF_ID;",
                        "SELECT Student.FIRST_NAME, Student.LAST_NAME, Scholarship.SCHOLARSHIP_AMOUNT, Scholarship.SCHOLARSHIP_DATE FROM Student LEFT JOIN Scholarship ON Student.STUDENT_ID = Scholarship.STUDENT_ID;",
                        "SELECT Student.FIRST_NAME, Student.LAST_NAME, Scholarship.SCHOLARSHIP_AMOUNT, Scholarship.SCHOLARSHIP_DATE FROM Student LEFT JOIN Scholarship ON Student.STUDENT_ID = Scholarship.STUDENT_REF_ID;",
                        "None of the above"
                ],
                "answer": 2
        },
        {
                "q": "Write an SQL query to show the top n (say 5) records of Student table order by descending GPA.",
                "options": [
                        "SELECT * from Student ORDER BY GPA DESC;",
                        "SELECT * from Student ORDER BY GPA DESC LIMIT 5;",
                        "SELECT * from Student GROUP BY GPA DESC LIMIT 5;",
                        "None of the above"
                ],
                "answer": 1
        },
        {
                "q": "Write an SQL query to fetch the first 50% records from a table.",
                "options": [
                        "SELECT * FROM Student LIMIT (SELECT COUNT(*) FROM Student) / 2;",
                        "SELECT * FROM Student LIMIT (SELECT COUNT(*) FROM Student) % 2;",
                        "SELECT * FROM Student LIMIT ((SELECT COUNT(*) FROM Student) / 2);",
                        "None of the above"
                ],
                "answer": 0
        },
        {
                "q": "Write an SQL query to show the current date and time.",
                "options": [
                        "SELECT CURDATE();",
                        "SELECT NOW();",
                        "SELECT DATETIME();",
                        "None of the above"
                ],
                "answer": 1
        },
        {
                "q": "Write a query to create a new table which consists of data and structure copied from the other table (say Student) or clone the table named Student.",
                "options": [
                        "CREATE CloneTable AS SELECT * FROM Student;",
                        "CREATE TABLE CloneTable SELECT * FROM Student;",
                        "CREATE TABLE CloneTable AS SELECT * FROM Student;",
                        "None of the above"
                ],
                "answer": 2
        },
        {
                "q": "Retrieve the full details of students along with their program names.",
                "options": [
                        "SELECT s.STUDENT_ID, s.FIRST_NAME, s.LAST_NAME, s.GPA, s.ENROLLMENT_DATE, s.MAJOR, p.PROGRAM_NAME FROM Student s JOIN Program p ON s.STUDENT_ID = p.STUDENT_REF_ID;",
                        "SELECT s.STUDENT_ID, s.FIRST_NAME, s.LAST_NAME, s.GPA, s.ENROLLMENT_DATE, s.MAJOR, FROM Student s JOIN Program p ON s.STUDENT_ID = p.STUDENT_REF_ID;",
                        "SELECT s.STUDENT_ID, s.FIRST_NAME, s.LAST_NAME, s.GPA, s.ENROLLMENT_DATE, s.MAJOR, p.PROGRAM_NAME FROM Student s JOIN Program p s.STUDENT_ID = p.STUDENT_REF_ID;",
                        "SELECT s.STUDENT_ID, s.FIRST_NAME, s.LAST_NAME, s.GPA, s.ENROLLMENT_DATE, s.MAJOR, p.PROGRAM_NAME FROM Student s JOIN Program p ON s.STUDENT_ID = p.STUDENT_ID;"
                ],
                "answer": 0
        },
        {
                "q": "List all students who received a scholarship along with the scholarship amount.",
                "options": [
                        "SELECT s.STUDENT_ID, s.FIRST_NAME, s.LAST_NAME, FROM Student s JOIN Scholarship sc ON s.STUDENT_ID = sc.STUDENT_REF_ID;",
                        "SELECT s.STUDENT_ID, s.FIRST_NAME, s.LAST_NAME, sc.SCHOLARSHIP_AMOUNT FROM JOIN Scholarship sc ON s.STUDENT_ID = sc.STUDENT_REF_ID;",
                        "SELECT s.STUDENT_ID, s.FIRST_NAME , s.LAST_NAME, sc.SCHOLARSHIP_AMOUNT FROM Student s JOIN Scholarship sc ON s.STUDENT_ID = sc.STUDENT_REF_ID;",
                        "None of the above"
                ],
                "answer": 2
        },
        {
                "q": "Get the names of students, their program names, and scholarship amounts (only for students who have a program and a scholarship).",
                "options": [
                        "SELECT s.FIRST_NAME, s.LAST_NAME, p.PROGRAM_NAME, sc.SCHOLARSHIP_AMOUNT FROM Student s JOIN Scholarship sc ON s.STUDENT_ID = sc.STUDENT_REF_ID;",
                        "SELECT s.FIRST_NAME, s.LAST_NAME, p.PROGRAM_NAME, sc.SCHOLARSHIP_AMOUNT FROM Student s JOIN Program p ON s.STUDENT_ID = p.STUDENT_REF_ID JOIN Scholarship sc ON s.STUDENT_ID = sc.STUDENT_REF_ID;",
                        "SELECT s.FIRST_NAME, s.LAST_NAME, p.PROGRAM_NAME, sc.SCHOLARSHIP_AMOUNT FROM Student s JOIN Program p ON s.STUDENT_ID = p.STUDENT_REF_ID",
                        "None of the above"
                ],
                "answer": 1
        },
        {
                "q": "List students who are enrolled in a program but haven’t received any scholarship.",
                "options": [
                        "SELECT s.STUDENT_ID, s.FIRST_NAME, s.LAST_NAME, p.PROGRAM_NAME FROM Student s JOIN Program p ON s.STUDENT_ID = p.STUDENT_REF_ID LEFT JOIN Scholarship sc ON s.STUDENT_ID = sc.STUDENT_REF_ID",
                        "SELECT s.STUDENT_ID, s.FIRST_NAME, s.LAST_NAME, p.PROGRAM_NAME FROM Student s JOIN Program p ON s.STUDENT_ID = p.STUDENT_ID LEFT JOIN Scholarship sc ON s.STUDENT_ID = sc.STUDENT_REF_ID WHERE sc.STUDENT_REF_ID IS NULL;",
                        "SELECT s.STUDENT_ID, s.FIRST_NAME, s.LAST_NAME, p.PROGRAM_NAME FROM Student s JOIN Program p ON s.STUDENT_ID = p.STUDENT_REF_ID LEFT JOIN Scholarship sc ON s.STUDENT_ID = sc.STUDENT_REF_ID WHERE sc.STUDENT_REF_ID IS NULL;",
                        "None"
                ],
                "answer": 2
        },
        {
                "q": "Show the GPA and scholarship amount for all students who have received a scholarship.",
                "options": [
                        "SELECT s.FIRST_NAME, s.LAST_NAME, s.GPA, sc.SCHOLARSHIP_AMOUNT FROM Student s JOIN Scholarship sc ON s.STUDENT_ID ;",
                        "SELECT s.FIRST_NAME, s.LAST_NAME, s.GPA, sc.SCHOLARSHIP_AMOUNT FROM Student s JOIN Scholarship sc ON s.STUDENT_ID = sc.STUDENT_REF_ID;",
                        "SELECT s.FIRST_NAME, s.LAST_NAME, s.GPA, sc.SCHOLARSHIP_AMOUNT FROM Student s JOIN Scholarship sc ON sc.STUDENT_REF_ID;",
                        "None of the above"
                ],
                "answer": 1
        },
        {
                "q": "Correct the syntax error in &quot;SELECT CEILING(Price) AS RoundedPrice FROM Products WHERE Price &gt; 0;&quot;",
                "options": [
                        "Change &#x27;CEILING&#x27; to &#x27;FLOOR&#x27;",
                        "Replace &#x27;AS RoundedPrice&#x27; with &#x27;AS PriceCeiling&#x27;",
                        "Remove &#x27;WHERE Price &gt; 0&#x27;",
                        "No error"
                ],
                "answer": 2
        },
        {
                "q": "How does the SQUARE function differ from the POWER function in SQL?",
                "options": [
                        "SQUARE calculates the square, POWER calculates any exponent",
                        "SQUARE and POWER are the same",
                        "SQUARE calculates the square root, POWER calculates the square",
                        "SQUARE calculates any exponent, POWER calculates the square"
                ],
                "answer": 0
        },
        {
                "q": "What does the CEILING function do in SQL?",
                "options": [
                        "Returns the smallest integer greater than or equal to a given number",
                        "Returns the largest integer less than or equal to a given number",
                        "Calculates the square of a number",
                        "Calculates the square root of a number"
                ],
                "answer": 0
        },
        {
                "q": "What is wrong in &quot;SELECT * FROM Employees FULL OUTER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID WHERE Departments.DepartmentName IS NULL;&quot;?",
                "options": [
                        "Replace &#x27;FULL OUTER JOIN&#x27; with &#x27;LEFT JOIN&#x27;",
                        "Change &#x27;WHERE&#x27; to &#x27;AND&#x27;",
                        "Remove &#x27;WHERE Departments.DepartmentName IS NULL&#x27;",
                        "No error"
                ],
                "answer": 2
        }
],
    },
]


# ============================================================ #
# PDF-based MCQ quizzes (21-22): Accenture Code MCQ + Paper    #
# Solution PDFs (extracted/downloaded/*-parsed.json).          #
# ============================================================ #

PDF_QUIZ_PROBLEMS = [
    # ------------------------------------------------------------------ #
    # 21. Accenture Code MCQ (Pseudocode)
    # ------------------------------------------------------------------ #
    {
        "id": 21,
        "slug": "code-mcq",
        "title": "Accenture Code MCQ (Pseudocode)",
        "difficulty": "Medium",
        "topics": "Pseudocode · Bitwise · Tracing".split(" · "),
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p>32 pseudo-code tracing MCQs from the <b>Accenture Code MCQ</b> PDF — trace the variable states and pick the printed output.</p>
<p>Select an option for every question, then press <b>Submit</b>. Correct answers
turn green; wrong picks show the right one. Your score out of 32 is shown at the end.</p>
""",
        "hint": "Source: KN Academy PDF (served in the PDF Resources section on the home page). "
                "Submit to see the full answer key; re-attempt any time.",
        "boilerplate": {},
        "samples": [],
        "questions": [
        {
                "q": "<b>1.</b> Pseudo-Code Tracing (Bitwise AND)<br>Initial values: p = 1, q = 8, r = 9 q = (11 + 9) &amp; q p = p + q Print p + q + r",
                "options": [
                        "6",
                        "10",
                        "18",
                        "24"
                ],
                "answer": 1
        },
        {
                "q": "<b>2.</b> Pseudo-Code Tracing<br>Values: a = 2, b = 8, c = 8 c = 9 + a if ((4 + 10 + a) &lt; (7 + c)) if ((7 + 6) &lt; c) if ((5 + c) &lt; (b + 5)) b = a + b Print a + b + c",
                "options": [
                        "17",
                        "21",
                        "22",
                        "23"
                ],
                "answer": 1
        },
        {
                "q": "<b>3.</b> Pseudo-Code Tracing<br>Values: a = 7, b = 4, c = 10 if ((b + c) &lt; (c + a + b)) b = b + c c = (b + b) + a Print a + b + c",
                "options": [
                        "32",
                        "35",
                        "56",
                        "28"
                ],
                "answer": 2
        },
        {
                "q": "<b>4.</b> Array / Bitwise AND<br>Array: arr = {{1,2},{2,4}} arr = arr + arr &amp; arr arr = (3 + 7) &amp; arr Print arr + arr",
                "options": [
                        "0.0",
                        "4.0",
                        "8.0",
                        "16.0"
                ],
                "answer": 0
        },
        {
                "q": "<b>5.</b> Pseudo-Code Tracing<br>Values: a = 1, b = 2, c = 10 if (((a+b)+(b+c)) &gt; (a+b+c)) if (a &lt; b) b = b + c Print a + b + c",
                "options": [
                        "9",
                        "13",
                        "15",
                        "23"
                ],
                "answer": 3
        },
        {
                "q": "<b>6.</b> Pseudo-Code Tracing<br>Values: a = 3, b = 8, c = 6 c = c + a b = (c + c) + c c = (b + b) + a Print a + b + c",
                "options": [
                        "37",
                        "51",
                        "87",
                        "39"
                ],
                "answer": 2
        },
        {
                "q": "<b>7.</b> Array / Bitwise XOR<br>Array: arr = {{0,1},{4,1}} arr = (4 + 1) + arr arr = 2 + arr arr = (arr ^ 1) + arr Print arr + arr",
                "options": [
                        "19",
                        "17",
                        "34",
                        "9"
                ],
                "answer": 2
        },
        {
                "q": "<b>8.</b> Recursive Pseudo-Code<br>A recursive function returns number + func(number - 1) if number &gt; 1.",
                "options": [
                        "Calculates factorial",
                        "Computes sum of number and predecessors",
                        "Multiplies predecessors",
                        "Finds square"
                ],
                "answer": 1
        },
        {
                "q": "<b>9.</b> JavaScript Array Method<br>var my_arr = [1,2,3]; function myfunction(elem) { return elem + 5; } document.write(my_arr.map(myfunction));",
                "options": [
                        "6,7,8",
                        "3,2,1",
                        "16",
                        "True"
                ],
                "answer": 0
        },
        {
                "q": "<b>10.</b> SQL UPDATE Query<br>Update the status of orders placed before January 1, 2023 to &#x27;Shipped&#x27;. Which SQL query correctly performs this update?",
                "options": [
                        "UPDATE orders SET status = &#x27;Delivered&#x27; WHERE order_date &lt; &#x27;2023-01-01&#x27;;",
                        "UPDATE orders SET status = &#x27;Shipped&#x27; WHERE order_date &gt; &#x27;2023-01-01&#x27;;",
                        "UPDATE orders SET status = &#x27;Shipped&#x27; WHERE status = &#x27;2023-01-01&#x27;;",
                        "UPDATE orders SET status = &#x27;Shipped&#x27; WHERE order_date &lt; &#x27;2023-01-01&#x27;;"
                ],
                "answer": 3
        },
        {
                "q": "<b>11.</b> SQL GROUP BY Clause<br>Which of the following shows the correct usage of the GROUP BY clause?",
                "options": [
                        "SELECT column_name1, column_name2 FROM table_name WHERE column_name = operator value GROUP BY column_name1",
                        "SELECT * FROM table_name WHERE column_name = operator value GROUP BY column_name",
                        "SELECT column_name, aggregate_function(column_name) FROM table_name WHERE column_name = operator value GROUP BY column_name",
                        "SELECT * FROM table_name GROUP BY column_name"
                ],
                "answer": 2
        },
        {
                "q": "<b>12.</b> SQL Query Optimization<br>Queries searching customers by Email are slow in a table with over 5 million rows. Which technique improves performance the most?",
                "options": [
                        "Adding more rows to the table",
                        "Creating an index on the Email column",
                        "Using a Foreign Key on the Email column",
                        "Denormalizing the table"
                ],
                "answer": 1
        },
        {
                "q": "<b>13.</b> HTML Audio Autoplay<br>Which code correctly implements autoplay for an audio element?",
                "options": [
                        "&lt;audio autoplay&gt; &lt;source src=&quot;test.mp3&quot;&gt; &lt;source src=&quot;test.ogg&quot;&gt; &lt;/audio&gt;",
                        "&lt;audio controls&gt;&lt;source src=&quot;test.mp3&quot;&gt;&lt;/audio&gt;",
                        "&lt;audio src=&quot;test.mp3&quot;&gt;&lt;/audio&gt;",
                        "&lt;audio autoplay controls src=&quot;test.mp3&quot;&gt;&lt;/audio&gt;"
                ],
                "answer": 0
        },
        {
                "q": "<b>14.</b> FUNCTION cal(number): IF number is 0 OR number is 1 RETURN 1 ELSE RETURN some_operation(number, cal(number - 1)) End IF END FUNCTION cal result = cal(input_number) PRINT result",
                "options": [
                        "Calculates the factorial of input_number",
                        "Computes the sum of input_number and its predecessors",
                        "Multiplies input_number by the product of its predecessors",
                        "Determines the square of input_number"
                ],
                "answer": 0
        },
        {
                "q": "<b>15.</b> &lt;body&gt; &lt;button onclick=&quot;myFunction(this);&quot;&gt;Test attribute!&lt;/button&gt; &lt;script type=&quot;text/javascript&quot;&gt; function myFunction(button) { var newAttr = document.createAttribute(&quot;myAttribute&quot;); newAttr.value = &quot;My Value&quot;; button.setAttributeNode(newAttr); document.write(button.getAttribute(&quot;myAttribute&quot;)); } &lt;/script&gt; &lt;/body&gt;",
                "options": [
                        "False",
                        "Test attribute!",
                        "My Value",
                        "Nothing will happen"
                ],
                "answer": 2
        },
        {
                "q": "<b>16.</b> &lt;html&gt; &lt;head&gt; &lt;script language=&quot;JavaScript&quot;&gt; function myFunction() { alert(&quot;My Function is called&quot;); } &lt;/script&gt; &lt;/head&gt; &lt;body&gt; &lt;img src=&quot;http://www.example.com/mylogo.png&quot; onabort=&quot;myFunction()&quot;&gt; &lt;/body&gt; &lt;/html&gt;",
                "options": [
                        "When the page is closed",
                        "When the page is loaded",
                        "When the user clicks on ESC before the page loads",
                        "When the page is refreshed"
                ],
                "answer": 2
        },
        {
                "q": "<b>17.</b> Which statement retrieves items in ascending order from a table in SQL?",
                "options": [
                        "SELECT * FROM [table] ORDER BY [tbl_clm];",
                        "SELECT * FROM [table] SORT BY [tbl_clm];",
                        "SELECT * FROM [table] ORDER BY [tbl_clm] ASC;",
                        "SELECT * FROM [table] GROUP BY [tbl_clm] ASC;"
                ],
                "answer": 2
        },
        {
                "q": "<b>18.</b> FUNCTION incrementByThree(n) RETURN n + 3 END FUNCTION total = 0 FOR i = 1 TO 3 total = total + incrementByThree(i) END FOR DISPLAY total",
                "options": [
                        "15",
                        "12",
                        "18",
                        "9"
                ],
                "answer": 0
        },
        {
                "q": "<b>19.</b> class Employee extends Person { Address address; }",
                "options": [
                        "Employee has &quot;Is-A&quot; relationship with Person and &quot;Has-A&quot; relationship with Address",
                        "Employee has &quot;Is-A&quot; relationship with Address and &quot;Has-A&quot; relationship with Person",
                        "Employee has &quot;Is-A&quot; relationship with Person and Address",
                        "Employee has &quot;Has-A&quot; relationship with Address and Person"
                ],
                "answer": 0
        },
        {
                "q": "<b>23.</b> class Children { private final void flipper() { System.out.println(&quot;Children&quot;); } } public class Parent extends Children { public final void flipper() { System.out.println(&quot;Parent&quot;); } public static void main(String[] args) { new Parent().flipper(); } }",
                "options": [
                        "Children",
                        "Parent",
                        "Children Parent",
                        "Parent Children"
                ],
                "answer": 1
        },
        {
                "q": "<b>24.</b> A company wants to automatically log whenever an employee record is deleted. Schema: CREATE TABLE Employees ( EmpID INT PRIMARY KEY , Name VARCHAR(50) ); CREATE TABLE Auditing ( LogID INT PRIMARY KEY AUTO_INCREMENT, EmpID INT, DeletedOn DATETIME );",
                "options": [
                        "CREATE TRIGGER trg_DeleteEmployee AFTER DELETE ON Employees FOR EACH ROW INSERT INTO Auditing (EmpID, DeletedOn) VALUES (OLD.EmpID, NOW());",
                        "CREATE TRIGGER trg_DeleteEmployee BEFORE DELETE ON Employees FOR EACH ROW INSERT INTO Auditing (EmpID, DeletedOn) VALUES (NEW.EmpID, NOW());",
                        "CREATE TRIGGER trg_DeleteEmployee AFTER INSERT ON Employees FOR EACH ROW INSERT INTO Auditing (EmpID, DeletedOn) VALUES (NEW.EmpID, NOW());",
                        "CREATE TRIGGER trg_DeleteEmployee AFTER DELETE ON Auditing FOR EACH ROW INSERT INTO Employees (EmpID) VALUES (OLD.EmpID);"
                ],
                "answer": 0
        },
        {
                "q": "<b>25.</b> Which statement retrieves items in ascending order from a table in SQL?",
                "options": [
                        "SELECT * FROM [table] ORDER BY [tbl_clm];",
                        "SELECT * FROM [table] SORT BY [tbl_clm];",
                        "SELECT * FROM [table] ORDER BY [tbl_clm] ASC;",
                        "SELECT * FROM [table] GROUP BY [tbl_clm] ASC;"
                ],
                "answer": 2
        },
        {
                "q": "<b>26.</b> FUNCTION incrementByThree(n) RETURN n + 3 END FUNCTION total = 0 FOR i = 1 TO 3 total = total + incrementByThree(i) END FOR DISPLAY total",
                "options": [
                        "15",
                        "12",
                        "18",
                        "9"
                ],
                "answer": 0
        },
        {
                "q": "<b>27.</b> A company wants to automatically log whenever an employee record is deleted. Schema: CREATE TABLE Employees ( EmpID INT PRIMARY KEY , Name VARCHAR(50) ); CREATE TABLE Auditing ( LogID INT PRIMARY KEY AUTO_INCREMENT, EmpID INT, DeletedOn DATETIME );",
                "options": [
                        "CREATE TRIGGER trg_DeleteEmployee AFTER DELETE ON Employees FOR EACH ROW INSERT INTO Auditing (EmpID, DeletedOn) VALUES (OLD.EmpID, NOW());",
                        "CREATE TRIGGER trg_DeleteEmployee BEFORE DELETE ON Employees FOR EACH ROW INSERT INTO Auditing (EmpID, DeletedOn) VALUES (NEW.EmpID, NOW());",
                        "CREATE TRIGGER trg_DeleteEmployee AFTER INSERT ON Employees FOR EACH ROW INSERT INTO Auditing (EmpID, DeletedOn) VALUES (NEW.EmpID, NOW());",
                        "CREATE TRIGGER trg_DeleteEmployee AFTER DELETE ON Auditing FOR EACH ROW INSERT INTO Employees (EmpID) VALUES (OLD.EmpID);"
                ],
                "answer": 0
        },
        {
                "q": "<b>28.</b> A company wants to automatically log whenever an employee record is deleted. Schema: CREATE TABLE Employees ( EmpID INT PRIMARY KEY , Name VARCHAR(50) ); CREATE TABLE Auditing ( LogID INT PRIMARY KEY AUTO_INCREMENT, EmpID INT, DeletedOn DATETIME );",
                "options": [
                        "A trigger using AFTER DELETE on Employees, FOR EACH ROW , inserting into Auditing (EmpID, DeletedOn) with values from OLD.EmpID and NOW().",
                        "A trigger using BEFORE DELETE on Employees, inserting into Auditing using NEW.EmpID.",
                        "A trigger using AFTER INSERT on Employees, inserting into Auditing using NEW .EmpID.",
                        "A trigger using AFTER DELETE on Auditing, inserting back into Employees."
                ],
                "answer": 0
        },
        {
                "q": "<b>29.</b> &lt;canvas id=&quot;myCanvas&quot;&gt;HTML5 Canvas not supported.&lt;/canvas&gt;",
                "options": [
                        "A comment for the user",
                        "A comment for incompatible browsers",
                        "A comment for Internet Explorer and Opera",
                        "All of the given options"
                ],
                "answer": 1
        },
        {
                "q": "<b>30.</b> class Employee extends Person { Address address; }",
                "options": [
                        "Employee has &quot;Is-A&quot; relationship with Person and &quot;Has-A&quot; relationship with Address",
                        "Employee has &quot;Is-A&quot; relationship with Address and &quot;Has-A&quot; relationship with Person",
                        "Employee has &quot;Is-A&quot; relationship with Person and Address",
                        "Employee has &quot;Has-A&quot; relationship with Address and Person"
                ],
                "answer": 0
        },
        {
                "q": "<b>32.</b> &lt;img src=&quot;...&quot; onabort=&quot;myFunction()&quot;&gt;",
                "options": [
                        "When the page is closed",
                        "When the page is loaded",
                        "When the user clicks on ESC before the page loads",
                        "When the page is refreshed"
                ],
                "answer": 2
        },
        {
                "q": "<b>33.</b> class Employee extends Person { Address address; }",
                "options": [
                        "Employee has &quot;Is-A&quot; relationship with Person and &quot;Has-A&quot; relationship with Address",
                        "Employee has &quot;Is-A&quot; relationship with Address and &quot;Has-A&quot; relationship with Person",
                        "Employee has &quot;Is-A&quot; relationship with Person and Address",
                        "Employee has &quot;Has-A&quot; relationship with Address and Person"
                ],
                "answer": 0
        },
        {
                "q": "<b>34.</b> var my_arr = [3, 16, 2, 18]; function myFunction(elem) { return elem + 5; } document.write(my_arr.map(myFunction));",
                "options": [
                        "8, 21, 7, 23",
                        "3, 16, 2, 18",
                        "False",
                        "True"
                ],
                "answer": 0
        },
        {
                "q": "<b>35.</b> Which optimization technique improves performance for: SELECT * FROM Customers WHERE Email = &#x27;abc@example.com&#x27;; when the table has over 5 million rows?",
                "options": [
                        "Adding more rows to the table",
                        "Creating an index on the Email column",
                        "Using a Foreign Key on the Email column",
                        "Denormalizing the table"
                ],
                "answer": 1
        },
        {
                "q": "<b>36.</b> SELECT emp_name FROM employees WHERE emp_name LIKE &#x27;%a%&#x27;;",
                "options": [
                        "Names starting with the alphabet &#x27;a&#x27;",
                        "Names ending with the alphabet &#x27;a&#x27;",
                        "Names containing the alphabet &#x27;a&#x27; anywhere",
                        "Names that do not contain the alphabet &#x27;a&#x27;"
                ],
                "answer": 2
        }
],
    },

    # ------------------------------------------------------------------ #
    # 22. Accenture Paper Solution (Cloud/DevOps/OS/Networks)
    # ------------------------------------------------------------------ #
    {
        "id": 22,
        "slug": "paper-solution",
        "title": "Accenture Paper Solution (Cloud/DevOps/OS/Networks)",
        "difficulty": "Medium",
        "topics": "Cloud · DevOps · OS · Networking · Security".split(" · "),
        "judge": "quiz",
        "languages": ["quiz"],
        "description": """
<p>43 MCQs from the <b>Accenture Paper Solution</b> PDF — the actual paper asked on campus, covering cloud, DevOps, OS, networking and security.</p>
<p>Select an option for every question, then press <b>Submit</b>. Correct answers
turn green; wrong picks show the right one. Your score out of 43 is shown at the end.</p>
""",
        "hint": "Source: KN Academy PDF (served in the PDF Resources section on the home page). "
                "Submit to see the full answer key; re-attempt any time.",
        "boilerplate": {},
        "samples": [],
        "questions": [
        {
                "q": "<b>1.</b> In a cloud-based application where scalability is crucial, which cloud storage option allows dynamic scaling without the need for manual intervention?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Object storage automatically scales as data grows, making it ideal for highly scalable cloud applications.</div>",
                "options": [
                        "Block storage",
                        "File storage",
                        "Object storage",
                        "Table storage"
                ],
                "answer": 2
        },
        {
                "q": "<b>2.</b> A mobile application needs to retrieve a list of all available restaurants from a food delivery service’s API. The application should only read data without making any changes to the server resources. Which HTTP method is most appropriate for this operation?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">GET is used to retrieve data from a server without modifying any existing resources.</div>",
                "options": [
                        "POST",
                        "PUT",
                        "DELETE",
                        "GET"
                ],
                "answer": 3
        },
        {
                "q": "<b>3.</b> During application development, a developer encounters an error due to an incorrect or unavailable API endpoint, resulting in a “Not Found” response. Which HTTP status code most accurately represents this error?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">HTTP 404 is returned when the requested endpoint or resource does not exist on the server.</div>",
                "options": [
                        "404",
                        "500",
                        "403",
                        "400"
                ],
                "answer": 0
        },
        {
                "q": "<b>5.</b> Which protocol is commonly used to secure data in transit over the internet by encrypting communication between systems?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">TLS (Transport Layer Security) encrypts data during transmission and is the modern, secure standard used for protecting data in transit.</div>",
                "options": [
                        "HTTP",
                        "MTP",
                        "SSL/TLS",
                        "SMTP"
                ],
                "answer": 2
        },
        {
                "q": "<b>10.</b> As a computer architect designing the control unit of a CPU, you need to specify how data is moved from the accumulator to memory. Which option best describes this operation?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Writing data from a CPU register (accumulator) into memory is classified as a memory write operation. 10. Hybrid Cloud Connectivity An enterprise is adopting a hybrid cloud model where they combine on-premise infrastructure with public cloud services to securely connect these environments and ensure reliability. What solutions should they implement? Answer: Secure VPN or dedicated connectivity like Direct Connect ensures reliable hybrid cloud integration. 11. VPN for Remote Access Assume that an</div>",
                "options": [
                        "The process of transferring data from the accumulator to memory is called a register transfer",
                        "The process of transferring data from the accumulator to memory is called a memory read operation",
                        "The process of transferring data from the accumulator to memory is called a memory write operation",
                        "The process of transferring data from the accumulator to memory is called an instruction fetch"
                ],
                "answer": 2
        },
        {
                "q": "<b>24.</b> You are building a training module in MS PowerPoint and want to restrict navigation so that users must view each slide sequentially with narration, without freely skipping slides. Which setting provides the strictest control over slide navigation?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">“Kiosk mode” disables manual slide navigation and forces slides to advance only as designed, providing the strictest control.</div>",
                "options": [
                        "Add hyperlinks between slides",
                        "Use normal Slide Show mode",
                        "Set up Slide Show as Browsed at a kiosk (full screen)",
                        "Enable Presenter View"
                ],
                "answer": 2
        },
        {
                "q": "<b>25.</b> If a company wants to ensure secure and reliable email transmission for its cloud-based email service, which protocol should they implement?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">SMTP (Simple Mail Transfer Protocol) is the standard protocol used for sending emails reliably between mail servers.</div>",
                "options": [
                        "HTTP",
                        "FTP",
                        "SMTP",
                        "POP3"
                ],
                "answer": 2
        },
        {
                "q": "<b>26.</b> To create a document template for repeated use, which file format should you save the document in?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">The .dotx format is specifically designed for Word document templates intended for repeated use.</div>",
                "options": [
                        ".docx",
                        ".pdf",
                        ".dotx",
                        ".txt"
                ],
                "answer": 2
        },
        {
                "q": "<b>27.</b> An application relies on multiple hardware peripherals and requires strict isolation from other running containers to maintain data integrity and operational security. The development team uses a kernel-level configuration to allocate specific hardware resources to each container and restrict access to non-allocated devices. What is the most critical factor in maintaining operational security and preventing resource contention among containers?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Strict kernel-level resource isolation prevents unauthorized hardware access and avoids resource contention between containers.</div>",
                "options": [
                        "Ensuring that the host OS scheduler allocates CPU cycles equally to all containers",
                        "Configuring the kernel to enforce strict resource isolation and limit peripheral access to only allocated devices",
                        "Allowing virtualization software to dynamically allocate additional memory as required",
                        "Allowing containers to share network interfaces with individual access control lists"
                ],
                "answer": 1
        },
        {
                "q": "<b>28.</b> Data is transferred between the CPU and a peripheral device through a shared bus controlled by device controllers to improve data transfer speed and reduce latency. The system uses controllers with dedicated high-speed buffers. Which of the following device controllers is most suitable for this purpose?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">SATA controllers provide high-speed buffered data transfer between storage devices and the CPU, minimizing latency and improving throughput.</div>",
                "options": [
                        "Wireless Controller",
                        "USB Controller",
                        "SATA Controller",
                        "Ethernet Controller"
                ],
                "answer": 2
        },
        {
                "q": "<b>29.</b> Hackers attempt to intercept and manipulate data packets traveling across a network by inserting malicious code or routing information, allowing them to redirect traffic through their own system. This enables them to eavesdrop or alter data without detection. What type of attack is this called?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Routing table poisoning redirects network traffic through the attacker’s system, enabling interception or modification of data packets.</div>",
                "options": [
                        "Packet Sniffing",
                        "IP Spoofing",
                        "Routing Table Poisoning",
                        "DNS Spoofing"
                ],
                "answer": 2
        },
        {
                "q": "<b>30.</b> Question: You are employed by a company that has recently suffered a security breach. As the IT manager, you are responsible for enhancing the security of the computer&#x27;s operating system. Which property of an operating system should you prioritize to achieve this goal?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Access control manages permissions and restricts unauthorized access, making it critical for operating system security.</div>",
                "options": [
                        "Access Control",
                        "User Interface",
                        "Multitasking",
                        "Virtual Memory"
                ],
                "answer": 0
        },
        {
                "q": "<b>31.</b> Jane wants to create a slide that illustrates a progression over time using icons, text, and blanks. She wants it to appear visually dynamic without manually animating each step. Which MS PowerPoint feature can help speed up this process?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">The Morph transition automatically animates objects across slides, creating a smooth visual progression without manual animation.</div>",
                "options": [
                        "Use Slide Zoom feature to create dynamic progression",
                        "Use a SmartArt process layout",
                        "Apply the Morph transition across duplicated slides for a smooth effect",
                        "Create a custom layout with background images and animation triggers"
                ],
                "answer": 2
        },
        {
                "q": "<b>31.</b> A cloud infrastructure requires running multiple isolated environments on a single physical server. Which technology is primarily used to achieve this?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Virtual machines provide full isolation for multiple environments on a single physical server, making them ideal for securely running separate workloads.</div>",
                "options": [
                        "Containers",
                        "Virtual Machines (VMs)",
                        "Serverless computing"
                ],
                "answer": 1
        },
        {
                "q": "<b>32.</b> During a context switch, the operating system saves the state of the currently running process and loads the state of the next process to be executed. Which CPU register, responsible for holding the address of the next instruction to be fetched, must be saved and restored during this operation?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">The Program Counter stores the address of the next instruction, so saving and restoring it ensures the process resumes correctly after a context switch.</div>",
                "options": [
                        "Stack Pointer",
                        "General Purpose Register",
                        "Program Counter",
                        "Instruction Register"
                ],
                "answer": 2
        },
        {
                "q": "<b>33.</b> Two geographically separate offices, Office A and Office B, need to allow all users in Office A to securely access resources in Office B and vice versa, as if they were on the same local network. Which VPN topology is most appropriate for this scenario?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">A Site-to-Site VPN connects entire networks across locations, allowing users in both offices to securely access each other’s resources as if on the same LAN.</div>",
                "options": [
                        "Remote Access VPN",
                        "Site-to-Site VPN",
                        "Client-to-Server VPN",
                        "Peer-to-Peer VPN"
                ],
                "answer": 1
        },
        {
                "q": "<b>34.</b> A development team is designing a new RESTful API to manage a product catalog for their ecommerce platform. They need to create an endpoint that retrieves details of a specific product using its unique product ID. Which HTTP method and URL structure best align with RESTful principles for this operation?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">The GET method is used in RESTful APIs to retrieve data, and including the product ID in the URL specifies the resource to fetch.</div>",
                "options": [
                        "POST /products/{productId}",
                        "GET /products/{productId}",
                        "PUT /products/{productId}",
                        "DELETE /products/{productId}"
                ],
                "answer": 1
        },
        {
                "q": "<b>35.</b> A containerized application is consuming massive memory, causing performance issues. What is the recommended approach to address this problem effectively?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Memory issues are best resolved by identifying and fixing leaks in the application code rather than just increasing container resources.</div>",
                "options": [
                        "Increase the memory limit for the container",
                        "Use a larger base image for the container",
                        "Reduce the number of replicas of the container",
                        "Analyze the application code for memory leaks"
                ],
                "answer": 3
        },
        {
                "q": "<b>37.</b> An internet connection is established by a user, connecting devices like a computer, smartphone, and smart TV to a router. Which OSI model layer is responsible for transmitting Ethernet, cable, and Wi-Fi signals between these devices?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">The Physical Layer handles the transmission of raw electrical, optical, or wireless signals over media like Ethernet cables and Wi-Fi.</div>",
                "options": [
                        "Physical Layer",
                        "Network Layer",
                        "Data Link Layer",
                        "Application Layer"
                ],
                "answer": 0
        },
        {
                "q": "<b>38.</b> Your machine may need to request a list of employees from the South region for an internal campaign. Which Excel formula allows you to generate this list dynamically from the dataset below? Sample Dataset: Employee Name Department Role Salary Bonus Join Date Region E001 Alice Sales Manager 70000 5000 01-03-2018 South E002 Bob HR Executive 50000 3000 12-06-2019 North E003 Carol IT Developer 60000 4000 15-08-2020 South E004 David Marketing Analyst 55000 3500 22-01-2021 East E005 Eve Sales Executive 52000 2500 30-11-2019 South<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">The FILTER function dynamically returns all rows where the Region column equals &quot;South,&quot; generating the required list automatically.</div>",
                "options": [
                        "=FILTER(A2:H6, H2:H6=&quot;South&quot;)",
                        "=VLOOKUP(&quot;South&quot;, H2:H6, 2, FALSE)",
                        "=INDEX(A2:A6, MATCH(&quot;South&quot;, H2:H6, 0))",
                        "=IF(H2:H6=&quot;South&quot;, A2:A6, &quot;&quot;)"
                ],
                "answer": 0
        },
        {
                "q": "<b>39.</b> In a PivotTable, which feature allows you to create custom calculations and summaries based on the existing data?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Calculated Fields let you define custom formulas in a PivotTable to perform calculations on the summarized data.</div>",
                "options": [
                        "Calculated Fields",
                        "Calculated Items",
                        "Slicers",
                        "Grouping"
                ],
                "answer": 0
        },
        {
                "q": "<b>40.</b> Data packets are transmitted between routers and switches to ensure proper delivery across different network segments. Which OSI model layer is responsible for establishing logical paths and routing data packets between different network segments?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">The Network Layer determines logical addressing and routing to deliver packets across multiple network segments.</div>",
                "options": [
                        "Data Link Layer",
                        "Network Layer",
                        "Transport Layer",
                        "Session Layer"
                ],
                "answer": 1
        },
        {
                "q": "<b>41.</b> In a cloud computing environment, which security measure helps protect user accounts by requiring two different types of identification before granting access?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">MFA enhances account security by requiring multiple forms of verification, such as a password and a one-time code.</div>",
                "options": [
                        "Firewalls",
                        "Encryption",
                        "Multi-Factor Authentication (MFA)",
                        "Antivirus Software"
                ],
                "answer": 2
        },
        {
                "q": "<b>42.</b> A small business uses ring network topology. If a single workstation goes down, what impact will it have on the network?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">In a ring topology, each device is connected in a closed loop, so the failure of one workstation disrupts the entire network.</div>",
                "options": [
                        "Minimal impact; network reroutes traffic",
                        "Network becomes isolated",
                        "Network slows down",
                        "Network breaks completely"
                ],
                "answer": 3
        },
        {
                "q": "<b>43.</b> What is the process of converting data into a secure format to prevent unauthorized access?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Encryption transforms data into a coded format to ensure that only authorized parties can access it.</div>",
                "options": [
                        "Encryption",
                        "Authentication",
                        "Authorization",
                        "Compression"
                ],
                "answer": 0
        },
        {
                "q": "<b>44.</b> A mobile application sends data to a server using an API. The developer decides to use the POST method for this operation. What is the primary characteristic of the POST method in this context?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">The POST method is used to send data to the server for processing, often resulting in the creation of a new resource.</div>",
                "options": [
                        "It retrieves data from the server",
                        "It updates existing data on the server",
                        "It submits data to be processed by the server",
                        "It deletes data from the server"
                ],
                "answer": 2
        },
        {
                "q": "<b>45.</b> A company needs to keep sensitive data on-premises while leveraging cloud resources for other operations. Which cloud deployment model should be used?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">A Hybrid Cloud combines on-premises infrastructure with cloud services, allowing sensitive data to remain local while using cloud resources for scalability.</div>",
                "options": [
                        "Public Cloud",
                        "Private Cloud",
                        "Hybrid Cloud",
                        "Community Cloud"
                ],
                "answer": 2
        },
        {
                "q": "<b>46.</b> A public-facing API has undergone significant breaking changes, including modifications to endpoints and data structures, making it incompatible with older client applications. The development team wants to deploy these changes without breaking existing integrations. Which API versioning strategy is generally recommended in this scenario?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">URL-based versioning clearly separates breaking changes while allowing older clients to continue using the previous API version.</div>",
                "options": [
                        "Make changes directly to the existing endpoints and update the documentation",
                        "Use query parameters to specify the version (e.g., /api/resource?version=2)",
                        "Include the version number in the URL path (e.g., /api/v2/resource)",
                        "Use custom HTTP headers to specify the API version"
                ],
                "answer": 2
        },
        {
                "q": "<b>47.</b> A network administrator wants to assign IP addresses dynamically to devices in a network. Which protocol is used for this purpose?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">DHCP automatically assigns IP addresses and network configuration details to devices on a network.</div>",
                "options": [
                        "DNS",
                        "DHCP",
                        "ARP",
                        "ICMP"
                ],
                "answer": 1
        },
        {
                "q": "<b>48.</b> A startup is concerned about unpredictable expenses due to variable cloud usage. Which cloud feature should they implement to manage and predict costs more accurately?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Reserved instances provide predictable, discounted pricing by committing to usage over a fixed term, helping control costs.</div>",
                "options": [
                        "Auto-scaling",
                        "Reserved instances",
                        "Load balancing",
                        "Content Delivery Network (CDN)"
                ],
                "answer": 1
        },
        {
                "q": "<b>49.</b> A company needs a security solution where the firewall acts as an intermediary, inspecting all incoming and outgoing traffic between the user’s device and the internet. Which type of firewall is most suitable for this requirement?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">A proxy firewall sits between users and the internet, inspecting and filtering all traffic by acting as an intermediary.</div>",
                "options": [
                        "Packet Filtering Firewall",
                        "Proxy Firewall",
                        "Circuit-Level Gateway",
                        "Application Firewall"
                ],
                "answer": 1
        },
        {
                "q": "<b>50.</b> You are a network administrator for a company with several remote offices. The company wants to implement a VPN to provide secure remote access to its internal network. Which VPN type is the best choice for this scenario?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">SSL VPNs provide secure remote access over the internet using a web browser and are ideal for remote users across multiple locations.</div>",
                "options": [
                        "PPTP",
                        "L2TP",
                        "SSL VPN",
                        "IPSec VPN"
                ],
                "answer": 2
        },
        {
                "q": "<b>51.</b> Question: A team wants to improve deployment speed and reduce downtime when updating their containerized application. Which practice should they adopt?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Rolling updates with health checks update containers gradually, ensuring availability and minimizing downtime during deployments.</div>",
                "options": [
                        "Use rolling updates with health checks",
                        "Increase the number of replicas",
                        "Disable the health checks",
                        "Use a larger base image"
                ],
                "answer": 0
        },
        {
                "q": "<b>52.</b> Which cloud service model provides users with hardware resources such as virtual machines and storage?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Infrastructure as a Service (IaaS) offers virtualized hardware resources like servers, storage, and networking.</div>",
                "options": [
                        "IaaS",
                        "PaaS",
                        "SaaS",
                        "DaaS"
                ],
                "answer": 0
        },
        {
                "q": "<b>53.</b> Your organization has decided to outsource antivirus management to a third party. Which of the following tasks cannot be assigned to the third party?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Defining internal security policies is a strategic responsibility of the organization and should not be outsourced to third parties.</div>",
                "options": [
                        "Monitoring of servers on your organization’s premises",
                        "Preparing the internal antivirus policy for the systems",
                        "Rectification of virus infections on systems",
                        "Updating the antivirus definition files on user systems"
                ],
                "answer": 1
        },
        {
                "q": "<b>54.</b> Google updates its website weekly by adding new features and fixing bugs using an Agile development approach. After each update, the new version is automatically deployed to the live environment. Which DevOps practice is being implemented to ensure rapid and frequent releases?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Continuous Deployment automates frequent and reliable releases to production without manual intervention.</div>",
                "options": [
                        "The practice involves automating the process of releasing software to production frequently and reliably",
                        "Continuous integration focuses on merging code changes regularly to prevent integration issues",
                        "Continuous testing ensures that automated tests are run continuously to validate code quality",
                        "Monitoring involves tracking application performance and user activity after deployment"
                ],
                "answer": 0
        },
        {
                "q": "<b>55.</b> What is the main purpose of network segmentation in security?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Network segmentation isolates network segments to prevent attackers from easily moving across the entire network.</div>",
                "options": [
                        "Increasing bandwidth",
                        "Improving signal strength",
                        "Limiting the spread of attacks",
                        "Reducing latency"
                ],
                "answer": 2
        },
        {
                "q": "<b>56.</b> A development team is designing a new RESTful API to manage a product catalog. They need to create an endpoint that retrieves detailed information about a specific product using its unique product ID. Which HTTP method and URL structure best align with RESTful principles?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">RESTful design uses the GET method to retrieve resources and identifies a specific resource through a clean, resource-based URL.</div>",
                "options": [
                        "POST /products/{id}/details",
                        "GET /product_details?id={id}",
                        "PUT /products/{id}/fetch",
                        "GET /products/{id}"
                ],
                "answer": 3
        },
        {
                "q": "<b>57.</b> Azure is migrating its legacy data sources to new cloud-based platforms while maintaining operations without downtime. During migration, data from both the old and new systems must be accessed simultaneously for real-time reporting and analytics, with logical integration and no physical data movement. Which architectural layer best handles this requirement while ensuring minimal disruption and secure access?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">An abstraction (data virtualization) layer enables unified, real-time access to multiple data sources without physically moving the data.</div>",
                "options": [
                        "Connection layer using direct database access protocols",
                        "Consumption layer utilizing middleware with abstracted APIs",
                        "Abstraction layer that logically unifies disparate data sources",
                        "Data caching layer storing temporary data"
                ],
                "answer": 2
        },
        {
                "q": "<b>58.</b> As part of a data center modernization initiative, the IoT team must address storage challenges by leveraging existing storage devices from multiple vendors and integrating them into a next- generation storage solution. How does resource pooling play a crucial role in achieving elasticity in cloud storage?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Resource pooling aggregates storage resources from different systems, enabling elastic scaling and high availability across the cloud environment.</div>",
                "options": [
                        "By eliminating the need for server virtualization",
                        "By minimizing financial and contractual commitments",
                        "By ensuring a globally scalable and resilient storage solution",
                        "By optimizing capacity for executing code and running instances"
                ],
                "answer": 2
        },
        {
                "q": "<b>59.</b> You are a software developer creating an application for a large corporation. The application is expected to run on various computers with different hardware and operating systems. Which operating system property is most important to ensure compatibility and smooth operation?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Device management ensures the OS can interface with different hardware components, allowing applications to run smoothly across diverse systems.</div>",
                "options": [
                        "User Interface",
                        "Security",
                        "Device Management",
                        "Resource Allocation"
                ],
                "answer": 2
        },
        {
                "q": "<b>60.</b> A company migrates its application to a cloud computing environment. How does the concept of &quot;shared responsibility&quot; impact security management in this scenario?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">In cloud computing, providers secure the infrastructure, while customers are responsible for securing their applications, data, and access.</div>",
                "options": [
                        "The cloud provider handles all security measures",
                        "Security is managed by third-party auditors",
                        "Both the cloud provider and the customer share security responsibilities",
                        "The customer is solely responsible for security"
                ],
                "answer": 2
        },
        {
                "q": "<b>61.</b> An embedded system encrypts data using a substitution cipher. After deployment, some characters in the encrypted text are not correctly decrypted. What is the most likely cause of this issue?<div class=\"quiz-q-text\" style=\"margin-top:6px;color:var(--text-dim);font-size:12.5px\">Using an incorrect key during decryption causes mismatched character mappings, resulting in incorrectly decrypted characters.</div>",
                "options": [
                        "The decryption map incorrectly handles negative indices",
                        "The decryption process incorrectly uses the encryption key, leading to incorrect character mapping",
                        "The encryption map creates duplicate character mappings",
                        "The length of the character string causes an incorrect modulo operation"
                ],
                "answer": 1
        }
],
    },
]
