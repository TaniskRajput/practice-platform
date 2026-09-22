"""
SQL problem shaped like the real Accenture coding-round SQL task reported
from the 17/18/20 Sept 2026 exams: two tables ("Animal" and "Thief"), a join,
and a numeric filter condition, selecting four specific columns.

The exact table/column names and condition were paraphrased rather than
shown verbatim in the source, so this is a faithful reconstruction of the
described shape (join two tables, filter on value > 15, select four
columns) rather than a byte-exact transcription.
"""

SQL_EXAM_PROBLEMS = [
    {
        "id": 4018,
        "slug": "stolen-animals-report",
        "title": "Stolen Animals Report (Animal / Thief Join)",
        "difficulty": "Medium",
        "topics": ["Database", "SQL"],
        "judge": "server",
        "languages": ["sql"],
        "description": """
<p class="text-muted">Coding round · SQL part (reconstructed from the 17/18/20 Sept 2026 exams —
exact table/column names weren't given in the source report, so this is a faithful
reconstruction of the described shape: join two tables, filter on a value greater than 15,
select four columns)</p>
<h3>Table: Animal</h3>
<pre>+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| animal_id   | int     |
| name        | varchar |
| species     | varchar |
| value       | int     |
| thief_id    | int     |
+-------------+---------+</pre>
<p><code>animal_id</code> is the unique identifier for this table.<br>
<code>thief_id</code> references <code>Thief.thief_id</code>, and is <code>NULL</code> if the
animal has not been stolen.</p>

<h3>Table: Thief</h3>
<pre>+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| thief_id    | int     |
| name        | varchar |
| city        | varchar |
+-------------+---------+</pre>
<p><code>thief_id</code> is the unique identifier for this table.</p>

<h3>Problem:</h3>
<p>Write a solution to report the <b>name</b> and <b>species</b> of every animal that has been
stolen and is worth <b>more than 15</b>, along with the <b>name</b> and <b>city</b> of the thief
who stole it.</p>
<p>Name your output columns <code>animal_name</code>, <code>species</code>,
<code>thief_name</code>, <code>city</code>.</p>

<h3>Example Output:</h3>
<pre>+-------------+---------+--------------+-------------+
| animal_name | species | thief_name   | city        |
+-------------+---------+--------------+-------------+
| Bella       | Dog     | Jack Sparrow | Portsmouth  |
| Luna        | Rabbit  | Marco Diaz   | Madrid      |
+-------------+---------+--------------+-------------+</pre>

<h3>Notes:</h3>
<ul>
  <li>The database dialect is <b>SQLite</b>.</li>
  <li>An animal that hasn't been stolen has <code>thief_id IS NULL</code> — it must not appear
      in the result, even if its <code>value</code> is over 15.</li>
  <li>"More than 15" is a strict inequality: an animal worth exactly <code>15</code> is
      excluded.</li>
</ul>
""",
        "hint": "An INNER JOIN between Animal and Thief on thief_id automatically excludes "
                 "animals with a NULL thief_id (never stolen) — you don't need an explicit "
                 "'IS NOT NULL' check. Filter with WHERE value > 15 (strictly greater than), "
                 "and alias each selected column to match the required output names.",
        "boilerplate": {
            "sql": """-- Write your SQLite query below
SELECT
FROM
JOIN
WHERE"""
        },
        "tests": [],
        "samples": [0],
        "databases": [
            {
                "name": "Sample database",
                "hidden": False,
                "schema": """
CREATE TABLE Animal (animal_id INTEGER PRIMARY KEY, name TEXT, species TEXT, value INTEGER, thief_id INTEGER);
CREATE TABLE Thief (thief_id INTEGER PRIMARY KEY, name TEXT, city TEXT);
""",
                "seed": {
                    "Animal": [
                        (1, "Bella", "Dog", 20, 1),
                        (2, "Milo", "Cat", 10, 2),
                        (3, "Rocky", "Parrot", 30, None),
                        (4, "Luna", "Rabbit", 18, 3),
                        (5, "Max", "Dog", 12, 1),
                        (6, "Coco", "Cat", 25, None),
                    ],
                    "Thief": [
                        (1, "Jack Sparrow", "Portsmouth"),
                        (2, "Ellen Vance", "London"),
                        (3, "Marco Diaz", "Madrid"),
                    ],
                },
                "reference_query": """
SELECT a.name AS animal_name, a.species, t.name AS thief_name, t.city
FROM Animal a
JOIN Thief t ON a.thief_id = t.thief_id
WHERE a.value > 15
""",
            },
            {
                "name": "Hidden database",
                "hidden": True,
                "schema": """
CREATE TABLE Animal (animal_id INTEGER PRIMARY KEY, name TEXT, species TEXT, value INTEGER, thief_id INTEGER);
CREATE TABLE Thief (thief_id INTEGER PRIMARY KEY, name TEXT, city TEXT);
""",
                "seed": {
                    "Animal": [
                        (1, "Whiskers", "Cat", 22, 10),
                        (2, "Buddy", "Dog", 15, 11),
                        (3, "Tweety", "Parrot", 40, None),
                        (4, "Nibbles", "Rabbit", 8, 12),
                        (5, "Shadow", "Cat", 35, 10),
                        (6, "Duke", "Dog", 19, None),
                        (7, "Peanut", "Hamster", 5, 11),
                    ],
                    "Thief": [
                        (10, "Vic Slade", "Berlin"),
                        (11, "Nora Quinn", "Dublin"),
                        (12, "Tomas Reyes", "Lisbon"),
                    ],
                },
                "reference_query": """
SELECT a.name AS animal_name, a.species, t.name AS thief_name, t.city
FROM Animal a
JOIN Thief t ON a.thief_id = t.thief_id
WHERE a.value > 15
""",
            },
        ],
    },
]
