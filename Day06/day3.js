// first question---------------------------------

(function () {
  let num1 = prompt("please enter the first number:");
  let operation = prompt(
    "please enter an operation (sum ,multi ,subtract ,division)"
  );
  let num2 = prompt("please enter the second number:");
  num1 = Number(num1);
  num2 = Number(num2);
  if (operation == "sum") {
    alert(`the result is: ${num1 + num2}`);
  } else if (operation == "multi") {
    alert(`the result is: ${num1 * num2}`);
  } else if (operation == "subtract") {
    alert(`the result is: ${num1 - num2}`);
  } else if (operation == "division") {
    alert(`the result is: ${num1 / num2}`);
  }
})();

// second question---------------------------------

(function () {
  let username = prompt("please enter the username:");
  let password = prompt("please enter the password:");
  if (username == "admin" && password == "421$$") {
    alert("Welcome login success");
  } else if (username !== "admin") {
    alert("Sorry, username is wrong");
  } else if (password !== "421$$") {
    alert("Sorry, password is wrong");
  }
})();

// third question---------------------------------

(function () {
  let num1 = prompt("please enter anumber between 0 and 9:");
  let random = Math.random() * 10;
  num1 = Number(num1);
  if (num1 == random) {
    alert("congratulation, you guessed the correct number.");
  } else {
    alert("Sorry, you guessed wrong");
  }
})();

// fourth question---------------------------------

let contact = [];

function addUser() {
  let username = prompt("Please enter the name of the contact");
  let phone = prompt("Please enter the phone number");
  let user = { name: username, phone: phone };
  contact.push(user);
}

function searchUser() {
  let search = prompt("What do you want to search for?");

  function findUserByName(name) {
    let foundUser = contact.find((user) => user.name === name);
    return foundUser || null;
  }

  let foundUser = findUserByName(search);
  if (foundUser) {
    alert(`Name: ${foundUser.name} and phone: ${foundUser.phone}.`);
  } else {
    alert("Sorry, not matched.");
  }
}

while (true) {
  let operation = prompt(
    "Please enter 'add' or 'search' (or click 'Cancel' to exit)"
  );

  if (operation == null) {
    break;
  } else if (operation === "add") {
    addUser();
  } else if (operation === "search") {
    searchUser();
  }
}
