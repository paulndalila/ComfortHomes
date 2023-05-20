const registerLink = document.getElementById("register-link");
const userLoginForm = document.getElementById("user-registration-form");
const ownerLoginForm = document.getElementById("owner-registration-form");

registerLink.addEventListener("click", function() {
  const loginChoice = prompt("Choose register as 'user' or 'owner':");
  if (loginChoice === "user") {
    userLoginForm.style.display = "block";
    ownerLoginForm.style.display = "none";
  } else if (loginChoice === "owner") {
    userLoginForm.style.display = "none";
    ownerLoginForm.style.display = "block";
  } else {
    alert("Invalid choice. Please choose 'user' or 'owner'.");
  }
});

