function generateGreetings() {
  const user1 = document.getElementById("user1").value.trim();
  const user2 = document.getElementById("user2").value.trim();
  const greeting1El = document.getElementById("greeting1");
  const greeting2El = document.getElementById("greeting2");
  const handIcon = document.getElementById("handIcon");

  greeting1El.textContent = "";
  greeting2El.textContent = "";

  if (!user1 || !user2) {
    greeting1El.textContent = "⚠️ Please enter both names.";
    return;
  }

  const hour = new Date().getHours();
  const greeting = hour < 12 ? "Good morning" : hour < 18 ? "Good afternoon" : "Good evening";

  greeting1El.textContent = `${greeting}, ${user1}!`;
  greeting2El.textContent = `${greeting}, ${user2}!`;

  // Animate hand wave
  handIcon.classList.remove("wave");
  void handIcon.offsetWidth;
  handIcon.classList.add("wave");

  // Wink effect after wave
  setTimeout(() => {
    handIcon.textContent = "😉";
    setTimeout(() => {
      handIcon.textContent = "👋";
    }, 800);
  }, 1000);
}