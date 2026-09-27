function switchTab(tab) {
  document.getElementById('loginForm').style.display = tab === 'login' ? 'flex' : 'none';
  document.getElementById('signupForm').style.display = tab === 'signup' ? 'flex' : 'none';
  document.getElementById('loginTabBtn').classList.toggle('active', tab === 'login');
  document.getElementById('signupTabBtn').classList.toggle('active', tab === 'signup');
}

document.getElementById('loginForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const email = document.getElementById('loginEmail').value;
  const password = document.getElementById('loginPassword').value;
  auth.signInWithEmailAndPassword(email, password)
    .then(() => { window.location.href = "index.html"; })
    .catch((err) => { document.getElementById('loginError').textContent = err.message; });
});

document.getElementById('signupForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const email = document.getElementById('signupEmail').value;
  const password = document.getElementById('signupPassword').value;
  auth.createUserWithEmailAndPassword(email, password)
    .then(() => { window.location.href = "index.html"; })
    .catch((err) => { document.getElementById('signupError').textContent = err.message; });
});

// Agar already logged in hai, seedha dashboard bhej do
auth.onAuthStateChanged((user) => {
  if (user && window.location.pathname.includes('login.html')) {
    window.location.href = "index.html";
  }
});