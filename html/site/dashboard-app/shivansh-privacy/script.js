let balance = 0;
let budget = 0;
let expenses = JSON.parse(localStorage.getItem("expenses") || "[]");
let notes = [];
let activityLog = JSON.parse(localStorage.getItem("activityLog") || "[]");
let selectedMonth = "";
let userDocRef = null;

function initApp() {
  userDocRef = db.collection('users').doc(window.currentUserId);
  loadUserData();
  rendermonthGrid();
  updateAccountInfo();
}

async function loadUserData() {
  const doc = await userDocRef.get();
  if (doc.exists) {
    const data = doc.data();
    balance = data.balance || 0;
    budget = data.budget || 0;
    expenses = data.expenses?.length
      ? data.expenses
      : JSON.parse(localStorage.getItem("expenses") || "[]");

    notes = data.notes || [];
    activityLog = data.activityLog?.length
      ? data.activityLog
      : JSON.parse(localStorage.getItem("activityLog") || "[]");
  } else {
    await userDocRef.set({ balance: 0, budget: 0, expenses: [], notes: [], activityLog: [] });
    balance = 0;
    budget = 0;
    expenses = [];
    notes = [];
    activityLog = [];
  }
  updateBalanceDisplay();
  updateBudgetDisplay();
  renderExpenses();
  renderNotes();
  renderMonthGrid();
}

async function saveToFirestore(fields) {
    try {
        // Local backup
        if (fields.expenses !== undefined) {
            localStorage.setItem(
                "expenses",
                JSON.stringify(fields.expenses)
            );
        }

        if (fields.activityLog !== undefined) {
            localStorage.setItem(
                "activityLog",
                JSON.stringify(fields.activityLog)
            );
        }

        // Firebase save
        await userDocRef.set(fields, { merge: true });

        console.log("DATA SAVED SUCCESSFULLY");
    } catch (error) {
        console.error("SAVE ERROR:", error);
        alert("Data save nahi hua: " + error.message);
    }
}


/* ---------- Clock ---------- */
function updateClock() {
  const now = new Date();
  document.getElementById('clock').textContent = now.toLocaleString('en-IN', { timeZone: 'Asia/Kolkata', hour12: true, hour:'2-digit', minute:'2-digit', second:'2-digit' });
  document.getElementById('clockDate').textContent = now.toLocaleDateString('en-IN', { timeZone: 'Asia/Kolkata', weekday:'short', day:'numeric', month:'short', year:'numeric' });
}
setInterval(updateClock, 1000);
updateClock();

/* ---------- Calendar ---------- */
function renderCalendar() {
  const now = new Date();
  const year = now.getFullYear();
  const month = now.getMonth();
  const monthNames = ["January","February","March","April","May","June","July","August","September","October","November","December"];
  document.getElementById('calMonthYear').textContent = monthNames[month] + " " + year;

  const firstDay = new Date(year, month, 1).getDay();
  const daysInMonth = new Date(year, month+1, 0).getDate();
  const grid = document.getElementById('calGrid');
  grid.innerHTML = '';

  ["S","M","T","W","T","F","S"].forEach(d => {
    const el = document.createElement('div');
    el.textContent = d;
    el.style.fontWeight = '600';
    el.style.color = '#9a9aa0';
    grid.appendChild(el);
  });

  for (let i=0; i<firstDay; i++) {
    const el = document.createElement('div');
    el.className = 'cal-day empty';
    grid.appendChild(el);
  }
  for (let d=1; d<=daysInMonth; d++) {
    const el = document.createElement('div');
    el.className = 'cal-day';
    el.textContent = d;
    if (d === now.getDate()) el.classList.add('today');
    grid.appendChild(el);
  }
}
renderCalendar();

/* ---------- Three-dot menu ---------- */
function toggleMenu() {
  document.getElementById('dropdownMenu').classList.toggle('show');
}
document.addEventListener('click', function(e) {
  if (!e.target.closest('.menu-wrap')) {
    document.getElementById('dropdownMenu').classList.remove('show');
  }
});
function linkGoogle() {
  const email = prompt("Enter your Google email to link:");
  if (email) { saveToFirestore({ linkedGoogle: email }); updateAccountInfo(email, null); }
}
function linkMobile() {
  const mobile = prompt("Enter your mobile number to link:");
  if (mobile) { saveToFirestore({ linkedMobile: mobile }); updateAccountInfo(null, mobile); }
}
async function updateAccountInfo() {
  const doc = await userDocRef.get();
  const data = doc.exists ? doc.data() : {};
  let text = [];
  if (data.linkedGoogle) text.push('Google: ' + data.linkedGoogle);
  if (data.linkedMobile) text.push('Mobile: ' + data.linkedMobile);
  text.push('Account: ' + auth.currentUser.email);
  document.getElementById('accountInfo').textContent = text.join('  |  ');
}

function logout() {
  if (confirm("Are you sure you want to logout?")) {
    auth.signOut().then(() => { window.location.href = "login.html"; });
  }
}

/* ---------- Page switching ---------- */
function showOverview() {
  document.getElementById('mainApp').style.display = 'flex';
  document.getElementById('dataPage').style.display = 'none';
  document.getElementById('navOverview').classList.add('active');
  document.getElementById('navData').classList.remove('active');
}
function openDataPage() {
  document.getElementById('mainApp').style.display = 'none';
  document.getElementById('dataPage').style.display = 'block';
  document.getElementById('navData').classList.add('active');
  document.getElementById('navOverview').classList.remove('active');
}
function closeDataPage() { showOverview(); }

function showTab(tab) {
  document.getElementById('notesTab').style.display = tab === 'notes' ? 'block' : 'none';
  document.getElementById('historyTab').style.display = tab === 'history' ? 'block' : 'none';
  document.getElementById('tabNotesBtn').classList.toggle('active', tab === 'notes');
  document.getElementById('tabHistoryBtn').classList.toggle('active', tab === 'history');
  if (tab === 'history') renderActivityHistory();
}

/* ---------- Month picker ---------- */
const monthNamesFull = ["January","February","March","April","May","June","July","August","September","October","November","December"];
function renderMonthGrid() {
  const grid = document.getElementById('monthGrid');
  grid.innerHTML = '';
  const currentMonthName = monthNamesFull[new Date().getMonth()];
  selectedMonth = selectedMonth || currentMonthName;
  monthNamesFull.forEach(m => {
    const btn = document.createElement('button');
    btn.className = 'month-btn' + (m === selectedMonth ? ' selected' : '');
    btn.textContent = m;
    btn.onclick = () => { selectedMonth = m; renderMonthGrid(); };
    grid.appendChild(btn);
  });
}

/* ---------- Balance & Budget ---------- */
function setBalance() {
  const val = parseFloat(document.getElementById('balanceInput').value);
  if (!isNaN(val)) {
    balance = val;
    saveToFirestore({ balance });
    updateBalanceDisplay();
    document.getElementById('balanceInput').value = '';
  }
}
function updateBalanceDisplay() {
  document.getElementById('balanceDisplay').textContent = '₹' + balance.toLocaleString('en-IN');
}

function setBudget() {
  const val = parseFloat(document.getElementById('budgetInput').value);
  if (!isNaN(val)) {
    budget = val;
    saveToFirestore({ budget });
    updateBudgetDisplay();
    document.getElementById('budgetInput').value = '';
  }
}
function updateBudgetDisplay() {
  const totalSpent = expenses.reduce((sum, e) => sum + e.amount, 0);
  const percent = budget > 0 ? Math.min((totalSpent/budget)*100, 100) : 0;
  document.getElementById('budgetFill').style.width = percent + '%';
  document.getElementById('budgetText').textContent = `Spent ₹${totalSpent.toLocaleString('en-IN')} of ₹${budget.toLocaleString('en-IN')}`;
}

/* ---------- Expenses ---------- */
function renderExpenses() {
  const body = document.getElementById('expenseBody');
  body.innerHTML = '';
  expenses.slice().reverse().forEach((exp, revIndex) => {
    const index = expenses.length - 1 - revIndex;
    const row = document.createElement('tr');
    row.innerHTML = `<td>${exp.date}</td><td>${exp.item}</td><td>${exp.category}</td><td>₹${exp.amount.toLocaleString('en-IN')}</td><td><button class="delete-btn" onclick="deleteExpense(${index})">✕</button></td>`;
    body.appendChild(row);
  });
  updateBudgetDisplay();
}
function deleteExpense(index) {
  balance += expenses[index].amount;
  expenses.splice(index, 1);
  saveToFirestore({ balance, expenses });
  updateBalanceDisplay();
  renderExpenses();
}

document.getElementById('expenseForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const item = document.getElementById('itemName').value;
  const category = document.getElementById('category').value;
  const amount = parseFloat(document.getElementById('itemAmount').value);
  const now = new Date();
  const date = now.toLocaleDateString('en-IN', { timeZone:'Asia/Kolkata', day:'2-digit', month:'short' });
  const time = now.toLocaleTimeString('en-IN', { timeZone:'Asia/Kolkata', hour:'2-digit', minute:'2-digit' });
  const fullDate = now.toLocaleDateString('en-IN', { timeZone:'Asia/Kolkata', day:'2-digit', month:'short', year:'numeric' });

  if (item && !isNaN(amount)) {
    expenses.push({ item, category, amount, date });

    activityLog.push({ item, category, amount, date: fullDate, time });
    balance -= amount;

    saveToFirestore({ expenses, activityLog, balance });
    updateBalanceDisplay();
    renderExpenses();
    this.reset();
  }
});

/* ---------- Activity History ---------- */
function renderActivityHistory() {
  const container = document.getElementById('activityHistory');
  container.innerHTML = '';
  if (activityLog.length === 0) {
    container.innerHTML = '<p style="color:#9a9aa0; font-size:13px;">No activity yet.</p>';
    return;
  }
  activityLog.slice().reverse().forEach(a => {
    const div = document.createElement('div');
    div.className = 'activity-item';
    div.innerHTML = `
      <div class="a-left">
        <b>${a.item}</b> — ${a.category}
        <span>${a.date} at ${a.time}</span>
      </div>
      <div class="a-amount">₹${a.amount.toLocaleString('en-IN')}</div>
    `;
    container.appendChild(div);
  });
}

/* ---------- Notes ---------- */
function saveNote() {
  const text = document.getElementById('noteText').value.trim();
  if (!text) return;
  const date = new Date().toLocaleDateString('en-IN', { timeZone:'Asia/Kolkata', day:'2-digit', month:'short', year:'numeric' });
  notes.push({ month: selectedMonth, text, date });
  saveToFirestore({ notes });
  document.getElementById('noteText').value = '';
  renderNotes();
}
function deleteNote(index) {
  notes.splice(index, 1);
  saveToFirestore({ notes });
  renderNotes();
}
function renderNotes() {
  const container = document.getElementById('notesHistory');
  container.innerHTML = '';
  notes.slice().reverse().forEach((n, revIndex) => {
    const index = notes.length - 1 - revIndex;
    const div = document.createElement('div');
    div.className = 'note-item';
    div.innerHTML = `
      <button class="delete-btn" onclick="deleteNote(${index})">✕</button>
      <p class="note-month">${n.month}</p>
      <p class="note-date">${n.date}</p>
      <p>${n.text}</p>
    `;
    container.appendChild(div);
  });
}