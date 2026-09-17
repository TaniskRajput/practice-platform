"""
68 (67 usable) coding problems sourced from the "Accenture Coding.pdf" question bank.
Every problem here is judged server-side against a Java program read via stdin.
All reference solutions were hand-verified by compiling and running a correct Java
program against each test's input and using its actual trimmed stdout as `expected`.
"""

T = "Accenture PDF Set"

ACCENTURE_CODING_PDF_PROBLEMS = [

    # 3001. Absolute Difference
    {
        "id": 3001,
        "slug": "absolute-difference",
        "title": "Absolute Difference Count",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Math"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an integer array <code>arr</code> and two integers <code>num</code> and <code>diff</code>,
find the number of elements of <code>arr</code> whose absolute difference with <code>num</code> is
less than or equal to <code>diff</code>.</p>
<p>If no such element exists, print <code>-1</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers. Line 3: <code>num</code>. Line 4: <code>diff</code>.</p>
<h3>Example:</h3>
<pre>Input:              Output:
6                    3
12 3 14 56 77 13
13
2</pre>
<p>Explanation: 12, 13 and 14 have an absolute difference &lt;= 2 with 13.</p>
""",
        "hint": "Loop through the array and count elements where Math.abs(num - arr[i]) <= diff. Return -1 if the count is 0.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int num = sc.nextInt();
        int diff = sc.nextInt();

        // TODO: count elements with |num - arr[i]| <= diff, return -1 if none
        int count = 0;

        System.out.println(count > 0 ? count : -1);
    }
}""",
        },
        "tests": [
            {"input": "6\n12 3 14 56 77 13\n13\n2", "expected": "3", "hidden": False},
        ],
        "samples": [0],
    },

    # 3002. Anagram Check
    {
        "id": 3002,
        "slug": "anagram-check",
        "title": "Anagram Check",
        "difficulty": "Easy",
        "topics": [T, "Strings", "Hash Table"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given two strings <code>s</code> and <code>t</code>, determine whether the characters of
<code>s</code> can be rearranged to form <code>t</code>.</p>
<p>Print <code>True</code> if possible, otherwise print <code>False</code> (comparison is case-insensitive).</p>
<h3>Input format:</h3>
<p>Line 1: <code>s</code>. Line 2: <code>t</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
listen      True
silent</pre>
""",
        "hint": "Lowercase both strings, sort their characters, and compare the sorted arrays for equality.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String t = sc.nextLine();

        // TODO: check if s and t are anagrams (case-insensitive)
        boolean isAnagram = false;

        System.out.println(isAnagram ? "True" : "False");
    }
}""",
        },
        "tests": [
            {"input": "listen\nsilent", "expected": "True", "hidden": False},
        ],
        "samples": [0],
    },

    # 3003. Autobiographical Number
    {
        "id": 3003,
        "slug": "autobiographical-number",
        "title": "Autobiographical Number",
        "difficulty": "Medium",
        "topics": [T, "Strings", "Math"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>A number <code>N</code> (given as a digit string) is <b>autobiographical</b> if, for every position
<code>i</code> (0-indexed), the digit at position <code>i</code> equals the count of how many times the
digit <code>i</code> appears in <code>N</code>.</p>
<p>If <code>N</code> is autobiographical, print the count of <b>distinct</b> digits used in <code>N</code>.
Otherwise print <code>0</code>.</p>
<h3>Input format:</h3>
<p>A single line containing the digit string.</p>
<h3>Example:</h3>
<pre>Input:      Output:
1210        3</pre>
<p>Explanation: position 0 has value 1 = count of 0s in "1210" (one 0). Position 1 has value 2 = count of
1s (two 1s). Position 2 has value 1 = count of 2s (one 2). Position 3 has value 0 = count of 3s (zero).
It is autobiographical, and the distinct digits used are {0,1,2} = 3.</p>
""",
        "hint": "Build a frequency array of digits 0-9 first, then check position-by-position that the digit at i equals freq[i]. If it all checks out, count distinct characters in the string.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n = sc.nextLine().trim();

        // TODO: check if n is autobiographical, print distinct digit count or 0
        int result = 0;

        System.out.println(result);
    }
}""",
        },
        "tests": [
            {"input": "1210", "expected": "3", "hidden": False},
        ],
        "samples": [0],
    },

    # 3004. Binary Operations
    {
        "id": 3004,
        "slug": "binary-operations",
        "title": "Binary Operations",
        "difficulty": "Medium",
        "topics": [T, "Strings", "Bit Manipulation"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>You are given a string made of binary digits ('0'/'1') separated by operator letters:
<code>A</code> = AND, <code>B</code> = OR, <code>C</code> = XOR.</p>
<p>Scanning left to right, apply each operation in order (no operator precedence) starting from the
first digit, and print the final integer result.</p>
<h3>Input format:</h3>
<p>A single line containing the string.</p>
<h3>Example:</h3>
<pre>Input:                 Output:
1C0C1C1A0B1            1</pre>
<p>Explanation: 1 XOR 0 XOR 1 XOR 1 AND 0 OR 1 = 1, evaluated strictly left to right.</p>
""",
        "hint": "The string alternates digit, operator, digit, operator, ... Start with the first digit as the running result, then for each (operator, digit) pair apply &, | or ^ in order.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine().trim();

        // TODO: scan left to right applying A=AND, B=OR, C=XOR
        int result = 0;

        System.out.println(result);
    }
}""",
        },
        "tests": [
            {"input": "1C0C1C1A0B1", "expected": "1", "hidden": False},
            {"input": "0C1A1B1C1C1B0A0", "expected": "0", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3005. Binary to Decimal
    {
        "id": 3005,
        "slug": "binary-to-decimal",
        "title": "Binary to Decimal",
        "difficulty": "Easy",
        "topics": [T, "Math", "Bit Manipulation"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a number made up only of binary digits (e.g. <code>1010</code>), print its decimal value.</p>
<h3>Input format:</h3>
<p>A single line containing the binary digits.</p>
<h3>Example:</h3>
<pre>Input:      Output:
1010        10</pre>
""",
        "hint": "Read each digit from the right, multiplying by increasing powers of 2 and summing them up.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();

        // TODO: convert binary-digit number n to its decimal value
        int decimal = 0;

        System.out.println(decimal);
    }
}""",
        },
        "tests": [
            {"input": "1010", "expected": "10", "hidden": False},
        ],
        "samples": [0],
    },

    # 3006. Bulb Switch
    {
        "id": 3006,
        "slug": "bulb-switch",
        "title": "Bulb Switch",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Greedy"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p><code>N</code> light bulbs are connected in a row. Pressing the switch of bulb <code>i</code> flips
bulb <code>i</code> itself and every bulb to its right (0 becomes 1, 1 becomes 0).</p>
<p>Given the initial 0/1 state array, find the minimum number of switch presses needed to turn
<b>all</b> bulbs on.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated 0/1 values.</p>
<h3>Example:</h3>
<pre>Input:      Output:
4           4
0 1 0 1</pre>
""",
        "hint": "Scan left to right. Whenever you hit a bulb that is currently 0, you must press its switch: flip it and everything to its right, and count the press. This greedy left-to-right simulation gives the minimum presses.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: greedily press switches left to right whenever a bulb is off
        int count = 0;

        System.out.println(count);
    }
}""",
        },
        "tests": [
            {"input": "4\n0 1 0 1", "expected": "4", "hidden": False},
            {"input": "5\n1 0 0 0 0", "expected": "1", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3007. Chocolate Distribution
    {
        "id": 3007,
        "slug": "chocolate-distribution",
        "title": "Chocolate Distribution",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Sorting", "Greedy"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an array of chocolate packet sizes and an integer <code>m</code> (number of students),
distribute exactly <code>m</code> packets, one per student, so that the difference between the
largest and smallest packet given out is minimized. Print that minimum difference.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers. Line 3: <code>m</code>.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
7                       2
7 3 2 4 9 12 56
3</pre>
""",
        "hint": "Sort the array, then slide a window of size m across it, tracking the minimum of (window's last element - window's first element).",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int m = sc.nextInt();

        // TODO: sort arr, slide a window of size m, find the minimum (max-min) in any window
        int minDiff = 0;

        System.out.println(minDiff);
    }
}""",
        },
        "tests": [
            {"input": "7\n7 3 2 4 9 12 56\n3", "expected": "2", "hidden": False},
        ],
        "samples": [0],
    },

    # 3008. Count Carry
    {
        "id": 3008,
        "slug": "count-carry",
        "title": "Count Carry Operations",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given two non-negative integers, count how many carries occur when adding them digit by digit
from right to left (elementary school addition).</p>
<h3>Input format:</h3>
<p>Line 1: <code>num1</code>. Line 2: <code>num2</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
451         2
349</pre>
""",
        "hint": "Repeatedly take the last digit of each number plus any carry from the previous step; if the sum exceeds 9, that's a carry.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int no1 = sc.nextInt();
        int no2 = sc.nextInt();

        // TODO: count carries produced while adding no1 + no2 digit by digit
        int count = 0;

        System.out.println(count);
    }
}""",
        },
        "tests": [
            {"input": "451\n349", "expected": "2", "hidden": False},
            {"input": "23\n563", "expected": "0", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3009. Decimal to Binary
    {
        "id": 3009,
        "slug": "decimal-to-binary",
        "title": "Decimal to Binary",
        "difficulty": "Easy",
        "topics": [T, "Math", "Bit Manipulation"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a decimal integer <code>n</code>, print its binary representation (no leading zeros, and
<code>0</code> for input <code>0</code>).</p>
<h3>Input format:</h3>
<p>A single integer <code>n</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
10          1010</pre>
""",
        "hint": "Repeatedly take n & 1 to get the next binary digit and shift n right by 1, then reverse the collected digits.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: convert n to its binary representation (string of 0/1)
        String binary = "0";

        System.out.println(binary);
    }
}""",
        },
        "tests": [
            {"input": "10", "expected": "1010", "hidden": False},
        ],
        "samples": [0],
    },

    # 3010. Palindrome Numbers in Range
    {
        "id": 3010,
        "slug": "palindrome-numbers-in-range",
        "title": "Palindrome Numbers in Range",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a lower bound and an upper bound (inclusive), print all palindrome numbers in that range,
space-separated, in increasing order.</p>
<h3>Input format:</h3>
<p>Line 1: <code>lower</code>. Line 2: <code>upper</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
10          11 22 33 44 55 66 77
80</pre>
""",
        "hint": "For each number in [lower, upper], reverse its digits and check if the reversed number equals the original.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int lower = sc.nextInt();
        int upper = sc.nextInt();

        // TODO: print all palindrome numbers in [lower, upper], space separated
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString().trim());
    }
}""",
        },
        "tests": [
            {"input": "10\n80", "expected": "11 22 33 44 55 66 77", "hidden": False},
            {"input": "100\n200", "expected": "101 111 121 131 141 151 161 171 181 191", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3011. Sum of Distances Between Three Points
    {
        "id": 3011,
        "slug": "sum-of-distances-three-points",
        "title": "Sum of Distances Between Three Points",
        "difficulty": "Easy",
        "topics": [T, "Math", "Geometry"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given three points <code>(x1,y1)</code>, <code>(x2,y2)</code>, <code>(x3,y3)</code>, compute the sum
of the three pairwise Euclidean distances (P1-P2 + P2-P3 + P1-P3), rounded to 2 decimal places.</p>
<h3>Input format:</h3>
<p>A single line with six space-separated numbers: <code>x1 y1 x2 y2 x3 y3</code>.</p>
<h3>Example:</h3>
<pre>Input:              Output:
1 1 2 4 3 6         10.78</pre>
""",
        "hint": "distance(P,Q) = sqrt((qx-px)^2 + (qy-py)^2). Sum all three pairwise distances and format with two decimal places.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double x1 = sc.nextDouble(), y1 = sc.nextDouble();
        double x2 = sc.nextDouble(), y2 = sc.nextDouble();
        double x3 = sc.nextDouble(), y3 = sc.nextDouble();

        // TODO: sum the three pairwise distances between the points
        double sum = 0.0;

        System.out.printf("%.2f%n", sum);
    }
}""",
        },
        "tests": [
            {"input": "1 1 2 4 3 6", "expected": "10.78", "hidden": False},
        ],
        "samples": [0],
    },

    # 3012. Count Occurrences
    {
        "id": 3012,
        "slug": "count-occurrences-array",
        "title": "Count Occurrences (First-Appearance Order)",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Hash Table"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an array, print the number of occurrences of each distinct value, one per line, in the
format <code>value - count</code>, ordered by each value's first appearance in the array.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
6                       10 - 3
10 5 10 15 10 5         5 - 2
                        15 - 1</pre>
""",
        "hint": "Use a LinkedHashMap (or equivalent) to preserve first-insertion order while counting frequencies.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: print "value - count" per distinct value, in first-appearance order
        StringBuilder sb = new StringBuilder();

        System.out.print(sb.toString().trim());
    }
}""",
        },
        "tests": [
            {"input": "6\n10 5 10 15 10 5", "expected": "10 - 3\n5 - 2\n15 - 1", "hidden": False},
        ],
        "samples": [0],
        "io_style": "lines",
    },

    # 3013. Elevation Point
    {
        "id": 3013,
        "slug": "elevation-point",
        "title": "Elevation Point (Peak Value)",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Binary Search"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an array, find a "peak" value: an element that is strictly greater than both its neighbors
(or greater than its only neighbor, at either edge). Print that peak's <b>value</b>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
7                       4
1 2 3 4 3 2 1</pre>
""",
        "hint": "Scan the array; an index i is a peak if (i==0 or arr[i]>arr[i-1]) and (i==n-1 or arr[i]>arr[i+1]). Print arr[i] for the first such i found.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: find a peak element (value strictly greater than its neighbors) and print its value
        int peak = arr[0];

        System.out.println(peak);
    }
}""",
        },
        "tests": [
            {"input": "7\n1 2 3 4 3 2 1", "expected": "4", "hidden": False},
            {"input": "2\n5 3", "expected": "5", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3014. Encode Number
    {
        "id": 3014,
        "slug": "encode-number",
        "title": "Encode Number",
        "difficulty": "Easy",
        "topics": [T, "Math", "Strings"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an integer <code>N</code>, square each of its digits and concatenate the resulting decimal
strings to form the encoded number. Print the encoded number.</p>
<h3>Input format:</h3>
<p>A single integer <code>n</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
34          916</pre>
<p>Explanation: 3^2 = 9, 4^2 = 16, concatenated: "9" + "16" = "916".</p>
""",
        "hint": "Process digits from the right, squaring each and prepending the square's decimal string to the accumulated result.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: square each digit of n and concatenate the results
        long encoded = 0;

        System.out.println(encoded);
    }
}""",
        },
        "tests": [
            {"input": "34", "expected": "916", "hidden": False},
        ],
        "samples": [0],
    },

    # 3015. Equilibrium Sum
    {
        "id": 3015,
        "slug": "equilibrium-sum",
        "title": "Equilibrium Index",
        "difficulty": "Easy",
        "topics": [T, "Arrays"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an integer array, find the index where the sum of elements strictly to its left equals the
sum of elements strictly to its right. Print that index, or <code>-1</code> if none exists.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:              Output:
5                   2
3 4 3 1 6</pre>
<p>Explanation: at index 2, left sum = 3+4 = 7 and right sum = 1+6 = 7.</p>
""",
        "hint": "Compute the total sum first. Then walk left to right tracking leftSum, and compute rightSum = total - leftSum - arr[i] at each index.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: find the equilibrium index (left sum == right sum), else -1
        int result = -1;

        System.out.println(result);
    }
}""",
        },
        "tests": [
            {"input": "5\n3 4 3 1 6", "expected": "2", "hidden": False},
        ],
        "samples": [0],
    },

    # 3016. Find the Missing Number
    {
        "id": 3016,
        "slug": "find-the-missing-number",
        "title": "Find the Missing Number",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Math"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>An array contains <code>n</code> distinct integers taken from the range <code>1</code> to
<code>n+1</code>, with exactly one number missing. Find and print the missing number.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code> (length of the given array). Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:              Output:
5                   3
1 2 4 5 6</pre>
""",
        "hint": "The full range 1..n+1 sums to (n+1)(n+2)/2. Subtract the actual array sum to get the missing number.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: find the missing number from range 1..n+1
        long missing = 0;

        System.out.println(missing);
    }
}""",
        },
        "tests": [
            {"input": "5\n1 2 4 5 6", "expected": "3", "hidden": False},
        ],
        "samples": [0],
    },

    # 3017. First K Words
    {
        "id": 3017,
        "slug": "first-k-words",
        "title": "First K Words",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a sentence and an integer <code>k</code>, print the first <code>k</code> words of the
sentence, space-separated. If <code>k</code> is greater than or equal to the number of words, print
the whole sentence unchanged (trimmed).</p>
<h3>Input format:</h3>
<p>Line 1: the sentence. Line 2: <code>k</code>.</p>
<h3>Example:</h3>
<pre>Input:                              Output:
Hello I am a passionate developer   Hello I am a
4</pre>
""",
        "hint": "Split the sentence on whitespace and join the first k tokens with single spaces.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        int k = Integer.parseInt(sc.nextLine().trim());

        // TODO: print the first k words of line, space separated
        System.out.println(line.trim());
    }
}""",
        },
        "tests": [
            {"input": "Hello I am a passionate developer\n4", "expected": "Hello I am a", "hidden": False},
        ],
        "samples": [0],
    },

    # 3018. Floyd's Triangle
    {
        "id": 3018,
        "slug": "floyds-triangle",
        "title": "Floyd's Triangle",
        "difficulty": "Easy",
        "topics": [T, "Math", "Patterns"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Print Floyd's Triangle with <code>n</code> rows: row <code>i</code> (1-indexed) contains
<code>i</code> numbers, continuing a running counter that starts at 1. Numbers in a row are
space-separated, and each row is on its own line.</p>
<h3>Input format:</h3>
<p>A single integer <code>n</code>.</p>
<h3>Example:</h3>
<pre>Input: 4        Output:
                 1
                 2 3
                 4 5 6
                 7 8 9 10</pre>
""",
        "hint": "Keep a running counter starting at 1. For row i, print i numbers from the counter, incrementing it each time.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: print Floyd's triangle with n rows
        System.out.println();
    }
}""",
        },
        "tests": [
            {"input": "4", "expected": "1\n2 3\n4 5 6\n7 8 9 10", "hidden": False},
        ],
        "samples": [0],
        "io_style": "lines",
    },

    # 3019. Googly Prime Number
    {
        "id": 3019,
        "slug": "googly-prime-number",
        "title": "Googly Prime Number",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>A number is called "googly prime" if the sum of its digits is a prime number. Given an integer,
print <code>YES</code> if it is a googly prime, otherwise print <code>NO</code>.</p>
<h3>Input format:</h3>
<p>A single integer.</p>
<h3>Example:</h3>
<pre>Input:      Output:
43          YES</pre>
<p>Explanation: 4+3 = 7, which is prime.</p>
""",
        "hint": "Sum the digits, then check if the sum is prime with a simple trial-division check up to sqrt(sum).",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: sum digits of n, print YES if the sum is prime, else NO
        System.out.println("NO");
    }
}""",
        },
        "tests": [
            {"input": "43", "expected": "YES", "hidden": False},
            {"input": "123", "expected": "NO", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3020. Intersection of Two Arrays
    {
        "id": 3020,
        "slug": "intersection-of-two-arrays",
        "title": "Intersection of Two Sorted Arrays",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Two Pointers"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given two arrays that are already sorted in non-decreasing order, print their intersection
(matching elements found via a two-pointer merge scan — duplicates are included exactly as many
times as the two-pointer walk matches them), space-separated.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n1</code>. Line 2: <code>n1</code> sorted integers. Line 3: <code>n2</code>. Line 4:
<code>n2</code> sorted integers.</p>
<h3>Example:</h3>
<pre>Input:              Output:
5                   2 2 3
1 2 2 3 4
4
2 2 3 5</pre>
""",
        "hint": "Use two pointers i, j starting at 0. If arr1[i]==arr2[j] add it and advance both; if arr1[i]<arr2[j] advance i; else advance j.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int[] a1 = new int[n1];
        for (int i = 0; i < n1; i++) a1[i] = sc.nextInt();
        int n2 = sc.nextInt();
        int[] a2 = new int[n2];
        for (int i = 0; i < n2; i++) a2[i] = sc.nextInt();

        // TODO: two-pointer intersection of the two sorted arrays
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString().trim());
    }
}""",
        },
        "tests": [
            {"input": "5\n1 2 2 3 4\n4\n2 2 3 5", "expected": "2 2 3", "hidden": False},
        ],
        "samples": [0],
    },

    # 3021. Large Small Sum
    {
        "id": 3021,
        "slug": "large-small-sum",
        "title": "Large Small Sum",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Sorting"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an array (with all unique elements), split it into the elements at even 0-indexed positions
and the elements at odd 0-indexed positions. Print the sum of the <b>2nd-largest</b> element among the
even-position group and the <b>2nd-smallest</b> element among the odd-position group.</p>
<p>If the array has 3 or fewer elements (or is empty), print <code>0</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
6                       7
3 2 1 7 5 4</pre>
<p>Explanation: even positions (0,2,4) = [3,1,5], sorted [1,3,5], 2nd largest = 3. Odd positions
(1,3,5) = [2,7,4], sorted [2,4,7], 2nd smallest = 4. Sum = 3 + 4 = 7.</p>
""",
        "hint": "Split by index parity into two lists, sort each ascending. 2nd largest of the even list is at index size-2; 2nd smallest of the odd list is at index 1.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: 2nd largest of even-index elements + 2nd smallest of odd-index elements
        int result = (n <= 3) ? 0 : 0;

        System.out.println(result);
    }
}""",
        },
        "tests": [
            {"input": "6\n3 2 1 7 5 4", "expected": "7", "hidden": False},
            {"input": "7\n1 8 0 2 3 5 6", "expected": "8", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3022. Length of Last Word
    {
        "id": 3022,
        "slug": "length-of-last-word",
        "title": "Length of Last Word",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a string possibly containing multiple/leading/trailing spaces, print the length of the
<b>last</b> word.</p>
<h3>Input format:</h3>
<p>A single line containing the string.</p>
<h3>Example:</h3>
<pre>Input: " I am  a passionate   Developer  "     Output: 9</pre>
""",
        "hint": "Trim the string, split on one-or-more whitespace characters, and take the length of the last resulting token.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        // TODO: find the length of the last word in s
        int length = 0;

        System.out.println(length);
    }
}""",
        },
        "tests": [
            {"input": " I am  a passionate   Developer  ", "expected": "9", "hidden": False},
        ],
        "samples": [0],
    },

    # 3023. Linked List Palindrome
    {
        "id": 3023,
        "slug": "linked-list-palindrome",
        "title": "Linked List Palindrome",
        "difficulty": "Easy",
        "topics": [T, "Linked List"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given <code>n</code> values used to build a singly linked list in order, print <code>true</code>
if the list is a palindrome, otherwise print <code>false</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers (the list values, head to tail).</p>
<h3>Example:</h3>
<pre>Input:          Output:
4               true
1 2 2 1</pre>
""",
        "hint": "Build the linked list, then walk it collecting values into a list, and check the value list reads the same forwards and backwards.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    static class Node { int val; Node next; Node(int v) { val = v; } }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Node head = null, tail = null;
        for (int i = 0; i < n; i++) {
            int v = sc.nextInt();
            Node node = new Node(v);
            if (head == null) { head = node; tail = node; }
            else { tail.next = node; tail = node; }
        }

        // TODO: check if the linked list starting at head is a palindrome
        boolean isPalindrome = false;

        System.out.println(isPalindrome);
    }
}""",
        },
        "tests": [
            {"input": "4\n1 2 2 1", "expected": "true", "hidden": False},
        ],
        "samples": [0],
    },

    # 3024. Longest Substring Without Repeating Characters
    {
        "id": 3024,
        "slug": "longest-substring-without-repeat",
        "title": "Longest Substring Without Repeating Characters",
        "difficulty": "Medium",
        "topics": [T, "Strings", "Sliding Window", "Hash Table"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a string <code>s</code>, find the length of the longest substring without repeating
characters.</p>
<h3>Input format:</h3>
<p>A single line containing <code>s</code>.</p>
<h3>Example:</h3>
<pre>Input: abcabcbb     Output: 3</pre>
""",
        "hint": "Use a sliding window with a set of characters currently in the window: expand the right edge, and shrink the left edge whenever you'd introduce a duplicate.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        // TODO: length of the longest substring of s without repeating characters
        int maxLen = 0;

        System.out.println(maxLen);
    }
}""",
        },
        "tests": [
            {"input": "abcabcbb", "expected": "3", "hidden": False},
        ],
        "samples": [0],
    },

    # 3025. Longest Word
    {
        "id": 3025,
        "slug": "longest-word",
        "title": "Longest Word in a Sentence",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a line of space-separated words, print the longest one in the exact format
<code>The longest string is: &lt;word&gt;</code>.</p>
<h3>Input format:</h3>
<p>A single line of words.</p>
<h3>Example:</h3>
<pre>Input: yes no number     Output: The longest string is: number</pre>
""",
        "hint": "Split on whitespace, then scan for the word with the maximum length.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();

        // TODO: find the longest word in line
        String longest = "";

        System.out.println("The longest string is: " + longest);
    }
}""",
        },
        "tests": [
            {"input": "yes no number", "expected": "The longest string is: number", "hidden": False},
        ],
        "samples": [0],
    },

    # 3026. Magical Numbers
    {
        "id": 3026,
        "slug": "magical-numbers",
        "title": "Count Magical Numbers",
        "difficulty": "Medium",
        "topics": [T, "Math", "Bit Manipulation"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>For a number, count how many even bits (i.e. 0-bits) appear in its binary representation. The
number is "magical" if that count of 0-bits is odd. Given <code>N</code>, print the count of magical
numbers in <code>[1, N]</code>.</p>
<h3>Input format:</h3>
<p>A single integer <code>N</code>.</p>
<h3>Example:</h3>
<pre>Input: 5     Output: 2</pre>
""",
        "hint": "For each number from 1 to N, count how many of its binary digits are 0 (using repeated division by 2), and check if that count is odd.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: count numbers in [1,n] whose binary form has an odd count of 0-bits
        int count = 0;

        System.out.println(count);
    }
}""",
        },
        "tests": [
            {"input": "5", "expected": "2", "hidden": False},
        ],
        "samples": [0],
    },

    # 3027. Matrix Even Odd Split Sum
    {
        "id": 3027,
        "slug": "matrix-even-odd-split-sum",
        "title": "Even/Odd Position Split Sum",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Sorting"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an array, split it into elements at even 0-indexed positions and elements at odd 0-indexed
positions. Sort each group ascending, then print the sum of the <b>2nd-largest</b> element of each
group.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:              Output:
5                   7
3 4 1 7 9</pre>
<p>Explanation: even positions [3,1,9] sorted [1,3,9], 2nd largest = 3. Odd positions [4,7] sorted
[4,7], 2nd largest = 4. Sum = 7.</p>
""",
        "hint": "Split by index parity, sort each list ascending, and take the element at index size-2 (the 2nd largest) from each.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: 2nd-largest of even-index elements + 2nd-largest of odd-index elements
        int result = 0;

        System.out.println(result);
    }
}""",
        },
        "tests": [
            {"input": "5\n3 4 1 7 9", "expected": "7", "hidden": False},
        ],
        "samples": [0],
    },

    # 3028. Max Exponent
    {
        "id": 3028,
        "slug": "max-exponent-range",
        "title": "Maximum Power-of-2 Exponent in Range",
        "difficulty": "Easy",
        "topics": [T, "Math", "Bit Manipulation"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a range <code>[a, b]</code> inclusive, find the number whose largest power-of-2 divisor has
the greatest exponent (i.e. the number with the most trailing factors of 2). On a tie, print the
smallest such number.</p>
<h3>Input format:</h3>
<p>A single line: <code>a b</code>.</p>
<h3>Example:</h3>
<pre>Input: 7 12     Output: 8</pre>
""",
        "hint": "For each number in [a,b], repeatedly divide by 2 while it's even, counting how many times you can. Track the number with the largest such count.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        // TODO: find the number in [a,b] with the largest power-of-2 exponent dividing it
        int best = a;

        System.out.println(best);
    }
}""",
        },
        "tests": [
            {"input": "7 12", "expected": "8", "hidden": False},
        ],
        "samples": [0],
    },

    # 3029. Max Favourite Song
    {
        "id": 3029,
        "slug": "max-favourite-song",
        "title": "Max Favourite Song",
        "difficulty": "Medium",
        "topics": [T, "Strings", "Sliding Window"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a string <code>S</code> and integer <code>K</code>, find the maximum number of occurrences
of the character <code>'a'</code> within any substring of <code>S</code> of length exactly
<code>K</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>S</code>. Line 2: <code>K</code>.</p>
<h3>Example:</h3>
<pre>Input:          Output:
acdbaaca        2
3</pre>
""",
        "hint": "Use a sliding window of size K: maintain a running count of 'a' characters in the window, adding the incoming character and removing the outgoing one as the window slides.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int k = Integer.parseInt(sc.nextLine().trim());

        // TODO: max count of 'a' in any window of length k
        int max = 0;

        System.out.println(max);
    }
}""",
        },
        "tests": [
            {"input": "acdbaaca\n3", "expected": "2", "hidden": False},
        ],
        "samples": [0],
    },

    # 3030. Maximum and Its Index
    {
        "id": 3030,
        "slug": "maximum-and-its-index",
        "title": "Maximum Element and Its Index",
        "difficulty": "Easy",
        "topics": [T, "Arrays"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an array, print its maximum value on one line, then its (0-indexed) index on the next
line.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                                  Output:
10                                      86
23 45 82 27 66 12 78 13 71 86          9</pre>
""",
        "hint": "Track the maximum value and its index while scanning the array once.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: find the max value and its index
        int maxVal = 0, maxIdx = 0;

        System.out.println(maxVal);
        System.out.println(maxIdx);
    }
}""",
        },
        "tests": [
            {"input": "10\n23 45 82 27 66 12 78 13 71 86", "expected": "86\n9", "hidden": False},
        ],
        "samples": [0],
        "io_style": "lines",
    },

    # 3031. Maximum With Index Format
    {
        "id": 3031,
        "slug": "maximum-with-index-format",
        "title": "Maximum With Index (Tuple Format)",
        "difficulty": "Easy",
        "topics": [T, "Arrays"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an array, find its maximum value and index, and print them formatted exactly as
<code>(max,index)</code> with no spaces.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:          Output:
5               (9,3)
1 8 4 9 6</pre>
""",
        "hint": "Track the max value and its index while scanning, then print \"(\" + max + \",\" + index + \")\" with no spaces.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: find the max value and its index, print as (max,index)
        int maxVal = 0, maxIdx = 0;

        System.out.println("(" + maxVal + "," + maxIdx + ")");
    }
}""",
        },
        "tests": [
            {"input": "5\n1 8 4 9 6", "expected": "(9,3)", "hidden": False},
        ],
        "samples": [0],
    },

    # 3032. Merge Sorted Arrays
    {
        "id": 3032,
        "slug": "merge-sorted-arrays",
        "title": "Merge Two Sorted Arrays",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Sorting", "Two Pointers"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given two arrays, each already sorted individually, print the merged sorted array, space
separated.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n1</code>. Line 2: <code>n1</code> sorted integers. Line 3: <code>n2</code>. Line 4:
<code>n2</code> sorted integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
5                       1 2 2 3 4 4 5 6 8 10
1 2 3 4 5
5
2 4 6 8 10</pre>
""",
        "hint": "Standard merge step from merge sort: use two pointers, always taking the smaller of the two current elements.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int[] a1 = new int[n1];
        for (int i = 0; i < n1; i++) a1[i] = sc.nextInt();
        int n2 = sc.nextInt();
        int[] a2 = new int[n2];
        for (int i = 0; i < n2; i++) a2[i] = sc.nextInt();

        // TODO: merge a1 and a2 into one sorted array
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString().trim());
    }
}""",
        },
        "tests": [
            {"input": "5\n1 2 3 4 5\n5\n2 4 6 8 10", "expected": "1 2 2 3 4 4 5 6 8 10", "hidden": False},
        ],
        "samples": [0],
    },

    # 3033. Most Frequent Vowel
    {
        "id": 3033,
        "slug": "most-frequent-vowel",
        "title": "Most Frequent Vowel",
        "difficulty": "Easy",
        "topics": [T, "Strings", "Hash Table"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a string, find the lowercase vowel (a, e, i, o, u) that occurs most frequently. You may
assume a unique most-frequent vowel exists.</p>
<h3>Input format:</h3>
<p>Line 1: length of the string (may be ignored). Line 2: the string.</p>
<h3>Example:</h3>
<pre>Input:      Output:
6           a
xyuaab</pre>
""",
        "hint": "Count occurrences of each of a,e,i,o,u and print the one with the highest count.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.nextLine();
        String s = sc.nextLine();

        // TODO: find the most frequent vowel in s
        char best = '?';

        System.out.println(best);
    }
}""",
        },
        "tests": [
            {"input": "6\nxyuaab", "expected": "a", "hidden": False},
        ],
        "samples": [0],
    },

    # 3034. Move Hyphens to Front
    {
        "id": 3034,
        "slug": "move-hyphens-to-front",
        "title": "Move Hyphens to Front",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a string containing letters and hyphens, move all hyphens to the front of the string,
preserving the relative order of the remaining characters.</p>
<h3>Input format:</h3>
<p>A single line containing the string.</p>
<h3>Example:</h3>
<pre>Input: Move-Hyphens-to-Front     Output: ---MoveHyphenstoFront</pre>
""",
        "hint": "Split the characters into two buffers as you scan: one for hyphens, one for everything else, then concatenate hyphens first.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        // TODO: move all '-' characters to the front, preserving order of the rest
        System.out.println(s);
    }
}""",
        },
        "tests": [
            {"input": "Move-Hyphens-to-Front", "expected": "---MoveHyphenstoFront", "hidden": False},
            {"input": "String-Compare", "expected": "-StringCompare", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3035. Negative Stock Price Days
    {
        "id": 3035,
        "slug": "negative-stock-price-days",
        "title": "Days With a Price Decrease",
        "difficulty": "Easy",
        "topics": [T, "Arrays"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an array of daily closing stock prices, count the number of days where the price decreased
from the previous day.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
6                       2
2 3 1 4 5 2</pre>
""",
        "hint": "Compare each element with the previous one and count strict decreases.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: count days where arr[i+1] < arr[i]
        int count = 0;

        System.out.println(count);
    }
}""",
        },
        "tests": [
            {"input": "6\n2 3 1 4 5 2", "expected": "2", "hidden": False},
            {"input": "1\n6", "expected": "0", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3036. Operation Choices
    {
        "id": 3036,
        "slug": "operation-choices",
        "title": "Operation Choices",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given three integers <code>c</code>, <code>a</code>, <code>b</code>, compute a result based on
<code>c</code>: if <code>c=1</code> print <code>a+b</code>, if <code>c=2</code> print
<code>a-b</code>, if <code>c=3</code> print <code>a*b</code>, if <code>c=4</code> print
<code>a/b</code> (integer division).</p>
<h3>Input format:</h3>
<p>Line 1: <code>c</code>. Line 2: <code>a</code>. Line 3: <code>b</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
1           28
12
16</pre>
""",
        "hint": "Use a switch/if-else on c to select the operation.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();

        // TODO: apply the operation selected by c (1=+, 2=-, 3=*, 4=/)
        int result = 0;

        System.out.println(result);
    }
}""",
        },
        "tests": [
            {"input": "1\n12\n16", "expected": "28", "hidden": False},
            {"input": "2\n16\n20", "expected": "-4", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3037. Pair Sum Max Product
    {
        "id": 3037,
        "slug": "pair-sum-max-product",
        "title": "Pair Sum With Maximum Product",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Two Pointers"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an array and a target sum, find the pair of elements <code>(x, y)</code> with
<code>x + y == target</code> that has the <b>maximum product</b>. Print the pair formatted as
<code>[larger, smaller]</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers. Line 3: <code>target</code>.</p>
<h3>Example:</h3>
<pre>Input:                          Output:
8                               [10, 8]
11 1 2 8 10 11 15 7
18</pre>
""",
        "hint": "Check every pair (i, j) with i != j; among those summing to target, keep the one with the highest product, printing the larger value first.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int target = sc.nextInt();

        // TODO: find the pair summing to target with the maximum product
        int bestX = 0, bestY = 0;

        System.out.println("[" + bestX + ", " + bestY + "]");
    }
}""",
        },
        "tests": [
            {"input": "8\n11 1 2 8 10 11 15 7\n18", "expected": "[10, 8]", "hidden": False},
        ],
        "samples": [0],
    },

    # 3038. Password Checker
    {
        "id": 3038,
        "slug": "password-checker-accenture",
        "title": "Password Validity Checker",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a candidate password string, print <code>1</code> if it is valid, otherwise print
<code>0</code>. A password is valid if:</p>
<ul>
  <li>its length is at least 4</li>
  <li>it contains at least one digit</li>
  <li>it contains at least one uppercase letter</li>
  <li>it contains no space and no <code>/</code> character</li>
  <li>it does not start with a digit</li>
</ul>
<h3>Input format:</h3>
<p>A single line containing the password (may contain spaces).</p>
<h3>Example:</h3>
<pre>Input: aA1_67           Output: 1
Input: a987 abC012       Output: 0  (contains a space)</pre>
""",
        "hint": "Scan the characters tracking whether a digit and an uppercase letter were seen, and whether a space or '/' appears; also check the first character isn't a digit.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        // TODO: validate the password per the stated rules
        boolean valid = false;

        System.out.println(valid ? 1 : 0);
    }
}""",
        },
        "tests": [
            {"input": "aA1_67", "expected": "1", "hidden": False},
            {"input": "a987 abC012", "expected": "0", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3039. Print Even Odd Labels
    {
        "id": 3039,
        "slug": "print-even-odd-labels",
        "title": "Label Array Elements Even/Odd",
        "difficulty": "Easy",
        "topics": [T, "Arrays"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an array, print <code>"odd"</code> or <code>"even"</code> for each element in order,
space-separated.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
6                       odd even odd even odd even
1 2 3 4 5 6</pre>
""",
        "hint": "For each element, append \"even\" or \"odd\" to a result buffer based on arr[i] % 2.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: label each element "odd" or "even", space separated
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString().trim());
    }
}""",
        },
        "tests": [
            {"input": "6\n1 2 3 4 5 6", "expected": "odd even odd even odd even", "hidden": False},
        ],
        "samples": [0],
    },

    # 3040. Product of Two Smallest
    {
        "id": 3040,
        "slug": "product-of-two-smallest",
        "title": "Product of Two Smallest Elements",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Sorting"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a target <code>sum</code> and an array, find the two smallest elements of the array. If
their sum is <code>&lt;= sum</code>, print their product; otherwise print <code>0</code>. If the
array has fewer than 2 elements, print <code>-1</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>sum</code>. Line 2: <code>n</code>. Line 3: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                      Output:
9                           2
7
5 2 4 3 9 7 1</pre>
""",
        "hint": "Sort a copy of the array; the two smallest are at index 0 and 1. Compare their sum to the given sum parameter before deciding what to print.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = sc.nextInt();
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: product of the two smallest elements if their sum <= sum, else 0 (or -1 if n<2)
        int result = (n < 2) ? -1 : 0;

        System.out.println(result);
    }
}""",
        },
        "tests": [
            {"input": "9\n7\n5 2 4 3 9 7 1", "expected": "2", "hidden": False},
            {"input": "4\n6\n9 8 3 -7 3 9", "expected": "-21", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3041. Rat Count House
    {
        "id": 3041,
        "slug": "rat-food-count-house",
        "title": "Houses Needed to Feed the Rats",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Greedy"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>There are <code>r</code> rats, each needing <code>unit</code> food. An array gives the food
available at each house, in order. Find the minimum number of houses (starting from the first) whose
cumulative food is enough to feed all the rats. If it's never enough, print <code>0</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>r</code>. Line 2: <code>unit</code>. Line 3: <code>n</code> (number of houses). Line 4:
<code>n</code> space-separated integers (food per house).</p>
<h3>Example:</h3>
<pre>Input:                      Output:
7                           4
2
8
2 8 3 5 7 4 1 2</pre>
""",
        "hint": "Compute the total food needed as r*unit, then accumulate food house by house until the running total reaches that need, counting how many houses were used.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        int unit = sc.nextInt();
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: min number of houses (from the start) whose cumulative food >= r*unit, else 0
        int houses = 0;

        System.out.println(houses);
    }
}""",
        },
        "tests": [
            {"input": "7\n2\n8\n2 8 3 5 7 4 1 2", "expected": "4", "hidden": False},
        ],
        "samples": [0],
    },

    # 3042. Rearrangement of Bits
    {
        "id": 3042,
        "slug": "rearrangement-of-bits",
        "title": "Rearrangement of Bits for Minimum Value",
        "difficulty": "Easy",
        "topics": [T, "Bit Manipulation", "Math"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a positive integer <code>N</code>, rearrange its binary bits so that all the set (1) bits
are moved to the least-significant end, forming the smallest possible resulting decimal value. Print
that minimum value.</p>
<h3>Input format:</h3>
<p>A single integer <code>N</code>.</p>
<h3>Example:</h3>
<pre>Input: 10     Output: 3</pre>
<p>Explanation: 10 = 1010 in binary, which has two set bits. The minimum arrangement is 0011 = 3.</p>
""",
        "hint": "Count the set bits c of N. The minimum value with c set bits, all packed at the low end, is (1 << c) - 1.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: count set bits c, print (1<<c) - 1
        int result = 0;

        System.out.println(result);
    }
}""",
        },
        "tests": [
            {"input": "10", "expected": "3", "hidden": False},
            {"input": "2", "expected": "1", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3043. Repeat a String
    {
        "id": 3043,
        "slug": "repeat-a-string",
        "title": "Repeat a String N Times",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an integer <code>N</code> and a string <code>S</code>, print <code>S</code> repeated
<code>N</code> times, concatenated with no separator.</p>
<h3>Input format:</h3>
<p>Line 1: <code>N</code>. Line 2: <code>S</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
3           abcabcabc
abc</pre>
""",
        "hint": "Use a StringBuilder and append S in a loop N times.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine().trim());
        String s = sc.nextLine();

        // TODO: repeat s, n times, concatenated
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString());
    }
}""",
        },
        "tests": [
            {"input": "3\nabc", "expected": "abcabcabc", "hidden": False},
        ],
        "samples": [0],
    },

    # 3044. Replace Character
    {
        "id": 3044,
        "slug": "replace-character",
        "title": "Swap Two Characters in a String",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a lowercase string and two characters <code>ch1</code>, <code>ch2</code>, simultaneously
swap every occurrence of <code>ch1</code> with <code>ch2</code> and every occurrence of
<code>ch2</code> with <code>ch1</code> in the original string. Print the transformed string.</p>
<h3>Input format:</h3>
<p>Line 1: the string. Line 2: <code>ch1</code>. Line 3: <code>ch2</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
apples      paales
a
p</pre>
""",
        "hint": "For each character c in the string: if c==ch1 output ch2; else if c==ch2 output ch1; else output c unchanged. This must be a simultaneous swap, not sequential replacement.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        char ch1 = sc.nextLine().trim().charAt(0);
        char ch2 = sc.nextLine().trim().charAt(0);

        // TODO: simultaneously swap ch1 and ch2 throughout s
        System.out.println(s);
    }
}""",
        },
        "tests": [
            {"input": "apples\na\np", "expected": "paales", "hidden": False},
        ],
        "samples": [0],
    },

    # 3045. Replace Most Frequent Character
    {
        "id": 3045,
        "slug": "replace-most-frequent-character",
        "title": "Replace the Most Frequent Character",
        "difficulty": "Easy",
        "topics": [T, "Strings", "Hash Table"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a string and a replacement character <code>c</code>, find the single most frequent
character in the string and replace <b>all</b> its occurrences with <code>c</code>. Print the
resulting string.</p>
<h3>Input format:</h3>
<p>Line 1: the string. Line 2: the replacement character.</p>
<h3>Example:</h3>
<pre>Input:              Output:
bbadbbababb         ttadttatatt
t</pre>
""",
        "hint": "Count character frequencies with a hash map, find the character with the highest count, then use String.replace to substitute it everywhere.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        char repl = sc.nextLine().trim().charAt(0);

        // TODO: replace the most frequent character in s with repl
        System.out.println(s);
    }
}""",
        },
        "tests": [
            {"input": "bbadbbababb\nt", "expected": "ttadttatatt", "hidden": False},
        ],
        "samples": [0],
    },

    # 3046. Reverse String
    {
        "id": 3046,
        "slug": "reverse-string-accenture",
        "title": "Reverse a String",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a string, print it reversed.</p>
<h3>Input format:</h3>
<p>A single line containing the string.</p>
<h3>Example:</h3>
<pre>Input: hello     Output: olleh</pre>
""",
        "hint": "Use StringBuilder's reverse() method, or build the reversed string manually from the last character to the first.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        // TODO: reverse s
        System.out.println(s);
    }
}""",
        },
        "tests": [
            {"input": "hello", "expected": "olleh", "hidden": False},
        ],
        "samples": [0],
    },

    # 3047. Reverse Words in a String
    {
        "id": 3047,
        "slug": "reverse-words-in-a-string",
        "title": "Reverse Words in a String",
        "difficulty": "Easy",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a line of space-separated words, reverse the order of the words (not the letters within
each word), and print the result space-separated.</p>
<h3>Input format:</h3>
<p>A single line of words.</p>
<h3>Example:</h3>
<pre>Input: Hello World     Output: World Hello</pre>
""",
        "hint": "Split the line on whitespace, then join the resulting words back together in reverse order.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();

        // TODO: reverse the order of the words in line
        System.out.println(line);
    }
}""",
        },
        "tests": [
            {"input": "Hello World", "expected": "World Hello", "hidden": False},
        ],
        "samples": [0],
    },

    # 3048. Roots of a Quadratic Equation
    {
        "id": 3048,
        "slug": "roots-of-quadratic-equation",
        "title": "Roots of a Quadratic Equation",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given coefficients <code>a</code>, <code>b</code>, <code>c</code> of the quadratic equation
<code>ax^2 + bx + c = 0</code> (assume the discriminant is non-negative), print its two real roots,
each rounded to 2 decimal places, separated by a space, with the "+" root first.</p>
<h3>Input format:</h3>
<p>A single line: <code>a b c</code>.</p>
<h3>Example:</h3>
<pre>Input: 1 -3 2     Output: 2.00 1.00</pre>
""",
        "hint": "Use the quadratic formula: root = (-b +/- sqrt(b^2 - 4ac)) / (2a). Print the plus root first, then the minus root, each formatted with two decimals.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();

        // TODO: compute the two roots using the quadratic formula
        double root1 = 0.0, root2 = 0.0;

        System.out.printf("%.2f %.2f%n", root1, root2);
    }
}""",
        },
        "tests": [
            {"input": "1 -3 2", "expected": "2.00 1.00", "hidden": False},
        ],
        "samples": [0],
    },

    # 3049. Rotate Array by K
    {
        "id": 3049,
        "slug": "rotate-array-by-k",
        "title": "Rotate Array by K Steps",
        "difficulty": "Easy",
        "topics": [T, "Arrays"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an array and an integer <code>k</code>, rotate the array to the right by <code>k</code>
steps and print the result, space-separated.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers. Line 3: <code>k</code>.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
7                       5 6 7 1 2 3 4
1 2 3 4 5 6 7
3</pre>
""",
        "hint": "Each element at index i moves to index (i+k) mod n in the result array. Remember to take k modulo n first.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();
        int k = sc.nextInt();

        // TODO: rotate arr to the right by k steps
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString().trim());
    }
}""",
        },
        "tests": [
            {"input": "7\n1 2 3 4 5 6 7\n3", "expected": "5 6 7 1 2 3 4", "hidden": False},
        ],
        "samples": [0],
    },

    # 3050. Second Largest Distinct Element
    {
        "id": 3050,
        "slug": "second-largest-distinct-element",
        "title": "Second Largest Distinct Element",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Sorting"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an array, find the second-largest <b>distinct</b> value.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
7                       6
1 3 5 2 4 6 8</pre>
""",
        "hint": "Insert all values into a sorted set of unique values (e.g. TreeSet), then take the element just below the maximum.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: find the second-largest distinct value
        int result = 0;

        System.out.println(result);
    }
}""",
        },
        "tests": [
            {"input": "7\n1 3 5 2 4 6 8", "expected": "6", "hidden": False},
        ],
        "samples": [0],
    },

    # 3051. Set Zero Matrix
    {
        "id": 3051,
        "slug": "set-zero-matrix",
        "title": "Set Zero Matrix",
        "difficulty": "Medium",
        "topics": [T, "Matrix", "Arrays"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an <code>m x n</code> matrix, if any element is 0, set its entire row and column to 0
(using the original positions of the zeroes). Print the resulting matrix, one row per line,
space-separated.</p>
<h3>Input format:</h3>
<p>Line 1: rows. Line 2: cols. Then <code>rows</code> lines of <code>cols</code> space-separated
integers.</p>
<h3>Example:</h3>
<pre>Input:          Output:
3               1 0 1
3               0 0 0
1 1 1           1 0 1
1 0 1
1 1 1</pre>
""",
        "hint": "First record which rows and columns contain a 0 (without modifying the matrix while scanning). Then in a second pass, zero out any cell whose row or column was flagged.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rows = sc.nextInt();
        int cols = sc.nextInt();
        int[][] m = new int[rows][cols];
        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++) m[i][j] = sc.nextInt();

        // TODO: zero out entire row/column for every 0 found in the original matrix

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                sb.append(m[i][j]);
                if (j < cols - 1) sb.append(" ");
            }
            sb.append("\\n");
        }
        System.out.print(sb.toString().trim());
    }
}""",
        },
        "tests": [
            {"input": "3\n3\n1 1 1\n1 0 1\n1 1 1", "expected": "1 0 1\n0 0 0\n1 0 1", "hidden": False},
        ],
        "samples": [0],
        "io_style": "lines",
    },

    # 3052. Small Large Sum
    {
        "id": 3052,
        "slug": "small-large-sum",
        "title": "Small Large Sum",
        "difficulty": "Medium",
        "topics": [T, "Arrays", "Sorting"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an array (all unique elements), split it into elements at even 0-indexed positions and
elements at odd 0-indexed positions. Print the sum of the <b>2nd-largest</b> element of each group.
If the array has 3 or fewer elements (or is empty), print <code>0</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
6                       7
3 2 1 7 5 4</pre>
""",
        "hint": "Split by index parity, sort each group ascending, and take the element at index size-2 (2nd largest) from each group, then sum them.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: 2nd-largest of even-index elements + 2nd-largest of odd-index elements
        int result = (n <= 3) ? 0 : 0;

        System.out.println(result);
    }
}""",
        },
        "tests": [
            {"input": "6\n3 2 1 7 5 4", "expected": "7", "hidden": False},
            {"input": "7\n4 0 7 9 6 4 2", "expected": "10", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3053. Standard Deviation
    {
        "id": 3053,
        "slug": "standard-deviation",
        "title": "Population Standard Deviation",
        "difficulty": "Easy",
        "topics": [T, "Math", "Arrays"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a list of integers, print their population standard deviation, rounded to 2 decimal
places.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                          Output:
8                               2.00
2 4 4 4 5 5 7 9</pre>
""",
        "hint": "Standard deviation = sqrt(mean of squared deviations from the mean). Compute the mean first, then average the squared differences, then take the square root.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double[] arr = new double[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextDouble();

        // TODO: compute the population standard deviation
        double sd = 0.0;

        System.out.printf("%.2f%n", sd);
    }
}""",
        },
        "tests": [
            {"input": "8\n2 4 4 4 5 5 7 9", "expected": "2.00", "hidden": False},
        ],
        "samples": [0],
    },

    # 3054. String Decoder
    {
        "id": 3054,
        "slug": "string-decoder",
        "title": "Run-Length Binary String Decoder",
        "difficulty": "Medium",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a binary string (only '0's and '1's), each maximal run of consecutive '1's encodes one
uppercase letter: the letter's position in the alphabet equals the length of that run (one '1' =
'A', two '1's = 'B', etc.), and each run is terminated by a '0' or by the end of the string. Decode
the string into the resulting uppercase word.</p>
<h3>Input format:</h3>
<p>A single line containing the binary string.</p>
<h3>Example:</h3>
<pre>Input: 10110111     Output: ABC</pre>
<p>Explanation: "1" -> A, "11" -> B, "111" -> C.</p>
""",
        "hint": "Scan the string counting consecutive 1s; whenever you hit a 0 (or reach the end), convert the current run length into a letter ('A' + runLength - 1) and reset the counter.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        // TODO: decode s into an uppercase word per the run-length rule
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString());
    }
}""",
        },
        "tests": [
            {"input": "10110111", "expected": "ABC", "hidden": False},
        ],
        "samples": [0],
    },

    # 3055. Sum of Multiples of 3 and 5
    {
        "id": 3055,
        "slug": "sum-of-multiples-of-3-and-5",
        "title": "Sum of Multiples of 15 in a Range",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given <code>m</code> and <code>n</code>, print the sum of all numbers in <code>[m, n]</code>
inclusive that are divisible by both 3 and 5 (i.e. by 15).</p>
<h3>Input format:</h3>
<p>Line 1: <code>m</code>. Line 2: <code>n</code>.</p>
<h3>Example:</h3>
<pre>Input:      Output:
12          90
50</pre>
""",
        "hint": "Loop from m to n, summing every value divisible by 15.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();

        // TODO: sum values in [m,n] divisible by both 3 and 5
        long sum = 0;

        System.out.println(sum);
    }
}""",
        },
        "tests": [
            {"input": "12\n50", "expected": "90", "hidden": False},
            {"input": "100\n160", "expected": "510", "hidden": False},
        ],
        "samples": [0, 1],
    },

    # 3056. Sum of Binary Digits (popcount)
    {
        "id": 3056,
        "slug": "sum-of-binary-digits-popcount",
        "title": "Sum of Binary Digits",
        "difficulty": "Easy",
        "topics": [T, "Math", "Bit Manipulation"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an integer <code>n</code>, convert it to binary and print the sum of its binary digits
(i.e. the count of set bits).</p>
<h3>Input format:</h3>
<p>A single integer <code>n</code>.</p>
<h3>Example:</h3>
<pre>Input: 15     Output: 4</pre>
<p>Explanation: 15 in binary is 1111, whose digits sum to 4.</p>
""",
        "hint": "Repeatedly check the lowest bit (n & 1) and shift right, counting how many bits are 1.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: count the number of 1-bits in n's binary representation
        int count = 0;

        System.out.println(count);
    }
}""",
        },
        "tests": [
            {"input": "15", "expected": "4", "hidden": False},
        ],
        "samples": [0],
    },

    # 3057. Sum at Even Index After Reverse
    {
        "id": 3057,
        "slug": "sum-at-even-index-after-reverse",
        "title": "Sum at Even Index After Reversing",
        "difficulty": "Easy",
        "topics": [T, "Arrays"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an array, reverse it, then sum the elements at even (0-indexed) positions of the
<b>reversed</b> array.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                          Output:
6                               120
10 20 30 40 50 60</pre>
<p>Explanation: reversed = [60,50,40,30,20,10]. Even indices 0,2,4 hold 60,40,20, summing to 120.</p>
""",
        "hint": "Build the reversed array first (or index from the end), then sum every second element starting at index 0.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: reverse arr, then sum elements at even indices of the reversed array
        long sum = 0;

        System.out.println(sum);
    }
}""",
        },
        "tests": [
            {"input": "6\n10 20 30 40 50 60", "expected": "120", "hidden": False},
        ],
        "samples": [0],
    },

    # 3058. Sum of Divisors
    {
        "id": 3058,
        "slug": "sum-of-divisors",
        "title": "Sum of All Divisors",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a positive integer <code>N</code>, print the sum of all its positive divisors (including 1
and N itself).</p>
<h3>Input format:</h3>
<p>A single integer <code>N</code>.</p>
<h3>Example:</h3>
<pre>Input: 12     Output: 28</pre>
<p>Explanation: 1+2+3+4+6+12 = 28.</p>
""",
        "hint": "Loop i from 1 to N and add i to the sum whenever N % i == 0.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: sum all divisors of n from 1 to n
        long sum = 0;

        System.out.println(sum);
    }
}""",
        },
        "tests": [
            {"input": "12", "expected": "28", "hidden": False},
        ],
        "samples": [0],
    },

    # 3059. Sum of Primes Below N
    {
        "id": 3059,
        "slug": "sum-of-primes-below-n",
        "title": "Sum of Primes Below N",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an integer <code>N</code>, print the sum of all prime numbers strictly less than
<code>N</code>.</p>
<h3>Input format:</h3>
<p>A single integer <code>N</code>.</p>
<h3>Example:</h3>
<pre>Input: 10     Output: 17</pre>
<p>Explanation: 2+3+5+7 = 17.</p>
""",
        "hint": "For each number from 2 to N-1, check primality by trial division up to its square root, and sum the primes.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: sum all primes strictly less than n
        long sum = 0;

        System.out.println(sum);
    }
}""",
        },
        "tests": [
            {"input": "10", "expected": "17", "hidden": False},
        ],
        "samples": [0],
    },

    # 3060. Multiplication Table and Sum
    {
        "id": 3060,
        "slug": "multiplication-table-and-sum",
        "title": "Multiplication Table and Sum",
        "difficulty": "Easy",
        "topics": [T, "Math"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a number <code>n</code>, print its multiplication table from <code>n*1</code> through
<code>n*10</code> (space-separated) on one line, then the sum of those 10 multiples on the next
line.</p>
<h3>Input format:</h3>
<p>A single integer <code>n</code>.</p>
<h3>Example:</h3>
<pre>Input: 5     Output: 5 10 15 20 25 30 35 40 45 50
                      275</pre>
""",
        "hint": "Loop i from 1 to 10, computing n*i, appending it to the output line and adding it to a running sum. Print the sum on the next line.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: print n*1..n*10 space separated, then the sum on the next line
        System.out.println();
        System.out.println(0);
    }
}""",
        },
        "tests": [
            {"input": "5", "expected": "5 10 15 20 25 30 35 40 45 50\n275", "hidden": False},
            {"input": "12", "expected": "12 24 36 48 60 72 84 96 108 120\n660", "hidden": False},
        ],
        "samples": [0, 1],
        "io_style": "lines",
    },

    # 3061. Vowel Permutation Count
    {
        "id": 3061,
        "slug": "vowel-permutation-count",
        "title": "Vowel-Fixed Permutation Count",
        "difficulty": "Easy",
        "topics": [T, "Strings", "Math"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a string <code>S</code>, fix the positions of all vowels (A,E,I,O,U, either case) and count
the number of permutations formed by permuting only the remaining (non-vowel) characters, i.e. the
factorial of the non-vowel character count.</p>
<h3>Input format:</h3>
<p>A single line containing <code>S</code>.</p>
<h3>Example:</h3>
<pre>Input: ABC     Output: 2</pre>
<p>Explanation: A is the only vowel (fixed); B and C are non-vowels, permuting in 2! = 2 ways.</p>
""",
        "hint": "Count how many characters are NOT one of A,E,I,O,U,a,e,i,o,u, then compute that count's factorial.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        // TODO: factorial of the count of non-vowel characters in s
        long result = 1;

        System.out.println(result);
    }
}""",
        },
        "tests": [
            {"input": "ABC", "expected": "2", "hidden": False},
        ],
        "samples": [0],
    },

    # 3062. Most Frequent Vowel II
    {
        "id": 3062,
        "slug": "most-frequent-vowel-ii",
        "title": "Most Frequent Vowel II",
        "difficulty": "Easy",
        "topics": [T, "Strings", "Hash Table"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a string, find the lowercase vowel (a, e, i, o, u) that occurs most frequently. You may
assume a unique most-frequent vowel exists.</p>
<h3>Input format:</h3>
<p>Line 1: length of the string (may be ignored). Line 2: the string.</p>
<h3>Example:</h3>
<pre>Input:      Output:
7           a
xayuaba</pre>
""",
        "hint": "Count occurrences of each of a,e,i,o,u and print the one with the highest count.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.nextLine();
        String s = sc.nextLine();

        // TODO: find the most frequent vowel in s
        char best = '?';

        System.out.println(best);
    }
}""",
        },
        "tests": [
            {"input": "7\nxayuaba", "expected": "a", "hidden": False},
        ],
        "samples": [0],
    },

    # 3063. Fibonacci Series
    {
        "id": 3063,
        "slug": "fibonacci-series-n-terms",
        "title": "Print Fibonacci Series (N Terms)",
        "difficulty": "Easy",
        "topics": [T, "Math", "Patterns"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an integer <code>N</code>, print the first <code>N</code> terms of the Fibonacci series
(starting <code>0, 1, 1, 2, ...</code>), space-separated.</p>
<h3>Input format:</h3>
<p>A single integer <code>N</code> (number of terms).</p>
<h3>Example:</h3>
<pre>Input: 9     Output: 0 1 1 2 3 5 8 13 21</pre>
""",
        "hint": "Keep two running variables a=0, b=1; print a, then advance (a, b) = (b, a+b), repeating N times.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: print the first n Fibonacci numbers, space separated
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString().trim());
    }
}""",
        },
        "tests": [
            {"input": "9", "expected": "0 1 1 2 3 5 8 13 21", "hidden": False},
        ],
        "samples": [0],
    },

    # 3064. Max Difference Between Successive Elements
    {
        "id": 3064,
        "slug": "max-diff-successive-elements",
        "title": "Max Difference Between Successive Elements",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Sorting"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an integer array, sort it, and print the maximum difference between two consecutive
elements in the sorted array. If the array has fewer than 2 elements, print <code>0</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:              Output:
4                   3
3 6 9 1</pre>
""",
        "hint": "Sort the array, then scan adjacent pairs tracking the largest gap.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: sort arr, find the max difference between consecutive elements
        int maxDiff = 0;

        System.out.println(maxDiff);
    }
}""",
        },
        "tests": [
            {"input": "4\n3 6 9 1", "expected": "3", "hidden": False},
        ],
        "samples": [0],
    },

    # 3065. Nth Fibonacci Number
    {
        "id": 3065,
        "slug": "nth-fibonacci-number",
        "title": "Nth Fibonacci Number",
        "difficulty": "Easy",
        "topics": [T, "Math", "Dynamic Programming"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given <code>n</code>, print the <code>n</code>-th Fibonacci number (0-indexed: fib(0)=0,
fib(1)=1, fib(2)=1, ...).</p>
<h3>Input format:</h3>
<p>A single integer <code>n</code>.</p>
<h3>Example:</h3>
<pre>Input: 9     Output: 34</pre>
""",
        "hint": "Iteratively build up fib values from fib(0) and fib(1) to fib(n) using a simple loop; avoid plain recursion to prevent excessive recomputation.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // TODO: compute the n-th Fibonacci number (fib(0)=0, fib(1)=1)
        long result = 0;

        System.out.println(result);
    }
}""",
        },
        "tests": [
            {"input": "9", "expected": "34", "hidden": False},
        ],
        "samples": [0],
    },

    # 3066. Remove Duplicates from Array
    {
        "id": 3066,
        "slug": "remove-duplicates-preserve-order",
        "title": "Remove Duplicates, Preserve Order",
        "difficulty": "Easy",
        "topics": [T, "Arrays", "Hash Table"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given an array of integers, remove duplicate values, keeping only the first occurrence of each
value and preserving the original relative order. Print the result space-separated.</p>
<h3>Input format:</h3>
<p>Line 1: <code>n</code>. Line 2: <code>n</code> space-separated integers.</p>
<h3>Example:</h3>
<pre>Input:                  Output:
7                       1 2 3 4 5
1 2 2 3 4 4 5</pre>
""",
        "hint": "Use an ordered set (e.g. LinkedHashSet) to collect values while preserving first-occurrence insertion order, then print its contents.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        // TODO: remove duplicates, preserving first-occurrence order
        StringBuilder sb = new StringBuilder();

        System.out.println(sb.toString().trim());
    }
}""",
        },
        "tests": [
            {"input": "7\n1 2 2 3 4 4 5", "expected": "1 2 3 4 5", "hidden": False},
        ],
        "samples": [0],
    },

    # 3067. Rhyme Words
    {
        "id": 3067,
        "slug": "rhyme-words",
        "title": "Best Rhyming Word",
        "difficulty": "Medium",
        "topics": [T, "Strings"],
        "judge": "server",
        "languages": ["java"],
        "description": """
<p>Given a target word <code>S</code> and a list of candidate words <code>D</code>, find the word in
<code>D</code> (excluding <code>S</code> itself if present) whose <b>suffix</b> matches <code>S</code>'s
suffix for the greatest number of characters (comparing from the end of each word backwards). Print
that best-matching word, or <code>No Word</code> if no candidate shares any suffix character with
<code>S</code>.</p>
<h3>Input format:</h3>
<p>Line 1: <code>S</code>. Line 2: the number of words in <code>D</code>. Line 3: the words of
<code>D</code>, space-separated.</p>
<h3>Example:</h3>
<pre>Input:                                          Output:
thunder                                         under
5
pukle thunder powder blender under</pre>
""",
        "hint": "For each candidate word (skipping one equal to S), compare characters from the end of both words backwards, counting how many match consecutively before the first mismatch. Track the candidate with the longest such run.",
        "boilerplate": {
            "java": """import java.util.*;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine().trim();
        int cnt = Integer.parseInt(sc.nextLine().trim());
        String[] d = sc.nextLine().trim().split("\\\\s+");

        // TODO: find the word in d (excluding s) with the longest matching suffix
        String best = "No Word";

        System.out.println(best);
    }
}""",
        },
        "tests": [
            {"input": "thunder\n5\npukle thunder powder blender under", "expected": "under", "hidden": False},
        ],
        "samples": [0],
    },
]
