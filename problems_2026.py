"""
Accenture 2026 expected-question bank (from Accenture_2026_Expected_Questions.xlsx).

- Problems 30-44: coding questions (server-judged Java/C++) — KN Academy mocks,
  PrepInsta and GfG recent-drive sets. (Primes in Range already exists as #4
  Prime Hideouts, Armstrong as #5, Remove Adjacent Duplicates as #7.)
- Problems 45-51: web-based coding tasks (browser-judged JavaScript/DOM) —
  KN Academy web labs + expected 2026-pattern variants.
- Problem 52: Web MCQ quiz (KN Academy web mocks 1-3, deduplicated against
  quizzes 16-18).

Merged into problems.PROBLEMS by problems.py wiring.
"""

CODE_HEADER_JAVA = """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
"""

CODE_HEADER_CPP = """#include <bits/stdc++.h>
using namespace std;

int main() {
"""


def _todo_java(todo):
    return CODE_HEADER_JAVA + f"""
        // TODO: {todo}
    }}
}}"""


def _todo_cpp(todo):
    return CODE_HEADER_CPP + f"""
    // TODO: {todo}
    return 0;
}}"""


CODE_2026_PROBLEMS = [

    # ------------------------------------------------------------------ #
    # 30. Count Vowels (Spell Bee Score) — KN Academy Coding Mock 16
    # ------------------------------------------------------------------ #
    {
        "id": 30,
        "slug": "count-vowels-spell-bee",
        "title": "Count Vowels (Spell Bee Score)",
        "difficulty": "Easy",
        "topics": ["Strings", "Loops"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p class="text-muted">KN Academy — Coding Mock 16</p>
<p>In a spell-bee contest a student's score is the number of <b>vowels</b> in the word they spelled.
Given a word, count how many vowels (<code>a, e, i, o, u</code>) it contains — vowels can be
upper-case or lower-case and both must be counted.</p>
<h3>Sample Test Case:</h3>
<pre>Input:
Accenture

Output:
4</pre>
<p class="text-muted">A, e, u and e are the vowels in "Accenture".</p>
<h3>Constraints:</h3>
<ul><li><code>1 &lt;= length of word &lt;= 1000</code> (letters only)</li></ul>
""",
        "hint": "Loop over every character, lowercase it, and check membership in {a, e, i, o, u}.",
        "boilerplate": {
            "java": _todo_java('read the word and print how many vowels (a e i o u, any case) it contains'),
            "cpp": _todo_cpp('read the word and print how many vowels (a e i o u, any case) it contains'),
        },
        "tests": [
            {"input": "Accenture", "expected": "4", "hidden": False},
            {"input": "Rhythm", "expected": "0", "hidden": False},
            {"input": "Education", "expected": "5", "hidden": True},
            {"input": "AEIOUaeiou", "expected": "10", "hidden": True},
            {"input": "bcdfg", "expected": "0", "hidden": True},
            {"input": "Programming", "expected": "3", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 31. Uniform Rows & Columns in Grid — KN Academy, Accenture 8 Jan actual
    # ------------------------------------------------------------------ #
    {
        "id": 31,
        "slug": "uniform-rows-columns-grid",
        "title": "Uniform Rows & Columns in Grid",
        "difficulty": "Easy",
        "topics": ["Strings", "Matrix"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p class="text-muted">KN Academy — Accenture 8 Jan (actual paper)</p>
<p>You are given a string <code>s</code> whose length is a <b>perfect square</b>. Fill an
<code>n &times; n</code> grid row by row with its characters, where <code>n = &radic;len(s)</code>.</p>
<p>Count how many <b>rows</b> have all identical characters plus how many <b>columns</b> have all
identical characters, and print the total.</p>
<h3>Sample Test Case:</h3>
<pre>Input:
aaaabbbcc

Output:
1</pre>
<p class="text-muted">The grid is <code>aaa / abb / bcc</code> — only the first row "aaa" is uniform,
and no column is, so the answer is 1.</p>
<h3>Constraints:</h3>
<ul><li><code>4 &lt;= len(s) &lt;= 400</code> (length is a perfect square)</li></ul>
""",
        "hint": "Character at row r, column c is s[r*n + c]. Check every row and every column with a "
                "double loop; a line is uniform when all its characters equal the first one.",
        "boilerplate": {
            "java": _todo_java('read the string s, build the n x n grid and print the number of uniform rows plus uniform columns'),
            "cpp": _todo_cpp('read the string s, build the n x n grid and print the number of uniform rows plus uniform columns'),
        },
        "tests": [
            {"input": "aaaabbbcc", "expected": "1", "hidden": False},
            {"input": "aaaa", "expected": "4", "hidden": False},
            {"input": "aabb", "expected": "2", "hidden": True},
            {"input": "bbbbbbbbb", "expected": "6", "hidden": True},
            {"input": "abba", "expected": "0", "hidden": True},
            {"input": "abczdefguh", "expected": "0", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 32. Rat Count House — PrepInsta
    # ------------------------------------------------------------------ #
    {
        "id": 32,
        "slug": "rat-count-house",
        "title": "Rat Count House",
        "difficulty": "Easy",
        "topics": ["Arrays", "Prefix Sum"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p class="text-muted">PrepInsta — recent Accenture drive</p>
<p><code>r</code> rats enter a street of houses. Each rat eats <code>unit</code> units of food, so the
street must provide <code>r &times; unit</code> food in total. House <code>i</code> (1-indexed) stores
<code>arr[i]</code> units of food, and the rats eat house by house from the first one until they have
consumed enough.</p>
<p>Print the <b>number of the house</b> at which the rats finish eating (i.e. how many houses they
consumed), or <code>-1</code> if the street does not have enough food.</p>
<h3>Sample Test Case 1:</h3>
<pre>Input:
7 2
9
2 8 3 5 7 4 1 2 50

Output:
4</pre>
<p class="text-muted">The rats need 7&times;2 = 14 units. The running total is 2, 10, 13, 18 &mdash; it first
reaches 14 at house 4, so the answer is 4.</p>
<h3>Sample Test Case 2:</h3>
<pre>Input:
2 4
2
2 2

Output:
-1</pre>
<p class="text-muted">The rats need 2&times;4 = 8 units but the two houses hold only 4.</p>
<h3>Constraints:</h3>
<ul><li><code>1 &lt;= r, unit, arr[i] &lt;= 1000</code></li></ul>
""",
        "hint": "Accumulate arr[i] into a running sum; the answer is i+1 the first time the sum reaches "
                "r*unit. If the loop ends first, print -1.",
        "boilerplate": {
            "java": _todo_java('read r unit, n and the array; print the 1-indexed house where the rats finish or -1'),
            "cpp": _todo_cpp('read r unit, n and the array; print the 1-indexed house where the rats finish or -1'),
        },
        "tests": [
            {"input": "7 2\n9\n2 8 3 5 7 4 1 2 50", "expected": "4", "hidden": False},
            {"input": "7 2\n8\n2 8 3 5 7 4 1 2", "expected": "4", "hidden": False},
            {"input": "3 2\n4\n1 2 3 4", "expected": "3", "hidden": True},
            {"input": "2 5\n3\n3 3 3", "expected": "-1", "hidden": True},
            {"input": "5 1\n5\n1 1 1 1 1", "expected": "5", "hidden": True},
            {"input": "1 1\n1\n5", "expected": "1", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 33. Operations on Binary String — PrepInsta
    # ------------------------------------------------------------------ #
    {
        "id": 33,
        "slug": "operations-binary-string",
        "title": "Operations on Binary String",
        "difficulty": "Easy",
        "topics": ["Strings", "Bit Manipulation"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p class="text-muted">PrepInsta — recent Accenture drive</p>
<p>You get a string like <code>1C0A1</code>: it starts with a binary digit, then alternates an
<b>operator letter</b> and a binary digit. The letters mean:</p>
<ul>
  <li><code>A</code> — AND</li>
  <li><code>B</code> — OR</li>
  <li><code>C</code> — XOR</li>
</ul>
<p>Start with the first digit as the answer, then apply every operator to it with the digit that
follows. Print the final result (0 or 1).</p>
<h3>Sample Test Case:</h3>
<pre>Input:
1C0A1

Output:
1</pre>
<p class="text-muted">1 XOR 0 = 1, then 1 AND 1 = 1.</p>
""",
        "hint": "Walk the string from index 1 in steps of two: op = s[i], bit = s[i+1]. Keep the running "
                "answer as an int and apply AND/OR/XOR with the digit value.",
        "boilerplate": {
            "java": _todo_java('read the expression string and print the computed 0/1 result (A=AND, B=OR, C=XOR)'),
            "cpp": _todo_cpp('read the expression string and print the computed 0/1 result (A=AND, B=OR, C=XOR)'),
        },
        "tests": [
            {"input": "1C0A1", "expected": "1", "hidden": False},
            {"input": "0C1A1B1", "expected": "1", "hidden": False},
            {"input": "1A0B1", "expected": "1", "hidden": True},
            {"input": "1A1", "expected": "1", "hidden": True},
            {"input": "0B0", "expected": "0", "hidden": True},
            {"input": "1C1C1C0", "expected": "1", "hidden": True},
            {"input": "0C1C1A0", "expected": "0", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 34. Password Checker — PrepInsta
    # ------------------------------------------------------------------ #
    {
        "id": 34,
        "slug": "password-checker",
        "title": "Password Checker",
        "difficulty": "Easy",
        "topics": ["Strings", "Validation"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p class="text-muted">PrepInsta — recent Accenture drive</p>
<p>A password is <b>valid</b> when all four rules hold:</p>
<ul>
  <li>it has at least <b>4</b> characters,</li>
  <li>it contains <b>no spaces</b>,</li>
  <li>it contains at least <b>one digit</b>,</li>
  <li>it contains at least <b>one capital letter</b>.</li>
</ul>
<p>Print <code>Valid</code> if the given password passes, otherwise <code>Invalid</code>.</p>
<h3>Sample Test Case 1:</h3>
<pre>Input:
1aA99

Output:
Valid</pre>
<h3>Sample Test Case 2:</h3>
<pre>Input:
aA1_9 b

Output:
Invalid</pre>
<p class="text-muted">It contains a space.</p>
""",
        "hint": "One pass over the characters: track length, a space flag, a digit flag and an "
                "uppercase flag, then combine them into the final verdict.",
        "boilerplate": {
            "java": _todo_java('read the password line and print Valid or Invalid per the four rules'),
            "cpp": _todo_cpp('read the password line and print Valid or Invalid per the four rules'),
        },
        "tests": [
            {"input": "1aA99", "expected": "Valid", "hidden": False},
            {"input": "aA1_9 b", "expected": "Invalid", "hidden": False},
            {"input": "abcd", "expected": "Invalid", "hidden": True},
            {"input": "A1b", "expected": "Invalid", "hidden": True},
            {"input": "aaaa5", "expected": "Invalid", "hidden": True},
            {"input": "AAAA1", "expected": "Valid", "hidden": True},
            {"input": "Qw3rt", "expected": "Valid", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 35. Product Smallest Pair — PrepInsta
    # ------------------------------------------------------------------ #
    {
        "id": 35,
        "slug": "product-smallest-pair",
        "title": "Product Smallest Pair",
        "difficulty": "Easy",
        "topics": ["Arrays", "Sorting"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p class="text-muted">PrepInsta — recent Accenture drive</p>
<p>Given an array of <code>n</code> integers and an integer <code>sum</code>: take the <b>two smallest</b>
values of the array. If their sum is <code>&le; sum</code>, print their product; otherwise print
<code>-1</code>.</p>
<h3>Sample Test Case:</h3>
<pre>Input:
7 9
5 2 4 3 9 7 1

Output:
2</pre>
<p class="text-muted">The two smallest values are 1 and 2; 1+2 = 3 &le; 9, so print 1&times;2 = 2.</p>
<h3>Constraints:</h3>
<ul><li><code>2 &lt;= n &lt;= 100</code>, <code>0 &lt;= arr[i], sum &lt;= 1000</code></li></ul>
""",
        "hint": "Sort the array and look at the first two elements only — no other pair can have a "
                "smaller sum.",
        "boilerplate": {
            "java": _todo_java('read n sum, the array; print the product of the two smallest values if their sum <= sum, else -1'),
            "cpp": _todo_cpp('read n sum, the array; print the product of the two smallest values if their sum <= sum, else -1'),
        },
        "tests": [
            {"input": "7 9\n5 2 4 3 9 7 1", "expected": "2", "hidden": False},
            {"input": "3 2\n5 5 5", "expected": "-1", "hidden": False},
            {"input": "4 10\n1 2 3 4", "expected": "2", "hidden": True},
            {"input": "2 5\n3 4", "expected": "-1", "hidden": True},
            {"input": "5 7\n9 2 1 5 6", "expected": "2", "hidden": True},
            {"input": "2 100\n0 0", "expected": "0", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 36. Decimal to N-Base — PrepInsta
    # ------------------------------------------------------------------ #
    {
        "id": 36,
        "slug": "decimal-to-n-base",
        "title": "Decimal to N-Base",
        "difficulty": "Easy",
        "topics": ["Math", "Number Bases"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p class="text-muted">PrepInsta — recent Accenture drive</p>
<p>Convert a decimal number to base <code>n</code> (2 &le; n &le; 36). Digits above 9 use the capital
letters <code>A-Z</code> (10 &rarr; A, 11 &rarr; B, &hellip;, 35 &rarr; Z).</p>
<h3>Sample Test Case:</h3>
<pre>Input:
718
12

Output:
4BA</pre>
<p class="text-muted">4&times;144 + 11&times;12 + 10 = 718, and 11 = B, 10 = A.</p>
<h3>Input format:</h3>
<p>First line: the decimal number. Second line: the base <code>n</code>.</p>
""",
        "hint": "Repeatedly divide by n; the remainders (converted 10→A … 35→Z) read in reverse order "
                "are the answer. Don't forget 0 converts to \"0\".",
        "boilerplate": {
            "java": _todo_java('read the decimal number and the base, print the n-base representation with A-Z digits'),
            "cpp": _todo_cpp('read the decimal number and the base, print the n-base representation with A-Z digits'),
        },
        "tests": [
            {"input": "718\n12", "expected": "4BA", "hidden": False},
            {"input": "718\n2", "expected": "1011001110", "hidden": False},
            {"input": "100\n16", "expected": "64", "hidden": True},
            {"input": "35\n36", "expected": "Z", "hidden": True},
            {"input": "718\n36", "expected": "JY", "hidden": True},
            {"input": "0\n8", "expected": "0", "hidden": True},
            {"input": "1000\n20", "expected": "2A0", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 37. Number of Carries — PrepInsta
    # ------------------------------------------------------------------ #
    {
        "id": 37,
        "slug": "number-of-carries",
        "title": "Number of Carries",
        "difficulty": "Easy",
        "topics": ["Math", "Digit Manipulation"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p class="text-muted">PrepInsta — recent Accenture drive</p>
<p>Add two numbers the way you do on paper and count how many <b>carries</b> happen in total.</p>
<h3>Sample Test Case:</h3>
<pre>Input:
451 349

Output:
2</pre>
<p class="text-muted">1+9 = 10 (carry), 5+4+1 = 10 (carry), 4+3+1 = 8 — two carries.</p>
<h3>Input format:</h3>
<p>One line with <code>num1</code> and <code>num2</code>.</p>
<h3>Constraints:</h3>
<ul><li><code>0 &lt;= num1, num2 &lt;= 10^9</code></li></ul>
""",
        "hint": "Peel digits with % 10 and / 10 in a loop; carry = (d1 + d2 + carry) >= 10 ? 1 : 0, "
                "counting every time it fires.",
        "boilerplate": {
            "java": _todo_java('read two integers and print how many carries their addition produces'),
            "cpp": _todo_cpp('read two integers and print how many carries their addition produces'),
        },
        "tests": [
            {"input": "451 349", "expected": "2", "hidden": False},
            {"input": "999 1", "expected": "3", "hidden": False},
            {"input": "123 321", "expected": "0", "hidden": True},
            {"input": "89 89", "expected": "2", "hidden": True},
            {"input": "5 5", "expected": "1", "hidden": True},
            {"input": "0 0", "expected": "0", "hidden": True},
            {"input": "1 999999999", "expected": "9", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 38. Difference of Sum — PrepInsta
    # ------------------------------------------------------------------ #
    {
        "id": 38,
        "slug": "difference-of-sum",
        "title": "Difference of Sum (Divisible by m)",
        "difficulty": "Easy",
        "topics": ["Math", "Loops"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p class="text-muted">PrepInsta — recent Accenture drive</p>
<p>Given <code>n</code> and <code>m</code>, compute the absolute difference between the sum of the
numbers 1..n that are <b>not divisible</b> by <code>m</code> and the sum of those that <b>are</b>
divisible by <code>m</code>.</p>
<h3>Sample Test Case:</h3>
<pre>Input:
10 3

Output:
19</pre>
<p class="text-muted">Divisible: 3+6+9 = 18. Not divisible: 1+2+4+5+7+8+10 = 37. |37 &minus; 18| = 19.</p>
<h3>Input format:</h3>
<p>One line with <code>n</code> and <code>m</code>.</p>
<h3>Constraints:</h3>
<ul><li><code>1 &lt;= m &lt;= n &lt;= 10^6</code></li></ul>
""",
        "hint": "One loop from 1 to n with two accumulators, or use closed formulas: total = n(n+1)/2 "
                "and divisible sum = m*k(k+1)/2 with k = n/m.",
        "boilerplate": {
            "java": _todo_java('read n and m, print |sum of 1..n not divisible by m - sum of those divisible by m|'),
            "cpp": _todo_cpp('read n and m, print |sum of 1..n not divisible by m - sum of those divisible by m|'),
        },
        "tests": [
            {"input": "10 3", "expected": "19", "hidden": False},
            {"input": "5 5", "expected": "5", "hidden": False},
            {"input": "20 4", "expected": "90", "hidden": True},
            {"input": "1 1", "expected": "1", "hidden": True},
            {"input": "1000000 7", "expected": "357142642858", "hidden": True},
            {"input": "100 7", "expected": "3580", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 39. Move Hyphen — PrepInsta
    # ------------------------------------------------------------------ #
    {
        "id": 39,
        "slug": "move-hyphen",
        "title": "Move Hyphen",
        "difficulty": "Easy",
        "topics": ["Strings"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p class="text-muted">PrepInsta — recent Accenture drive</p>
<p>Given a string containing letters and hyphens, move <b>every hyphen to the front</b> and keep the
letters in their original order. Print the result.</p>
<h3>Sample Test Case:</h3>
<pre>Input:
String-Compare-Move-Hyphen

Output:
---StringCompareMoveHyphen</pre>
""",
        "hint": "Count the hyphens, then output that many '-' followed by the string without hyphens.",
        "boilerplate": {
            "java": _todo_java('read the string and print it with all hyphens moved to the front'),
            "cpp": _todo_cpp('read the string and print it with all hyphens moved to the front'),
        },
        "tests": [
            {"input": "String-Compare-Move-Hyphen", "expected": "---StringCompareMoveHyphen", "hidden": False},
            {"input": "abc", "expected": "abc", "hidden": False},
            {"input": "a-b-c", "expected": "--abc", "hidden": True},
            {"input": "---", "expected": "---", "hidden": True},
            {"input": "Java-Is-Fun", "expected": "--JavaIsFun", "hidden": True},
            {"input": "-", "expected": "-", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 40. Max Exponents — PrepInsta
    # ------------------------------------------------------------------ #
    {
        "id": 40,
        "slug": "max-exponents-power-of-2",
        "title": "Max Exponents (Power of 2)",
        "difficulty": "Easy",
        "topics": ["Math", "Loops"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p class="text-muted">PrepInsta — recent Accenture drive</p>
<p>Given <code>a</code> and <code>b</code>, find the number <code>x</code> in <code>[a, b]</code> whose
factorization contains the <b>highest power of 2</b> (i.e. the largest count of times 2 divides x).
If several numbers tie, print the <b>smallest</b> of them.</p>
<h3>Sample Test Case:</h3>
<pre>Input:
7 12

Output:
8</pre>
<p class="text-muted">8 = 2&sup3; has exponent 3, the largest in the range.</p>
<h3>Input format:</h3>
<p>One line with <code>a</code> and <code>b</code>.</p>
<h3>Constraints:</h3>
<ul><li><code>1 &lt;= a &lt;= b &lt;= 10^6</code></li></ul>
""",
        "hint": "For each x, count how many times 2 divides it with a while loop. Track the best exponent "
                "and update the answer only on strictly greater counts so ties keep the smaller x.",
        "boilerplate": {
            "java": _todo_java('read a and b, print the smallest x in [a,b] with the maximum power of 2 dividing it'),
            "cpp": _todo_cpp('read a and b, print the smallest x in [a,b] with the maximum power of 2 dividing it'),
        },
        "tests": [
            {"input": "7 12", "expected": "8", "hidden": False},
            {"input": "1 10", "expected": "8", "hidden": False},
            {"input": "5 6", "expected": "6", "hidden": True},
            {"input": "15 16", "expected": "16", "hidden": True},
            {"input": "9 14", "expected": "12", "hidden": True},
            {"input": "17 31", "expected": "24", "hidden": True},
            {"input": "1 1", "expected": "1", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 41. Second Smallest Element — GfG, Accenture On-Campus 2024
    # ------------------------------------------------------------------ #
    {
        "id": 41,
        "slug": "second-smallest-element",
        "title": "Second Smallest Element",
        "difficulty": "Easy",
        "topics": ["Arrays", "Sorting"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p class="text-muted">GeeksforGeeks — Accenture On-Campus 2024</p>
<p>Given an array, print its <b>second smallest distinct</b> element. Duplicates count once — for
<code>[4, 4, 2]</code> the second smallest is 4, and for <code>[1, 1, 2]</code> it is 2.</p>
<h3>Sample Test Case:</h3>
<pre>Input:
6
5 6 1 2 6 1

Output:
2</pre>
<p class="text-muted">Distinct values sorted: 1, 2, 5, 6 — the second smallest is 2.</p>
<h3>Input format:</h3>
<p>First line: <code>n</code>. Second line: the array.</p>
<h3>Constraints:</h3>
<ul><li><code>2 &lt;= n &lt;= 10^5</code>; the array always has at least two distinct values</li></ul>
""",
        "hint": "Either sort a de-duplicated copy of the array, or do one pass tracking the smallest and "
                "second-smallest distinct values.",
        "boilerplate": {
            "java": _todo_java('read n and the array, print the second smallest distinct element'),
            "cpp": _todo_cpp('read n and the array, print the second smallest distinct element'),
        },
        "tests": [
            {"input": "6\n5 6 1 2 6 1", "expected": "2", "hidden": False},
            {"input": "3\n1 1 2", "expected": "2", "hidden": False},
            {"input": "3\n4 4 2", "expected": "4", "hidden": True},
            {"input": "4\n10 3 3 1", "expected": "3", "hidden": True},
            {"input": "4\n-5 -1 -5 0", "expected": "-1", "hidden": True},
            {"input": "5\n7 7 7 7 1", "expected": "7", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 42. Team with Maximum Wins — GfG, Accenture On-Campus 2024
    # ------------------------------------------------------------------ #
    {
        "id": 42,
        "slug": "team-with-maximum-wins",
        "title": "Team with Maximum Wins",
        "difficulty": "Easy",
        "topics": ["Strings", "Hash Table"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p class="text-muted">GeeksforGeeks — Accenture On-Campus 2024</p>
<p>You are given the name of the winning team for each of <code>n</code> matches. Print the team that
won the <b>most</b> matches. (The test data always has a single team with a strictly largest count.)</p>
<h3>Sample Test Case:</h3>
<pre>Input:
4
TeamA TeamB TeamA TeamA

Output:
TeamA</pre>
<h3>Input format:</h3>
<p>First line: <code>n</code>. Second line: <code>n</code> team names separated by spaces
(names contain no spaces).</p>
""",
        "hint": "Count wins per team in a hash map, then scan for the key with the maximum count.",
        "boilerplate": {
            "java": _todo_java('read n and n team names, print the team with the most wins'),
            "cpp": _todo_cpp('read n and n team names, print the team with the most wins'),
        },
        "tests": [
            {"input": "4\nTeamA TeamB TeamA TeamA", "expected": "TeamA", "hidden": False},
            {"input": "3\nIndia Pakistan India", "expected": "India", "hidden": False},
            {"input": "1\nLions", "expected": "Lions", "hidden": True},
            {"input": "5\nwin lose win lose win", "expected": "win", "hidden": True},
            {"input": "6\na b b c c c", "expected": "c", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 43. Count Odd Index + Odd Value — GfG, AAEA Campus Visit 2024
    # ------------------------------------------------------------------ #
    {
        "id": 43,
        "slug": "count-odd-index-odd-value",
        "title": "Count Odd Index + Odd Value",
        "difficulty": "Easy",
        "topics": ["Arrays", "Loops"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p class="text-muted">GeeksforGeeks — Accenture AAEA Campus Visit 2024</p>
<p>Given an array, count how many elements sit at an <b>odd index</b> <i>and</i> hold an
<b>odd value</b>.</p>
<h3>Sample Test Case:</h3>
<pre>Input:
6
1 2 3 3 5 7

Output:
2</pre>
<p class="text-muted">Index 3 holds 3 and index 5 holds 7 — both odd index, odd value. (Index 1 holds
2, which is even.)</p>
<h3>Input format:</h3>
<p>First line: <code>n</code>. Second line: the array.</p>
""",
        "hint": "Loop i = 1, 3, 5, … and count whenever a[i] % 2 == 1.",
        "boilerplate": {
            "java": _todo_java('read n and the array, print how many elements at odd indexes have odd values'),
            "cpp": _todo_cpp('read n and the array, print how many elements at odd indexes have odd values'),
        },
        "tests": [
            {"input": "6\n1 2 3 3 5 7", "expected": "2", "hidden": False},
            {"input": "3\n1 1 1", "expected": "1", "hidden": False},
            {"input": "3\n2 4 6", "expected": "0", "hidden": True},
            {"input": "4\n0 1 0 3", "expected": "2", "hidden": True},
            {"input": "5\n9 9 9 9 9", "expected": "2", "hidden": True},
        ],
        "samples": [0, 1],
    },

    # ------------------------------------------------------------------ #
    # 44. Count Even Index + Even Value — GfG, AAEA Campus Visit 2024
    # ------------------------------------------------------------------ #
    {
        "id": 44,
        "slug": "count-even-index-even-value",
        "title": "Count Even Index + Even Value",
        "difficulty": "Easy",
        "topics": ["Arrays", "Loops"],
        "judge": "server",
        "languages": ["java", "cpp"],
        "description": """
<p class="text-muted">GeeksforGeeks — Accenture AAEA Campus Visit 2024</p>
<p>Given an array, count how many elements sit at an <b>even index</b> (0, 2, 4, &hellip;) <i>and</i>
hold an <b>even value</b> (0 counts as even).</p>
<h3>Sample Test Case:</h3>
<pre>Input:
6
2 1 4 3 6 5

Output:
3</pre>
<p class="text-muted">Indexes 0, 2 and 4 hold 2, 4 and 6 — all even at even indexes.</p>
<h3>Input format:</h3>
<p>First line: <code>n</code>. Second line: the array.</p>
""",
        "hint": "Loop i = 0, 2, 4, … and count whenever a[i] % 2 == 0.",
        "boilerplate": {
            "java": _todo_java('read n and the array, print how many elements at even indexes have even values'),
            "cpp": _todo_cpp('read n and the array, print how many elements at even indexes have even values'),
        },
        "tests": [
            {"input": "6\n2 1 4 3 6 5", "expected": "3", "hidden": False},
            {"input": "3\n1 2 3", "expected": "0", "hidden": False},
            {"input": "3\n2 2 2", "expected": "2", "hidden": True},
            {"input": "2\n0 0", "expected": "1", "hidden": True},
            {"input": "4\n8 8 8 8", "expected": "2", "hidden": True},
        ],
        "samples": [0, 1],
    },
]

# ---------------------------------------------------------------------- #
# Web-based coding tasks (browser-judged JavaScript/DOM) — ids 45-51.
# The frontend runner supports steps: {"click": id}, {"type": id, "value": v}
# and expects: msg/color/count/text/style/visible (see static/app.js).
# ---------------------------------------------------------------------- #

WEB_2026_PROBLEMS = [

    # ------------------------------------------------------------------ #
    # 45. Dynamic Shopping Cart Total & Discount — KN Academy Web Lab 1
    # ------------------------------------------------------------------ #
    {
        "id": 45,
        "slug": "shopping-cart-discount",
        "title": "Dynamic Shopping Cart Total & Discount",
        "difficulty": "Medium",
        "topics": ["JavaScript", "DOM Manipulation", "Events"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p class="text-muted">KN Academy — Web Lab 1 (Cognizant/Accenture style)</p>
<p>Build the behavior for a shopping cart with the following HTML:</p>
<pre>&lt;table&gt;
  &lt;tbody id="cartBody"&gt;
    &lt;tr data-price="40"&gt;
      &lt;td&gt;Widget&lt;/td&gt;
      &lt;td&gt;&lt;button class="btn"&gt;-&lt;/button&gt;&lt;/td&gt;
      &lt;td class="qty"&gt;1&lt;/td&gt;
      &lt;td&gt;&lt;button class="btn"&gt;+&lt;/button&gt;&lt;/td&gt;
      &lt;td class="subtotal"&gt;40.00&lt;/td&gt;
    &lt;/tr&gt;
    &lt;!-- one more row with data-price="75", qty 1 --&gt;
  &lt;/tbody&gt;
&lt;/table&gt;
&lt;p&gt;Total: $&lt;span id="cartTotal"&gt;0.00&lt;/span&gt;
   Discount applied: &lt;span id="discountNote"&gt;&lt;/span&gt;&lt;/p&gt;</pre>
<p>Write JavaScript to fulfill the following specifications:</p>
<ul>
  <li><b>Row subtotals:</b> each row's <code>.subtotal</code> must equal
      <code>data-price &times; .qty</code>, formatted with two decimals
      (<code>v.toFixed(2)</code>). Recalculate whenever a +/− button is clicked.</li>
  <li><b>Bounds:</b> quantities must never drop below <code>0</code> — clicking − at 0 keeps it 0.</li>
  <li><b>Total:</b> <code>#cartTotal</code> shows the sum of all row subtotals, two decimals.</li>
  <li><b>Discount:</b> when the pre-discount total exceeds <code>$100</code>, a 10% discount is
      applied: the shown total becomes <code>total &times; 0.9</code> and
      <code>#discountNote</code> reads <code>10% discount applied</code>. Otherwise the note is
      empty and the total is undiscounted.</li>
  <li><b>Initial state:</b> on load the totals must be calculated once from the starting quantities
      (row 1: 40.00, row 2: 75.00 → total 115.00 &rarr; 10% off → <code>103.50</code> with the note).</li>
</ul>
<p>Use the <b>Preview</b> tab to try the cart live. Submitting runs automated tests that click the
buttons in a fresh page.</p>
""",
        "hint": "Attach one handler per button (query all '.btn' in each row: index 0 is minus, 1 is "
                "plus). Keep a recalc() that loops rows, writes .qty clamped to 0, writes each "
                ".subtotal, sums data-price*qty, applies the >100 discount, and writes #cartTotal and "
                "#discountNote. Call recalc() once on load.",
        "boilerplate": {
            "javascript": """function initializeCart() {
  // TODO: wire the +/- buttons and recalculate subtotals, total and discount
}

initializeCart();
""",
        },
        "tests": [],
        "samples": [],
        "browser_html": """<table>
  <tbody id="cartBody">
    <tr data-price="40">
      <td>Widget</td>
      <td><button class="btn">-</button></td>
      <td class="qty">1</td>
      <td><button class="btn">+</button></td>
      <td class="subtotal">40.00</td>
    </tr>
    <tr data-price="75">
      <td>Gadget</td>
      <td><button class="btn">-</button></td>
      <td class="qty">1</td>
      <td><button class="btn">+</button></td>
      <td class="subtotal">75.00</td>
    </tr>
  </tbody>
</table>
<p>Total: $<span id="cartTotal">0.00</span>
   <span id="discountNote"></span></p>""",
        "browser_tests": [
            {
                "name": "Initial load: totals computed with 10% discount over $100",
                "hidden": False,
                "steps": [],
                "expect": {
                    "subtotal": {"row": 0, "value": "40.00"},
                    "text": {"id": "cartTotal", "value": "103.50"},
                },
            },
            {
                "name": "Discount note is shown",
                "hidden": False,
                "steps": [],
                "expect": {"text": {"id": "discountNote", "value": "10% discount applied"}},
            },
            {
                "name": "Plus on row 1 raises its subtotal",
                "hidden": False,
                "steps": [{"rowBtn": {"row": 0, "which": 1}}],
                "expect": {"subtotal": {"row": 0, "value": "80.00"}},
            },
            {
                "name": "Minus at qty 0 never goes negative",
                "hidden": True,
                "steps": [
                    {"rowBtn": {"row": 0, "which": 0}},
                    {"rowBtn": {"row": 0, "which": 0}},
                ],
                "expect": {
                    "qty": {"row": 0, "value": "0"},
                    "subtotal": {"row": 0, "value": "0.00"},
                },
            },
            {
                "name": "Total with row1=2, row2=1 stays discounted (155 -> 139.50)",
                "hidden": True,
                "steps": [{"rowBtn": {"row": 0, "which": 1}}],
                "expect": {"text": {"id": "cartTotal", "value": "139.50"}},
            },
            {
                "name": "Total at or below $100 drops the discount (row2=0: 80.00)",
                "hidden": True,
                "steps": [
                    {"rowBtn": {"row": 1, "which": 0}},
                ],
                "expect": {
                    "text": {"id": "cartTotal", "value": "80.00"},
                    "text2": {"id": "discountNote", "value": ""},
                },
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # 46. Live Character Counter with Post Disable — 2026 pattern
    # ------------------------------------------------------------------ #
    {
        "id": 46,
        "slug": "char-counter-post-disable",
        "title": "Live Character Counter with Post Disable",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "Events"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Expected 2026-pattern task. The page contains:</p>
<pre>&lt;textarea id="post-text" placeholder="What's happening?"&gt;&lt;/textarea&gt;
&lt;p&gt;&lt;span id="char-count"&gt;&lt;/span&gt;&lt;/p&gt;
&lt;button id="post-btn"&gt;Post&lt;/button&gt;</pre>
<p>Write JavaScript to fulfill the following specifications:</p>
<ul>
  <li><b>Limit:</b> the post may be at most <code>50</code> characters.</li>
  <li><b>Counter:</b> <code>#char-count</code> always shows
      <code>&lt;used&gt;/50 characters</code> (e.g. <code>0/50 characters</code>,
      <code>12/50 characters</code>). It must be set on load and update on every
      <code>input</code> event.</li>
  <li><b>Disable rule:</b> <code>#post-btn</code> must be <code>disabled</code> whenever the text
      is empty <i>or</i> longer than 50 characters; otherwise it is enabled.</li>
  <li><b>Initial state:</b> on load the counter reads <code>0/50 characters</code> and the button is
      disabled (the textarea starts empty).</li>
</ul>
<p>Use the <b>Preview</b> tab to try it live. Submitting runs automated tests that type into the
textarea in a fresh page.</p>
""",
        "hint": "Write one update() that reads textarea.value.length, writes `${len}/50 characters` "
                "into #char-count and sets postBtn.disabled = len === 0 || len > 50. Wire it to the "
                "input event and call it once.",
        "boilerplate": {
            "javascript": """function initializePostBox() {
  const textarea = document.getElementById('post-text');
  const counter = document.getElementById('char-count');
  const postBtn = document.getElementById('post-btn');

  // TODO: update the counter and button state on input and on load
}

initializePostBox();
""",
        },
        "tests": [],
        "samples": [],
        "browser_html": """<textarea id="post-text" placeholder="What's happening?"></textarea>
<p><span id="char-count"></span></p>
<button id="post-btn">Post</button>""",
        "browser_tests": [
            {
                "name": "Initial state: 0/50 and Post disabled",
                "hidden": False,
                "steps": [],
                "expect": {"text": {"id": "char-count", "value": "0/50 characters"}},
            },
            {
                "name": "Button starts disabled",
                "hidden": False,
                "steps": [],
                "expect": {"style": {"selector": "#post-btn", "property": "disabled", "value": "true"}},
            },
            {
                "name": "Typing 5 chars shows 5/50 and enables Post",
                "hidden": False,
                "steps": [{"type": "post-text", "value": "hello"}],
                "expect": {
                    "text": {"id": "char-count", "value": "5/50 characters"},
                    "style": {"selector": "#post-btn", "property": "disabled", "value": "false"},
                },
            },
            {
                "name": "Exactly 50 chars stays enabled",
                "hidden": True,
                "steps": [{"type": "post-text", "value": "x" * 50}],
                "expect": {
                    "text": {"id": "char-count", "value": "50/50 characters"},
                    "style": {"selector": "#post-btn", "property": "disabled", "value": "false"},
                },
            },
            {
                "name": "51 chars disables Post again",
                "hidden": True,
                "steps": [{"type": "post-text", "value": "x" * 51}],
                "expect": {"style": {"selector": "#post-btn", "property": "disabled", "value": "true"}},
            },
            {
                "name": "Clearing back to empty disables Post and resets the counter",
                "hidden": True,
                "steps": [{"type": "post-text", "value": ""}],
                "expect": {
                    "text": {"id": "char-count", "value": "0/50 characters"},
                    "style": {"selector": "#post-btn", "property": "disabled", "value": "true"},
                },
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # 47. Form Validation with Inline Error Messages — 2026 pattern
    # ------------------------------------------------------------------ #
    {
        "id": 47,
        "slug": "form-validation-errors",
        "title": "Form Validation with Inline Error Messages",
        "difficulty": "Medium",
        "topics": ["JavaScript", "Forms", "Regular Expressions"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Expected 2026-pattern task. The page contains a sign-up form:</p>
<pre>&lt;form id="signup-form" novalidate&gt;
  &lt;input type="text" id="name"&gt;
  &lt;span class="err" id="name-err"&gt;&lt;/span&gt;
  &lt;input type="text" id="email"&gt;
  &lt;span class="err" id="email-err"&gt;&lt;/span&gt;
  &lt;input type="text" id="phone"&gt;
  &lt;span class="err" id="phone-err"&gt;&lt;/span&gt;
  &lt;button type="submit" id="submit-btn"&gt;Sign Up&lt;/button&gt;
&lt;/form&gt;
&lt;p id="form-result"&gt;&lt;/p&gt;</pre>
<p>Write JavaScript to validate the form when it is <b>submitted</b> (listen for the
<code>submit</code> event and call <code>preventDefault()</code> so the page never reloads):</p>
<ul>
  <li><b>Name:</b> must be non-empty, else <code>#name-err</code> shows
      <code>Name is required</code>.</li>
  <li><b>Email:</b> must match a standard pattern (something<code>@</code>something
      <code>.</code>something, e.g. <code>/^\\S+@\\S+\\.\\S+$/</code>), else
      <code>#email-err</code> shows <code>Invalid email</code>.</li>
  <li><b>Phone:</b> must be exactly <b>10 digits</b>, else <code>#phone-err</code> shows
      <code>Invalid phone</code>.</li>
  <li><b>Clearing:</b> every error span must be reset to <code>""</code> at the start of each
      submit — only the currently invalid fields keep a message.</li>
  <li><b>Success:</b> when all three are valid, no error span has text and
      <code>#form-result</code> shows <code>Form submitted</code>.</li>
</ul>
<p>Submitting on the platform runs automated tests that fill the fields, click
<code>#submit-btn</code> and check the error spans.</p>
""",
        "hint": "Add a submit listener on the form, call e.preventDefault() first, clear all three "
                "error spans, then validate each field and write its message. Only when nothing "
                "failed set #form-result.textContent = 'Form submitted'.",
        "boilerplate": {
            "javascript": """function initializeForm() {
  const form = document.getElementById('signup-form');

  // TODO: validate name/email/phone on submit and show inline errors
}

initializeForm();
""",
        },
        "tests": [],
        "samples": [],
        "browser_html": """<form id="signup-form" novalidate>
  <input type="text" id="name">
  <span class="err" id="name-err"></span>
  <input type="text" id="email">
  <span class="err" id="email-err"></span>
  <input type="text" id="phone">
  <span class="err" id="phone-err"></span>
  <button type="submit" id="submit-btn">Sign Up</button>
</form>
<p id="form-result"></p>""",
        "browser_tests": [
            {
                "name": "Empty form: name error shown",
                "hidden": False,
                "steps": [{"click": "submit-btn"}],
                "expect": {"text": {"id": "name-err", "value": "Name is required"}},
            },
            {
                "name": "Bad email and phone flagged",
                "hidden": False,
                "steps": [
                    {"type": "name", "value": "Tanisk"},
                    {"type": "email", "value": "not-an-email"},
                    {"type": "phone", "value": "12345"},
                    {"click": "submit-btn"},
                ],
                "expect": {
                    "text": {"id": "email-err", "value": "Invalid email"},
                    "text2": {"id": "phone-err", "value": "Invalid phone"},
                },
            },
            {
                "name": "Valid input submits",
                "hidden": False,
                "steps": [
                    {"type": "name", "value": "Tanisk"},
                    {"type": "email", "value": "tanisk@example.com"},
                    {"type": "phone", "value": "9876543210"},
                    {"click": "submit-btn"},
                ],
                "expect": {"text": {"id": "form-result", "value": "Form submitted"}},
            },
            {
                "name": "Valid email but 9-digit phone fails",
                "hidden": True,
                "steps": [
                    {"type": "name", "value": "A"},
                    {"type": "email", "value": "a@b.co"},
                    {"type": "phone", "value": "123456789"},
                    {"click": "submit-btn"},
                ],
                "expect": {"text": {"id": "phone-err", "value": "Invalid phone"}},
            },
            {
                "name": "Phone with letters fails",
                "hidden": True,
                "steps": [
                    {"type": "name", "value": "A"},
                    {"type": "email", "value": "a@b.co"},
                    {"type": "phone", "value": "12345abcde"},
                    {"click": "submit-btn"},
                ],
                "expect": {"text": {"id": "phone-err", "value": "Invalid phone"}},
            },
            {
                "name": "Fixing fields clears earlier errors",
                "hidden": True,
                "steps": [
                    {"type": "name", "value": "Tanisk"},
                    {"type": "email", "value": "bad"},
                    {"type": "phone", "value": "9876543210"},
                    {"click": "submit-btn"},
                    {"type": "email", "value": "tanisk@example.com"},
                    {"click": "submit-btn"},
                ],
                "expect": {
                    "text": {"id": "email-err", "value": ""},
                    "text2": {"id": "form-result", "value": "Form submitted"},
                },
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # 48. FAQ Accordion — 2026 pattern
    # ------------------------------------------------------------------ #
    {
        "id": 48,
        "slug": "faq-accordion",
        "title": "FAQ Accordion (Show/Hide Sections)",
        "difficulty": "Medium",
        "topics": ["JavaScript", "DOM Manipulation", "CSS"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Expected 2026-pattern task. The page contains:</p>
<pre>&lt;div class="faq-item"&gt;
  &lt;button class="faq-q" id="q1"&gt;What is Accenture?&lt;/button&gt;
  &lt;div class="faq-a" style="display:none"&gt;A global IT services company.&lt;/div&gt;
&lt;/div&gt;
&lt;div class="faq-item"&gt;
  &lt;button class="faq-q" id="q2"&gt;When was it founded?&lt;/button&gt;
  &lt;div class="faq-a" style="display:none"&gt;1989 (as Andersen Consulting).&lt;/div&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript so that:</p>
<ul>
  <li><b>Toggle:</b> clicking a question shows its answer
      (<code>style.display = "block"</code>) and adds the class <code>active</code> to the clicked
      button; clicking it again hides the answer and removes <code>active</code>.</li>
  <li><b>One open at a time:</b> opening an item closes every other one (their answers go back to
      <code>display:none</code> and their buttons lose <code>active</code>).</li>
</ul>
<p>Use the <b>Preview</b> tab to try it live. Submitting runs automated tests that click the
questions in a fresh page.</p>
""",
        "hint": "querySelectorAll('.faq-q') gives the question buttons in order; the matching answer "
                "is btn.closest('.faq-item').querySelector('.faq-a'). Write openItem(btn) that closes "
                "all items first, then shows this one — and if the clicked one was already open, just "
                "leave everything closed.",
        "boilerplate": {
            "javascript": """function initializeAccordion() {
  // TODO: one question open at a time, with .active on its button
}

initializeAccordion();
""",
        },
        "tests": [],
        "samples": [],
        "browser_html": """<div class="faq-item">
  <button class="faq-q" id="q1">What is Accenture?</button>
  <div class="faq-a" style="display:none">A global IT services company.</div>
</div>
<div class="faq-item">
  <button class="faq-q" id="q2">When was it founded?</button>
  <div class="faq-a" style="display:none">1989 (as Andersen Consulting).</div>
</div>""",
        "browser_tests": [
            {
                "name": "Initially everything is closed",
                "hidden": False,
                "steps": [],
                "expect": {"style": {"selector": ".faq-a", "property": "display", "value": "none"}},
            },
            {
                "name": "Clicking Q1 opens A1",
                "hidden": False,
                "steps": [{"click": "q1"}],
                "expect": {
                    "style": {"selector": ".faq-a", "property": "display", "value": "block"},
                    "style2": {"selector": ".faq-q", "property": "className", "value": "faq-q active"},
                },
            },
            {
                "name": "Clicking Q1 again closes it",
                "hidden": False,
                "steps": [{"click": "q1"}, {"click": "q1"}],
                "expect": {"style": {"selector": ".faq-a", "property": "display", "value": "none"}},
            },
            {
                "name": "Opening Q2 closes Q1 (one at a time)",
                "hidden": True,
                "steps": [{"click": "q1"}, {"click": "q2"}],
                "expect": {
                    "style": {"selector": ".faq-a", "property": "display", "value": "none"},
                    "style2": {"selector": ".faq-item:nth-child(2) .faq-a", "property": "display", "value": "block"},
                },
            },
            {
                "name": "Q2 button carries the active class",
                "hidden": True,
                "steps": [{"click": "q2"}],
                "expect": {"style": {"selector": ".faq-item:nth-child(2) .faq-q", "property": "className", "value": "faq-q active"}},
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # 49. Image Slider / Carousel — 2026 pattern
    # ------------------------------------------------------------------ #
    {
        "id": 49,
        "slug": "image-slider-carousel",
        "title": "Image Slider / Carousel",
        "difficulty": "Medium",
        "topics": ["JavaScript", "DOM Manipulation"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Expected 2026-pattern task. The page contains:</p>
<pre>&lt;div id="slider"&gt;
  &lt;div class="slide"&gt;Slide 1&lt;/div&gt;
  &lt;div class="slide"&gt;Slide 2&lt;/div&gt;
  &lt;div class="slide"&gt;Slide 3&lt;/div&gt;
&lt;/div&gt;
&lt;button id="prev-btn"&gt;Prev&lt;/button&gt;
&lt;button id="next-btn"&gt;Next&lt;/button&gt;
&lt;p id="slide-indicator"&gt;&lt;/p&gt;</pre>
<p>Write JavaScript so that:</p>
<ul>
  <li><b>One at a time:</b> only the current slide has <code>style.display = "block"</code>; all
      others are <code>"none"</code>. Set this up on load for slide 1.</li>
  <li><b>Next/Prev with wrap-around:</b> <code>#next-btn</code> moves forward and
      <code>#prev-btn</code> backward, cycling (slide 3 &rarr; Next &rarr; slide 1; slide 1 &rarr;
      Prev &rarr; slide 3).</li>
  <li><b>Indicator:</b> <code>#slide-indicator</code> always reads
      <code>Slide &lt;n&gt; of 3</code> (e.g. <code>Slide 1 of 3</code>).</li>
</ul>
<p>Use the <b>Preview</b> tab to try it live. Submitting runs automated tests that click the
buttons in a fresh page.</p>
""",
        "hint": "Keep an index variable and a show() that loops document.querySelectorAll('.slide'), "
                "setting display per position, then writes `Slide ${i+1} of 3`. Advance with "
                "(i + 1) % slides.length and (i - 1 + slides.length) % slides.length.",
        "boilerplate": {
            "javascript": """function initializeSlider() {
  // TODO: show one slide at a time with wrap-around Prev/Next
}

initializeSlider();
""",
        },
        "tests": [],
        "samples": [],
        "browser_html": """<div id="slider">
  <div class="slide">Slide 1</div>
  <div class="slide">Slide 2</div>
  <div class="slide">Slide 3</div>
</div>
<button id="prev-btn">Prev</button>
<button id="next-btn">Next</button>
<p id="slide-indicator"></p>""",
        "browser_tests": [
            {
                "name": "Initial: slide 1 visible, indicator reads Slide 1 of 3",
                "hidden": False,
                "steps": [],
                "expect": {
                    "style": {"selector": ".slide", "property": "display", "value": "block"},
                    "text": {"id": "slide-indicator", "value": "Slide 1 of 3"},
                },
            },
            {
                "name": "Next goes to slide 2",
                "hidden": False,
                "steps": [{"click": "next-btn"}],
                "expect": {
                    "style": {"selector": ".slide", "property": "display", "value": "none"},
                    "style2": {"selector": ".slide:nth-child(2)", "property": "display", "value": "block"},
                    "text": {"id": "slide-indicator", "value": "Slide 2 of 3"},
                },
            },
            {
                "name": "Next three times wraps back to slide 1",
                "hidden": True,
                "steps": [{"click": "next-btn"}, {"click": "next-btn"}, {"click": "next-btn"}],
                "expect": {"text": {"id": "slide-indicator", "value": "Slide 1 of 3"}},
            },
            {
                "name": "Prev from slide 1 wraps to slide 3",
                "hidden": True,
                "steps": [{"click": "prev-btn"}],
                "expect": {"text": {"id": "slide-indicator", "value": "Slide 3 of 3"}},
            },
            {
                "name": "Prev then Next returns to slide 1",
                "hidden": True,
                "steps": [{"click": "prev-btn"}, {"click": "next-btn"}],
                "expect": {"text": {"id": "slide-indicator", "value": "Slide 1 of 3"}},
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # 50. Dark/Light Theme Toggle with LocalStorage — 2026 pattern
    # ------------------------------------------------------------------ #
    {
        "id": 50,
        "slug": "theme-toggle-localstorage",
        "title": "Dark/Light Theme Toggle with LocalStorage",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "LocalStorage"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Expected 2026-pattern task. The page contains:</p>
<pre>&lt;body&gt;
  &lt;button id="theme-btn"&gt;Toggle Theme&lt;/button&gt;
  &lt;p id="theme-label"&gt;Light mode&lt;/p&gt;
&lt;/body&gt;</pre>
<p>Write JavaScript so that:</p>
<ul>
  <li><b>Toggle:</b> clicking <code>#theme-btn</code> toggles the class <code>dark</code> on
      <code>document.body</code> and updates <code>#theme-label</code> to
      <code>Dark mode</code> (when dark) or <code>Light mode</code> (when light).</li>
  <li><b>Persist:</b> the choice is saved to <b>LocalStorage</b> under the key
      <code>theme</code> with value <code>"dark"</code> or <code>"light"</code>.</li>
  <li><b>Restore on load:</b> when the script runs, if <code>localStorage.theme === "dark"</code>
      the dark class and label must be applied immediately.</li>
</ul>
<p>The grader's fresh page starts with an empty LocalStorage, so the first test always sees
light mode.</p>
""",
        "hint": "Read localStorage.getItem('theme') at startup and call the same apply() the button "
                "uses. Write with localStorage.setItem('theme', 'dark'|'light') on every toggle.",
        "boilerplate": {
            "javascript": """function initializeTheme() {
  // TODO: restore the saved theme, then toggle + persist on click
}

initializeTheme();
""",
        },
        "tests": [],
        "samples": [],
        "browser_html": """<button id="theme-btn">Toggle Theme</button>
<p id="theme-label">Light mode</p>""",
        "browser_tests": [
            {
                "name": "Initial: light mode (no saved theme)",
                "hidden": False,
                "steps": [],
                "expect": {
                    "style": {"selector": "body", "property": "className", "value": ""},
                    "text": {"id": "theme-label", "value": "Light mode"},
                },
            },
            {
                "name": "First click: body gets dark class",
                "hidden": False,
                "steps": [{"click": "theme-btn"}],
                "expect": {
                    "style": {"selector": "body", "property": "className", "value": "dark"},
                    "text": {"id": "theme-label", "value": "Dark mode"},
                },
            },
            {
                "name": "Dark theme persisted to LocalStorage",
                "hidden": True,
                "steps": [{"click": "theme-btn"}],
                "expect": {"storage": {"key": "theme", "value": "dark"}},
            },
            {
                "name": "Second click returns to light",
                "hidden": True,
                "steps": [{"click": "theme-btn"}, {"click": "theme-btn"}],
                "expect": {
                    "style": {"selector": "body", "property": "className", "value": ""},
                    "text": {"id": "theme-label", "value": "Light mode"},
                },
            },
            {
                "name": "Light value stored after toggling back",
                "hidden": True,
                "steps": [{"click": "theme-btn"}, {"click": "theme-btn"}],
                "expect": {"storage": {"key": "theme", "value": "light"}},
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # 54. Product Rating System with Star Icons — KN Academy (adapted)
    # Original task had HTML/CSS/JS tabs; this platform's runner is
    # JavaScript-only, so the base markup and the gold .filled style are
    # already in the page and the candidate implements the behaviour.
    # ------------------------------------------------------------------ #
    {
        "id": 54,
        "slug": "product-rating-stars",
        "title": "Product Rating System with Star Icons",
        "difficulty": "Medium",
        "topics": ["JavaScript", "DOM Manipulation", "Events", "CSS Classes"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p class="text-muted">KN Academy — Web Lab (Cognizant/Accenture style). Adapted from the
original HTML/CSS/JS task: the product card and the <code>.filled</code> gold styling are
already in the page, so only the JavaScript behaviour is missing.</p>
<p>The card renders an empty rating container:</p>
<pre>&lt;div class="product"&gt;
  &lt;img src="..." alt="Wireless Headphones"&gt;
  &lt;h2&gt;Wireless Headphones&lt;/h2&gt;
  &lt;p class="price"&gt;$59.99&lt;/p&gt;
  &lt;div class="rating-stars" id="rating-stars"&gt;&lt;/div&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript to fulfill the following specifications:</p>
<ul>
  <li><b>Stars:</b> add <b>five</b> star icons <code>&lt;i class="fa-star star"&gt;&lt;/i&gt;</code>
      inside <code>.rating-stars</code> when the page loads.</li>
  <li><b>Click:</b> clicking the <i>n</i>-th star calls <code>setRating(n)</code>, which adds the
      class <code>filled</code> to stars 1 through <i>n</i> and removes it from every star after
      <i>n</i>.</li>
  <li><b>Immediate:</b> the display updates on every click — no reload and no form submit.</li>
</ul>
<p>The <code>filled</code> class is already styled gold (<code>#ffd700</code>) in the page; you only
toggle it.</p>
""",
        "hint": "Create the icons in a loop: for each index i build an <i> with classes "
                "'fa-star star', append it to #rating-stars and set its onclick to call "
                "setRating(i + 1). In setRating, loop over all stars and toggle the 'filled' "
                "class with classList.toggle('filled', index < rating).",
        "boilerplate": {
            "javascript": """function setRating(rating) {
  // TODO: add .filled to stars 1..rating and remove it from the rest
}

function initRating() {
  const starsBox = document.getElementById('rating-stars');

  // TODO: create five <i class="fa-star star"></i> icons inside starsBox,
  // each one calling setRating with its 1-based position
}

initRating();
""",
        },
        "tests": [],
        "samples": [],
        "browser_style": """
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css');

body { font-family: -apple-system, "Segoe UI", sans-serif; display: flex; justify-content: center;
       padding-top: 60px; background: #fafafa; margin: 0; }
.product { text-align: center; background: #fff; border: 1px solid #ddd; border-radius: 14px;
           padding: 30px 40px; box-shadow: 0 4px 18px rgba(0,0,0,.08); width: 280px; }
.product img { width: 120px; height: 120px; object-fit: cover; border-radius: 10px; }
.product h2 { font-size: 18px; margin: 14px 0 4px; color: #222; }
.product .price { color: #555; margin: 0 0 14px; }
.rating-stars { display: flex; justify-content: center; gap: 6px; font-size: 28px; }
.rating-stars .star { color: #ccc; cursor: pointer; }
.rating-stars .star.filled { color: #ffd700; }
""",
        "browser_html": """<div class="product">
  <img src="https://placehold.co/120x120?text=Product" alt="Wireless Headphones">
  <h2>Wireless Headphones</h2>
  <p class="price">$59.99</p>
  <div class="rating-stars" id="rating-stars"></div>
</div>""",
        "browser_tests": [
            {
                "name": "Five stars rendered, none filled on load",
                "hidden": False,
                "steps": [],
                "expect": {"stars": 5, "filled": 0},
            },
            {
                "name": "Clicking the 3rd star fills three stars",
                "hidden": False,
                "steps": [{"starClick": 3}],
                "expect": {"filled": 3},
            },
            {
                "name": "Clicking the 1st star fills only one",
                "hidden": False,
                "steps": [{"starClick": 1}],
                "expect": {"filled": 1},
            },
            {
                "name": "Clicking the 5th star fills all five",
                "hidden": False,
                "steps": [{"starClick": 5}],
                "expect": {"filled": 5},
            },
            {
                "name": "Filled stars are gold (#ffd700)",
                "hidden": True,
                "steps": [{"starClick": 4}],
                "expect": {"starColor": {"index": 4, "value": "rgb(255, 215, 0)"}},
            },
            {
                "name": "Choosing a lower rating unfills the higher stars",
                "hidden": True,
                "steps": [{"starClick": 5}, {"starClick": 2}],
                "expect": {"filled": 2},
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # 55. iPod Interface — KN Academy (adapted)
    # Original task had HTML/CSS/JS tabs; this platform's runner is
    # JavaScript-only, so the iPod markup and styles are already in the
    # page and the candidate implements the three objectives in JS.
    # ------------------------------------------------------------------ #
    {
        "id": 55,
        "slug": "ipod-interface",
        "title": "iPod Interface — Add Next Button & Wire Actions",
        "difficulty": "Medium",
        "topics": ["JavaScript", "DOM Manipulation", "Events", "CSS Styling"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p class="text-muted">KN Academy — Web Lab (Cognizant/Accenture style). Adapted from the
original HTML/CSS/JS task: the iPod markup and the base styles are already in the page, so the
three objectives are done in JavaScript.</p>
<p>The partially built iPod looks like this:</p>
<pre>&lt;div class="ipod" id="ipod"&gt;
  &lt;div class="screen"&gt;&lt;p id="screen-text"&gt;Ready&lt;/p&gt;&lt;/div&gt;
  &lt;div class="controls" id="controls"&gt;
    &lt;button class="nav-btn" id="menu-btn"&gt;Menu&lt;/button&gt;
    &lt;button class="nav-btn" id="prev-btn"&gt;&amp;#9664;&amp;#9664;&lt;/button&gt;
    &lt;button class="nav-btn" id="play-btn"&gt;&amp;#9654;&amp;#10074;&amp;#10074;&lt;/button&gt;
  &lt;/div&gt;
&lt;/div&gt;</pre>
<p>Finish the interface in JavaScript so that:</p>
<ul>
  <li><b>Next button:</b> a new <code>&lt;button id="next-btn" class="nav-btn"&gt;Next&lt;/button&gt;</code>
      is added to <code>#controls</code>.</li>
  <li><b>Pink body:</b> the iPod's background (<code>#ipod</code>) becomes <b>pink</b>
      (<code>#ffc0cb</code>).</li>
  <li><b>Action text:</b> clicking any of the four buttons writes its action into
      <code>#screen-text</code>: <code>#menu-btn</code> &rarr; <code>Menu</code>,
      <code>#prev-btn</code> &rarr; <code>Previous</code>, <code>#play-btn</code> &rarr;
      <code>Play/Pause</code>, <code>#next-btn</code> &rarr; <code>Next</code>.</li>
</ul>
<p>Keep the existing ids and classes unchanged — the grader and the JavaScript rely on them.</p>
""",
        "hint": "Create the button with document.createElement('button'), set its id to 'next-btn', "
                "its className to 'nav-btn' and its textContent to 'Next', then append it to "
                "#controls. Set the body colour with document.getElementById('ipod').style"
                ".backgroundColor = 'pink'. For the actions, one click listener per button that "
                "writes the matching label into #screen-text is the simplest approach.",
        "boilerplate": {
            "javascript": """function initIpod() {
  const ipod = document.getElementById('ipod');
  const controls = document.getElementById('controls');
  const screen = document.getElementById('screen-text');

  // TODO 1: add a <button id="next-btn" class="nav-btn">Next</button> to #controls

  // TODO 2: set the iPod's background colour to pink

  // TODO 3: make every button write its action text into #screen-text:
  //         #menu-btn -> "Menu", #prev-btn -> "Previous",
  //         #play-btn -> "Play/Pause", #next-btn -> "Next"
}

initIpod();
""",
        },
        "tests": [],
        "samples": [],
        "browser_style": """
body { font-family: -apple-system, "Segoe UI", sans-serif; display: flex; justify-content: center;
       padding-top: 60px; background: #fafafa; margin: 0; }
.ipod { width: 260px; background: #e8e8e8; border: 1px solid #ccc; border-radius: 22px;
        padding: 22px; box-shadow: 0 6px 20px rgba(0,0,0,.12); }
.ipod .screen { background: #fff; border: 1px solid #bbb; border-radius: 8px; height: 90px;
                display: flex; align-items: center; justify-content: center; margin-bottom: 18px; }
.ipod .screen p { margin: 0; font-size: 16px; color: #222; }
.ipod .controls { display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; }
.ipod .nav-btn { min-width: 64px; padding: 8px 10px; font-size: 13px; border-radius: 8px;
                 border: 1px solid #bbb; background: #fff; cursor: pointer; }
.ipod .nav-btn:hover { background: #f0f0f0; }
""",
        "browser_html": """<div class="ipod" id="ipod">
  <div class="screen"><p id="screen-text">Ready</p></div>
  <div class="controls" id="controls">
    <button class="nav-btn" id="menu-btn">Menu</button>
    <button class="nav-btn" id="prev-btn">&#9664;&#9664;</button>
    <button class="nav-btn" id="play-btn">&#9654;&#10074;&#10074;</button>
  </div>
</div>""",
        "browser_tests": [
            {
                "name": "Next button added with the right id and label",
                "hidden": False,
                "steps": [],
                "expect": {"exists": {"selector": "#next-btn", "value": True, "text": "Next"}},
            },
            {
                "name": "iPod body is pink",
                "hidden": False,
                "steps": [],
                "expect": {"css": {"selector": "#ipod", "property": "backgroundColor", "value": "rgb(255, 192, 203)"}},
            },
            {
                "name": "Menu button shows its action text",
                "hidden": False,
                "steps": [{"click": "menu-btn"}],
                "expect": {"text": {"id": "screen-text", "value": "Menu"}},
            },
            {
                "name": "Next button shows its action text",
                "hidden": False,
                "steps": [{"click": "next-btn"}],
                "expect": {"text": {"id": "screen-text", "value": "Next"}},
            },
            {
                "name": "Previous button shows its action text",
                "hidden": True,
                "steps": [{"click": "prev-btn"}],
                "expect": {"text": {"id": "screen-text", "value": "Previous"}},
            },
            {
                "name": "Play button shows its action text",
                "hidden": True,
                "steps": [{"click": "play-btn"}],
                "expect": {"text": {"id": "screen-text", "value": "Play/Pause"}},
            },
        ],
    },
]


# ---------------------------------------------------------------------- #
# MCQ quizzes built from the 2026 expected-question bank (ids 52-53).
# ---------------------------------------------------------------------- #

QUIZ_WEB_MCQ_2026 = {
    "id": 52,
    "slug": "web-mcq-2026",
    "title": "Web MCQs — KN Academy Set (2026 Expected)",
    "difficulty": "Easy",
    "topics": "HTML · CSS · JavaScript".split(" · "),
    "judge": "quiz",
    "languages": ["quiz"],
    "description": (
        "<p>12 web-technology MCQs from the KN Academy web mocks — the set of "
        "questions not already used in Web Mock-1/2/3. HTML semantics, CSS box model, "
        "JavaScript operators, arrays and objects — expected in the 2026 web-based "
        "technical assessment.</p>"
        "<p>Select an option for every question, then press <b>Submit</b>. Correct "
        "answers turn green; wrong picks show the right one.</p>"
    ),
    "hint": "Watch the JS output questions closely: + with strings concatenates, === "
            "compares type and value, arrays keep holes when you assign past the end, "
            "and objects are compared by reference, not by content.",
    "boilerplate": {},
    "samples": [],
    "questions": [
        {
            "q": "<b>1.</b> How do you select elements with the class name 'example'?",
            "options": [
                ".example",
                "#example",
                "example",
                "*example"
            ],
            "answer": 0
        },
        {
            "q": "<b>2.</b> Which of the following is a correct syntax to display 'Hello World' in an alert box?",
            "options": [
                "alert('Hello World');",
                "msgBox('Hello World');",
                "alertBox('Hello World');",
                "prompt('Hello World');"
            ],
            "answer": 0
        },
        {
            "q": "<b>3.</b> A script creates a <p> with createElement + appendChild, then runs document.write(document.getElementsByTagName('p').length). Output?",
            "options": [
                "1",
                "0",
                "2",
                "Undefined"
            ],
            "answer": 0
        },
        {
            "q": "<b>4.</b> A button's onclick sets btn.innerHTML='Clicked' then calls document.write(btn.innerHTML). What appears?",
            "options": [
                "'Clicked' is written and the rest of the page is replaced",
                "Button text changes and page stays",
                "'Clicked' written, page replaced",
                "Error",
                "No change"
            ],
            "answer": 0
        },
        {
            "q": "<b>5.</b> document.getElementById('demo').innerHTML = 10 + 20 + '30'. What shows in the div?",
            "options": [
                "3030 (string)",
                "3030",
                "102030",
                "3030 (string type)"
            ],
            "answer": 0
        },
        {
            "q": "<b>6.</b> An element has width:100px; padding:15px; border:5px. Total width with default box-sizing?",
            "options": [
                "140px",
                "100px",
                "120px",
                "105px"
            ],
            "answer": 0
        },
        {
            "q": "<b>7.</b> How does setting 'margin: auto;' affect a block element?",
            "options": [
                "Centers the element horizontally",
                "Removes margin",
                "Centers horizontally",
                "Adds margin everywhere",
                "Sticks to right"
            ],
            "answer": 0
        },
        {
            "q": "<b>8.</b> let arr=[1,2,3]; arr.push(4); console.log(arr.length)?",
            "options": [
                "4",
                "3",
                "5",
                "undefined"
            ],
            "answer": 0
        },
        {
            "q": "<b>9.</b> How can you check if a variable is an array in JavaScript?",
            "options": [
                "Array.isArray(variable)",
                "typeof v === 'array'",
                "Array.isArray(v)",
                "v.isArray()",
                "is_array(v)"
            ],
            "answer": 0
        },
        {
            "q": "<b>10.</b> let numbers=[1,2,3]; numbers[10]=11; console.log(numbers.length)?",
            "options": [
                "11",
                "4",
                "10",
                "3"
            ],
            "answer": 0
        },
        {
            "q": "<b>11.</b> let obj1={a:1}; let obj2={a:1}; console.log(obj1===obj2)?",
            "options": [
                "false",
                "true",
                "undefined",
                "error"
            ],
            "answer": 0
        },
        {
            "q": "<b>12.</b> Which position value positions an element relative to its nearest positioned ancestor?",
            "options": [
                "absolute",
                "static",
                "relative",
                "fixed"
            ],
            "answer": 0
        }
    ],
}

QUIZ_SQL_2026 = {
    "id": 53,
    "slug": "sql-mock-3-2026",
    "title": "SQL Mock-3 — KN Academy Set (2026 Expected)",
    "difficulty": "Medium",
    "topics": "SQL · Queries · Functions".split(" · "),
    "judge": "quiz",
    "languages": ["quiz"],
    "description": (
        "<p>9 SQL MCQs from the KN Academy SQL mock tests — the questions not "
        "already in SQL Mock-1/2. String functions, NULLIF, CASE, joins and "
        "error-spotting, as expected in the 2026 technical assessment.</p>"
        "<p>Select an option for every question, then press <b>Submit</b>. Correct "
        "answers turn green; wrong picks show the right one.</p>"
    ),
    "hint": "For the spot-the-error questions read the query clause by clause: redundant "
            "WHERE, misused functions (AGE, CEILING, SQUARE), missing aliases and MySQL's "
            "lack of FULL OUTER JOIN are the recurring traps.",
    "boilerplate": {},
    "samples": [],
    "questions": [
        {
            "q": "<b>1.</b> Show products whose names contain the word \"Table.\"",
            "options": [
                "SELECT * FROM Products WHERE Product_Name LIKE '%Table%';",
                "SELECT * FROM Products WHERE Product_Name LIKE 'Table%';",
                "SELECT * FROM Products WHERE Product_Name LIKE '%Table_';",
                "SELECT * FROM Products WHERE Product_Name = '%Table%';"
            ],
            "answer": 0
        },
        {
            "q": "<b>2.</b> Write a SQL query to fetch \"FIRST_NAME\" from the Student table in upper case and use ALIAS name as STUDENT_NAME.",
            "options": [
                "SELECT upper(FIRST_NAME) as STUDENT_NAME from Student;",
                "SELECT FIRST_NAME as STUDENT_NAME from Student;",
                "SELECT upper(FIRST_NAME)from Student;",
                "SELECT upper(FIRSTNAME) as STUDENT_NAME from Student;"
            ],
            "answer": 0
        },
        {
            "q": "<b>3.</b> Write a SQL query to print FIRST_NAME from the Student table after replacing 'a' with 'A'.",
            "options": [
                "SELECT REPLACE(FIRST_NAME, 'a', 'A') FROM Student;",
                "SELECT REPLACE('a', 'A') FROM Student;",
                "SELECT REPLACE(FIRST_NAME, 'A', 'a') FROM Student;",
                "None of the above"
            ],
            "answer": 0
        },
        {
            "q": "<b>4.</b> Identify the error in \"SELECT Name, NULLIF(Age, 30) FROM Employees WHERE Age IS NOT NULL;\"",
            "options": [
                "Remove 'WHERE Age IS NOT NULL'",
                "Change 'NULLIF' to 'ISNULL'",
                "Replace 'Age, 30' with 'Age, 0'",
                "No error"
            ],
            "answer": 0
        },
        {
            "q": "<b>5.</b> What needs to be corrected in \"SELECT CURRENT_DATE FROM Employees;\"?",
            "options": [
                "Remove 'FROM Employees'",
                "Replace 'CURRENT_DATE' with 'GETDATE()'",
                "Add 'AS Today'",
                "No error"
            ],
            "answer": 0
        },
        {
            "q": "<b>6.</b> In \"SELECT Name, AGE(BirthDate) AS Age FROM Customers;\", what needs correction?",
            "options": [
                "AGE",
                "AS Age",
                "BirthDate",
                "No error"
            ],
            "answer": 0
        },
        {
            "q": "<b>7.</b> What needs to be corrected in \"SELECT CONCAT(FirstName, ' ', LastName) FROM Employees;\"?",
            "options": [
                "Add 'AS FullName' for clarity",
                "Change 'CONCAT' to 'CONCATENATE'",
                "Replace ',' with '+'",
                "No error"
            ],
            "answer": 0
        },
        {
            "q": "<b>8.</b> Correct the syntax error in \"SELECT CEILING(Price) AS RoundedPrice FROM Products WHERE Price > 0;\"",
            "options": [
                "Remove 'WHERE Price > 0'",
                "Change 'CEILING' to 'FLOOR'",
                "Replace 'AS RoundedPrice' with 'AS PriceCeiling'",
                "No error"
            ],
            "answer": 0
        },
        {
            "q": "<b>9.</b> What is wrong in \"SELECT * FROM Employees FULL OUTER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID WHERE Departments.DepartmentName IS NULL;\"?",
            "options": [
                "Remove 'WHERE Departments.DepartmentName IS NULL'",
                "Replace 'FULL OUTER JOIN' with 'LEFT JOIN'",
                "Change 'WHERE' to 'AND'",
                "No error"
            ],
            "answer": 0
        }
    ],
}


# ---------------------------------------------------------------------- #
# MCQ quizzes built from the 2026 expected-question bank (ids 52-53).
# ---------------------------------------------------------------------- #

QUIZ_WEB_MCQ_2026 = {
    "id": 52,
    "slug": "web-mcq-2026",
    "title": "Web MCQs — KN Academy Set (2026 Expected)",
    "difficulty": "Easy",
    "topics": "HTML · CSS · JavaScript".split(" · "),
    "judge": "quiz",
    "languages": ["quiz"],
    "description": (
        "<p>12 web-technology MCQs from the KN Academy web mocks — the set of "
        "questions not already used in Web Mock-1/2/3. HTML semantics, CSS box model, "
        "JavaScript operators, arrays and objects — expected in the 2026 web-based "
        "technical assessment.</p>"
        "<p>Select an option for every question, then press <b>Submit</b>. Correct "
        "answers turn green; wrong picks show the right one.</p>"
    ),
    "hint": "Watch the JS output questions closely: + with strings concatenates, === "
            "compares type and value, arrays keep holes when you assign past the end, "
            "and objects are compared by reference, not by content.",
    "boilerplate": {},
    "samples": [],
    "questions": [
        {
            "q": "<b>1.</b> How do you select elements with the class name 'example'?",
            "options": [
                ".example",
                "#example",
                "example",
                "*example"
            ],
            "answer": 0
        },
        {
            "q": "<b>2.</b> Which of the following is a correct syntax to display 'Hello World' in an alert box?",
            "options": [
                "alert('Hello World');",
                "msgBox('Hello World');",
                "alertBox('Hello World');",
                "prompt('Hello World');"
            ],
            "answer": 0
        },
        {
            "q": "<b>3.</b> A script creates a <p> with createElement + appendChild, then runs document.write(document.getElementsByTagName('p').length). Output?",
            "options": [
                "1",
                "0",
                "2",
                "Undefined"
            ],
            "answer": 0
        },
        {
            "q": "<b>4.</b> A button's onclick sets btn.innerHTML='Clicked' then calls document.write(btn.innerHTML). What appears?",
            "options": [
                "'Clicked' is written and the rest of the page is replaced",
                "Button text changes and page stays",
                "'Clicked' written, page replaced",
                "Error"
            ],
            "answer": 0
        },
        {
            "q": "<b>5.</b> document.getElementById('demo').innerHTML = 10 + 20 + '30'. What shows in the div?",
            "options": [
                "3030 (string)",
                "3030",
                "102030",
                "3030 (string type)"
            ],
            "answer": 0
        },
        {
            "q": "<b>6.</b> An element has width:100px; padding:15px; border:5px. Total width with default box-sizing?",
            "options": [
                "140px",
                "100px",
                "120px",
                "105px"
            ],
            "answer": 0
        },
        {
            "q": "<b>7.</b> How does setting 'margin: auto;' affect a block element?",
            "options": [
                "Centers the element horizontally",
                "Removes margin",
                "Centers horizontally",
                "Adds margin everywhere"
            ],
            "answer": 0
        },
        {
            "q": "<b>8.</b> let arr=[1,2,3]; arr.push(4); console.log(arr.length)?",
            "options": [
                "4",
                "3",
                "5",
                "undefined"
            ],
            "answer": 0
        },
        {
            "q": "<b>9.</b> How can you check if a variable is an array in JavaScript?",
            "options": [
                "Array.isArray(variable)",
                "typeof v === 'array'",
                "Array.isArray(v)",
                "v.isArray()"
            ],
            "answer": 0
        },
        {
            "q": "<b>10.</b> let numbers=[1,2,3]; numbers[10]=11; console.log(numbers.length)?",
            "options": [
                "11",
                "4",
                "10",
                "3"
            ],
            "answer": 0
        },
        {
            "q": "<b>11.</b> let obj1={a:1}; let obj2={a:1}; console.log(obj1===obj2)?",
            "options": [
                "false",
                "true",
                "undefined",
                "error"
            ],
            "answer": 0
        },
        {
            "q": "<b>12.</b> Which position value positions an element relative to its nearest positioned ancestor?",
            "options": [
                "absolute",
                "static",
                "relative",
                "fixed"
            ],
            "answer": 0
        }
    ],
}

QUIZ_SQL_2026 = {
    "id": 53,
    "slug": "sql-mock-3-2026",
    "title": "SQL Mock-3 — KN Academy Set (2026 Expected)",
    "difficulty": "Medium",
    "topics": "SQL · Queries · Functions".split(" · "),
    "judge": "quiz",
    "languages": ["quiz"],
    "description": (
        "<p>9 SQL MCQs from the KN Academy SQL mock tests — the questions not "
        "already in SQL Mock-1/2. String functions, NULLIF, CASE, joins and "
        "error-spotting, as expected in the 2026 technical assessment.</p>"
        "<p>Select an option for every question, then press <b>Submit</b>. Correct "
        "answers turn green; wrong picks show the right one.</p>"
    ),
    "hint": "For the spot-the-error questions read the query clause by clause: redundant "
            "WHERE, misused functions (AGE, CEILING, SQUARE), missing aliases and MySQL's "
            "lack of FULL OUTER JOIN are the recurring traps.",
    "boilerplate": {},
    "samples": [],
    "questions": [
        {
            "q": "<b>1.</b> Show products whose names contain the word \"Table.\"",
            "options": [
                "SELECT * FROM Products WHERE Product_Name LIKE '%Table%';",
                "SELECT * FROM Products WHERE Product_Name LIKE 'Table%';",
                "SELECT * FROM Products WHERE Product_Name LIKE '%Table_';",
                "SELECT * FROM Products WHERE Product_Name = '%Table%';"
            ],
            "answer": 0
        },
        {
            "q": "<b>2.</b> Write a SQL query to fetch \"FIRST_NAME\" from the Student table in upper case and use ALIAS name as STUDENT_NAME.",
            "options": [
                "SELECT upper(FIRST_NAME) as STUDENT_NAME from Student;",
                "SELECT FIRST_NAME as STUDENT_NAME from Student;",
                "SELECT upper(FIRST_NAME)from Student;",
                "SELECT upper(FIRSTNAME) as STUDENT_NAME from Student;"
            ],
            "answer": 0
        },
        {
            "q": "<b>3.</b> Write a SQL query to print FIRST_NAME from the Student table after replacing 'a' with 'A'.",
            "options": [
                "SELECT REPLACE(FIRST_NAME, 'a', 'A') FROM Student;",
                "SELECT REPLACE('a', 'A') FROM Student;",
                "SELECT REPLACE(FIRST_NAME, 'A', 'a') FROM Student;",
                "None of the above"
            ],
            "answer": 0
        },
        {
            "q": "<b>4.</b> Identify the error in \"SELECT Name, NULLIF(Age, 30) FROM Employees WHERE Age IS NOT NULL;\"",
            "options": [
                "Remove 'WHERE Age IS NOT NULL'",
                "Change 'NULLIF' to 'ISNULL'",
                "Replace 'Age, 30' with 'Age, 0'",
                "No error"
            ],
            "answer": 0
        },
        {
            "q": "<b>5.</b> What needs to be corrected in \"SELECT CURRENT_DATE FROM Employees;\"?",
            "options": [
                "Remove 'FROM Employees'",
                "Replace 'CURRENT_DATE' with 'GETDATE()'",
                "Add 'AS Today'",
                "No error"
            ],
            "answer": 0
        },
        {
            "q": "<b>6.</b> In \"SELECT Name, AGE(BirthDate) AS Age FROM Customers;\", what needs correction?",
            "options": [
                "AGE",
                "AS Age",
                "BirthDate",
                "No error"
            ],
            "answer": 0
        },
        {
            "q": "<b>7.</b> What needs to be corrected in \"SELECT CONCAT(FirstName, ' ', LastName) FROM Employees;\"?",
            "options": [
                "Add 'AS FullName' for clarity",
                "Change 'CONCAT' to 'CONCATENATE'",
                "Replace ',' with '+'",
                "No error"
            ],
            "answer": 0
        },
        {
            "q": "<b>8.</b> Correct the syntax error in \"SELECT CEILING(Price) AS RoundedPrice FROM Products WHERE Price > 0;\"",
            "options": [
                "Remove 'WHERE Price > 0'",
                "Change 'CEILING' to 'FLOOR'",
                "Replace 'AS RoundedPrice' with 'AS PriceCeiling'",
                "No error"
            ],
            "answer": 0
        },
        {
            "q": "<b>9.</b> What is wrong in \"SELECT * FROM Employees FULL OUTER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID WHERE Departments.DepartmentName IS NULL;\"?",
            "options": [
                "Remove 'WHERE Departments.DepartmentName IS NULL'",
                "Replace 'FULL OUTER JOIN' with 'LEFT JOIN'",
                "Change 'WHERE' to 'AND'",
                "No error"
            ],
            "answer": 0
        }
    ],
}
