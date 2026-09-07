
    let activeModule = 1;
    let activeTab = 'html';

    // Modules Configuration
    const modules = {
      1: {
        title: "Dynamic Shopping Cart Total & Discount",
        render: `
          <table>
            <thead><tr><th>Item</th><th>Price</th><th>Qty</th><th>Subtotal</th></tr></thead>
            <tbody id="cartBody">
              <tr data-price="25">
                <td>Mouse</td><td>$25</td>
                <td><button class="ui-btn" onclick="adjustQty(this, -1)">-</button> <span class="qty">1</span> <button class="ui-btn" onclick="adjustQty(this, 1)">+</button></td>
                <td class="subtotal">$25.00</td>
              </tr>
              <tr data-price="80">
                <td>Keyboard</td><td>$80</td>
                <td><button class="ui-btn" onclick="adjustQty(this, -1)">-</button> <span class="qty">1</span> <button class="ui-btn" onclick="adjustQty(this, 1)">+</button></td>
                <td class="subtotal">$80.00</td>
              </tr>
            </tbody>
          </table>
          <h4 style="margin-top:16px;">Total: $<span id="cartTotal">105.00</span> <span id="cartBadge" class="pass" style="font-size:0.8rem; display:inline-block;">(10% Discount Applied)</span></h4>
        `,
        tasks: [
          "Recalculate row subtotals when quantity changes.",
          "Prevent quantities from dropping below zero.",
          "Apply 10% discount if total exceeds $100."
        ],
        html: `<table>
  <thead>
    <tr><th>Item</th><th>Price</th><th>Qty</th><th>Subtotal</th></tr>
  </thead>
  <tbody id="cartBody">
    <tr data-price="25">
      <td>Wireless Mouse</td>
      <td>$25</td>
      <td>
        <button class="btn" onclick="adjustQty(this, -1)">-</button>
        <span class="qty">1</span>
        <button class="btn" onclick="adjustQty(this, 1)">+</button>
      </td>
      <td class="subtotal">$25.00</td>
    </tr>
  </tbody>
</table>
<h4>Total: $<span id="cartTotal">25.00</span> <span id="cartBadge" class="badge">10% Discount</span></h4>`,
        css: `table { width: 100%; border-collapse: collapse; }
th, td { border: 1px solid #334155; padding: 8px; text-align: left; }
.btn { background: #0284c7; color: #fff; border: none; padding: 4px 8px; cursor: pointer; }
.badge { background: #22c55e; color: #000; padding: 2px 6px; font-size: 0.75rem; border-radius: 4px; display: none; }`,
        js: `function adjustQty(btn, delta) {
  const row = btn.closest('tr');
  const qtySpan = row.querySelector('.qty');
  let qty = Math.max(0, parseInt(qtySpan.innerText) + delta);
  qtySpan.innerText = qty;

  const price = parseFloat(row.dataset.price);
  row.querySelector('.subtotal').innerText = \`$\${(price * qty).toFixed(2)}\`;

  recalculateTotal();
}

function recalculateTotal() {
  let total = 0;
  document.querySelectorAll('#cartBody tr').forEach(r => {
    const price = parseFloat(r.dataset.price);
    const qty = parseInt(r.querySelector('.qty').innerText);
    total += price * qty;
  });

  const badge = document.getElementById('cartBadge');
  if (total > 100) {
    total *= 0.9; // Apply 10% discount
    badge.style.display = 'inline-block';
  } else {
    badge.style.display = 'none';
  }

  document.getElementById('cartTotal').innerText = total.toFixed(2);
}`
      },
      2: {
        title: "Student Grade Calculator & Filter",
        render: `
          <div style="display:flex; gap:8px; margin-bottom:12px;">
            <input type="text" id="sName" placeholder="Name" style="flex:1;" />
            <input type="number" id="sMarks" placeholder="Marks" style="width:80px;" />
            <button class="ui-btn" onclick="addStudent()">Add</button>
          </div>
          <select id="sFilter" onchange="filterStudents(this.value)" style="width:100%;">
            <option value="all">Show All</option>
            <option value="pass">Pass Only</option>
            <option value="fail">Fail Only</option>
          </select>
          <table>
            <thead><tr><th>Name</th><th>Marks</th><th>Status</th></tr></thead>
            <tbody id="sBody"></tbody>
          </table>
        `,
        tasks: [
          "Validate input presence and range (0-100).",
          "Classify marks >= 40 as 'Pass' and < 40 as 'Fail'.",
          "Filter visible rows dynamically on dropdown selection."
        ],
        html: `<div class="form">
  <input type="text" id="sName" placeholder="Student Name" />
  <input type="number" id="sMarks" placeholder="Marks (0-100)" />
  <button onclick="addStudent()">Add Student</button>
</div>

<select id="sFilter" onchange="filterStudents(this.value)">
  <option value="all">All</option>
  <option value="pass">Pass Only</option>
  <option value="fail">Fail Only</option>
</select>

<table>
  <thead><tr><th>Name</th><th>Marks</th><th>Status</th></tr></thead>
  <tbody id="sBody"></tbody>
</table>`,
        css: `.form { display: flex; gap: 8px; margin-bottom: 12px; }
input, select { padding: 6px; background: #334155; color: #fff; border: 1px solid #475569; }
.pass { color: #4ade80; font-weight: bold; }
.fail { color: #f87171; font-weight: bold; }`,
        js: `function addStudent() {
  const name = document.getElementById('sName').value.trim();
  const marks = parseInt(document.getElementById('sMarks').value);

  if (!name || isNaN(marks) || marks < 0 || marks > 100) {
    alert('Enter valid name and marks (0-100)');
    return;
  }

  const status = marks >= 40 ? 'pass' : 'fail';
  const tr = document.createElement('tr');
  tr.className = status;
  tr.innerHTML = \`<td>\${name}</td><td>\${marks}</td><td class="\${status}">\${status.toUpperCase()}</td>\`;

  document.getElementById('sBody').appendChild(tr);
  document.getElementById('sName').value = '';
  document.getElementById('sMarks').value = '';
}

function filterStudents(val) {
  document.querySelectorAll('#sBody tr').forEach(r => {
    r.style.display = (val === 'all' || r.classList.contains(val)) ? '' : 'none';
  });
}`
      },
      3: {
        title: "Password Strength Validator",
        render: `
          <input type="password" id="p1" placeholder="Password" style="width:100%; margin-bottom:8px;" oninput="valPass()" />
          <input type="password" id="p2" placeholder="Confirm Password" style="width:100%; margin-bottom:12px;" oninput="valPass()" />
          <button id="pSub" class="ui-btn" style="width:100%; opacity:0.5;" disabled>Submit</button>
        `,
        tasks: [
          "Evaluate strength (Weak/Medium/Strong) while typing.",
          "Apply corresponding border colors visually.",
          "Enable Submit button only when passwords match."
        ],
        html: `<input type="password" id="p1" placeholder="Password" oninput="valPass()" />
<input type="password" id="p2" placeholder="Confirm Password" oninput="valPass()" />
<button id="pSub" disabled>Submit Registration</button>`,
        css: `input { width: 100%; padding: 8px; margin-bottom: 8px; border: 2px solid #334155; }
input.weak { border-color: #ef4444; }
input.medium { border-color: #f59e0b; }
input.strong { border-color: #22c55e; }
button:disabled { opacity: 0.5; cursor: not-allowed; }`,
        js: `function valPass() {
  const p1 = document.getElementById('p1');
  const p2 = document.getElementById('p2');
  const btn = document.getElementById('pSub');
  const v = p1.value;

  p1.className = '';
  if (v.length >= 8 && /[0-9]/.test(v) && /[^a-zA-Z0-9]/.test(v)) {
    p1.classList.add('strong');
  } else if (v.length >= 6 && /[0-9]/.test(v)) {
    p1.classList.add('medium');
  } else if (v.length > 0) {
    p1.classList.add('weak');
  }

  const match = v !== '' && v === p2.value;
  btn.disabled = !match;
  btn.style.opacity = match ? '1' : '0.5';
}`
      },
      4: {
        title: "Multi-Step Quiz Navigator",
        render: `
          <div id="q1" class="q-group"><b>Q1: Is JavaScript single-threaded?</b><br><label><input type="radio" name="q1" value="1"> Yes</label></div>
          <div id="q2" class="q-group hidden"><b>Q2: Does CSS stand for Cascading Style Sheets?</b><br><label><input type="radio" name="q2" value="1"> Yes</label></div>
          <div style="margin-top:12px; display:flex; gap:8px;">
            <button id="qPrev" class="ui-btn" onclick="navStep(-1)" disabled>Prev</button>
            <button id="qNext" class="ui-btn" onclick="navStep(1)">Next</button>
          </div>
          <h4 id="qScore" style="margin-top:12px;" class="hidden"></h4>
        `,
        tasks: [
          "Display one question step at a time.",
          "Manage Prev/Next button states.",
          "Calculate final score upon completion."
        ],
        html: `<div id="q1" class="q-step">
  <p>Q1: Is JS single-threaded?</p>
  <label><input type="radio" name="q1" value="1"> Yes</label>
</div>
<div id="q2" class="q-step hidden">
  <p>Q2: Does CSS mean Cascading Style Sheets?</p>
  <label><input type="radio" name="q2" value="1"> Yes</label>
</div>

<div class="nav-btns">
  <button id="qPrev" onclick="navStep(-1)" disabled>Prev</button>
  <button id="qNext" onclick="navStep(1)">Next</button>
</div>
<h4 id="qScore" class="hidden"></h4>`,
        css: `.q-step { padding: 12px; background: #1e293b; border-radius: 6px; }
.hidden { display: none !important; }
.nav-btns { display: flex; gap: 8px; margin-top: 12px; }`,
        js: `let qStep = 1;

function navStep(dir) {
  document.getElementById(\`q\${qStep}\`).classList.add('hidden');
  qStep += dir;
  document.getElementById(\`q\${qStep}\`).classList.remove('hidden');

  document.getElementById('qPrev').disabled = (qStep === 1);

  if (qStep === 2) {
    document.getElementById('qNext').innerText = 'Submit';
    document.getElementById('qNext').onclick = () => {
      let score = document.querySelectorAll('input:checked').length;
      document.getElementById('qScore').innerText = \`Score: \${score} / 2\`;
      document.getElementById('qScore').classList.remove('hidden');
    };
  }
}`
      },
      5: {
        title: "Product Grid Filter",
        render: `
          <input type="text" id="pSearch" placeholder="Search product..." oninput="filterGrid()" style="width:100%; margin-bottom:8px;" />
          <div style="display:flex; gap:12px; margin-bottom:12px;" onchange="filterGrid()">
            <label><input type="radio" name="pCat" value="all" checked> All</label>
            <label><input type="radio" name="pCat" value="tech"> Tech</label>
            <label><input type="radio" name="pCat" value="book"> Book</label>
          </div>
          <div id="pGrid" style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
            <div class="pCard" data-cat="tech" style="background:#334155; padding:8px; border-radius:4px;">Laptop</div>
            <div class="pCard" data-cat="book" style="background:#334155; padding:8px; border-radius:4px;">JS Guide</div>
          </div>
        `,
        tasks: [
          "Filter grid items by text search box input.",
          "Filter simultaneously based on selected radio category.",
          "Perform case-insensitive title matching."
        ],
        html: `<input type="text" id="pSearch" placeholder="Search product..." oninput="filterGrid()" />

<div class="categories" onchange="filterGrid()">
  <label><input type="radio" name="pCat" value="all" checked> All</label>
  <label><input type="radio" name="pCat" value="tech"> Tech</label>
  <label><input type="radio" name="pCat" value="book"> Books</label>
</div>

<div class="grid">
  <div class="pCard" data-cat="tech">Laptop</div>
  <div class="pCard" data-cat="book">JS Handbook</div>
</div>`,
        css: `.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 12px; }
.pCard { background: #334155; padding: 12px; border-radius: 4px; }`,
        js: `function filterGrid() {
  const query = document.getElementById('pSearch').value.toLowerCase();
  const cat = document.querySelector('input[name="pCat"]:checked').value;

  document.querySelectorAll('.pCard').forEach(card => {
    const titleMatch = card.innerText.toLowerCase().includes(query);
    const catMatch = (cat === 'all' || card.dataset.cat === cat);

    card.style.display = (titleMatch && catMatch) ? 'block' : 'none';
  });
}`
      },
      6: {
        title: "Modal Dialog & Timer",
        render: `
          <button class="ui-btn" onclick="toggleModal(true)">Open Promo Modal</button>
          <div id="demoModal" class="hidden" style="position:fixed; inset:0; background:rgba(0,0,0,0.7); display:grid; place-items:center;">
            <div style="background:#1e293b; padding:20px; border-radius:8px; text-align:center;">
              <h3>🔥 Exclusive Offer!</h3>
              <p style="margin:12px 0;">Get 20% Off your next exam purchase.</p>
              <button class="ui-btn" onclick="toggleModal(false)">Close</button>
            </div>
          </div>
        `,
        tasks: [
          "Toggle modal visibility on button click.",
          "Close modal when clicking the backdrop overlay.",
          "Trigger modal automatically using setTimeout."
        ],
        html: `<button onclick="toggleModal(true)">Open Promo Modal</button>

<div id="demoModal" class="modal-overlay hidden" onclick="closeOnBackdrop(event)">
  <div class="modal-content">
    <h3>🔥 Exclusive Offer!</h3>
    <p>Get 20% Off your purchase!</p>
    <button onclick="toggleModal(false)">Close</button>
  </div>
</div>`,
        css: `.modal-overlay { position: fixed; inset: 0; background: rgba(0, 0, 0, 0.7); display: grid; place-items: center; }
.modal-content { background: #1e293b; padding: 20px; border-radius: 8px; text-align: center; }
.hidden { display: none !important; }`,
        js: `function toggleModal(show) {
  document.getElementById('demoModal').classList.toggle('hidden', !show);
}

function closeOnBackdrop(e) {
  if (e.target.id === 'demoModal') toggleModal(false);
}

// Automatically trigger after 4 seconds
setTimeout(() => toggleModal(true), 4000);`
      },
      7: {
        title: "Responsive Drawer Navigation",
        render: `
          <div style="border:1px solid #334155; height:120px; display:flex; overflow:hidden;">
            <div id="drawer" style="width:100px; background:#0284c7; padding:8px; transition:0.3s;">Sidebar</div>
            <div style="flex:1; padding:8px;">
              <button class="ui-btn" onclick="toggleDrawer()">☰ Toggle</button>
            </div>
          </div>
        `,
        tasks: [
          "Animate sidebar width or positioning on toggle.",
          "Toggle drawer visibility using hamburger icon.",
          "Auto-collapse on smaller window screen sizes."
        ],
        html: `<div class="wrapper">
  <div id="drawer" class="sidebar">Sidebar Menu</div>
  <div class="content">
    <button onclick="toggleDrawer()">☰ Toggle Menu</button>
  </div>
</div>`,
        css: `.wrapper { display: flex; height: 150px; border: 1px solid #334155; }
.sidebar { width: 120px; background: #0284c7; transition: width 0.3s; overflow: hidden; white-space: nowrap; }
.sidebar.collapsed { width: 0; }`,
        js: `function toggleDrawer() {
  document.getElementById('drawer').classList.toggle('collapsed');
}

window.addEventListener('resize', () => {
  if (window.innerWidth < 600) {
    document.getElementById('drawer').classList.add('collapsed');
  }
});`
      },
      8: {
        title: "LocalStorage Persistent To-Do List",
        render: `
          <div style="display:flex; gap:8px; margin-bottom:8px;">
            <input type="text" id="tInp" placeholder="New Task" style="flex:1;" />
            <button class="ui-btn" onclick="addTask()">Add</button>
          </div>
          <ul id="tList" style="list-style:none;"></ul>
        `,
        tasks: [
          "Dynamically append new task items into the DOM list.",
          "Toggle strikethrough styling on task item click.",
          "Persist array updates inside browser LocalStorage."
        ],
        html: `<div class="input-row">
  <input type="text" id="tInp" placeholder="Enter task..." />
  <button onclick="addTask()">Add Task</button>
</div>
<ul id="tList"></ul>`,
        css: `ul { list-style: none; padding: 0; }
li { padding: 6px; cursor: pointer; border-bottom: 1px solid #334155; }
li.completed { text-decoration: line-through; color: #64748b; }`,
        js: `let tasks = JSON.parse(localStorage.getItem('lab_tasks') || '[]');

function renderTasks() {
  const ul = document.getElementById('tList');
  if(!ul) return;
  ul.innerHTML = tasks.map((t, i) => 
    \`<li class="\${t.c ? 'completed' : ''}" onclick="toggleTask(\${i})">\${t.txt}</li>\`
  ).join('');
}

function addTask() {
  const input = document.getElementById('tInp');
  if (!input.value.trim()) return;

  tasks.push({ txt: input.value.trim(), c: false });
  localStorage.setItem('lab_tasks', JSON.stringify(tasks));
  input.value = '';
  renderTasks();
}

function toggleTask(i) {
  tasks[i].c = !tasks[i].c;
  localStorage.setItem('lab_tasks', JSON.stringify(tasks));
  renderTasks();
}`
      },
      9: {
        title: "Tabbed Content Switcher & Badge",
        render: `
          <div style="display:flex; gap:4px; margin-bottom:8px;">
            <button class="ui-btn" onclick="switchTab(1)">Profile</button>
            <button class="ui-btn" onclick="switchTab(2)">Alerts (<span id="nBadge">0</span>)</button>
          </div>
          <div id="tab1" class="tPane">User Profile Details</div>
          <div id="tab2" class="tPane hidden">Notification Center</div>
          <button class="ui-btn" style="margin-top:12px; background:#334155;" onclick="incBadge()">Simulate Trigger</button>
        `,
        tasks: [
          "Switch active content panel based on tab click.",
          "Maintain visual active border/background on tabs.",
          "Dynamically increment counter badge value."
        ],
        html: `<div class="tabs">
  <button class="tab-btn active" onclick="switchTab(1)">Profile</button>
  <button class="tab-btn" onclick="switchTab(2)">Alerts (<span id="nBadge">0</span>)</button>
</div>

<div id="tab1" class="tPane">Profile Panel Content</div>
<div id="tab2" class="tPane hidden">Alerts Panel Content</div>

<button onclick="incBadge()">Trigger Notification</button>`,
        css: `.tab-btn { padding: 6px 12px; background: #334155; border: none; color: white; }
.tab-btn.active { background: #0284c7; font-weight: bold; }
.tPane { padding: 12px; background: #1e293b; margin-top: 8px; }
.hidden { display: none !important; }`,
        js: `function switchTab(idx) {
  document.querySelectorAll('.tPane').forEach((p, i) => p.classList.toggle('hidden', i !== (idx - 1)));
  document.querySelectorAll('.tab-btn').forEach((b, i) => b.classList.toggle('active', i === (idx - 1)));
}

function incBadge() {
  const badge = document.getElementById('nBadge');
  badge.innerText = parseInt(badge.innerText) + 1;
}`
      },
      10: {
        title: "Character Limit & Progress Bar",
        render: `
          <textarea id="lblTxt" maxlength="100" style="width:100%; height:60px;" oninput="updateLimit(this)"></textarea>
          <div style="display:flex; justify-content:space-between; font-size:0.8rem; margin:4px 0;">
            <span id="lblCount">0 / 100</span>
          </div>
          <div style="background:#334155; height:6px; border-radius:3px; overflow:hidden;">
            <div id="lblBar" style="width:0%; height:100%; background:#38bdf8; transition:0.1s;"></div>
          </div>
        `,
        tasks: [
          "Track string input length in real-time.",
          "Calculate percentage and update progress bar width.",
          "Change warning color when approaching character limit."
        ],
        html: `<textarea id="lblTxt" maxlength="100" oninput="updateLimit(this)"></textarea>
<div id="lblCount">0 / 100</div>
<div class="progress-track">
  <div id="lblBar" class="progress-fill"></div>
</div>`,
        css: `textarea { width: 100%; height: 60px; background: #334155; color: #fff; }
.progress-track { background: #334155; height: 6px; border-radius: 3px; overflow: hidden; }
.progress-fill { width: 0%; height: 100%; background: #38bdf8; transition: width 0.1s; }`,
        js: `function updateLimit(ta) {
  const len = ta.value.length;
  document.getElementById('lblCount').innerText = \`\${len} / 100\`;

  const bar = document.getElementById('lblBar');
  bar.style.width = \`\${len}%\`;

  if (len >= 90) {
    bar.style.background = '#ef4444'; // Danger Red
  } else if (len >= 75) {
    bar.style.background = '#f59e0b'; // Warning Yellow
  } else {
    bar.style.background = '#38bdf8'; // Normal Blue
  }
}`
      }
    };

    // Load selected problem module
    function loadModule(num) {
      activeModule = num;
      document.querySelectorAll('nav button').forEach((b, i) => b.classList.toggle('active', (i + 1) === num));
      const mod = modules[num];
      
      document.getElementById('interactiveDemo').innerHTML = mod.render;
      
      const checklist = document.getElementById('taskChecklist');
      checklist.innerHTML = mod.tasks.map(t => `<li><input type="checkbox" checked disabled /> ${t}</li>`).join('');

      // Render Active Tab Code
      displayCode();

      // Post-mount hook for LocalStorage task rendering
      if(num === 8 && typeof renderTasks === 'function') renderTasks();
    }

    // Switch between HTML, CSS, JS Tabs
    function switchCodeTab(tab) {
      activeTab = tab;
      document.querySelectorAll('.code-tab-btn').forEach(b => {
        b.classList.toggle('active', b.innerText.toLowerCase() === tab);
      });
      displayCode();
    }

    // Display active code language inside pre tag
    function displayCode() {
      const mod = modules[activeModule];
      document.getElementById('codeDisplay').innerText = mod[activeTab];
    }

    // Copy solution code snippet
    function copyCode() {
      const code = document.getElementById('codeDisplay').innerText;
      navigator.clipboard.writeText(code);
      alert(`${activeTab.toUpperCase()} solution code copied to clipboard!`);
    }

    // Initialize default module view
    loadModule(1);
  