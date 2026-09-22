"""
Web-dev problems shaped like the real Accenture coding-round web task: a
fixed HTML/CSS shell (the CSS-tweak and HTML-element sub-tasks are treated
as already done, since that's how the real students who reported these
questions described them — trivial one-line changes) plus a JS behavior
that's the actual substantive part to implement.

The platform's browser judge only grades a single JavaScript answer per
problem (HTML/CSS are fixed context, not separately editable) — see
static/app.js's counterPreviewDoc(). These problems are written to fit that
shape rather than needing a multi-file editor.
"""

WEBDEV_EXAM_PROBLEMS = [
    # ------------------------------------------------------------------ #
    # 4016. Countdown Timer with Completion Popup
    # ------------------------------------------------------------------ #
    {
        "id": 4016,
        "slug": "countdown-timer-popup",
        "title": "Countdown Timer with Completion Popup",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "Events"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p class="text-muted">Coding round · Web development part</p>
<p>A real Accenture coding-round web task (reported 20th Sept 2026) gave a page with a countdown
timer and asked for three changes: (1) set the timer's text color via CSS, (2) add a label
<code>&lt;span&gt;</code> in the HTML, and (3) wire up the countdown logic and a completion popup
in JavaScript. The reporting student solved the first two (both one-line changes) but ran out of
time on the JavaScript.</p>
<p>The color and label are already applied below — <b>this problem is that third part</b>, the
one that actually matters: implement the countdown and popup logic.</p>
<p>The page has:</p>
<pre>&lt;div class="timer-box"&gt;
  &lt;span id="timer-label"&gt;Seconds left:&lt;/span&gt;
  &lt;h1 id="timer"&gt;10&lt;/h1&gt;
  &lt;button id="start-btn"&gt;Start Countdown&lt;/button&gt;
  &lt;p id="popup" class="hidden"&gt;⏰ Time's up!&lt;/p&gt;
&lt;/div&gt;</pre>
<p>Implement the following in JavaScript:</p>
<ul>
  <li><b>Each click</b> on <code>#start-btn</code> decrements the number shown in
      <code>#timer</code> by 1, down to a minimum of <code>0</code>.</li>
  <li><b>On reaching 0:</b> remove the <code>"hidden"</code> class from <code>#popup</code>
      (making it visible) and stop decrementing further — the timer stays at
      <code>0</code> on any additional clicks.</li>
  <li><b>Initial state:</b> the timer shows <code>10</code> and the popup stays hidden until
      the count reaches <code>0</code>.</li>
</ul>
<p class="text-muted">Note: in the real exam this was a genuine <code>setInterval</code>-driven
timer ticking once per second automatically. Here each click stands in for one "tick" so the
logic can be graded instantly rather than making you wait out a real countdown — the underlying
event-handling and state logic you need to write is the same either way.</p>
<p>Use the <b>Preview</b> tab to click the button and watch your countdown and popup live.
Submitting runs automated tests that simulate clicks in a fresh page.</p>
""",
        "hint": "Keep a `seconds` variable starting at 10. On each click, only decrement if "
                 "seconds > 0, then update timerEl.textContent. After decrementing, check if "
                 "seconds has reached 0 and if so remove the 'hidden' class from popupEl — do "
                 "this check every click, not just the first time, so it also fires correctly "
                 "on the exact click that reaches zero.",
        "boilerplate": {
            "javascript": """function initializeTimer() {
  const timerEl = document.getElementById('timer');
  const startBtn = document.getElementById('start-btn');
  const popupEl = document.getElementById('popup');

  // TODO: each click on startBtn should decrement the number in timerEl by 1
  // (minimum 0). When it reaches 0, remove the "hidden" class from popupEl
  // and stop responding to further clicks (stay at 0, popup stays visible).
}

initializeTimer();
""",
        },
        "tests": [],
        "samples": [0, 1, 2],
        "browser_html": """<div class="timer-box">
  <span id="timer-label">Seconds left:</span>
  <h1 id="timer">10</h1>
  <button id="start-btn">Start Countdown</button>
  <p id="popup" class="hidden">⏰ Time's up!</p>
</div>""",
        "browser_style": """
body { font-family: -apple-system, "Segoe UI", sans-serif; display: flex; justify-content: center; padding-top: 60px; background: #fafafa; }
.timer-box { text-align: center; background: #fff; border: 1px solid #ddd; border-radius: 14px; padding: 34px 44px; box-shadow: 0 4px 18px rgba(0,0,0,.08); }
#timer-label { font-size: 14px; color: #888; display: block; margin-bottom: 6px; }
#timer { font-size: 56px; margin: 4px 0 18px; color: #2ecc71; }
#start-btn { padding: 10px 22px; font-size: 15px; border-radius: 8px; border: 1px solid #ccc; cursor: pointer; background: #f3f3f3; }
#start-btn:hover { background: #e8e8e8; }
.hidden { display: none; }
#popup { margin-top: 18px; font-size: 18px; color: #e74c3c; font-weight: 600; }
""",
        # NOTE: browser-judge tests run cumulatively on ONE page load (see
        # counterPreviewDoc's tests.forEach in static/app.js — it never
        # resets the DOM between tests), so each test's steps are the
        # INCREMENT since the previous test's checkpoint, not a full replay
        # from a fresh page. Running total of clicks at each checkpoint is
        # noted alongside each test below.
        "browser_tests": [
            {
                "name": "Initial state: timer shows 10, popup hidden",
                "hidden": False,
                "steps": [],  # 0 clicks total
                "expect": {
                    "text": {"id": "timer", "value": "10"},
                    "style": {"selector": "#popup", "property": "className", "value": "hidden"},
                },
            },
            {
                "name": "One click decrements to 9, popup still hidden",
                "hidden": False,
                "steps": [{"click": "start-btn"}],  # 1 click total
                "expect": {
                    "text": {"id": "timer", "value": "9"},
                    "style": {"selector": "#popup", "property": "className", "value": "hidden"},
                },
            },
            {
                "name": "Nine clicks reach 1, popup still hidden",
                "hidden": False,
                "steps": [{"click": "start-btn"} for _ in range(8)],  # 1+8 = 9 clicks total
                "expect": {
                    "text": {"id": "timer", "value": "1"},
                    "style": {"selector": "#popup", "property": "className", "value": "hidden"},
                },
            },
            {
                "name": "Ten clicks reach 0, popup becomes visible",
                "hidden": True,
                "steps": [{"click": "start-btn"}],  # 9+1 = 10 clicks total
                "expect": {
                    "text": {"id": "timer", "value": "0"},
                    "style": {"selector": "#popup", "property": "className", "value": ""},
                },
            },
            {
                "name": "An extra click after reaching 0 stays clamped at 0",
                "hidden": True,
                "steps": [{"click": "start-btn"}],  # 10+1 = 11 clicks total
                "expect": {
                    "text": {"id": "timer", "value": "0"},
                    "style": {"selector": "#popup", "property": "className", "value": ""},
                },
            },
        ],
    },

    # ------------------------------------------------------------------ #
    # 4017. Character Counter with Post Limit
    # ------------------------------------------------------------------ #
    {
        "id": 4017,
        "slug": "character-counter-post-limit",
        "title": "Character Counter with Post Limit",
        "difficulty": "Easy",
        "topics": ["JavaScript", "DOM Manipulation", "Events"],
        "judge": "browser",
        "languages": ["javascript"],
        "description": """
<p class="text-muted">Coding round · Web development part</p>
<p>A common exam-style task: a social-post text box with a live character counter that enforces
a limit before the post can be submitted.</p>
<p>The page has:</p>
<pre>&lt;div class="counter-box"&gt;
  &lt;textarea id="message" placeholder="Type your message..."&gt;&lt;/textarea&gt;
  &lt;p id="char-count"&gt;0 / 100&lt;/p&gt;
  &lt;button id="post-btn"&gt;Post&lt;/button&gt;
&lt;/div&gt;</pre>
<p>Implement the following in JavaScript:</p>
<ul>
  <li><b>On every keystroke</b> in <code>#message</code>, update <code>#char-count</code> to
      show <code>"&lt;current length&gt; / 100"</code>.</li>
  <li><b>Over the limit:</b> once the length exceeds <code>100</code>, add the class
      <code>"over-limit"</code> to <code>#char-count</code> (and remove it again if the text is
      edited back under the limit).</li>
  <li><b>Post button:</b> <code>#post-btn</code> must be <b>disabled</b> whenever the text is
      empty OR over 100 characters, and <b>enabled</b> otherwise.</li>
  <li><b>Initial state:</b> the counter shows <code>"0 / 100"</code> and the Post button starts
      disabled (the box is empty).</li>
</ul>
<p>Use the <b>Preview</b> tab to type into the box and watch the counter and button live.
Submitting runs automated tests that simulate typing in a fresh page.</p>
""",
        "hint": "Listen for the 'input' event on the textarea. Read textarea.value.length each "
                 "time, update the counter text, toggle the 'over-limit' class with "
                 "classList.toggle(name, condition), and set postBtn.disabled based on both the "
                 "empty AND over-limit conditions together.",
        "boilerplate": {
            "javascript": """function initializeCounter() {
  const textarea = document.getElementById('message');
  const countEl = document.getElementById('char-count');
  const postBtn = document.getElementById('post-btn');
  const LIMIT = 100;

  // TODO: on every input event, update countEl's text to "<length> / 100",
  // toggle the "over-limit" class on countEl when length > LIMIT, and set
  // postBtn.disabled when the text is empty or over the limit.
}

initializeCounter();
""",
        },
        "tests": [],
        "samples": [0, 1, 2],
        "browser_html": """<div class="counter-box">
  <textarea id="message" placeholder="Type your message..."></textarea>
  <p id="char-count">0 / 100</p>
  <button id="post-btn" disabled>Post</button>
</div>""",
        "browser_style": """
body { font-family: -apple-system, "Segoe UI", sans-serif; display: flex; justify-content: center; padding-top: 60px; background: #fafafa; }
.counter-box { width: 360px; background: #fff; border: 1px solid #ddd; border-radius: 14px; padding: 24px; box-shadow: 0 4px 18px rgba(0,0,0,.08); }
textarea { width: 100%; height: 100px; padding: 10px; font-size: 14px; border-radius: 8px; border: 1px solid #ccc; resize: vertical; box-sizing: border-box; }
#char-count { text-align: right; color: #888; margin-top: 6px; font-size: 13px; }
#char-count.over-limit { color: #e74c3c; font-weight: 700; }
#post-btn { margin-top: 12px; padding: 9px 22px; font-size: 14px; border-radius: 8px; border: none; background: #2ecc71; color: #fff; cursor: pointer; }
#post-btn:disabled { opacity: .5; cursor: not-allowed; }
""",
        "browser_tests": [
            {
                "name": "Initial state: '0 / 100', Post disabled",
                "hidden": False,
                "steps": [],
                "expect": {
                    "text": {"id": "char-count", "value": "0 / 100"},
                    "style": {"selector": "#post-btn", "property": "disabled", "value": "true"},
                },
            },
            {
                "name": "Typing 'Hello' shows '5 / 100', Post enabled",
                "hidden": False,
                "steps": [{"type": "message", "value": "Hello"}],
                "expect": {
                    "text": {"id": "char-count", "value": "5 / 100"},
                    "style": {"selector": "#post-btn", "property": "disabled", "value": "false"},
                },
            },
            {
                "name": "Exactly 100 characters stays enabled, no over-limit class",
                "hidden": False,
                "steps": [{"type": "message", "value": "a" * 100}],
                "expect": {
                    "text": {"id": "char-count", "value": "100 / 100"},
                    "style": {"selector": "#post-btn", "property": "disabled", "value": "false"},
                    "style2": {"selector": "#char-count", "property": "className", "value": ""},
                },
            },
            {
                "name": "101 characters: over-limit class added, Post disabled",
                "hidden": True,
                "steps": [{"type": "message", "value": "a" * 101}],
                "expect": {
                    "text": {"id": "char-count", "value": "101 / 100"},
                    "style": {"selector": "#post-btn", "property": "disabled", "value": "true"},
                    "style2": {"selector": "#char-count", "property": "className", "value": "over-limit"},
                },
            },
            {
                "name": "Editing back down to 100 removes over-limit and re-enables Post",
                "hidden": True,
                "steps": [
                    {"type": "message", "value": "a" * 101},
                    {"type": "message", "value": "a" * 100},
                ],
                "expect": {
                    "text": {"id": "char-count", "value": "100 / 100"},
                    "style": {"selector": "#post-btn", "property": "disabled", "value": "false"},
                    "style2": {"selector": "#char-count", "property": "className", "value": ""},
                },
            },
            {
                "name": "Clearing back to empty disables Post again",
                "hidden": True,
                "steps": [
                    {"type": "message", "value": "Hello"},
                    {"type": "message", "value": ""},
                ],
                "expect": {
                    "text": {"id": "char-count", "value": "0 / 100"},
                    "style": {"selector": "#post-btn", "property": "disabled", "value": "true"},
                },
            },
        ],
    },
]
