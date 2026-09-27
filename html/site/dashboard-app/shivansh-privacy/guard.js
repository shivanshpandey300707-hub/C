auth.onAuthStateChanged((user) => {
  if (!user) {
    window.location.href = "login.html";
  } else {
    window.currentUserId = user.uid;
    initApp();
  }
});