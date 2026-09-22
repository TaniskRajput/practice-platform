"""Generates the 100-question Accenture pseudocode quiz (problem id 29).

Each question's stem, four options and answer index are inlined below
(originally parsed from Pseudocodes_Complete.pdf).  The pseudocode bodies
were images in the original PDF, so each question is presented with its
full stem and options; the answers follow the PDF's own answer key.
"""


PSEUDOCODE_QUESTIONS = [
    (
        "What will be the output of the following pseudocode for A = [4, 8, 15, 16, 23], n = 5?",
        ["8 4 16 15 23", "4 8 15 16 23", "8 4 15 16 23", "4 8 16 15 23"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for S = \"ACCENTURE\"?",
        ["2", "3", "4", "5"],
        2,
    ),
    (
        "What will be the output of the following pseudocode for x = 5, y = 3?",
        ["8", "11", "9", "13"],
        2,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["30,3", "40,2", "30,2", "40,3"],
        3,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["10,3", "15,3", "10,2", "15,2"],
        3,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["5", "8", "13", "6"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for array A = [_, 1, 2, 3, 4, 5, 6, 7] (1- indexed, index 0 unused), n = 7? (Left child of node i = 2i, Right child = 2i+1; a node is a leaf if 2i > n)",
        ["18", "28", "22", "15"],
        2,
    ),
    (
        "What will be the output of the following pseudocode for the adjacency matrix below (n = 4)?",
        ["5", "6", "4", "3"],
        2,
    ),
    (
        "What will be the output of the following pseudocode for A = [5, 3, 8, 4, 2], n = 5 (single pass only)?",
        ["3 5 4 2 8", "2 3 4 5 8", "3 4 5 2 8", "3 5 8 4 2"],
        0,
    ),
    (
        "What will be the index (0-based) returned by the following pseudocode for A = [2, 4, 6, 8, 10, 12, 14], target = 10?",
        ["-1", "5", "4", "3"],
        2,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["6 12", "7 12", "7 13", "6 13"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for matrix A (3x3)?",
        ["6", "24", "11", "15"],
        2,
    ),
    (
        "What will be the output of the following pseudocode for S = \"ABC\"?",
        ["CDE", "BCD", "DEF", "CDA"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for n = 13?",
        ["5", "4", "2", "3"],
        3,
    ),
    (
        "What will be the output of the following pseudocode for marks = 82?",
        ["A", "B", "C", "D"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for list 10 → 20 → 30 → 40 → NULL?",
        ["10 20 30 40", "40 30 20 10 NULL", "Error", "40 30 20 10"],
        3,
    ),
    (
        "What will be the output of the following pseudocode for A = [1, 2, 3, 2, 1, 4, 1]?",
        ["3", "4", "1", "2"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for n = 5?",
        ["5", "13", "8", "9"],
        2,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["9", "14", "6", "10"],
        3,
    ),
    (
        "What will be the output of the following pseudocode for postfix expression \"5 3 2 * +\"?",
        ["11", "16", "21", "13"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for a circular queue of capacity 3?",
        ["1,4", "2,4", "2,3", "1,3"],
        1,
    ),
    (
        "What will be the BFS traversal output starting from node 0 for the following adjacency list? 0: [1, 2] 1: [0, 3] 2: [0, 3] 3: [1, 2]",
        ["0 3 1 2", "0 1 2 3", "0 2 1 3", "0 1 3 2"],
        1,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["10", "8", "6", "24"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for A = [1, 2, 3, 4, 5], k = 2?",
        ["1 2 3 4 5", "4 5 1 2 3", "2 3 4 5 1", "3 4 5 1 2"],
        3,
    ),
    (
        "What will be the output of the following pseudocode for S = \"MALAYALAM\"?",
        ["true", "false", "error", "1"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for a = 15, b = 10?",
        ["10", "25", "5", "-5"],
        2,
    ),
    (
        "What will be the output of the following pseudocode for A = [-2, 3, -1, 4, -2, 5], n = 6?",
        ["9", "7", "5", "11"],
        0,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["15", "5", "10", "error"],
        1,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["14", "21", "28", "25"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for n = 16?",
        ["true", "false", "0", "Error"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for A = [1, 2, 3, 4, 2, 5, 1], n = 7?",
        ["1", "2", "5", "4"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for the binary tree below?",
        ["5", "2", "4", "3"],
        2,
    ),
    (
        "What will be the DFS traversal output starting from node 0 for the following adjacency list?",
        ["0 1 3 2", "0 1 2 3", "0 2 3 1", "0 3 1 2"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for coins = [1, 3, 4], amount = 6?",
        ["6", "4", "3", "2"],
        3,
    ),
    (
        "What will be the output of the following pseudocode for expr = \"{[()]}\"?",
        ["error", "false", "true", "empty"],
        2,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["4", "0", "7", "8"],
        3,
    ),
    (
        "What will be the output of the following pseudocode for A = [12, 35, 1, 10, 34, 1], n = 6?",
        ["10", "12", "34", "35"],
        2,
    ),
    (
        "What will be the output of the following pseudocode for S1 = \"LISTEN\", S2 = \"SILENT\"?",
        ["false", "true", "error", "empty"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for x = 20?",
        ["5", "40", "25", "45"],
        3,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["45", "120", "24", "60"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for matrix A (2x3)?",
        ["1 4 / 2 5 / 3 6", "1 2 3 / 4 5 6", "4 5 6 / 1 2 3", "3 2 1 / 6 5 4"],
        0,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["16", "30", "20", "25"],
        3,
    ),
    (
        "What will be the output of the following pseudocode for the BST below, searching for key = 45? (assume searching 45, which does not exist)",
        ["false", "true", "error", "NULL"],
        0,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["9", "12", "10", "1234"],
        2,
    ),
    (
        "What will be the output of the following pseudocode for a = 6, b = 9?",
        ["9 6", "6 9", "0 15", "15 0"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for A = [3, 7, 2, 7, 5, 7, 1], n = 7?",
        ["7,2", "7,3", "5,1", "7,4"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for S = \"PROGRAMMING\"?",
        ["PROGAMING", "PROGRAMING", "PROGAMIN", "PROGRAMMIN"],
        2,
    ),
    (
        "What will be the output of the following pseudocode for A = [4, 5, 2, 10, 8], n = 5 (find next greater for last element only)?",
        ["10", "8", "2", "6"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for Queue Q = [1, 2, 3, 4]?",
        ["1 2 3 4", "1 3 2 4", "4 1 3 2", "4 3 2 1"],
        3,
    ),
    (
        "What will be the output of the following pseudocode for the binary tree below?",
        ["6", "5", "7", "4"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for adjacency list (directed graph)?",
        ["true", "false", "error", "1"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for S1 = \"ABC\", S2 = \"AC\"?",
        ["0", "1", "2", "3"],
        2,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["25", "10", "16", "32"],
        3,
    ),
    (
        "What will be the output of the following pseudocode for A = [0, 1, 0, 3, 12], n = 5?",
        ["1 0 3 12 0", "1 3 12 0 0", "0 0 1 3 12", "1 3 12 0 12"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for S = \"AAABBCCCC\"?",
        ["A3B3C4", "A2B2C4", "A3B2C3", "A3B2C4"],
        3,
    ),
    (
        "What will be the output of the following pseudocode for A = [4, 1, 2, 1, 2], n = 5?",
        ["4", "1", "2", "0"],
        0,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["2.512", "1.567", "2.083", "3.0"],
        2,
    ),
    (
        "What will be the output of the following pseudocode for a = 8, b = 12?",
        ["4", "8", "12", "2"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for A = [2, 7, 11, 15], n = 4, target = 18?",
        ["11,7", "2,15", "7,11", "15,2"],
        2,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["8", "7", "5", "6"],
        3,
    ),
    (
        "What will be the output of the following pseudocode for A = [1, 2, 3, 4, 5], n = 5?",
        ["1 5 3 2 4", "5 4 3 1 2", "1 2 3 4 5", "5 4 3 2 1"],
        3,
    ),
    (
        "What will be the output of the following pseudocode for S = \"GOOD IS BETTER\"?",
        ["BETTER IS GOOD", "GOOD IS BETTER", "BETTER GOOD IS", "IS BETTER GOOD"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for n = 12?",
        ["10", "4", "8", "14"],
        2,
    ),
    (
        "What will be the output (top to bottom) of the following pseudocode for Stack S = [3, 1, 4, 2] (bottom to top)?",
        ["1 2 3 4", "4 3 2 1", "2 4 1 3", "3 1 4 2"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for Queue Q = [1, 2, 3, 4, 5, 6]?",
        ["Depends on implementation details (ambiguous/error - S is empty in second pop loop)", "1 4 2 5 3 6", "4 5 6 1 2 3", "1 2 3 4 5 6"],
        0,  # answer key in the source PDF says "option a" (ambiguous/error)
    ),
    (
        "What will be the output of the following pseudocode for the binary tree below?",
        ["50", "60", "45", "39"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for adjacency list?",
        ["3", "2", "4", "5"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for weights=[1,3,4], values= [15,20,30], capacity=4? Integer funn(Integer wt[], Integer val[], Integer n, Integer cap) Integer dp[n+1][cap+1] for i = 0 to n for w = 0 to cap if (i == 0 or w == 0) dp[i][w] = 0 else if (wt[i-1] <= w) dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w]) else dp[i][w] = dp[i-1][w] end if end for end for return dp[n][cap] end function Print funn([1,3,4], [15,20,30], 3, 4)",
        ["35", "30", "45", "50"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for n = 4?",
        ["13", "14", "15", "16"],
        2,
    ),
    (
        "What will be the output of the following pseudocode for A = [1, 2, 4, 5, 6], n = 5 (numbers should be 1 to 6)?",
        ["2", "3", "4", "5"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for S1 = \"ABCD\", S2 = \"CDAB\"?",
        ["false", "true", "error", "1"],
        1,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["-1", "1", "2", "-2"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for A = [7, 10, 4, 3, 20, 15], n = 6, k = 3?",
        ["15", "10", "7", "20"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for n = 10?",
        ["19", "20", "25", "30"],
        3,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["1 2 3", "1 1 1", "0 1 2", "3 3 3"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for n = 10, pos = 1?",
        ["11", "12", "8", "9"],
        2,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["error", "false", "true", "0"],
        2,
    ),
    (
        "What will be the output of the following pseudocode for the weighted adjacency matrix (n=3)?",
        ["14", "7", "22", "11"],
        3,
    ),
    (
        "What will be the output of the following pseudocode for grid (2x2)?",
        ["5", "9", "7", "10"],
        2,
    ),
    (
        "What will be the output of the following pseudocode for A = [2, 4, 6, 8], n = 4?",
        ["20", "18", "16", "24"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for A = [16, 17, 4, 3, 5, 2], n = 6?",
        ["17 5 2", "2 5 17", "2 5 17 16", "16 17 5 2"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for S = \"SWISS\"?",
        ["I", "S", "W", "_"],
        2,
    ),
    (
        "What will be the output of the following pseudocode for a = 10, b = 20?",
        ["2", "5", "3", "4"],
        3,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["1", "2", "5", "8"],
        1,
    ),
    (
        "What will be the first 3 outputs of the following pseudocode?",
        ["1, 10, 11", "1, 11, 10", "10, 11, 1", "1, 10, 100"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for the binary tree below?",
        ["1 3 2 6 5 4", "4 5 2 6 3 1", "1 2 3 4 5 6", "1 2 4 5 3 6"],
        2,
    ),
    (
        "What will be the output of the following pseudocode for A = [2, 3, -2, 4], n = 4?",
        ["24", "6", "-2", "4"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for A = [1, 3, 5, 7, 9, 11], target = 7?",
        ["4", "2", "3", "-1"],
        2,
    ),
    (
        "What will be the output of the following pseudocode for A = [1, 2, 3, 4], n = 4?",
        ["1 2 3 4", "24 12 8 6", "6 8 12 24", "4 3 2 1"],
        1,
    ),
    (
        "What will be the output (length) of the following pseudocode for S = \"ABCABCBB\"?",
        ["4", "3", "5", "2"],
        1,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["5, false", "15, false", "5, true", "15, true"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for n = 7, k = 3?",
        ["21", "58", "56", "49"],
        2,
    ),
    (
        "What will be the output (diameter, in number of edges) of the following pseudocode for the binary tree below?",
        ["4", "3", "5", "2"],
        0,
    ),
    (
        "What will be one valid output of the following pseudocode (Kahn's algorithm) for adjacency list?",
        ["0 2 1 3", "0 1 2 3", "1 2 0 3", "3 2 1 0"],
        1,
    ),
    (
        "What will be the output of the following pseudocode for S1 = \"CAT\", S2 = \"CUT\"?",
        ["0", "3", "2", "1"],
        3,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["20", "0", "120", "60"],
        3,
    ),
    (
        "What will be the output of the following pseudocode for A = [-7, 1, 5, 2, -4, 3, 0], n = 7 (equilibrium index: sum of elements left equals sum of elements right)?",
        ["3", "2", "4", "-1"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for a = -5, b = 3?",
        ["true", "false", "error", "0"],
        0,
    ),
    (
        "What will be the output of the following pseudocode for A = [1, 2, 3, -4, -1, 4], n = 6?",
        ["0", "-1", "-4", "4"],
        2,
    ),
    (
        "What will be the output of the following pseudocode?",
        ["24", "14", "20", "9"],
        2,
    ),
]


from html import escape

from pseudocode_listings import LISTINGS


def _stem_with_code(n, stem):
    """The code blocks live as images in the source PDF, so they were
    transcribed separately and are spliced back in here."""
    code = LISTINGS.get(n)
    if not code:
        return f"<b>{n}.</b> {stem}"
    return f"<b>{n}.</b> {stem}<pre>{escape(code)}</pre>"


PSEUDOCODE_QUIZ_QUESTIONS = [
    {
        "q": _stem_with_code(i + 1, stem),
        "options": options,
        "answer": answer,
    }
    for i, (stem, options, answer) in enumerate(PSEUDOCODE_QUESTIONS)
]


PSEUDOCODE_QUIZ = {
    "id": 29,
    "slug": "pseudocode-complete-100",
    "title": "Pseudocode Complete (100 Questions)",
    "difficulty": "Medium",
    "topics": ["Pseudocode", "Accenture", "Output Prediction"],
    "judge": "quiz",
    "languages": ["quiz"],
    "description": (
        "<p class=\"text-muted\">Source: Pseudocodes_Complete.pdf (Parts 1 &amp; 2)</p>"
        "<p>100 Accenture-style pseudocode output-prediction questions covering arrays, "
        "strings, loops, recursion, stacks, queues, linked lists, trees, graphs, "
        "dynamic programming and bit manipulation. Each question shows the inputs and "
        "four options — pick the correct output.</p>"
    ),
    "hint": "Trace the code line by line, keeping a variable table. Watch for integer division, loop bounds and pass-by-value semantics.",
    "boilerplate": {},
    "samples": [],
    "questions": PSEUDOCODE_QUIZ_QUESTIONS,
}
