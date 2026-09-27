const firebaseConfig = {
  apiKey: "AIzaSyDgtHL8zkb8uF5AyPm9pFw53VQsYHRAzLk",
  authDomain: "count-ur-mon9e.firebaseapp.com",
  projectId: "count-ur-mon9e",
  storageBucket: "count-ur-mon9e.firebasestorage.app",
  messagingSenderId: "953745102481",
  appId: "1:953745102481:web:232faa81ede13197f21130",
  measurementId: "G-D8B7LH8V6Y"
};

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.firestore();