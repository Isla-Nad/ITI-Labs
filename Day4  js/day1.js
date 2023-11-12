let fName = prompt("What is your first name?");
let lName = prompt("What is your last name?");
confirm("Your name is " + fName + " " + lName);

let birthYear = prompt("What is your birth year?");
let age = 2023 - Number(birthYear);
confirm("Your age is " + age);

alert("Welcome, " + fName + " " + lName + " you are " + age + " years old.");

alert("I apologize but this is the first release of a calculator it only has a summation feature");

let fNum = prompt("Please enter the first number.");
let sNum = prompt("Please enter the second number.");
let result = Number(fNum) + Number(sNum);
alert("The result is: " + result)