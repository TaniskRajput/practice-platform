"""
JavaScript DOM Practice — a self-contained, chunked curriculum for learning DOM
manipulation by doing, one small skill at a time (selecting elements, changing
text/attributes, styling with classes, handling events, creating/removing
elements, traversal, forms, and finally combining everything into five mini
projects). 8 chunks x 5 exercises = 40 original "browser" judge problems
(ids 6001-6040) — the student writes JS against fixed HTML/CSS and grading
simulates clicks/typing/selecting in a real browser, then checks DOM state.

Every exercise's browser_tests were verified against a harness that extracts
the real grading runner straight from static/app.js (headless Chrome): a
correct reference solution passes 100%, and the shipped boilerplate stub
fails at least one test.
"""


# ============================================================================
# Chunk 1
# ============================================================================
CHUNK1_STYLE = """
body { font-family: -apple-system, "Segoe UI", sans-serif; display: flex; justify-content: center; padding-top: 50px; background: #fafafa; }
.panel { text-align: center; background: #fff; border: 1px solid #ddd; border-radius: 14px; padding: 28px 36px; min-width: 280px; box-shadow: 0 4px 18px rgba(0,0,0,.08); }
ul { text-align: left; padding-left: 20px; }
table { margin: 0 auto 14px; border-collapse: collapse; }
td { border: 1px solid #ddd; padding: 6px 16px; }
button { margin-top: 10px; padding: 10px 18px; font-size: 15px; border-radius: 8px; border: 1px solid #ccc; cursor: pointer; background: #f3f3f3; }
button:hover { background: #e8e8e8; }
input { padding: 8px 10px; font-size: 14px; border-radius: 6px; border: 1px solid #ccc; margin-right: 6px; }
#output { margin-top: 14px; font-size: 15px; min-height: 20px; color: #222; }
"""

CHUNK1_PROBLEMS = [
    {
        "id": 6001,
        "slug": "dom-show-welcome-message",
        "title": "Show a Welcome Message",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Selecting & Reading Elements"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>This is the very first exercise in the <b>Selecting &amp; Reading Elements</b> chunk — it only
needs <code>document.getElementById</code> and setting <code>textContent</code>.</p>
<pre>&lt;div class="panel"&gt;
  &lt;p id="output"&gt;Click the button to see a message.&lt;/p&gt;
  &lt;button id="show-btn"&gt;Show Message&lt;/button&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript so that:</p>
<ul>
  <li>Clicking <code>#show-btn</code> sets <code>#output</code>'s text to exactly
      <code>"Welcome to JavaScript DOM practice!"</code>.</li>
  <li>Clicking it again (or any number of times) leaves the same message showing.</li>
</ul>
""",
        "hint": "Select both elements once with document.getElementById, then call "
                 "addEventListener('click', ...) on the button and set "
                 "outputEl.textContent inside the handler.",
        "boilerplate": {
            "javascript": """const outputEl = document.getElementById('output');
const showBtn = document.getElementById('show-btn');

// TODO: when show-btn is clicked, set outputEl's text to the welcome message
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <p id="output">Click the button to see a message.</p>
  <button id="show-btn">Show Message</button>
</div>""",
        "browser_style": CHUNK1_STYLE,
        "browser_tests": [
            {
                "name": "Initial text is unchanged before any click",
                "hidden": False,
                "steps": [],
                "expect": {"text": {"id": "output", "value": "Click the button to see a message."}},
            },
            {
                "name": "Clicking shows the welcome message",
                "hidden": False,
                "steps": [{"click": "show-btn"}],
                "expect": {"text": {"id": "output", "value": "Welcome to JavaScript DOM practice!"}},
            },
            {
                "name": "Clicking again keeps showing the same message",
                "hidden": True,
                "steps": [{"click": "show-btn"}, {"click": "show-btn"}, {"click": "show-btn"}],
                "expect": {"text": {"id": "output", "value": "Welcome to JavaScript DOM practice!"}},
            },
        ],
    },
    {
        "id": 6002,
        "slug": "dom-count-list-items",
        "title": "Count the List Items",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Selecting & Reading Elements"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Practice <code>querySelectorAll</code> and reading a NodeList's <code>length</code>.</p>
<pre>&lt;div class="panel"&gt;
  &lt;ul id="fruit-list"&gt;
    &lt;li&gt;Apple&lt;/li&gt;&lt;li&gt;Banana&lt;/li&gt;&lt;li&gt;Cherry&lt;/li&gt;&lt;li&gt;Date&lt;/li&gt;&lt;li&gt;Elderberry&lt;/li&gt;
  &lt;/ul&gt;
  &lt;p id="output"&gt;&lt;/p&gt;
  &lt;button id="count-btn"&gt;Count Items&lt;/button&gt;
&lt;/div&gt;</pre>
<p>Clicking <code>#count-btn</code> should set <code>#output</code>'s text to
<code>"5 items"</code> — the number of <code>&lt;li&gt;</code> elements inside
<code>#fruit-list</code>, followed by the word <code>items</code>.</p>
""",
        "hint": "document.querySelectorAll('#fruit-list li').length gives you the count as a "
                 "number — build the string with a template literal: `${count} items`.",
        "boilerplate": {
            "javascript": """const outputEl = document.getElementById('output');
const countBtn = document.getElementById('count-btn');

// TODO: on click, count the <li> elements inside #fruit-list and show "N items"
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <ul id="fruit-list">
    <li>Apple</li><li>Banana</li><li>Cherry</li><li>Date</li><li>Elderberry</li>
  </ul>
  <p id="output"></p>
  <button id="count-btn">Count Items</button>
</div>""",
        "browser_style": CHUNK1_STYLE,
        "browser_tests": [
            {
                "name": "Output is empty before any click",
                "hidden": False,
                "steps": [],
                "expect": {"text": {"id": "output", "value": ""}},
            },
            {
                "name": "Clicking shows '5 items'",
                "hidden": False,
                "steps": [{"click": "count-btn"}],
                "expect": {"text": {"id": "output", "value": "5 items"}},
            },
            {
                "name": "Clicking again still shows '5 items'",
                "hidden": True,
                "steps": [{"click": "count-btn"}, {"click": "count-btn"}],
                "expect": {"text": {"id": "output", "value": "5 items"}},
            },
        ],
    },
    {
        "id": 6003,
        "slug": "dom-echo-input-value",
        "title": "Echo the Input Value",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Selecting & Reading Elements"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Practice reading an <code>&lt;input&gt;</code>'s <code>.value</code> property.</p>
<pre>&lt;div class="panel"&gt;
  &lt;input type="text" id="name-input" placeholder="Type your name"&gt;
  &lt;button id="echo-btn"&gt;Echo&lt;/button&gt;
  &lt;p id="output"&gt;&lt;/p&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript so that clicking <code>#echo-btn</code>:</p>
<ul>
  <li>Sets <code>#output</code>'s text to whatever is currently typed in
      <code>#name-input</code>, if it's non-empty.</li>
  <li>If the input is empty (or only spaces), shows
      <code>"You didn't type anything."</code> instead.</li>
</ul>
""",
        "hint": "Read inputEl.value.trim() once per click. An empty trimmed string is falsy in "
                 "an if-check, so `if (!name) { ... } else { ... }` covers both cases.",
        "boilerplate": {
            "javascript": """const nameInput = document.getElementById('name-input');
const echoBtn = document.getElementById('echo-btn');
const outputEl = document.getElementById('output');

// TODO: on click, echo the trimmed input value, or a fallback message if it's empty
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <input type="text" id="name-input" placeholder="Type your name">
  <button id="echo-btn">Echo</button>
  <p id="output"></p>
</div>""",
        "browser_style": CHUNK1_STYLE,
        "browser_tests": [
            {
                "name": "Typing a name and clicking echoes it",
                "hidden": False,
                "steps": [{"type": "name-input", "value": "Aria"}, {"click": "echo-btn"}],
                "expect": {"text": {"id": "output", "value": "Aria"}},
            },
            {
                "name": "Clicking with an empty input shows the fallback",
                "hidden": False,
                "steps": [{"type": "name-input", "value": ""}, {"click": "echo-btn"}],
                "expect": {"text": {"id": "output", "value": "You didn't type anything."}},
            },
            {
                "name": "A spaces-only input also shows the fallback",
                "hidden": True,
                "steps": [{"type": "name-input", "value": "   "}, {"click": "echo-btn"}],
                "expect": {"text": {"id": "output", "value": "You didn't type anything."}},
            },
            {
                "name": "Typing a new name overwrites the previous output",
                "hidden": True,
                "steps": [{"type": "name-input", "value": "Ben"}, {"click": "echo-btn"}],
                "expect": {"text": {"id": "output", "value": "Ben"}},
            },
        ],
    },
    {
        "id": 6004,
        "slug": "dom-find-longest-word",
        "title": "Find the Longest Word",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Selecting & Reading Elements"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Practice looping over a NodeList read from the DOM.</p>
<pre>&lt;div class="panel"&gt;
  &lt;ul id="word-list"&gt;
    &lt;li&gt;cat&lt;/li&gt;&lt;li&gt;elephant&lt;/li&gt;&lt;li&gt;ox&lt;/li&gt;&lt;li&gt;hippopotamus&lt;/li&gt;&lt;li&gt;dog&lt;/li&gt;
  &lt;/ul&gt;
  &lt;p id="output"&gt;&lt;/p&gt;
  &lt;button id="find-btn"&gt;Find Longest&lt;/button&gt;
&lt;/div&gt;</pre>
<p>Clicking <code>#find-btn</code> should set <code>#output</code>'s text to whichever
<code>&lt;li&gt;</code>'s text is longest (here, <code>"hippopotamus"</code>).</p>
""",
        "hint": "Convert the NodeList to an array with Array.from(...) or the spread operator so "
                 "you can use .reduce() to keep the longest word seen so far.",
        "boilerplate": {
            "javascript": """const outputEl = document.getElementById('output');
const findBtn = document.getElementById('find-btn');

// TODO: on click, find the <li> with the longest text and show it in #output
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <ul id="word-list">
    <li>cat</li><li>elephant</li><li>ox</li><li>hippopotamus</li><li>dog</li>
  </ul>
  <p id="output"></p>
  <button id="find-btn">Find Longest</button>
</div>""",
        "browser_style": CHUNK1_STYLE,
        "browser_tests": [
            {
                "name": "Output is empty before any click",
                "hidden": False,
                "steps": [],
                "expect": {"text": {"id": "output", "value": ""}},
            },
            {
                "name": "Clicking finds 'hippopotamus'",
                "hidden": False,
                "steps": [{"click": "find-btn"}],
                "expect": {"text": {"id": "output", "value": "hippopotamus"}},
            },
            {
                "name": "Clicking again still finds the same word",
                "hidden": True,
                "steps": [{"click": "find-btn"}, {"click": "find-btn"}],
                "expect": {"text": {"id": "output", "value": "hippopotamus"}},
            },
        ],
    },
    {
        "id": 6005,
        "slug": "dom-sum-table-column",
        "title": "Sum a Column of Numbers",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Selecting & Reading Elements"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Practice reading numeric text out of table cells.</p>
<pre>&lt;div class="panel"&gt;
  &lt;table id="score-table"&gt;
    &lt;tbody&gt;
      &lt;tr&gt;&lt;td&gt;12&lt;/td&gt;&lt;/tr&gt;
      &lt;tr&gt;&lt;td&gt;7&lt;/td&gt;&lt;/tr&gt;
      &lt;tr&gt;&lt;td&gt;25&lt;/td&gt;&lt;/tr&gt;
      &lt;tr&gt;&lt;td&gt;3&lt;/td&gt;&lt;/tr&gt;
    &lt;/tbody&gt;
  &lt;/table&gt;
  &lt;p id="output"&gt;&lt;/p&gt;
  &lt;button id="sum-btn"&gt;Sum Scores&lt;/button&gt;
&lt;/div&gt;</pre>
<p>Clicking <code>#sum-btn</code> should set <code>#output</code>'s text to
<code>"Total: 47"</code> — the sum of every <code>&lt;td&gt;</code> in the table,
parsed as numbers.</p>
""",
        "hint": "Each cell's text is a string — use parseInt(cell.textContent, 10) (or Number(...)) "
                 "before adding, otherwise + will concatenate the text instead of adding numbers.",
        "boilerplate": {
            "javascript": """const outputEl = document.getElementById('output');
const sumBtn = document.getElementById('sum-btn');

// TODO: on click, sum every <td> in #score-table (parsed as numbers) and show "Total: N"
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <table id="score-table">
    <tbody>
      <tr><td>12</td></tr>
      <tr><td>7</td></tr>
      <tr><td>25</td></tr>
      <tr><td>3</td></tr>
    </tbody>
  </table>
  <p id="output"></p>
  <button id="sum-btn">Sum Scores</button>
</div>""",
        "browser_style": CHUNK1_STYLE,
        "browser_tests": [
            {
                "name": "Output is empty before any click",
                "hidden": False,
                "steps": [],
                "expect": {"text": {"id": "output", "value": ""}},
            },
            {
                "name": "Clicking shows 'Total: 47'",
                "hidden": False,
                "steps": [{"click": "sum-btn"}],
                "expect": {"text": {"id": "output", "value": "Total: 47"}},
            },
            {
                "name": "Clicking again still shows 'Total: 47'",
                "hidden": True,
                "steps": [{"click": "sum-btn"}, {"click": "sum-btn"}],
                "expect": {"text": {"id": "output", "value": "Total: 47"}},
            },
        ],
    },
]

# ============================================================================
# Chunk 2
# ============================================================================
"""Chunk 2: "Changing Text & Attributes" — 5 browser-judge DOM exercises (ids 6006-6010).

Each problem uses the "browser" judge: the student writes plain JS against a fixed
browser_html/browser_style, and browser_tests simulate clicks/typing/selecting and then
assert on live DOM state. See static/app.js's runner for the exact expect vocabulary.
"""

CHUNK2_STYLE = """
body { font-family: -apple-system, "Segoe UI", sans-serif; display: flex; justify-content: center; padding-top: 50px; background: #fafafa; }
.panel { text-align: center; background: #fff; border: 1px solid #ddd; border-radius: 14px; padding: 28px 36px; min-width: 280px; box-shadow: 0 4px 18px rgba(0,0,0,.08); }
button { margin-top: 10px; padding: 10px 18px; font-size: 15px; border-radius: 8px; border: 1px solid #ccc; cursor: pointer; background: #f3f3f3; }
button:hover { background: #e8e8e8; }
button:disabled { opacity: .5; cursor: not-allowed; }
input, textarea { padding: 8px 10px; font-size: 14px; border-radius: 6px; border: 1px solid #ccc; margin: 6px 0; width: 220px; }
img { max-width: 160px; border-radius: 10px; display: block; margin: 0 auto 12px; }
a { display: inline-block; margin-bottom: 12px; }
#output, #hint-msg { margin-top: 14px; font-size: 15px; min-height: 20px; color: #222; }
"""


CHUNK2_PROBLEMS = [
    # ------------------------------------------------------------------ #
    # 6006. Live Character Counter
    # ------------------------------------------------------------------ #
    {
        "id": 6006,
        "slug": "dom-live-character-counter",
        "title": "Live Character Counter",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Changing Text & Attributes"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Implement a live character counter for a message box with the following HTML layout:</p>
<pre>&lt;div class="panel"&gt;
  &lt;textarea id="msg-input" rows="3"&gt;&lt;/textarea&gt;
  &lt;p id="output"&gt;0 characters&lt;/p&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript to fulfill the following specifications:</p>
<ul>
  <li><b>Live Update:</b> On every <code>input</code> event fired on <code>#msg-input</code>,
      set <code>#output</code>'s text to <code>`${length} characters`</code>, where
      <code>length</code> is the current length of the textarea's value.</li>
  <li><b>Initial State:</b> On page load, before any typing, <code>#output</code> already
      shows <code>"0 characters"</code> (matching the empty textarea).</li>
</ul>
""",
        "hint": "Listen for the `input` event on the textarea and read `.value.length` inside "
                "the handler — no separate counter variable needed.",
        "boilerplate": {
            "javascript": """const msgInput = document.getElementById('msg-input');
const output = document.getElementById('output');

// TODO: whenever msgInput fires an "input" event, set output's text to
// `${msgInput.value.length} characters`
""",
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <textarea id="msg-input" rows="3"></textarea>
  <p id="output">0 characters</p>
</div>""",
        "browser_style": CHUNK2_STYLE,
        "browser_tests": [
            {
                "name": "Initial state: shows 0 characters",
                "hidden": False,
                "steps": [],
                "expect": {"text": {"id": "output", "value": "0 characters"}},
            },
            {
                "name": "Typing 'Hello' shows 5 characters",
                "hidden": False,
                "steps": [{"type": "msg-input", "value": "Hello"}],
                "expect": {"text": {"id": "output", "value": "5 characters"}},
            },
            {
                "name": "Clearing the textarea shows 0 characters",
                "hidden": True,
                "steps": [{"type": "msg-input", "value": ""}],
                "expect": {"text": {"id": "output", "value": "0 characters"}},
            },
            {
                "name": "Typing 'Hi there' shows 8 characters",
                "hidden": True,
                "steps": [{"type": "msg-input", "value": "Hi there"}],
                "expect": {"text": {"id": "output", "value": "8 characters"}},
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # 6007. Swap the Image
    # ------------------------------------------------------------------ #
    {
        "id": 6007,
        "slug": "dom-swap-the-image",
        "title": "Swap the Image",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Changing Text & Attributes"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Implement an image-swap button with the following HTML layout:</p>
<pre>&lt;div class="panel"&gt;
  &lt;img id="photo" src="cat.jpg" alt="A cat"&gt;
  &lt;button id="swap-btn"&gt;Show Dog&lt;/button&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript to fulfill the following specifications:</p>
<ul>
  <li><b>Swap on Click:</b> Clicking <code>#swap-btn</code> sets <code>#photo</code>'s
      <code>src</code> attribute to <code>"dog.jpg"</code> and its <code>alt</code>
      attribute to <code>"A dog"</code>.</li>
  <li><b>Idempotent:</b> Clicking <code>#swap-btn</code> again leaves the image pointed at
      the dog photo (it does not toggle back).</li>
</ul>
""",
        "hint": "Use `setAttribute('src', ...)` and `setAttribute('alt', ...)` inside the "
                "button's click handler — both attributes change together, every click.",
        "boilerplate": {
            "javascript": """const photo = document.getElementById('photo');
const swapBtn = document.getElementById('swap-btn');

// TODO: on click of swapBtn, set photo's src attribute to "dog.jpg"
// and its alt attribute to "A dog"
""",
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <img id="photo" src="cat.jpg" alt="A cat">
  <button id="swap-btn">Show Dog</button>
</div>""",
        "browser_style": CHUNK2_STYLE,
        "browser_tests": [
            {
                "name": "Initial state: shows cat.jpg",
                "hidden": False,
                "steps": [],
                "expect": {"attr": {"selector": "#photo", "name": "src", "value": "cat.jpg"}},
            },
            {
                "name": "Clicking swaps src to dog.jpg and alt to 'A dog'",
                "hidden": False,
                "steps": [{"click": "swap-btn"}],
                "expect": {
                    "attr": {"selector": "#photo", "name": "src", "value": "dog.jpg"},
                    "exists": {"selector": '#photo[alt="A dog"]', "value": True},
                },
            },
            {
                "name": "Clicking again stays on dog.jpg (idempotent)",
                "hidden": True,
                "steps": [{"click": "swap-btn"}],
                "expect": {"attr": {"selector": "#photo", "name": "src", "value": "dog.jpg"}},
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # 6008. Greet From a Data Attribute
    # ------------------------------------------------------------------ #
    {
        "id": 6008,
        "slug": "dom-greet-from-a-data-attribute",
        "title": "Greet From a Data Attribute",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Changing Text & Attributes"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Implement a greeting button that reads a name out of a data attribute, with the
following HTML layout:</p>
<pre>&lt;div class="panel"&gt;
  &lt;div id="user-card" data-name="Priya"&gt;&lt;/div&gt;
  &lt;button id="greet-btn"&gt;Greet&lt;/button&gt;
  &lt;p id="output"&gt;&lt;/p&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript to fulfill the following specifications:</p>
<ul>
  <li><b>Read the Data Attribute:</b> Clicking <code>#greet-btn</code> reads the
      <code>data-name</code> attribute off <code>#user-card</code> via its
      <code>.dataset.name</code> property.</li>
  <li><b>Greet:</b> After reading the name, set <code>#output</code>'s text to
      <code>`Hello, ${name}!`</code> (for this card, exactly <code>"Hello, Priya!"</code>).</li>
  <li><b>Initial State:</b> On page load, before any click, <code>#output</code> is empty.</li>
</ul>
""",
        "hint": "`data-name` on an element is readable in JS as `element.dataset.name` — no "
                "need to call `getAttribute('data-name')` directly.",
        "boilerplate": {
            "javascript": """const userCard = document.getElementById('user-card');
const greetBtn = document.getElementById('greet-btn');
const output = document.getElementById('output');

// TODO: on click of greetBtn, read userCard.dataset.name and set
// output's text to `Hello, ${name}!`
""",
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <div id="user-card" data-name="Priya"></div>
  <button id="greet-btn">Greet</button>
  <p id="output"></p>
</div>""",
        "browser_style": CHUNK2_STYLE,
        "browser_tests": [
            {
                "name": "Initial state: output is empty",
                "hidden": False,
                "steps": [],
                "expect": {"text": {"id": "output", "value": ""}},
            },
            {
                "name": "Clicking greets by name from the data attribute",
                "hidden": False,
                "steps": [{"click": "greet-btn"}],
                "expect": {"text": {"id": "output", "value": "Hello, Priya!"}},
            },
            {
                "name": "Clicking again shows the same greeting",
                "hidden": True,
                "steps": [{"click": "greet-btn"}],
                "expect": {"text": {"id": "output", "value": "Hello, Priya!"}},
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # 6009. Enable Submit When Filled
    # ------------------------------------------------------------------ #
    {
        "id": 6009,
        "slug": "dom-enable-submit-when-filled",
        "title": "Enable Submit When Filled",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Changing Text & Attributes"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Implement a title field that enables a Post button only once it has real content, with
the following HTML layout:</p>
<pre>&lt;div class="panel"&gt;
  &lt;input type="text" id="title-input" placeholder="Post title"&gt;
  &lt;br&gt;
  &lt;button id="post-btn" disabled&gt;Post&lt;/button&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript to fulfill the following specifications:</p>
<ul>
  <li><b>Live Validation:</b> On every <code>input</code> event fired on
      <code>#title-input</code>, set <code>#post-btn</code>'s <code>disabled</code> property
      to <code>true</code> if the input's trimmed value is empty, otherwise <code>false</code>.</li>
  <li><b>Whitespace Counts as Empty:</b> A value made up only of spaces (e.g.
      <code>"   "</code>) must still leave the button disabled — trim before checking.</li>
  <li><b>Initial State:</b> On page load, the input is empty and <code>#post-btn</code>
      starts disabled.</li>
</ul>
""",
        "hint": "Set `postBtn.disabled = titleInput.value.trim().length === 0` inside the "
                "`input` event handler.",
        "boilerplate": {
            "javascript": """const titleInput = document.getElementById('title-input');
const postBtn = document.getElementById('post-btn');

// TODO: whenever titleInput fires an "input" event, set postBtn.disabled
// to true if the trimmed value is empty, otherwise false
""",
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <input type="text" id="title-input" placeholder="Post title">
  <br>
  <button id="post-btn" disabled>Post</button>
</div>""",
        "browser_style": CHUNK2_STYLE,
        "browser_tests": [
            {
                "name": "Initial state: button is disabled",
                "hidden": False,
                "steps": [],
                "expect": {"style": {"selector": "#post-btn", "property": "disabled", "value": "true"}},
            },
            {
                "name": "Typing 'Hi' enables the button",
                "hidden": False,
                "steps": [{"type": "title-input", "value": "Hi"}],
                "expect": {"style": {"selector": "#post-btn", "property": "disabled", "value": "false"}},
            },
            {
                "name": "Clearing the input disables the button again",
                "hidden": True,
                "steps": [{"type": "title-input", "value": ""}],
                "expect": {"style": {"selector": "#post-btn", "property": "disabled", "value": "true"}},
            },
            {
                "name": "Spaces-only input keeps the button disabled",
                "hidden": True,
                "steps": [{"type": "title-input", "value": "   "}],
                "expect": {"style": {"selector": "#post-btn", "property": "disabled", "value": "true"}},
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # 6010. Update the Link Destination
    # ------------------------------------------------------------------ #
    {
        "id": 6010,
        "slug": "dom-update-the-link-destination",
        "title": "Update the Link Destination",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Changing Text & Attributes"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Implement a button that repoints a profile link, with the following HTML layout:</p>
<pre>&lt;div class="panel"&gt;
  &lt;a id="profile-link" href="#" target="_blank"&gt;View Profile&lt;/a&gt;
  &lt;br&gt;
  &lt;button id="update-btn"&gt;Point to GitHub&lt;/button&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript to fulfill the following specifications:</p>
<ul>
  <li><b>Update on Click:</b> Clicking <code>#update-btn</code> sets <code>#profile-link</code>'s
      <code>href</code> attribute to <code>"https://github.com"</code> and its text to
      <code>"View on GitHub"</code>.</li>
  <li><b>Idempotent:</b> Clicking <code>#update-btn</code> again leaves the link exactly the
      same (it does not toggle back to the original).</li>
  <li><b>Initial State:</b> On page load, the link's <code>href</code> is still
      <code>"#"</code>.</li>
</ul>
""",
        "hint": "Use `setAttribute('href', ...)` to change the destination and `.textContent` "
                "to change the visible label, both inside the button's click handler.",
        "boilerplate": {
            "javascript": """const profileLink = document.getElementById('profile-link');
const updateBtn = document.getElementById('update-btn');

// TODO: on click of updateBtn, set profileLink's href attribute to
// "https://github.com" and its text to "View on GitHub"
""",
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <a id="profile-link" href="#" target="_blank">View Profile</a>
  <br>
  <button id="update-btn">Point to GitHub</button>
</div>""",
        "browser_style": CHUNK2_STYLE,
        "browser_tests": [
            {
                "name": "Initial state: href is '#'",
                "hidden": False,
                "steps": [],
                "expect": {"attr": {"selector": "#profile-link", "name": "href", "value": "#"}},
            },
            {
                "name": "Clicking points the link to GitHub and relabels it",
                "hidden": False,
                "steps": [{"click": "update-btn"}],
                "expect": {
                    "attr": {"selector": "#profile-link", "name": "href", "value": "https://github.com"},
                    "text": {"id": "profile-link", "value": "View on GitHub"},
                },
            },
            {
                "name": "Clicking again stays on GitHub (idempotent)",
                "hidden": True,
                "steps": [{"click": "update-btn"}],
                "expect": {
                    "attr": {"selector": "#profile-link", "name": "href", "value": "https://github.com"},
                    "text": {"id": "profile-link", "value": "View on GitHub"},
                },
            },
        ],
    },
]

# ============================================================================
# Chunk 3
# ============================================================================
CHUNK3_STYLE = """
body { font-family: -apple-system, "Segoe UI", sans-serif; display: flex; justify-content: center; padding-top: 50px; background: #fafafa; }
.panel { text-align: center; background: #fff; border: 1px solid #ddd; border-radius: 14px; padding: 28px 36px; min-width: 280px; box-shadow: 0 4px 18px rgba(0,0,0,.08); }
button { margin: 4px; padding: 10px 18px; font-size: 15px; border-radius: 8px; border: 1px solid #ccc; cursor: pointer; background: #f3f3f3; }
button:hover { background: #e8e8e8; }
ul, nav { list-style: none; padding: 0; margin: 0; }
li, .nav-link { padding: 10px 14px; margin: 6px 0; border-radius: 8px; background: #f3f3f3; cursor: pointer; display: block; text-decoration: none; color: #222; }
.item.highlight, li.highlight { background: #ffe9a8; }
.nav-link.active { background: #4a90d9; color: #fff; }
.page.dark { background: #1a1a1a; color: #eee; }
.page { padding: 16px; border-radius: 10px; transition: background .2s; }
.error { border-color: #c0392b !important; background: #fdecea; }
#hint-msg { margin-top: 10px; font-size: 13px; color: #c0392b; min-height: 18px; }
input.error { outline: 2px solid #c0392b; }
"""

CHUNK3_STYLE_6014_EXTRA = """
#bar-track{width:150px;height:10px;background:#eee;border-radius:6px;overflow:hidden;} #bar-fill{height:10px;background:#4a90d9;} .step-1{width:50px;} .step-2{width:100px;} .step-3{width:150px;}
"""

CHUNK3_PROBLEMS = [
    {
        "id": 6011,
        "slug": "dom-highlight-on-click",
        "title": "Highlight on Click",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Styling with Classes"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Practice toggling a CSS class with <code>classList.toggle</code>.</p>
<pre>&lt;div class="panel"&gt;
  &lt;ul id="list"&gt;
    &lt;li id="item-1" class="item"&gt;Milk&lt;/li&gt;
    &lt;li id="item-2" class="item"&gt;Eggs&lt;/li&gt;
    &lt;li id="item-3" class="item"&gt;Bread&lt;/li&gt;
  &lt;/ul&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript so that:</p>
<ul>
  <li>Clicking any <code>&lt;li&gt;</code> toggles the class <code>"highlight"</code> on
      that same <code>&lt;li&gt;</code> — nothing else changes.</li>
  <li>Clicking an already-highlighted item removes the highlight again.</li>
  <li>Each item's highlight state is independent of the others.</li>
</ul>
""",
        "hint": "Attach one click listener per <li> (or delegate a single listener on #list and "
                 "use event.target), then call event.target.classList.toggle('highlight').",
        "boilerplate": {
            "javascript": """const list = document.getElementById('list');

// TODO: when a <li> inside #list is clicked, toggle the 'highlight' class on it
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <ul id="list">
    <li id="item-1" class="item">Milk</li>
    <li id="item-2" class="item">Eggs</li>
    <li id="item-3" class="item">Bread</li>
  </ul>
</div>""",
        "browser_style": CHUNK3_STYLE,
        "browser_tests": [
            {
                "name": "No items are highlighted initially",
                "hidden": False,
                "steps": [],
                "expect": {"hasClass": {"selector": "#item-1", "class": "highlight", "value": False}},
            },
            {
                "name": "Clicking an item highlights it",
                "hidden": False,
                "steps": [{"click": "item-1"}],
                "expect": {"hasClass": {"selector": "#item-1", "class": "highlight", "value": True}},
            },
            {
                "name": "Clicking it again removes the highlight",
                "hidden": True,
                "steps": [{"click": "item-1"}],
                "expect": {"hasClass": {"selector": "#item-1", "class": "highlight", "value": False}},
            },
            {
                "name": "Clicking a different item highlights only that one",
                "hidden": True,
                "steps": [{"click": "item-2"}],
                "expect": {"hasClass": {"selector": "#item-2", "class": "highlight", "value": True}},
            },
            {
                "name": "item-1 stays un-highlighted (independence check)",
                "hidden": True,
                "steps": [],
                "expect": {"hasClass": {"selector": "#item-1", "class": "highlight", "value": False}},
            },
        ],
    },
    {
        "id": 6012,
        "slug": "dom-dark-mode-toggle",
        "title": "Dark Mode Toggle",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Styling with Classes"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Practice toggling a class on an element that isn't the one clicked.</p>
<pre>&lt;div class="panel"&gt;
  &lt;div id="page" class="page"&gt;
    &lt;p id="output"&gt;Toggle the theme below.&lt;/p&gt;
    &lt;button id="theme-btn"&gt;Toggle Dark Mode&lt;/button&gt;
  &lt;/div&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript so that clicking <code>#theme-btn</code> toggles the class
<code>"dark"</code> on <code>#page</code> (on, then off, then on again, and so on).</p>
""",
        "hint": "Select #page once outside the handler, then inside the click handler call "
                 "pageEl.classList.toggle('dark').",
        "boilerplate": {
            "javascript": """const page = document.getElementById('page');
const themeBtn = document.getElementById('theme-btn');

// TODO: on click, toggle the 'dark' class on #page
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <div id="page" class="page">
    <p id="output">Toggle the theme below.</p>
    <button id="theme-btn">Toggle Dark Mode</button>
  </div>
</div>""",
        "browser_style": CHUNK3_STYLE,
        "browser_tests": [
            {
                "name": "Page is not dark initially",
                "hidden": False,
                "steps": [],
                "expect": {"hasClass": {"selector": "#page", "class": "dark", "value": False}},
            },
            {
                "name": "Clicking turns dark mode on",
                "hidden": False,
                "steps": [{"click": "theme-btn"}],
                "expect": {"hasClass": {"selector": "#page", "class": "dark", "value": True}},
            },
            {
                "name": "Clicking again turns dark mode off",
                "hidden": True,
                "steps": [{"click": "theme-btn"}],
                "expect": {"hasClass": {"selector": "#page", "class": "dark", "value": False}},
            },
        ],
    },
    {
        "id": 6013,
        "slug": "dom-active-nav-item",
        "title": "Active Nav Item",
        "difficulty": "Medium",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Styling with Classes"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Practice making sure only one element in a group has a class at a time.</p>
<pre>&lt;nav id="nav" class="panel"&gt;
  &lt;a id="nav-home" class="nav-link active" href="#"&gt;Home&lt;/a&gt;
  &lt;a id="nav-about" class="nav-link" href="#"&gt;About&lt;/a&gt;
  &lt;a id="nav-contact" class="nav-link" href="#"&gt;Contact&lt;/a&gt;
&lt;/nav&gt;</pre>
<p>Write JavaScript so that clicking any <code>.nav-link</code>:</p>
<ul>
  <li>Adds the class <code>"active"</code> to the clicked link.</li>
  <li>Removes <code>"active"</code> from every other <code>.nav-link</code>, so exactly
      one link is ever active.</li>
</ul>
<p><code>#nav-home</code> starts out active, matching the page load.</p>
""",
        "hint": "Loop over document.querySelectorAll('.nav-link') and call classList.remove('active') "
                 "on each one, then classList.add('active') on the one that was actually clicked.",
        "boilerplate": {
            "javascript": """const nav = document.getElementById('nav');
const links = document.querySelectorAll('.nav-link');

// TODO: when a .nav-link is clicked, make it (and only it) have the 'active' class
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<nav id="nav" class="panel">
  <a id="nav-home" class="nav-link active" href="#">Home</a>
  <a id="nav-about" class="nav-link" href="#">About</a>
  <a id="nav-contact" class="nav-link" href="#">Contact</a>
</nav>""",
        "browser_style": CHUNK3_STYLE,
        "browser_tests": [
            {
                "name": "Home starts active",
                "hidden": False,
                "steps": [],
                "expect": {"hasClass": {"selector": "#nav-home", "class": "active", "value": True}},
            },
            {
                "name": "About starts inactive",
                "hidden": False,
                "steps": [],
                "expect": {"hasClass": {"selector": "#nav-about", "class": "active", "value": False}},
            },
            {
                "name": "Clicking About makes it active",
                "hidden": False,
                "steps": [{"click": "nav-about"}],
                "expect": {"hasClass": {"selector": "#nav-about", "class": "active", "value": True}},
            },
            {
                "name": "Home is no longer active after About is clicked",
                "hidden": True,
                "steps": [],
                "expect": {"hasClass": {"selector": "#nav-home", "class": "active", "value": False}},
            },
            {
                "name": "Clicking Contact makes it active",
                "hidden": True,
                "steps": [{"click": "nav-contact"}],
                "expect": {"hasClass": {"selector": "#nav-contact", "class": "active", "value": True}},
            },
            {
                "name": "About is no longer active after Contact is clicked",
                "hidden": True,
                "steps": [],
                "expect": {"hasClass": {"selector": "#nav-about", "class": "active", "value": False}},
            },
        ],
    },
    {
        "id": 6014,
        "slug": "dom-step-progress-bar",
        "title": "Step Progress Bar",
        "difficulty": "Medium",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Styling with Classes"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Practice swapping one class for another to drive a visual change.</p>
<pre>&lt;div class="panel"&gt;
  &lt;div id="bar-track"&gt;
    &lt;div id="bar-fill" class="step-1"&gt;&lt;/div&gt;
  &lt;/div&gt;
  &lt;button id="next-btn"&gt;Next Step&lt;/button&gt;
&lt;/div&gt;</pre>
<p><code>#bar-fill</code> starts with class <code>"step-1"</code>. Write JavaScript so that
each click of <code>#next-btn</code> advances it:</p>
<ul>
  <li><code>"step-1"</code> &rarr; <code>"step-2"</code> &rarr; <code>"step-3"</code>.</li>
  <li>Once at <code>"step-3"</code>, further clicks do nothing more &mdash; it stays at
      <code>"step-3"</code> and never wraps back to <code>"step-1"</code>.</li>
</ul>
""",
        "hint": "Keep track of the current step number in a variable, remove the old step-N class "
                 "with classList.remove(...), then add the new one with classList.add(...) — clamp "
                 "the number so it never exceeds 3.",
        "boilerplate": {
            "javascript": """const barFill = document.getElementById('bar-fill');
const nextBtn = document.getElementById('next-btn');
let step = 1;

// TODO: on click, advance barFill's class from step-1 to step-2 to step-3, capped at step-3
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <div id="bar-track">
    <div id="bar-fill" class="step-1"></div>
  </div>
  <button id="next-btn">Next Step</button>
</div>""",
        "browser_style": CHUNK3_STYLE + CHUNK3_STYLE_6014_EXTRA,
        "browser_tests": [
            {
                "name": "Bar starts at step 1 (50px)",
                "hidden": False,
                "steps": [],
                "expect": {"css": {"selector": "#bar-fill", "property": "width", "value": "50px"}},
            },
            {
                "name": "One click advances to step 2 (100px)",
                "hidden": False,
                "steps": [{"click": "next-btn"}],
                "expect": {"css": {"selector": "#bar-fill", "property": "width", "value": "100px"}},
            },
            {
                "name": "Another click advances to step 3 (150px)",
                "hidden": True,
                "steps": [{"click": "next-btn"}],
                "expect": {"css": {"selector": "#bar-fill", "property": "width", "value": "150px"}},
            },
            {
                "name": "Further clicks stay capped at step 3 (150px)",
                "hidden": True,
                "steps": [{"click": "next-btn"}],
                "expect": {"css": {"selector": "#bar-fill", "property": "width", "value": "150px"}},
            },
        ],
    },
    {
        "id": 6015,
        "slug": "dom-flag-invalid-input",
        "title": "Flag Invalid Input",
        "difficulty": "Medium",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Styling with Classes"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Practice validating input live and reflecting the result with a class and a message.</p>
<pre>&lt;div class="panel"&gt;
  &lt;input type="text" id="age-input" placeholder="Your age"&gt;
  &lt;p id="hint-msg"&gt;&lt;/p&gt;
&lt;/div&gt;</pre>
<p>On every keystroke in <code>#age-input</code>, check whether the value is a valid
positive integer (no letters, no decimals, not empty, not zero, not negative):</p>
<ul>
  <li>If it's <b>not</b> valid, add the class <code>"error"</code> to
      <code>#age-input</code> and set <code>#hint-msg</code>'s text to
      <code>"Please enter a valid age."</code>.</li>
  <li>If it <b>is</b> valid, remove the class <code>"error"</code> from
      <code>#age-input</code> and clear <code>#hint-msg</code>'s text (empty string).</li>
</ul>
""",
        "hint": "A regex like /^[1-9]\\d*$/.test(value) is a clean way to check for a positive "
                 "integer, then use classList.add('error') / classList.remove('error') on the input "
                 "based on the result.",
        "boilerplate": {
            "javascript": """const ageInput = document.getElementById('age-input');
const hintMsg = document.getElementById('hint-msg');

// TODO: on input, flag ageInput with the 'error' class (and set hintMsg's text) when
// the value isn't a valid positive integer, otherwise clear both
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <input type="text" id="age-input" placeholder="Your age">
  <p id="hint-msg"></p>
</div>""",
        "browser_style": CHUNK3_STYLE,
        "browser_tests": [
            {
                "name": "No error before any typing",
                "hidden": False,
                "steps": [],
                "expect": {"hasClass": {"selector": "#age-input", "class": "error", "value": False}},
            },
            {
                "name": "Typing letters flags an error with a message",
                "hidden": False,
                "steps": [{"type": "age-input", "value": "abc"}],
                "expect": {
                    "hasClass": {"selector": "#age-input", "class": "error", "value": True},
                    "text": {"id": "hint-msg", "value": "Please enter a valid age."},
                },
            },
            {
                "name": "Typing a valid age clears the error and message",
                "hidden": True,
                "steps": [{"type": "age-input", "value": "25"}],
                "expect": {
                    "hasClass": {"selector": "#age-input", "class": "error", "value": False},
                    "text": {"id": "hint-msg", "value": ""},
                },
            },
            {
                "name": "Typing a negative number flags an error again",
                "hidden": True,
                "steps": [{"type": "age-input", "value": "-5"}],
                "expect": {"hasClass": {"selector": "#age-input", "class": "error", "value": True}},
            },
        ],
    },
]

# ============================================================================
# Chunk 4
# ============================================================================
"""
Chunk 4 — "Handling Events" — 5 browser-judge JS/DOM exercises (ids 6016-6020).
"""
import html as _html

CHUNK4_STYLE = """
body { font-family: -apple-system, "Segoe UI", sans-serif; display: flex; justify-content: center; padding-top: 50px; background: #fafafa; }
.panel { text-align: center; background: #fff; border: 1px solid #ddd; border-radius: 14px; padding: 28px 36px; min-width: 300px; box-shadow: 0 4px 18px rgba(0,0,0,.08); }
button, select { margin-top: 10px; padding: 9px 16px; font-size: 14px; border-radius: 8px; border: 1px solid #ccc; cursor: pointer; background: #f3f3f3; }
button:hover { background: #e8e8e8; }
input[type="text"] { padding: 8px 10px; font-size: 14px; border-radius: 6px; border: 1px solid #ccc; width: 200px; }
ul { list-style: none; padding: 0; text-align: left; }
li { padding: 8px 12px; margin: 4px 0; border-radius: 8px; background: #f3f3f3; cursor: pointer; }
li.selected { background: #4a90d9; color: #fff; }
li input[type="checkbox"] { margin-right: 8px; }
#output { margin-top: 14px; font-size: 15px; min-height: 20px; color: #222; }
"""


def _desc(browser_html, points):
    escaped = _html.escape(browser_html)
    items = "".join(f"<li>{p}</li>" for p in points)
    return f"<pre>{escaped}</pre><ul>{items}</ul>"


# ---------------------------------------------------------------------------
# 6016 — Ring the Bell
# ---------------------------------------------------------------------------

_6016_HTML = (
    '<div class="panel"><p id="output">Bell rung 0 times</p>'
    '<button id="bell-btn">Ring Bell</button></div>'
)

PROBLEM_6016 = {
    "id": 6016,
    "slug": "dom-ring-the-bell",
    "title": "Ring the Bell",
    "difficulty": "Easy",
    "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Handling Events"],
    "judge": "browser",
    "languages": ["javascript"],
    "description": _desc(_6016_HTML, [
        "Clicking <code>#bell-btn</code> increments an internal counter by 1, up to a maximum of 5.",
        "After each click, set <code>#output</code>'s text to exactly <code>Bell rung ${n} times</code>, where <code>n</code> is the current counter value.",
        "Once the counter reaches 5, further clicks must not increase it or change the text.",
    ]),
    "hint": "Store the counter in a variable outside the click handler so it persists between clicks, and check its value against the cap before incrementing.",
    "boilerplate": {
        "javascript": (
            "const bellBtn = document.getElementById('bell-btn');\n"
            "const output = document.getElementById('output');\n"
            "\n"
            "// TODO: keep a counter starting at 0, capped at a maximum of 5.\n"
            "// On each click of bellBtn, increment the counter (if below the cap)\n"
            "// and update output's text to `Bell rung ${n} times`.\n"
        )
    },
    "tests": [],
    "samples": [0, 1],
    "browser_html": _6016_HTML,
    "browser_style": CHUNK4_STYLE,
    "browser_tests": [
        {
            "name": "Initial state: shows 0",
            "hidden": False,
            "steps": [],
            "expect": {"text": {"id": "output", "value": "Bell rung 0 times"}},
        },
        {
            "name": "One click increments to 1",
            "hidden": False,
            "steps": [{"click": "bell-btn"}],
            "expect": {"text": {"id": "output", "value": "Bell rung 1 times"}},
        },
        {
            "name": "Clicking past the cap stops at 5",
            "hidden": True,
            # cumulative total clicks so far = 1 (above) + 9 = 10, deliberately overshoots the max
            "steps": [{"click": "bell-btn"} for _ in range(9)],
            "expect": {"text": {"id": "output", "value": "Bell rung 5 times"}},
        },
        {
            "name": "Further clicks stay capped at 5",
            "hidden": True,
            # cumulative total clicks so far = 11
            "steps": [{"click": "bell-btn"}],
            "expect": {"text": {"id": "output", "value": "Bell rung 5 times"}},
        },
    ],
}


# ---------------------------------------------------------------------------
# 6017 — Filter by Category Dropdown
# ---------------------------------------------------------------------------

_6017_HTML = (
    '<div class="panel">'
    '<select id="category-select">'
    '<option value="all">All</option>'
    '<option value="fruit">Fruit</option>'
    '<option value="veg">Vegetable</option>'
    '</select>'
    '<ul id="produce-list">'
    '<li class="produce" data-cat="fruit">Apple</li>'
    '<li class="produce" data-cat="veg">Carrot</li>'
    '<li class="produce" data-cat="fruit">Banana</li>'
    '<li class="produce" data-cat="veg">Potato</li>'
    '</ul></div>'
)

PROBLEM_6017 = {
    "id": 6017,
    "slug": "dom-filter-by-category-dropdown",
    "title": "Filter by Category Dropdown",
    "difficulty": "Medium",
    "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Handling Events"],
    "judge": "browser",
    "languages": ["javascript"],
    "description": _desc(_6017_HTML, [
        "Listen for the <code>change</code> event on <code>#category-select</code>.",
        "When it fires, show only the <code>.produce</code> items whose <code>data-cat</code> attribute equals the selected value (<code>style.display = ''</code>).",
        "Hide every other <code>.produce</code> item (<code>style.display = 'none'</code>).",
        "The value <code>\"all\"</code> must show every item.",
    ]),
    "hint": "Listen for the select's change event, read its .value, and compare it against each item's dataset.cat to decide whether to show or hide it.",
    "boilerplate": {
        "javascript": (
            "const categorySelect = document.getElementById('category-select');\n"
            "const produceItems = document.querySelectorAll('.produce');\n"
            "\n"
            "// TODO: on change of categorySelect, show only .produce items whose\n"
            "// data-cat matches the selected value; hide the rest. \"all\" shows everything.\n"
        )
    },
    "tests": [],
    "samples": [0, 1],
    "browser_html": _6017_HTML,
    "browser_style": CHUNK4_STYLE,
    "browser_tests": [
        {
            "name": "Initial state: all items visible",
            "hidden": False,
            "steps": [],
            "expect": {"visibleList": {
                "selector": "#produce-list li",
                "visible": ["Apple", "Carrot", "Banana", "Potato"],
                "hidden": [],
            }},
        },
        {
            "name": "Selecting fruit shows only fruit",
            "hidden": False,
            "steps": [{"select": {"id": "category-select", "value": "fruit"}}],
            "expect": {"visibleList": {
                "selector": "#produce-list li",
                "visible": ["Apple", "Banana"],
                "hidden": ["Carrot", "Potato"],
            }},
        },
        {
            "name": "Selecting vegetable shows only vegetables",
            "hidden": True,
            "steps": [{"select": {"id": "category-select", "value": "veg"}}],
            "expect": {"visibleList": {
                "selector": "#produce-list li",
                "visible": ["Carrot", "Potato"],
                "hidden": ["Apple", "Banana"],
            }},
        },
        {
            "name": "Selecting all shows everything again",
            "hidden": True,
            "steps": [{"select": {"id": "category-select", "value": "all"}}],
            "expect": {"visibleList": {
                "selector": "#produce-list li",
                "visible": ["Apple", "Carrot", "Banana", "Potato"],
                "hidden": [],
            }},
        },
    ],
}


# ---------------------------------------------------------------------------
# 6018 — Event Delegation Highlight
# ---------------------------------------------------------------------------

_6018_HTML = (
    '<div class="panel"><ul id="task-list">'
    '<li id="task-1" class="task">Buy milk</li>'
    '<li id="task-2" class="task">Walk dog</li>'
    '<li id="task-3" class="task">Read book</li>'
    '</ul><p id="output">Click a task</p></div>'
)

PROBLEM_6018 = {
    "id": 6018,
    "slug": "dom-event-delegation-highlight",
    "title": "Event Delegation Highlight",
    "difficulty": "Medium",
    "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Handling Events"],
    "judge": "browser",
    "languages": ["javascript"],
    "description": _desc(_6018_HTML, [
        "Attach exactly ONE click listener, on <code>#task-list</code> itself — not one listener per <code>&lt;li&gt;</code>. Use event delegation via <code>event.target</code> to work out which task was clicked.",
        "On click, remove the class <code>selected</code> from every <code>.task</code> item, then add it to the one that was clicked.",
        "Set <code>#output</code>'s text to exactly <code>Selected: ${text}</code>, where <code>text</code> is the clicked task's text.",
    ]),
    "hint": "Use event delegation: attach a single click listener to #task-list and use event.target inside the handler to figure out which .task was actually clicked.",
    "boilerplate": {
        "javascript": (
            "const taskList = document.getElementById('task-list');\n"
            "const output = document.getElementById('output');\n"
            "const tasks = document.querySelectorAll('.task');\n"
            "\n"
            "// TODO: attach exactly ONE click listener on taskList (event delegation).\n"
            "// Inside the handler, use event.target to find which .task was clicked,\n"
            "// remove the \"selected\" class from all tasks, add it to the clicked one,\n"
            "// and set output's text to `Selected: ${text}`.\n"
        )
    },
    "tests": [],
    "samples": [0, 1],
    "browser_html": _6018_HTML,
    "browser_style": CHUNK4_STYLE,
    "browser_tests": [
        {
            "name": "Initial state: nothing selected",
            "hidden": False,
            "steps": [],
            "expect": {
                "hasClass": {"selector": "#task-1", "class": "selected", "value": False},
                "text": {"id": "output", "value": "Click a task"},
            },
        },
        {
            "name": "Clicking task-2 selects it",
            "hidden": False,
            "steps": [{"click": "task-2"}],
            "expect": {
                "hasClass": {"selector": "#task-2", "class": "selected", "value": True},
                "text": {"id": "output", "value": "Selected: Walk dog"},
            },
        },
        {
            "name": "Clicking task-2 deselects task-1",
            "hidden": False,
            "steps": [],
            "expect": {"hasClass": {"selector": "#task-1", "class": "selected", "value": False}},
        },
        {
            "name": "Clicking task-3 selects it",
            "hidden": True,
            "steps": [{"click": "task-3"}],
            "expect": {
                "hasClass": {"selector": "#task-3", "class": "selected", "value": True},
                "text": {"id": "output", "value": "Selected: Read book"},
            },
        },
        {
            "name": "Clicking task-3 deselects task-2",
            "hidden": True,
            "steps": [],
            "expect": {"hasClass": {"selector": "#task-2", "class": "selected", "value": False}},
        },
    ],
}


# ---------------------------------------------------------------------------
# 6019 — Live Search Box
# ---------------------------------------------------------------------------

_6019_HTML = (
    '<div class="panel">'
    '<input type="text" id="search-input" placeholder="Search animals">'
    '<ul id="animal-list">'
    '<li class="animal">Lion</li>'
    '<li class="animal">Tiger</li>'
    '<li class="animal">Zebra</li>'
    '<li class="animal">Leopard</li>'
    '</ul></div>'
)

PROBLEM_6019 = {
    "id": 6019,
    "slug": "dom-live-search-box",
    "title": "Live Search Box",
    "difficulty": "Medium",
    "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Handling Events"],
    "judge": "browser",
    "languages": ["javascript"],
    "description": _desc(_6019_HTML, [
        "Listen for the <code>input</code> event on <code>#search-input</code>.",
        "On every input, show only the <code>.animal</code> items whose text (case-insensitive) includes the current search term.",
        "Hide every <code>.animal</code> item that doesn't match.",
        "An empty search term must show all items.",
    ]),
    "hint": "Listen for the input event on the search box, lowercase both the query and each item's text, and use String.includes to decide visibility.",
    "boilerplate": {
        "javascript": (
            "const searchInput = document.getElementById('search-input');\n"
            "const animalItems = document.querySelectorAll('.animal');\n"
            "\n"
            "// TODO: on input, filter animalItems: show only those whose text\n"
            "// (case-insensitive) includes the current search term; empty term shows all.\n"
        )
    },
    "tests": [],
    "samples": [0, 1],
    "browser_html": _6019_HTML,
    "browser_style": CHUNK4_STYLE,
    "browser_tests": [
        {
            "name": "Initial state: all animals visible",
            "hidden": False,
            "steps": [],
            "expect": {"visibleList": {
                "selector": "#animal-list li",
                "visible": ["Lion", "Tiger", "Zebra", "Leopard"],
                "hidden": [],
            }},
        },
        {
            "name": "Typing 'e' filters to matches",
            "hidden": False,
            "steps": [{"type": "search-input", "value": "e"}],
            "expect": {"visibleList": {
                "selector": "#animal-list li",
                "visible": ["Tiger", "Zebra", "Leopard"],
                "hidden": ["Lion"],
            }},
        },
        {
            "name": "Clearing the search shows everything again",
            "hidden": True,
            "steps": [{"type": "search-input", "value": ""}],
            "expect": {"visibleList": {
                "selector": "#animal-list li",
                "visible": ["Lion", "Tiger", "Zebra", "Leopard"],
                "hidden": [],
            }},
        },
        {
            "name": "Search is case-insensitive",
            "hidden": True,
            "steps": [{"type": "search-input", "value": "z"}],
            "expect": {"visibleList": {
                "selector": "#animal-list li",
                "visible": ["Zebra"],
                "hidden": ["Lion", "Tiger", "Leopard"],
            }},
        },
    ],
}


# ---------------------------------------------------------------------------
# 6020 — Mark Task Done via Checkbox
# ---------------------------------------------------------------------------

_6020_HTML = (
    '<div class="panel"><ul id="todo-list">'
    '<li id="row-1"><input type="checkbox" id="chk-1"> Buy milk</li>'
    '<li id="row-2"><input type="checkbox" id="chk-2"> Walk dog</li>'
    '<li id="row-3"><input type="checkbox" id="chk-3"> Read book</li>'
    '</ul><p id="output">0 of 3 done</p></div>'
)

PROBLEM_6020 = {
    "id": 6020,
    "slug": "dom-mark-task-done-via-checkbox",
    "title": "Mark Task Done via Checkbox",
    "difficulty": "Medium",
    "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Handling Events"],
    "judge": "browser",
    "languages": ["javascript"],
    "description": _desc(_6020_HTML, [
        "Listen for the <code>change</code> event on each checkbox inside <code>#todo-list</code>.",
        "Whenever any checkbox changes, recompute how many checkboxes are currently checked and set <code>#output</code>'s text to exactly <code>${n} of 3 done</code>.",
        "Also toggle the class <code>done</code> on that checkbox's parent <code>&lt;li&gt;</code> so it matches the checkbox's checked state.",
    ]),
    "hint": "Attach a change listener to each checkbox (or use event delegation on the list) and recompute the checked count from scratch each time, rather than trying to increment or decrement a running total.",
    "boilerplate": {
        "javascript": (
            "const checkboxes = document.querySelectorAll('#todo-list input[type=\"checkbox\"]');\n"
            "const output = document.getElementById('output');\n"
            "\n"
            "// TODO: on change of any checkbox, recompute the count of checked boxes and\n"
            "// set output's text to `${n} of 3 done`. Also toggle the \"done\" class on\n"
            "// that checkbox's parent <li> to match its checked state.\n"
        )
    },
    "tests": [],
    "samples": [0, 1],
    "browser_html": _6020_HTML,
    "browser_style": CHUNK4_STYLE,
    "browser_tests": [
        {
            "name": "Initial state: none done",
            "hidden": False,
            "steps": [],
            "expect": {
                "text": {"id": "output", "value": "0 of 3 done"},
                "hasClass": {"selector": "#row-1", "class": "done", "value": False},
            },
        },
        {
            "name": "Checking chk-1 marks it done",
            "hidden": False,
            "steps": [{"click": "chk-1"}],
            "expect": {
                "text": {"id": "output", "value": "1 of 3 done"},
                "hasClass": {"selector": "#row-1", "class": "done", "value": True},
            },
        },
        {
            "name": "Checking chk-2 as well updates the count",
            "hidden": True,
            "steps": [{"click": "chk-2"}],
            "expect": {"text": {"id": "output", "value": "2 of 3 done"}},
        },
        {
            "name": "Unchecking chk-1 again decrements the count",
            "hidden": True,
            "steps": [{"click": "chk-1"}],
            "expect": {
                "text": {"id": "output", "value": "1 of 3 done"},
                "hasClass": {"selector": "#row-1", "class": "done", "value": False},
            },
        },
    ],
}


CHUNK4_PROBLEMS = [PROBLEM_6016, PROBLEM_6017, PROBLEM_6018, PROBLEM_6019, PROBLEM_6020]

# ============================================================================
# Chunk 5
# ============================================================================
CHUNK5_STYLE = """
body { font-family: -apple-system, "Segoe UI", sans-serif; display: flex; justify-content: center; padding-top: 50px; background: #fafafa; }
.panel { text-align: center; background: #fff; border: 1px solid #ddd; border-radius: 14px; padding: 28px 36px; min-width: 300px; box-shadow: 0 4px 18px rgba(0,0,0,.08); }
button { margin-top: 10px; padding: 9px 16px; font-size: 14px; border-radius: 8px; border: 1px solid #ccc; cursor: pointer; background: #f3f3f3; }
button:hover { background: #e8e8e8; }
input[type="text"] { padding: 8px 10px; font-size: 14px; border-radius: 6px; border: 1px solid #ccc; width: 200px; }
ul { list-style: none; padding: 0; text-align: left; margin-top: 12px; }
li { padding: 8px 12px; margin: 4px 0; border-radius: 8px; background: #f3f3f3; display: flex; justify-content: space-between; align-items: center; }
.remove-btn, .del-btn { background: #f5c2c2; border: none; border-radius: 6px; width: 24px; height: 24px; cursor: pointer; }
.card { background: #eef4fb; border: 1px solid #cdddee; border-radius: 8px; padding: 14px; margin: 8px 0; }
"""

CHUNK5_PROBLEMS = [
    {
        "id": 6021,
        "slug": "dom-add-item-to-a-to-do-list",
        "title": "Add Item to a To-Do List",
        "difficulty": "Medium",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Creating & Removing Elements"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Practice creating a brand new element and appending it to the DOM.</p>
<pre>&lt;div class="panel"&gt;
  &lt;input type="text" id="task-input" placeholder="New task"&gt;
  &lt;button id="add-btn"&gt;Add&lt;/button&gt;
  &lt;ul id="todo-list"&gt;&lt;/ul&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript so that clicking <code>#add-btn</code>:</p>
<ul>
  <li>If <code>#task-input</code>'s trimmed value is non-empty, creates a new
      <code>&lt;li&gt;</code> containing that text and appends it to
      <code>#todo-list</code>, then clears the input.</li>
  <li>If the trimmed value is empty (or only whitespace), does nothing.</li>
</ul>
""",
        "hint": "Use document.createElement('li') to build the new item, set its textContent, "
                 "then call todoList.appendChild(li) — check input.value.trim() first and bail out "
                 "early if it's empty.",
        "boilerplate": {
            "javascript": """const input = document.getElementById('task-input');
const addBtn = document.getElementById('add-btn');
const list = document.getElementById('todo-list');

addBtn.addEventListener('click', function() {
  // TODO: if input.value.trim() is non-empty, create a new <li> with that text,
  // append it to `list`, then clear the input value. If it's empty, do nothing.
});
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <input type="text" id="task-input" placeholder="New task">
  <button id="add-btn">Add</button>
  <ul id="todo-list"></ul>
</div>""",
        "browser_style": CHUNK5_STYLE,
        "browser_tests": [
            {
                "name": "List starts empty",
                "hidden": False,
                "steps": [],
                "expect": {"elemCount": {"selector": "#todo-list li", "value": 0}},
            },
            {
                "name": "Adding 'Buy milk' creates one item",
                "hidden": False,
                "steps": [
                    {"type": "task-input", "value": "Buy milk"},
                    {"click": "add-btn"},
                ],
                "expect": {
                    "elemCount": {"selector": "#todo-list li", "value": 1},
                    "exists": {"selector": "#todo-list li:last-child", "value": True, "text": "Buy milk"},
                },
            },
            {
                "name": "Adding 'Walk dog' creates a second item",
                "hidden": True,
                "steps": [
                    {"type": "task-input", "value": "Walk dog"},
                    {"click": "add-btn"},
                ],
                "expect": {
                    "elemCount": {"selector": "#todo-list li", "value": 2},
                    "exists": {"selector": "#todo-list li:last-child", "value": True, "text": "Walk dog"},
                },
            },
            {
                "name": "Clicking Add with an empty input does nothing",
                "hidden": True,
                "steps": [{"click": "add-btn"}],
                "expect": {"elemCount": {"selector": "#todo-list li", "value": 2}},
            },
        ],
    },
    {
        "id": 6022,
        "slug": "dom-remove-an-item-from-the-list",
        "title": "Remove an Item from the List",
        "difficulty": "Medium",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Creating & Removing Elements"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Practice removing an existing element from the DOM in response to a click.</p>
<pre>&lt;div class="panel"&gt;
  &lt;ul id="todo-list"&gt;
    &lt;li&gt;Buy milk &lt;button class="remove-btn" id="remove-0"&gt;x&lt;/button&gt;&lt;/li&gt;
    &lt;li&gt;Walk dog &lt;button class="remove-btn" id="remove-1"&gt;x&lt;/button&gt;&lt;/li&gt;
    &lt;li&gt;Read book &lt;button class="remove-btn" id="remove-2"&gt;x&lt;/button&gt;&lt;/li&gt;
  &lt;/ul&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript so that clicking any <code>.remove-btn</code> removes its own parent
<code>&lt;li&gt;</code> from the DOM (and only that one).</p>
""",
        "hint": "From inside the click handler, use event.target.closest('li').remove() (or "
                 "event.target.parentElement.remove()) to remove just the <li> that was clicked in.",
        "boilerplate": {
            "javascript": """const list = document.getElementById('todo-list');

list.addEventListener('click', function(event) {
  // TODO: if the clicked element has class "remove-btn", remove its closest
  // parent <li> from the DOM.
});
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <ul id="todo-list">
    <li>Buy milk <button class="remove-btn" id="remove-0">x</button></li>
    <li>Walk dog <button class="remove-btn" id="remove-1">x</button></li>
    <li>Read book <button class="remove-btn" id="remove-2">x</button></li>
  </ul>
</div>""",
        "browser_style": CHUNK5_STYLE,
        "browser_tests": [
            {
                "name": "List starts with 3 items",
                "hidden": False,
                "steps": [],
                "expect": {"elemCount": {"selector": "#todo-list li", "value": 3}},
            },
            {
                "name": "Removing 'Walk dog' leaves 2 items, 'Read book' shifts up",
                "hidden": False,
                "steps": [{"click": "remove-1"}],
                "expect": {
                    "elemCount": {"selector": "#todo-list li", "value": 2},
                    "exists": {"selector": "#todo-list li:nth-child(2)", "value": True, "text": "Read book x"},
                },
            },
            {
                "name": "Removing 'Buy milk' leaves only 'Read book'",
                "hidden": True,
                "steps": [{"click": "remove-0"}],
                "expect": {
                    "elemCount": {"selector": "#todo-list li", "value": 1},
                    "exists": {"selector": "#todo-list li:first-child", "value": True, "text": "Read book x"},
                },
            },
        ],
    },
    {
        "id": 6023,
        "slug": "dom-clear-all-items",
        "title": "Clear All Items",
        "difficulty": "Medium",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Creating & Removing Elements"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Practice removing every child of a container at once.</p>
<pre>&lt;div class="panel"&gt;
  &lt;ul id="todo-list"&gt;
    &lt;li&gt;Milk&lt;/li&gt;
    &lt;li&gt;Eggs&lt;/li&gt;
    &lt;li&gt;Bread&lt;/li&gt;
  &lt;/ul&gt;
  &lt;button id="clear-btn"&gt;Clear All&lt;/button&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript so that clicking <code>#clear-btn</code> removes every
<code>&lt;li&gt;</code> inside <code>#todo-list</code>, leaving it empty. Clicking it again
on an already-empty list should simply leave it empty (no error).</p>
""",
        "hint": "Setting todoList.innerHTML = '' wipes out all of its children in one step; an "
                 "empty list has nothing left to remove, so the same code is safe to run again.",
        "boilerplate": {
            "javascript": """const list = document.getElementById('todo-list');
const clearBtn = document.getElementById('clear-btn');

clearBtn.addEventListener('click', function() {
  // TODO: remove every <li> inside `list`.
});
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <ul id="todo-list">
    <li>Milk</li>
    <li>Eggs</li>
    <li>Bread</li>
  </ul>
  <button id="clear-btn">Clear All</button>
</div>""",
        "browser_style": CHUNK5_STYLE,
        "browser_tests": [
            {
                "name": "List starts with 3 items",
                "hidden": False,
                "steps": [],
                "expect": {"elemCount": {"selector": "#todo-list li", "value": 3}},
            },
            {
                "name": "Clicking Clear All empties the list",
                "hidden": False,
                "steps": [{"click": "clear-btn"}],
                "expect": {"elemCount": {"selector": "#todo-list li", "value": 0}},
            },
            {
                "name": "Clicking Clear All again on an empty list is a safe no-op",
                "hidden": True,
                "steps": [{"click": "clear-btn"}],
                "expect": {"elemCount": {"selector": "#todo-list li", "value": 0}},
            },
        ],
    },
    {
        "id": 6024,
        "slug": "dom-duplicate-a-card",
        "title": "Duplicate a Card",
        "difficulty": "Medium",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Creating & Removing Elements"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Practice cloning an existing element instead of building one from scratch.</p>
<pre>&lt;div class="panel"&gt;
  &lt;div id="card-container"&gt;
    &lt;div class="card" id="card-1"&gt;Original Card&lt;/div&gt;
  &lt;/div&gt;
  &lt;button id="dup-btn"&gt;Duplicate&lt;/button&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript so that each click of <code>#dup-btn</code> clones
<code>#card-1</code> (including its content) and appends the clone into
<code>#card-container</code>, so the number of <code>.card</code> elements grows by one
every click.</p>
""",
        "hint": "card.cloneNode(true) makes a deep copy of the element and its content, which you "
                 "then append into the container with appendChild. Note the clone will keep the same "
                 "id as the original — that's technically invalid HTML, but harmless here, so there's "
                 "no need to strip it.",
        "boilerplate": {
            "javascript": """const card = document.getElementById('card-1');
const container = document.getElementById('card-container');
const dupBtn = document.getElementById('dup-btn');

dupBtn.addEventListener('click', function() {
  // TODO: clone `card` (including its content) and append the clone into `container`.
});
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <div id="card-container">
    <div class="card" id="card-1">Original Card</div>
  </div>
  <button id="dup-btn">Duplicate</button>
</div>""",
        "browser_style": CHUNK5_STYLE,
        "browser_tests": [
            {
                "name": "Starts with 1 card",
                "hidden": False,
                "steps": [],
                "expect": {"elemCount": {"selector": ".card", "value": 1}},
            },
            {
                "name": "Clicking Duplicate creates a second card",
                "hidden": False,
                "steps": [{"click": "dup-btn"}],
                "expect": {
                    "elemCount": {"selector": ".card", "value": 2},
                    "exists": {"selector": ".card", "value": True, "text": "Original Card"},
                },
            },
            {
                "name": "Clicking Duplicate again creates a third card",
                "hidden": True,
                "steps": [{"click": "dup-btn"}],
                "expect": {"elemCount": {"selector": ".card", "value": 3}},
            },
        ],
    },
    {
        "id": 6025,
        "slug": "dom-insert-a-new-item-at-the-top",
        "title": "Insert a New Item at the Top",
        "difficulty": "Medium",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Creating & Removing Elements"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Practice inserting a new element at a specific position instead of always at the end.</p>
<pre>&lt;div class="panel"&gt;
  &lt;input type="text" id="task-input" placeholder="New task"&gt;
  &lt;button id="add-top-btn"&gt;Add to Top&lt;/button&gt;
  &lt;ul id="todo-list"&gt;
    &lt;li&gt;Existing task&lt;/li&gt;
  &lt;/ul&gt;
&lt;/div&gt;</pre>
<p>Write JavaScript so that clicking <code>#add-top-btn</code>:</p>
<ul>
  <li>If <code>#task-input</code>'s trimmed value is non-empty, creates a new
      <code>&lt;li&gt;</code> containing that text and inserts it as the <b>first</b> child
      of <code>#todo-list</code> (not appended at the end), then clears the input.</li>
  <li>If the trimmed value is empty (or only whitespace), does nothing.</li>
</ul>
""",
        "hint": "Build the new <li> with document.createElement the same way you would to append "
                 "one, but insert it at the front with todoList.prepend(li) (or "
                 "todoList.insertBefore(li, todoList.firstChild)) instead of appendChild.",
        "boilerplate": {
            "javascript": """const input = document.getElementById('task-input');
const addTopBtn = document.getElementById('add-top-btn');
const list = document.getElementById('todo-list');

addTopBtn.addEventListener('click', function() {
  // TODO: if input.value.trim() is non-empty, create a new <li> with that text
  // and insert it as the FIRST child of `list` (not appended at the end),
  // then clear the input. If it's empty, do nothing.
});
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <input type="text" id="task-input" placeholder="New task">
  <button id="add-top-btn">Add to Top</button>
  <ul id="todo-list">
    <li>Existing task</li>
  </ul>
</div>""",
        "browser_style": CHUNK5_STYLE,
        "browser_tests": [
            {
                "name": "List starts with the existing task first",
                "hidden": False,
                "steps": [],
                "expect": {
                    "elemCount": {"selector": "#todo-list li", "value": 1},
                    "exists": {"selector": "#todo-list li:first-child", "value": True, "text": "Existing task"},
                },
            },
            {
                "name": "Adding 'Urgent task' puts it at the top",
                "hidden": False,
                "steps": [
                    {"type": "task-input", "value": "Urgent task"},
                    {"click": "add-top-btn"},
                ],
                "expect": {
                    "elemCount": {"selector": "#todo-list li", "value": 2},
                    "exists": {"selector": "#todo-list li:first-child", "value": True, "text": "Urgent task"},
                },
            },
            {
                "name": "Adding another item still goes to the very top",
                "hidden": True,
                "steps": [
                    {"type": "task-input", "value": "Even more urgent"},
                    {"click": "add-top-btn"},
                ],
                "expect": {
                    "elemCount": {"selector": "#todo-list li", "value": 3},
                    "exists": {"selector": "#todo-list li:first-child", "value": True, "text": "Even more urgent"},
                },
            },
        ],
    },
]

# ============================================================================
# Chunk 6
# ============================================================================
"""
Chunk 6 — "DOM Traversal" — 5 browser-judge JS/DOM exercises (ids 6026-6030).
"""
import html as _html

CHUNK6_STYLE = """
body { font-family: -apple-system, "Segoe UI", sans-serif; display: flex; justify-content: center; padding-top: 50px; background: #fafafa; }
.panel { text-align: center; background: #fff; border: 1px solid #ddd; border-radius: 14px; padding: 28px 36px; min-width: 320px; box-shadow: 0 4px 18px rgba(0,0,0,.08); }
table { border-collapse: collapse; width: 100%; margin-top: 10px; }
td { border: 1px solid #ddd; padding: 8px 12px; text-align: left; }
tr.selected td { background: #dbeafe; }
button { padding: 6px 12px; font-size: 13px; border-radius: 6px; border: 1px solid #ccc; cursor: pointer; background: #f3f3f3; }
button:hover { background: #e8e8e8; }
ol { list-style: none; padding: 0; display: flex; gap: 8px; justify-content: center; margin: 14px 0; }
.step { padding: 8px 14px; border-radius: 8px; background: #eee; font-size: 13px; }
.step.current { background: #4a90d9; color: #fff; font-weight: 600; }
#container { border: 1px dashed #ccc; padding: 10px; margin: 10px 0; text-align: left; }
#output { margin-top: 12px; font-size: 15px; min-height: 20px; }
.accordion-section { border: 1px solid #ddd; border-radius: 8px; margin: 8px 0; overflow: hidden; }
.acc-header { width: 100%; padding: 10px; background: #f3f3f3; border: none; cursor: pointer; font-size: 14px; }
.acc-body { padding: 10px; text-align: left; font-size: 13px; }
.acc-body.hidden { display: none; }
ul#item-list { list-style: none; padding: 0; text-align: left; }
ul#item-list li { padding: 8px 12px; margin: 4px 0; border-radius: 8px; background: #f3f3f3; display: flex; justify-content: space-between; }
.del-btn { background: #f5c2c2; border: none; border-radius: 6px; width: 22px; cursor: pointer; }
"""


def _desc(browser_html, points):
    escaped = _html.escape(browser_html)
    items = "".join(f"<li>{p}</li>" for p in points)
    return f"<pre>{escaped}</pre><ul>{items}</ul>"


# ---------------------------------------------------------------------------
# 6026 — Highlight the Row via a Button Inside It
# ---------------------------------------------------------------------------

_6026_HTML = (
    '<div class="panel"><table id="data-table"><tbody>'
    '<tr id="row-1"><td>Alice</td><td><button id="pick-1">Select</button></td></tr>'
    '<tr id="row-2"><td>Bob</td><td><button id="pick-2">Select</button></td></tr>'
    '<tr id="row-3"><td>Carol</td><td><button id="pick-3">Select</button></td></tr>'
    '</tbody></table></div>'
)

PROBLEM_6026 = {
    "id": 6026,
    "slug": "dom-highlight-the-row-via-a-button-inside-it",
    "title": "Highlight the Row via a Button Inside It",
    "difficulty": "Medium",
    "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "DOM Traversal"],
    "judge": "browser",
    "languages": ["javascript"],
    "description": _desc(_6026_HTML, [
        "Each row has a \"Select\" button inside it. Clicking any button should highlight that button's OWN row, not some other row.",
        "On click, use <code>event.target.closest('tr')</code> to find the row the clicked button lives in.",
        "Remove the class <code>selected</code> from ALL rows, then add <code>selected</code> to that one row (the <code>&lt;tr&gt;</code> itself, not the button).",
    ]),
    "hint": "You don't need one listener per button — use event.target.closest('tr') inside a single delegated click handler to walk up from the clicked button to its containing row.",
    "boilerplate": {
        "javascript": (
            "const table = document.getElementById('data-table');\n"
            "\n"
            "// TODO: listen for clicks on table (event delegation). When a \"Select\"\n"
            "// button is clicked, use event.target.closest('tr') to find its own row,\n"
            "// remove the \"selected\" class from every row, then add \"selected\" to\n"
            "// that one row.\n"
        )
    },
    "tests": [],
    "samples": [0, 1],
    "browser_html": _6026_HTML,
    "browser_style": CHUNK6_STYLE,
    "browser_tests": [
        {
            "name": "Initial state: no row selected",
            "hidden": False,
            "steps": [],
            "expect": {"hasClass": {"selector": "#row-1", "class": "selected", "value": False}},
        },
        {
            "name": "Clicking pick-2 selects row-2",
            "hidden": False,
            "steps": [{"click": "pick-2"}],
            "expect": {"hasClass": {"selector": "#row-2", "class": "selected", "value": True}},
        },
        {
            "name": "Selecting row-2 leaves row-1 unselected",
            "hidden": False,
            "steps": [],
            "expect": {"hasClass": {"selector": "#row-1", "class": "selected", "value": False}},
        },
        {
            "name": "Clicking pick-3 selects row-3",
            "hidden": True,
            "steps": [{"click": "pick-3"}],
            "expect": {"hasClass": {"selector": "#row-3", "class": "selected", "value": True}},
        },
        {
            "name": "Selecting row-3 deselects row-2",
            "hidden": True,
            "steps": [],
            "expect": {"hasClass": {"selector": "#row-2", "class": "selected", "value": False}},
        },
    ],
}


# ---------------------------------------------------------------------------
# 6027 — Step-by-Step Wizard
# ---------------------------------------------------------------------------

_6027_HTML = (
    '<div class="panel"><ol id="steps">'
    '<li id="step-1" class="step current">Details</li>'
    '<li id="step-2" class="step">Payment</li>'
    '<li id="step-3" class="step">Confirm</li>'
    '</ol><button id="next-step-btn">Next</button></div>'
)

PROBLEM_6027 = {
    "id": 6027,
    "slug": "dom-step-by-step-wizard",
    "title": "Step-by-Step Wizard",
    "difficulty": "Medium",
    "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "DOM Traversal"],
    "judge": "browser",
    "languages": ["javascript"],
    "description": _desc(_6027_HTML, [
        "Clicking <code>#next-step-btn</code> advances the wizard to the next step.",
        "Find the <code>.step</code> element that currently has class <code>current</code>, remove that class from it, and add <code>current</code> to its <code>nextElementSibling</code>.",
        "If the current step is already the last one, do nothing — stay on the last step.",
    ]),
    "hint": "Use document.querySelector('.step.current') to find the active step, then move to currentStep.nextElementSibling — but check it exists first, since the last step has none.",
    "boilerplate": {
        "javascript": (
            "const nextStepBtn = document.getElementById('next-step-btn');\n"
            "\n"
            "// TODO: on click, find the .step with class \"current\", remove \"current\"\n"
            "// from it, and add \"current\" to its nextElementSibling — unless it's\n"
            "// already the last step, in which case do nothing.\n"
        )
    },
    "tests": [],
    "samples": [0, 1],
    "browser_html": _6027_HTML,
    "browser_style": CHUNK6_STYLE,
    "browser_tests": [
        {
            "name": "Initial state: step-1 is current",
            "hidden": False,
            "steps": [],
            "expect": {"hasClass": {"selector": "#step-1", "class": "current", "value": True}},
        },
        {
            "name": "Clicking next moves to step-2",
            "hidden": False,
            "steps": [{"click": "next-step-btn"}],
            "expect": {"hasClass": {"selector": "#step-2", "class": "current", "value": True}},
        },
        {
            "name": "step-1 is no longer current",
            "hidden": False,
            "steps": [],
            "expect": {"hasClass": {"selector": "#step-1", "class": "current", "value": False}},
        },
        {
            "name": "Clicking next again moves to step-3",
            "hidden": True,
            "steps": [{"click": "next-step-btn"}],
            "expect": {"hasClass": {"selector": "#step-3", "class": "current", "value": True}},
        },
        {
            "name": "step-2 is no longer current",
            "hidden": True,
            "steps": [],
            "expect": {"hasClass": {"selector": "#step-2", "class": "current", "value": False}},
        },
        {
            "name": "Clicking next at the last step does nothing",
            "hidden": True,
            "steps": [{"click": "next-step-btn"}],
            "expect": {"hasClass": {"selector": "#step-3", "class": "current", "value": True}},
        },
    ],
}


# ---------------------------------------------------------------------------
# 6028 — Count Direct Children Only
# ---------------------------------------------------------------------------

_6028_HTML = (
    '<div class="panel"><div id="container">'
    '<p>One</p><div><span>Nested, doesn\'t count</span></div><p>Two</p>'
    '</div><p id="output"></p><button id="count-children-btn">Count Direct Children</button></div>'
)

PROBLEM_6028 = {
    "id": 6028,
    "slug": "dom-count-direct-children-only",
    "title": "Count Direct Children Only",
    "difficulty": "Medium",
    "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "DOM Traversal"],
    "judge": "browser",
    "languages": ["javascript"],
    "description": _desc(_6028_HTML, [
        "<code>#container</code> holds two <code>&lt;p&gt;</code> elements and one <code>&lt;div&gt;</code> (which itself contains a nested <code>&lt;span&gt;</code>).",
        "Clicking <code>#count-children-btn</code> sets <code>#output</code>'s text to exactly <code>${n} direct children</code>, where <code>n</code> counts ONLY <code>#container</code>'s direct children (3), not the nested <code>&lt;span&gt;</code>.",
    ]),
    "hint": "Use container.children.length, not querySelectorAll('*') — .children only returns direct child elements, ignoring anything nested deeper.",
    "boilerplate": {
        "javascript": (
            "const container = document.getElementById('container');\n"
            "const output = document.getElementById('output');\n"
            "const countChildrenBtn = document.getElementById('count-children-btn');\n"
            "\n"
            "// TODO: on click, set output's text to `${n} direct children`, where n is\n"
            "// container.children.length (direct children only, not nested descendants).\n"
        )
    },
    "tests": [],
    "samples": [0, 1],
    "browser_html": _6028_HTML,
    "browser_style": CHUNK6_STYLE,
    "browser_tests": [
        {
            "name": "Initial state: output is empty",
            "hidden": False,
            "steps": [],
            "expect": {"text": {"id": "output", "value": ""}},
        },
        {
            "name": "Clicking counts 3 direct children",
            "hidden": False,
            "steps": [{"click": "count-children-btn"}],
            "expect": {"text": {"id": "output", "value": "3 direct children"}},
        },
        {
            "name": "Clicking again gives the same count",
            "hidden": True,
            "steps": [{"click": "count-children-btn"}],
            "expect": {"text": {"id": "output", "value": "3 direct children"}},
        },
    ],
}


# ---------------------------------------------------------------------------
# 6029 — Independent Accordion Sections
# ---------------------------------------------------------------------------

_6029_HTML = (
    '<div class="panel">'
    '<div class="accordion-section"><button class="acc-header" id="head-1">Section 1</button>'
    '<div class="acc-body hidden" id="body-1">Content 1</div></div>'
    '<div class="accordion-section"><button class="acc-header" id="head-2">Section 2</button>'
    '<div class="acc-body hidden" id="body-2">Content 2</div></div>'
    '</div>'
)

PROBLEM_6029 = {
    "id": 6029,
    "slug": "dom-independent-accordion-sections",
    "title": "Independent Accordion Sections",
    "difficulty": "Medium",
    "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "DOM Traversal"],
    "judge": "browser",
    "languages": ["javascript"],
    "description": _desc(_6029_HTML, [
        "There are two independent accordion sections, each with its own header and body.",
        "Clicking a header must toggle the class <code>hidden</code> on ITS OWN <code>.acc-body</code> only — never the other section's body.",
        "Use <code>event.target.closest('.accordion-section')</code> to find the clicked header's own section, then <code>.querySelector('.acc-body')</code> inside it to find its own body.",
    ]),
    "hint": "Scope your lookup with event.target.closest('.accordion-section').querySelector('.acc-body') so each header only ever touches the body inside its own section.",
    "boilerplate": {
        "javascript": (
            "const headers = document.querySelectorAll('.acc-header');\n"
            "\n"
            "// TODO: for each header, listen for clicks. Inside the handler, use\n"
            "// event.target.closest('.accordion-section').querySelector('.acc-body')\n"
            "// to find that header's OWN body, and toggle the \"hidden\" class on it.\n"
            "// Clicking one header must never affect the other section's body.\n"
        )
    },
    "tests": [],
    "samples": [0, 1],
    "browser_html": _6029_HTML,
    "browser_style": CHUNK6_STYLE,
    "browser_tests": [
        {
            "name": "Initial state: body-1 is hidden",
            "hidden": False,
            "steps": [],
            "expect": {"hasClass": {"selector": "#body-1", "class": "hidden", "value": True}},
        },
        {
            "name": "Initial state: body-2 is hidden",
            "hidden": False,
            "steps": [],
            "expect": {"hasClass": {"selector": "#body-2", "class": "hidden", "value": True}},
        },
        {
            "name": "Clicking head-1 opens body-1",
            "hidden": False,
            "steps": [{"click": "head-1"}],
            "expect": {"hasClass": {"selector": "#body-1", "class": "hidden", "value": False}},
        },
        {
            "name": "Opening body-1 leaves body-2 untouched (still hidden)",
            "hidden": False,
            "steps": [],
            "expect": {"hasClass": {"selector": "#body-2", "class": "hidden", "value": True}},
        },
        {
            "name": "Clicking head-2 opens body-2",
            "hidden": True,
            "steps": [{"click": "head-2"}],
            "expect": {"hasClass": {"selector": "#body-2", "class": "hidden", "value": False}},
        },
        {
            "name": "Opening body-2 leaves body-1 untouched (still open)",
            "hidden": True,
            "steps": [],
            "expect": {"hasClass": {"selector": "#body-1", "class": "hidden", "value": False}},
        },
        {
            "name": "Clicking head-1 again closes body-1",
            "hidden": True,
            "steps": [{"click": "head-1"}],
            "expect": {"hasClass": {"selector": "#body-1", "class": "hidden", "value": True}},
        },
        {
            "name": "Closing body-1 leaves body-2 untouched (still open)",
            "hidden": True,
            "steps": [],
            "expect": {"hasClass": {"selector": "#body-2", "class": "hidden", "value": False}},
        },
    ],
}


# ---------------------------------------------------------------------------
# 6030 — Remove via the Closest List Item
# ---------------------------------------------------------------------------

_6030_HTML = (
    '<div class="panel"><ul id="item-list">'
    '<li>Apples <button class="del-btn" id="del-1">x</button></li>'
    '<li>Bananas <button class="del-btn" id="del-2">x</button></li>'
    '<li>Cherries <button class="del-btn" id="del-3">x</button></li>'
    '</ul></div>'
)

PROBLEM_6030 = {
    "id": 6030,
    "slug": "dom-remove-via-the-closest-list-item",
    "title": "Remove via the Closest List Item",
    "difficulty": "Medium",
    "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "DOM Traversal"],
    "judge": "browser",
    "languages": ["javascript"],
    "description": _desc(_6030_HTML, [
        "Each list item has its own \"x\" delete button.",
        "Clicking any <code>.del-btn</code> should remove ONLY its own containing <code>&lt;li&gt;</code> from <code>#item-list</code>.",
        "Use <code>event.target.closest('li').remove()</code> to do this — do not track indexes manually.",
    ]),
    "hint": "closest('li') walks up from the clicked button to find its containing list item directly, so you never need to compute or store a manual index for it.",
    "boilerplate": {
        "javascript": (
            "const itemList = document.getElementById('item-list');\n"
            "\n"
            "// TODO: listen for clicks on itemList (event delegation). When a\n"
            "// .del-btn is clicked, use event.target.closest('li').remove() to\n"
            "// remove its own containing <li>.\n"
        )
    },
    "tests": [],
    "samples": [0, 1],
    "browser_html": _6030_HTML,
    "browser_style": CHUNK6_STYLE,
    "browser_tests": [
        {
            "name": "Initial state: 3 items",
            "hidden": False,
            "steps": [],
            "expect": {"elemCount": {"selector": "#item-list li", "value": 3}},
        },
        {
            "name": "Deleting Bananas leaves 2 items",
            "hidden": False,
            "steps": [{"click": "del-2"}],
            "expect": {"elemCount": {"selector": "#item-list li", "value": 2}},
        },
        {
            "name": "Cherries shifts up to the 2nd position",
            "hidden": False,
            "steps": [],
            "expect": {"exists": {"selector": "#item-list li:nth-child(2)", "value": True, "text": "Cherries x"}},
        },
        {
            "name": "Deleting Apples leaves 1 item",
            "hidden": True,
            "steps": [{"click": "del-1"}],
            "expect": {"elemCount": {"selector": "#item-list li", "value": 1}},
        },
        {
            "name": "Cherries is now the only (first) item",
            "hidden": True,
            "steps": [],
            "expect": {"exists": {"selector": "#item-list li:first-child", "value": True, "text": "Cherries x"}},
        },
    ],
}


CHUNK6_PROBLEMS = [PROBLEM_6026, PROBLEM_6027, PROBLEM_6028, PROBLEM_6029, PROBLEM_6030]

# ============================================================================
# Chunk 7
# ============================================================================
"""
Chunk 7 — "Working with Forms" — 5 browser-judge DOM exercises (ids 6031-6035).
"""
import html as _html


CHUNK7_STYLE = """
body { font-family: -apple-system, "Segoe UI", sans-serif; display: flex; justify-content: center; padding-top: 50px; background: #fafafa; }
.panel { text-align: center; background: #fff; border: 1px solid #ddd; border-radius: 14px; padding: 28px 36px; min-width: 300px; box-shadow: 0 4px 18px rgba(0,0,0,.08); }
input[type="text"], input[type="password"], input[type="number"], select { padding: 8px 10px; font-size: 14px; border-radius: 6px; border: 1px solid #ccc; width: 200px; margin: 6px 0; display: block; }
button { margin-top: 10px; padding: 9px 16px; font-size: 14px; border-radius: 8px; border: 1px solid #ccc; cursor: pointer; background: #f3f3f3; }
button:disabled { opacity: .5; cursor: not-allowed; }
label { display: block; text-align: left; margin: 6px 0; font-size: 14px; }
ul { list-style: none; padding: 0; text-align: left; margin-top: 10px; }
li { padding: 8px 12px; margin: 4px 0; border-radius: 8px; background: #f3f3f3; }
#output { margin-top: 14px; font-size: 15px; min-height: 20px; color: #222; }
"""


def _desc(browser_html, spec_items):
    items = "\n".join(f"  <li>{it}</li>" for it in spec_items)
    return (
        "<p>Given the following fixed HTML:</p>\n"
        f"<pre>{_html.escape(browser_html)}</pre>\n"
        "<p>Implement the behavior described below:</p>\n"
        f"<ul>\n{items}\n</ul>"
    )


# ---------------------------------------------------------------------------
# 6031 — Enable Submit When All Fields Filled
# ---------------------------------------------------------------------------

HTML_6031 = (
    '<div class="panel">'
    '<input type="text" id="fname" placeholder="First name">'
    '<input type="text" id="lname" placeholder="Last name">'
    '<button id="submit-btn" disabled>Submit</button>'
    '</div>'
)

BOILERPLATE_6031 = """const fname = document.getElementById('fname');
const lname = document.getElementById('lname');
const submitBtn = document.getElementById('submit-btn');

// TODO: listen for the 'input' event on both #fname and #lname.
// TODO: on each input event, enable #submit-btn only when BOTH fields
//       have a non-empty trimmed value; otherwise keep it disabled.
"""

PROBLEM_6031 = {
    "id": 6031,
    "slug": "dom-enable-submit-when-all-fields-filled",
    "title": "Enable Submit When All Fields Filled",
    "difficulty": "Medium",
    "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Working with Forms"],
    "judge": "browser",
    "languages": ["javascript"],
    "browser_html": HTML_6031,
    "browser_style": CHUNK7_STYLE,
    "description": _desc(HTML_6031, [
        "On the <code>input</code> event of either <code>#fname</code> or <code>#lname</code>, re-check both fields.",
        "Enable <code>#submit-btn</code> (set its <code>disabled</code> property to <code>false</code>) only when BOTH fields have a non-empty trimmed value.",
        "If either field is empty (after trimming), keep/set <code>#submit-btn</code> disabled.",
    ]),
    "hint": "Write one shared check function that reads both inputs' trimmed values and sets submitBtn.disabled accordingly, then call it from both fields' input listeners.",
    "boilerplate": {"javascript": BOILERPLATE_6031},
    "tests": [],
    "samples": [0, 1],
    "browser_tests": [
        {
            "name": "Initial state: submit is disabled",
            "hidden": False,
            "steps": [],
            "expect": {"style": {"selector": "#submit-btn", "property": "disabled", "value": "true"}},
        },
        {
            "name": "Only first name filled: still disabled",
            "hidden": False,
            "steps": [{"type": "fname", "value": "Ann"}],
            "expect": {"style": {"selector": "#submit-btn", "property": "disabled", "value": "true"}},
        },
        {
            "name": "Both fields filled: enabled",
            "hidden": True,
            "steps": [{"type": "lname", "value": "Lee"}],
            "expect": {"style": {"selector": "#submit-btn", "property": "disabled", "value": "false"}},
        },
        {
            "name": "Clearing a field disables again",
            "hidden": True,
            "steps": [{"type": "fname", "value": ""}],
            "expect": {"style": {"selector": "#submit-btn", "property": "disabled", "value": "true"}},
        },
    ],
}


# ---------------------------------------------------------------------------
# 6032 — Password Match Checker
# ---------------------------------------------------------------------------

HTML_6032 = (
    '<div class="panel">'
    '<input type="password" id="pw1" placeholder="Password">'
    '<input type="password" id="pw2" placeholder="Confirm password">'
    '<p id="output"></p>'
    '</div>'
)

BOILERPLATE_6032 = """const pw1 = document.getElementById('pw1');
const pw2 = document.getElementById('pw2');
const output = document.getElementById('output');

// TODO: listen for the 'input' event on both #pw1 and #pw2.
// TODO: when BOTH fields are non-empty, set #output text to
//       "Passwords match" or "Passwords do not match".
// TODO: when either field is empty, clear #output (empty string).
"""

PROBLEM_6032 = {
    "id": 6032,
    "slug": "dom-password-match-checker",
    "title": "Password Match Checker",
    "difficulty": "Medium",
    "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Working with Forms"],
    "judge": "browser",
    "languages": ["javascript"],
    "browser_html": HTML_6032,
    "browser_style": CHUNK7_STYLE,
    "description": _desc(HTML_6032, [
        "On the <code>input</code> event of either <code>#pw1</code> or <code>#pw2</code>, re-check both fields.",
        "If BOTH fields are non-empty: set <code>#output</code> text to <code>\"Passwords match\"</code> when equal, or <code>\"Passwords do not match\"</code> when different.",
        "If either field is empty: clear <code>#output</code> (set its text to an empty string).",
    ]),
    "hint": "Guard the comparison behind a check that both values are non-empty before comparing pw1.value to pw2.value.",
    "boilerplate": {"javascript": BOILERPLATE_6032},
    "tests": [],
    "samples": [0, 1],
    "browser_tests": [
        {
            "name": "Initial state: output empty",
            "hidden": False,
            "steps": [],
            "expect": {"text": {"id": "output", "value": ""}},
        },
        {
            "name": "Only pw1 filled: still empty",
            "hidden": False,
            "steps": [{"type": "pw1", "value": "secret123"}],
            "expect": {"text": {"id": "output", "value": ""}},
        },
        {
            "name": "Matching passwords",
            "hidden": True,
            "steps": [{"type": "pw2", "value": "secret123"}],
            "expect": {"text": {"id": "output", "value": "Passwords match"}},
        },
        {
            "name": "Non-matching passwords",
            "hidden": True,
            "steps": [{"type": "pw2", "value": "different"}],
            "expect": {"text": {"id": "output", "value": "Passwords do not match"}},
        },
    ],
}


# ---------------------------------------------------------------------------
# 6033 — Filter by Size Dropdown
# ---------------------------------------------------------------------------

HTML_6033 = (
    '<div class="panel">'
    '<select id="size-select">'
    '<option value="all">All Sizes</option>'
    '<option value="s">Small</option>'
    '<option value="m">Medium</option>'
    '<option value="l">Large</option>'
    '</select>'
    '<ul id="shirt-list">'
    '<li class="shirt" data-size="s">Red T-Shirt</li>'
    '<li class="shirt" data-size="m">Blue Hoodie</li>'
    '<li class="shirt" data-size="l">Green Jacket</li>'
    '<li class="shirt" data-size="s">White Tee</li>'
    '</ul>'
    '</div>'
)

BOILERPLATE_6033 = """const sizeSelect = document.getElementById('size-select');
const shirts = document.querySelectorAll('.shirt');

// TODO: listen for the 'change' event on #size-select.
// TODO: for each .shirt element, show it if the select's value is "all"
//       or matches the shirt's data-size attribute; hide it otherwise.
"""

PROBLEM_6033 = {
    "id": 6033,
    "slug": "dom-filter-by-size-dropdown",
    "title": "Filter by Size Dropdown",
    "difficulty": "Medium",
    "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Working with Forms"],
    "judge": "browser",
    "languages": ["javascript"],
    "browser_html": HTML_6033,
    "browser_style": CHUNK7_STYLE,
    "description": _desc(HTML_6033, [
        "On the <code>change</code> event of <code>#size-select</code>, filter the <code>.shirt</code> list items.",
        "Show only the <code>.shirt</code> items whose <code>data-size</code> matches the selected value; hide the rest.",
        "When the selected value is <code>\"all\"</code>, show every <code>.shirt</code> item.",
    ]),
    "hint": "Loop over document.querySelectorAll('.shirt') and toggle each element's style.display based on whether its dataset.size matches the select's current value.",
    "boilerplate": {"javascript": BOILERPLATE_6033},
    "tests": [],
    "samples": [0, 1],
    "browser_tests": [
        {
            "name": "Initial state: all shirts visible",
            "hidden": False,
            "steps": [],
            "expect": {"visibleList": {
                "selector": "#shirt-list li",
                "visible": ["Red T-Shirt", "Blue Hoodie", "Green Jacket", "White Tee"],
                "hidden": [],
            }},
        },
        {
            "name": "Filter to Small",
            "hidden": False,
            "steps": [{"select": {"id": "size-select", "value": "s"}}],
            "expect": {"visibleList": {
                "selector": "#shirt-list li",
                "visible": ["Red T-Shirt", "White Tee"],
                "hidden": ["Blue Hoodie", "Green Jacket"],
            }},
        },
        {
            "name": "Filter to Medium",
            "hidden": True,
            "steps": [{"select": {"id": "size-select", "value": "m"}}],
            "expect": {"visibleList": {
                "selector": "#shirt-list li",
                "visible": ["Blue Hoodie"],
                "hidden": ["Red T-Shirt", "Green Jacket", "White Tee"],
            }},
        },
        {
            "name": "Back to All Sizes",
            "hidden": True,
            "steps": [{"select": {"id": "size-select", "value": "all"}}],
            "expect": {"visibleList": {
                "selector": "#shirt-list li",
                "visible": ["Red T-Shirt", "Blue Hoodie", "Green Jacket", "White Tee"],
                "hidden": [],
            }},
        },
    ],
}


# ---------------------------------------------------------------------------
# 6034 — Choose a Plan via Radio Buttons
# ---------------------------------------------------------------------------

HTML_6034 = (
    '<div class="panel">'
    '<label><input type="radio" name="plan" id="plan-basic" value="9" checked> Basic ($9/mo)</label>'
    '<label><input type="radio" name="plan" id="plan-pro" value="29"> Pro ($29/mo)</label>'
    '<label><input type="radio" name="plan" id="plan-team" value="99"> Team ($99/mo)</label>'
    '<p id="output">Selected: Basic ($9/mo)</p>'
    '</div>'
)

BOILERPLATE_6034 = """const radios = document.querySelectorAll('input[name="plan"]');
const output = document.getElementById('output');

// TODO: listen for the 'change' event on each radio in the "plan" group.
// TODO: when a radio becomes checked, update #output text to
//       "Selected: Basic ($9/mo)" / "Selected: Pro ($29/mo)" / "Selected: Team ($99/mo)"
//       matching whichever radio is now checked.
"""

PROBLEM_6034 = {
    "id": 6034,
    "slug": "dom-choose-a-plan-via-radio-buttons",
    "title": "Choose a Plan via Radio Buttons",
    "difficulty": "Medium",
    "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Working with Forms"],
    "judge": "browser",
    "languages": ["javascript"],
    "browser_html": HTML_6034,
    "browser_style": CHUNK7_STYLE,
    "description": _desc(HTML_6034, [
        "On the <code>change</code> event of any radio in the <code>plan</code> group, update <code>#output</code>.",
        "Set <code>#output</code> text to <code>\"Selected: Basic ($9/mo)\"</code>, <code>\"Selected: Pro ($29/mo)\"</code>, or <code>\"Selected: Team ($99/mo)\"</code> depending on which radio is now checked.",
    ]),
    "hint": "Attach a change listener to each radio (or the group), then check which one is currently .checked to build the output string.",
    "boilerplate": {"javascript": BOILERPLATE_6034},
    "tests": [],
    "samples": [0, 1],
    "browser_tests": [
        {
            "name": "Initial state: Basic selected",
            "hidden": False,
            "steps": [],
            "expect": {"text": {"id": "output", "value": "Selected: Basic ($9/mo)"}},
        },
        {
            "name": "Select Pro",
            "hidden": False,
            "steps": [{"click": "plan-pro"}],
            "expect": {"text": {"id": "output", "value": "Selected: Pro ($29/mo)"}},
        },
        {
            "name": "Select Team",
            "hidden": True,
            "steps": [{"click": "plan-team"}],
            "expect": {"text": {"id": "output", "value": "Selected: Team ($99/mo)"}},
        },
        {
            "name": "Back to Basic",
            "hidden": True,
            "steps": [{"click": "plan-basic"}],
            "expect": {"text": {"id": "output", "value": "Selected: Basic ($9/mo)"}},
        },
    ],
}


# ---------------------------------------------------------------------------
# 6035 — Live Order Summary
# ---------------------------------------------------------------------------

HTML_6035 = (
    '<div class="panel">'
    '<select id="product-select">'
    '<option value="Pen" data-price="2">Pen ($2)</option>'
    '<option value="Notebook" data-price="5">Notebook ($5)</option>'
    '</select>'
    '<input type="number" id="qty-input" value="1">'
    '<p id="output">1 x Pen = $2</p>'
    '</div>'
)

BOILERPLATE_6035 = """const productSelect = document.getElementById('product-select');
const qtyInput = document.getElementById('qty-input');
const output = document.getElementById('output');

// TODO: listen for 'change' on #product-select and 'input' on #qty-input.
// TODO: on either event, recompute and show `${qty} x ${productName} = $${price * qty}`
//       in #output. Read productName/price off the currently selected <option>
//       (e.g. productSelect.options[productSelect.selectedIndex].dataset.price),
//       and convert qtyInput.value to a Number before multiplying.
"""

PROBLEM_6035 = {
    "id": 6035,
    "slug": "dom-live-order-summary",
    "title": "Live Order Summary",
    "difficulty": "Medium",
    "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Working with Forms"],
    "judge": "browser",
    "languages": ["javascript"],
    "browser_html": HTML_6035,
    "browser_style": CHUNK7_STYLE,
    "description": _desc(HTML_6035, [
        "On the <code>change</code> event of <code>#product-select</code> OR the <code>input</code> event of <code>#qty-input</code>, recompute the summary.",
        "Read the currently selected option's product name (its <code>value</code>) and unit price (its <code>data-price</code> attribute).",
        "Read the quantity from <code>#qty-input</code>, converted to a number.",
        "Set <code>#output</code> text to <code>`${qty} x ${productName} = $${price * qty}`</code>.",
    ]),
    "hint": "Use productSelect.options[productSelect.selectedIndex].dataset.price (a string) and Number(qtyInput.value) to get numeric values before multiplying.",
    "boilerplate": {"javascript": BOILERPLATE_6035},
    "tests": [],
    "samples": [0, 1],
    "browser_tests": [
        {
            "name": "Initial state: 1 x Pen = $2",
            "hidden": False,
            "steps": [],
            "expect": {"text": {"id": "output", "value": "1 x Pen = $2"}},
        },
        {
            "name": "Change quantity to 3",
            "hidden": False,
            "steps": [{"type": "qty-input", "value": "3"}],
            "expect": {"text": {"id": "output", "value": "3 x Pen = $6"}},
        },
        {
            "name": "Switch product, quantity carries over",
            "hidden": True,
            "steps": [{"select": {"id": "product-select", "value": "Notebook"}}],
            "expect": {"text": {"id": "output", "value": "3 x Notebook = $15"}},
        },
        {
            "name": "Change quantity again",
            "hidden": True,
            "steps": [{"type": "qty-input", "value": "2"}],
            "expect": {"text": {"id": "output", "value": "2 x Notebook = $10"}},
        },
    ],
}


CHUNK7_PROBLEMS = [
    PROBLEM_6031,
    PROBLEM_6032,
    PROBLEM_6033,
    PROBLEM_6034,
    PROBLEM_6035,
]

# ============================================================================
# Chunk 8
# ============================================================================
CHUNK8_STYLE_BASE = """
body { font-family: -apple-system, "Segoe UI", sans-serif; display: flex; justify-content: center; padding-top: 40px; background: #fafafa; }
.panel { text-align: center; background: #fff; border: 1px solid #ddd; border-radius: 14px; padding: 28px 36px; min-width: 320px; box-shadow: 0 4px 18px rgba(0,0,0,.08); }
button { padding: 8px 14px; font-size: 14px; border-radius: 8px; border: 1px solid #ccc; cursor: pointer; background: #f3f3f3; margin: 3px; }
button:hover { background: #e8e8e8; }
button:disabled { opacity: .5; cursor: not-allowed; }
ul { list-style: none; padding: 0; text-align: left; }
li { padding: 8px 12px; margin: 4px 0; border-radius: 8px; background: #f3f3f3; }
input[type="text"], textarea { padding: 8px 10px; font-size: 14px; border-radius: 6px; border: 1px solid #ccc; width: 200px; }
#output { margin-top: 14px; font-size: 15px; min-height: 20px; color: #222; }
table { border-collapse: collapse; width: 100%; margin-top: 10px; }
td, th { border: 1px solid #ddd; padding: 8px 10px; text-align: center; }
"""

CHUNK8_PROBLEMS = [
    {
        "id": 6036,
        "slug": "dom-shopping-cart",
        "title": "Shopping Cart Quantity & Subtotal",
        "difficulty": "Hard",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Mini Projects"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>A mini shopping cart — the first Mini Project, combining event handling with per-row
state.</p>
<pre>&lt;table&gt;
  &lt;tbody id="cartBody"&gt;
    &lt;tr data-price="10"&gt;
      &lt;td&gt;Widget&lt;/td&gt;&lt;td&gt;$10&lt;/td&gt;&lt;td class="qty"&gt;1&lt;/td&gt;&lt;td class="subtotal"&gt;$10&lt;/td&gt;
      &lt;td&gt;&lt;button class="btn dec"&gt;-&lt;/button&gt;&lt;button class="btn inc"&gt;+&lt;/button&gt;&lt;/td&gt;
    &lt;/tr&gt;
    &lt;tr data-price="25"&gt;...&lt;/tr&gt;
  &lt;/tbody&gt;
&lt;/table&gt;</pre>
<p>Write JavaScript so that, for EACH row independently:</p>
<ul>
  <li>Clicking that row's <code>+</code> button increases its quantity (the
      <code>.qty</code> cell) by 1.</li>
  <li>Clicking that row's <code>-</code> button decreases its quantity by 1, but never below
      <code>1</code>.</li>
  <li>After any change, that row's <code>.subtotal</code> cell updates to
      <code>price &times; quantity</code>, formatted as <code>"$N"</code>.</li>
  <li>Changing one row must never affect any other row.</li>
</ul>
""",
        "hint": "Loop over document.querySelectorAll('#cartBody tr') once at startup, and for each "
                 "row read its own data-price with parseInt(row.dataset.price, 10), then attach "
                 "click listeners to that row's own .dec/.inc buttons with the quantity kept in a "
                 "variable closed over per-row (not a single shared variable).",
        "boilerplate": {
            "javascript": """const rows = document.querySelectorAll('#cartBody tr');

// TODO: for each row, track its own quantity (starting at 1) and wire up
// that row's .dec/.inc buttons to update its .qty and .subtotal cells
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <table>
    <thead><tr><th>Item</th><th>Price</th><th>Qty</th><th>Subtotal</th><th></th></tr></thead>
    <tbody id="cartBody">
      <tr data-price="10">
        <td>Widget</td><td>$10</td><td class="qty">1</td><td class="subtotal">$10</td>
        <td><button class="btn dec">-</button><button class="btn inc">+</button></td>
      </tr>
      <tr data-price="25">
        <td>Gadget</td><td>$25</td><td class="qty">1</td><td class="subtotal">$25</td>
        <td><button class="btn dec">-</button><button class="btn inc">+</button></td>
      </tr>
    </tbody>
  </table>
</div>""",
        "browser_style": CHUNK8_STYLE_BASE,
        "browser_tests": [
            {
                "name": "Initial state: both rows start at qty 1",
                "hidden": False,
                "steps": [],
                "expect": {"qty": {"row": 0, "value": "1"}, "subtotal": {"row": 0, "value": "$10"}},
            },
            {
                "name": "Incrementing row 0 updates its qty and subtotal",
                "hidden": False,
                "steps": [{"rowBtn": {"row": 0, "which": 1}}],
                "expect": {"qty": {"row": 0, "value": "2"}, "subtotal": {"row": 0, "value": "$20"}},
            },
            {
                "name": "Incrementing row 0 three more times reaches qty 5",
                "hidden": True,
                "steps": [{"rowBtn": {"row": 0, "which": 1}} for _ in range(3)],
                "expect": {"qty": {"row": 0, "value": "5"}, "subtotal": {"row": 0, "value": "$50"}},
            },
            {
                "name": "Decrementing row 0 ten times clamps at a minimum of 1",
                "hidden": True,
                "steps": [{"rowBtn": {"row": 0, "which": 0}} for _ in range(10)],
                "expect": {"qty": {"row": 0, "value": "1"}, "subtotal": {"row": 0, "value": "$10"}},
            },
            {
                "name": "Incrementing row 1 twice is independent of row 0",
                "hidden": True,
                "steps": [{"rowBtn": {"row": 1, "which": 1}} for _ in range(2)],
                "expect": {"qty": {"row": 1, "value": "3"}, "subtotal": {"row": 1, "value": "$75"}},
            },
        ],
    },
    {
        "id": 6037,
        "slug": "dom-star-rating",
        "title": "Star Rating Widget",
        "difficulty": "Hard",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Mini Projects"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Build a classic 5-star rating widget.</p>
<pre>&lt;div class="rating-stars"&gt;
  &lt;span class="star" data-value="1"&gt;&#9733;&lt;/span&gt;
  &lt;span class="star" data-value="2"&gt;&#9733;&lt;/span&gt;
  &lt;span class="star" data-value="3"&gt;&#9733;&lt;/span&gt;
  &lt;span class="star" data-value="4"&gt;&#9733;&lt;/span&gt;
  &lt;span class="star" data-value="5"&gt;&#9733;&lt;/span&gt;
&lt;/div&gt;
&lt;p id="output"&gt;No rating yet&lt;/p&gt;</pre>
<p>Write JavaScript so that clicking any star with value <code>N</code>:</p>
<ul>
  <li>Adds class <code>"filled"</code> to that star and every star to its left (values
      <code>1..N</code>).</li>
  <li>Removes <code>"filled"</code> from every star to its right (values greater than
      <code>N</code>).</li>
  <li>Sets <code>#output</code>'s text to <code>"Rated N star(s)"</code>.</li>
</ul>
""",
        "hint": "Read each star's rating from its data-value with Number(star.dataset.value), "
                 "then loop over ALL stars and toggle 'filled' based on whether that star's own "
                 "value is <= the clicked value.",
        "boilerplate": {
            "javascript": """const stars = document.querySelectorAll('.rating-stars .star');
const outputEl = document.getElementById('output');

// TODO: on click of any star, fill it and every star to its left, unfill the rest
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <div class="rating-stars">
    <span class="star" data-value="1">&#9733;</span>
    <span class="star" data-value="2">&#9733;</span>
    <span class="star" data-value="3">&#9733;</span>
    <span class="star" data-value="4">&#9733;</span>
    <span class="star" data-value="5">&#9733;</span>
  </div>
  <p id="output">No rating yet</p>
</div>""",
        "browser_style": CHUNK8_STYLE_BASE + """
.rating-stars { font-size: 30px; cursor: pointer; }
.star { color: #ccc; }
.star.filled { color: #f5a623; }
""",
        "browser_tests": [
            {
                "name": "Initial state: 5 stars, none filled",
                "hidden": False,
                "steps": [],
                "expect": {"stars": 5, "filled": 0, "text": {"id": "output", "value": "No rating yet"}},
            },
            {
                "name": "Clicking the 3rd star fills exactly 3",
                "hidden": False,
                "steps": [{"starClick": 3}],
                "expect": {"filled": 3, "text": {"id": "output", "value": "Rated 3 star(s)"}},
            },
            {
                "name": "Clicking the 5th star fills all 5",
                "hidden": True,
                "steps": [{"starClick": 5}],
                "expect": {"filled": 5, "text": {"id": "output", "value": "Rated 5 star(s)"}},
            },
            {
                "name": "Clicking the 1st star unfills the rest, leaving only 1",
                "hidden": True,
                "steps": [{"starClick": 1}],
                "expect": {"filled": 1, "text": {"id": "output", "value": "Rated 1 star(s)"}},
            },
        ],
    },
    {
        "id": 6038,
        "slug": "dom-todo-with-filter",
        "title": "To-Do List with Filter",
        "difficulty": "Hard",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Mini Projects"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Combine checkboxes, filtering, and dynamic creation into one to-do list.</p>
<pre>&lt;ul id="todo-list"&gt;
  &lt;li class="todo-item"&gt;&lt;input type="checkbox" id="chk-1"&gt; Buy milk&lt;/li&gt;
  &lt;li class="todo-item"&gt;&lt;input type="checkbox" id="chk-2"&gt; Walk dog&lt;/li&gt;
  &lt;li class="todo-item"&gt;&lt;input type="checkbox" id="chk-3"&gt; Read book&lt;/li&gt;
&lt;/ul&gt;
&lt;button id="filter-all"&gt;All&lt;/button&gt;
&lt;button id="filter-active"&gt;Active&lt;/button&gt;
&lt;button id="filter-done"&gt;Done&lt;/button&gt;
&lt;input type="text" id="task-input"&gt;
&lt;button id="add-btn"&gt;Add&lt;/button&gt;</pre>
<p>Write JavaScript so that:</p>
<ul>
  <li>Checking/unchecking any task's checkbox marks it done/not-done.</li>
  <li><b>All</b> shows every task. <b>Active</b> shows only unchecked tasks.
      <b>Done</b> shows only checked tasks (hide the rest via
      <code>style.display = 'none'</code>).</li>
  <li>Toggling a checkbox while a filter is active immediately re-applies that filter (e.g.
      checking a task while "Active" is selected should immediately hide it).</li>
  <li>Clicking <code>#add-btn</code> with non-empty text in <code>#task-input</code> appends a
      new unchecked task (with its own checkbox) to the list, then clears the input. A newly
      added task must also respect whichever filter is currently active.</li>
</ul>
""",
        "hint": "Keep a single 'currentFilter' variable and a single applyFilter() function that "
                 "loops over every li in #todo-list and shows/hides it based on its checkbox's "
                 "checked state and currentFilter — call applyFilter() after every checkbox "
                 "change, filter button click, and newly added task.",
        "boilerplate": {
            "javascript": """const todoList = document.getElementById('todo-list');
const taskInput = document.getElementById('task-input');
const addBtn = document.getElementById('add-btn');

// TODO: wire up checkboxes, the three filter buttons, and add-btn,
// re-applying the current filter after every change
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <ul id="todo-list">
    <li class="todo-item"><input type="checkbox" id="chk-1"> Buy milk</li>
    <li class="todo-item"><input type="checkbox" id="chk-2"> Walk dog</li>
    <li class="todo-item"><input type="checkbox" id="chk-3"> Read book</li>
  </ul>
  <div>
    <button id="filter-all">All</button>
    <button id="filter-active">Active</button>
    <button id="filter-done">Done</button>
  </div>
  <input type="text" id="task-input" placeholder="New task">
  <button id="add-btn">Add</button>
</div>""",
        "browser_style": CHUNK8_STYLE_BASE,
        "browser_tests": [
            {
                "name": "Initial state: All filter shows every task",
                "hidden": False,
                "steps": [],
                "expect": {"visibleList": {"selector": "#todo-list li",
                                            "visible": ["Buy milk", "Walk dog", "Read book"],
                                            "hidden": []}},
            },
            {
                "name": "Checking a task then filtering Active hides it",
                "hidden": False,
                "steps": [{"click": "chk-1"}, {"click": "filter-active"}],
                "expect": {"visibleList": {"selector": "#todo-list li",
                                            "visible": ["Walk dog", "Read book"],
                                            "hidden": ["Buy milk"]}},
            },
            {
                "name": "Filtering Done shows only the checked task",
                "hidden": True,
                "steps": [{"click": "filter-done"}],
                "expect": {"visibleList": {"selector": "#todo-list li",
                                            "visible": ["Buy milk"],
                                            "hidden": ["Walk dog", "Read book"]}},
            },
            {
                "name": "Filtering All shows everything again",
                "hidden": True,
                "steps": [{"click": "filter-all"}],
                "expect": {"visibleList": {"selector": "#todo-list li",
                                            "visible": ["Buy milk", "Walk dog", "Read book"],
                                            "hidden": []}},
            },
            {
                "name": "Adding a task while All is active shows it immediately",
                "hidden": True,
                "steps": [{"type": "task-input", "value": "Clean house"}, {"click": "add-btn"}],
                "expect": {"elemCount": {"selector": "#todo-list li", "value": 4},
                           "visibleList": {"selector": "#todo-list li",
                                            "visible": ["Buy milk", "Walk dog", "Read book", "Clean house"],
                                            "hidden": []}},
            },
        ],
    },
    {
        "id": 6039,
        "slug": "dom-tabs-component",
        "title": "Tabs Component",
        "difficulty": "Hard",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Mini Projects"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>Build a classic tabbed panel: exactly one tab and its matching panel are visible at a
time.</p>
<pre>&lt;div class="tabs"&gt;
  &lt;button class="tab-btn active" id="tab-home" data-target="panel-home"&gt;Home&lt;/button&gt;
  &lt;button class="tab-btn" id="tab-profile" data-target="panel-profile"&gt;Profile&lt;/button&gt;
  &lt;button class="tab-btn" id="tab-settings" data-target="panel-settings"&gt;Settings&lt;/button&gt;
&lt;/div&gt;
&lt;div class="tab-panel" id="panel-home"&gt;Welcome home!&lt;/div&gt;
&lt;div class="tab-panel hidden" id="panel-profile"&gt;Your profile info.&lt;/div&gt;
&lt;div class="tab-panel hidden" id="panel-settings"&gt;Adjust your settings.&lt;/div&gt;</pre>
<p>Write JavaScript so that clicking any <code>.tab-btn</code>:</p>
<ul>
  <li>Adds class <code>"active"</code> to that button and removes it from the other tab
      buttons.</li>
  <li>Shows its target panel (read from the button's <code>data-target</code> attribute) by
      removing class <code>"hidden"</code> from it.</li>
  <li>Hides every OTHER panel by adding class <code>"hidden"</code> to it.</li>
</ul>
""",
        "hint": "On click, read event.target.dataset.target to know which panel to show, then "
                 "loop over all .tab-panel elements adding 'hidden' to everything except the one "
                 "whose id matches that target.",
        "boilerplate": {
            "javascript": """const tabButtons = document.querySelectorAll('.tab-btn');
const panels = document.querySelectorAll('.tab-panel');

// TODO: on click of a tab button, activate it (and only it), and show only its target panel
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <div class="tabs">
    <button class="tab-btn active" id="tab-home" data-target="panel-home">Home</button>
    <button class="tab-btn" id="tab-profile" data-target="panel-profile">Profile</button>
    <button class="tab-btn" id="tab-settings" data-target="panel-settings">Settings</button>
  </div>
  <div class="tab-panel" id="panel-home">Welcome home!</div>
  <div class="tab-panel hidden" id="panel-profile">Your profile info.</div>
  <div class="tab-panel hidden" id="panel-settings">Adjust your settings.</div>
</div>""",
        "browser_style": CHUNK8_STYLE_BASE + """
.hidden { display: none; }
.tab-btn.active { background: #4a90d9; color: #fff; }
.tab-panel { padding: 14px; border: 1px solid #ddd; border-radius: 8px; margin-top: 10px; }
""",
        "browser_tests": [
            {
                "name": "Initial state: Home panel visible, others hidden",
                "hidden": False,
                "steps": [],
                "expect": {"hasClass": {"selector": "#panel-home", "class": "hidden", "value": False}},
            },
            {
                "name": "Home panel visible check part 2: Profile stays hidden",
                "hidden": False,
                "steps": [],
                "expect": {"hasClass": {"selector": "#panel-profile", "class": "hidden", "value": True}},
            },
            {
                "name": "Clicking Profile tab shows its panel",
                "hidden": False,
                "steps": [{"click": "tab-profile"}],
                "expect": {"hasClass": {"selector": "#panel-profile", "class": "hidden", "value": False}},
            },
            {
                "name": "Clicking Profile tab activates its own button",
                "hidden": True,
                "steps": [],
                "expect": {"hasClass": {"selector": "#tab-profile", "class": "active", "value": True}},
            },
            {
                "name": "Clicking Profile tab deactivates the Home button",
                "hidden": True,
                "steps": [],
                "expect": {"hasClass": {"selector": "#tab-home", "class": "active", "value": False}},
            },
            {
                "name": "Clicking Profile tab hides the Home panel",
                "hidden": True,
                "steps": [],
                "expect": {"hasClass": {"selector": "#panel-home", "class": "hidden", "value": True}},
            },
            {
                "name": "Clicking Settings tab shows only the Settings panel",
                "hidden": True,
                "steps": [{"click": "tab-settings"}],
                "expect": {"hasClass": {"selector": "#panel-settings", "class": "hidden", "value": False}},
            },
            {
                "name": "Clicking Settings tab hides Profile panel too",
                "hidden": True,
                "steps": [],
                "expect": {"hasClass": {"selector": "#panel-profile", "class": "hidden", "value": True}},
            },
        ],
    },
    {
        "id": 6040,
        "slug": "dom-character-budget-localstorage",
        "title": "Character Budget with Save",
        "difficulty": "Hard",
        "topics": ["JavaScript", "DOM Manipulation", "JS DOM Practice", "Mini Projects"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p>The final Mini Project: a character-limited note box that persists to
<code>localStorage</code>.</p>
<pre>&lt;textarea id="note-input" rows="4" placeholder="Write a note (max 50 chars)"&gt;&lt;/textarea&gt;
&lt;p id="output"&gt;50 characters remaining&lt;/p&gt;
&lt;button id="save-btn" disabled&gt;Save&lt;/button&gt;</pre>
<p>Write JavaScript so that:</p>
<ul>
  <li>On every keystroke, <code>#output</code> shows
      <code>"N characters remaining"</code>, where <code>N = 50 - length</code> (this can go
      negative when over the limit).</li>
  <li><code>#save-btn</code> is disabled whenever the note is empty OR over the 50-character
      limit; enabled otherwise.</li>
  <li>Clicking <code>#save-btn</code> saves the current text to
      <code>localStorage</code> under the key <code>"note"</code>.</li>
</ul>
""",
        "hint": "Compute remaining = 50 - textarea.value.length inside the input handler, and "
                 "disable the button when textarea.value.length === 0 || remaining < 0. Use "
                 "localStorage.setItem('note', textarea.value) in the save button's click handler.",
        "boilerplate": {
            "javascript": """const noteInput = document.getElementById('note-input');
const outputEl = document.getElementById('output');
const saveBtn = document.getElementById('save-btn');

// TODO: track remaining characters live, enable/disable Save, and save to localStorage on click
"""
        },
        "tests": [],
        "samples": [0, 1],
        "browser_html": """<div class="panel">
  <textarea id="note-input" rows="4" placeholder="Write a note (max 50 chars)"></textarea>
  <p id="output">50 characters remaining</p>
  <button id="save-btn" disabled>Save</button>
</div>""",
        "browser_style": CHUNK8_STYLE_BASE,
        "browser_tests": [
            {
                "name": "Initial state: 50 remaining, Save disabled",
                "hidden": False,
                "steps": [],
                "expect": {"text": {"id": "output", "value": "50 characters remaining"},
                           "style": {"selector": "#save-btn", "property": "disabled", "value": "true"}},
            },
            {
                "name": "Typing 'Hello' leaves 45 remaining and enables Save",
                "hidden": False,
                "steps": [{"type": "note-input", "value": "Hello"}],
                "expect": {"text": {"id": "output", "value": "45 characters remaining"},
                           "style": {"selector": "#save-btn", "property": "disabled", "value": "false"}},
            },
            {
                "name": "Clicking Save stores the text in localStorage",
                "hidden": True,
                "steps": [{"click": "save-btn"}],
                "expect": {"storage": {"key": "note", "value": "Hello"}},
            },
            {
                "name": "Typing 55 characters goes over budget and disables Save",
                "hidden": True,
                "steps": [{"type": "note-input", "value": "A" * 55}],
                "expect": {"text": {"id": "output", "value": "-5 characters remaining"},
                           "style": {"selector": "#save-btn", "property": "disabled", "value": "true"}},
            },
            {
                "name": "Typing back under budget re-enables Save",
                "hidden": True,
                "steps": [{"type": "note-input", "value": "Back to normal"}],
                "expect": {"text": {"id": "output", "value": "36 characters remaining"},
                           "style": {"selector": "#save-btn", "property": "disabled", "value": "false"}},
            },
        ],
    },
]


DOM_PRACTICE_PROBLEMS = (
    CHUNK1_PROBLEMS
    + CHUNK2_PROBLEMS
    + CHUNK3_PROBLEMS
    + CHUNK4_PROBLEMS
    + CHUNK5_PROBLEMS
    + CHUNK6_PROBLEMS
    + CHUNK7_PROBLEMS
    + CHUNK8_PROBLEMS
)
