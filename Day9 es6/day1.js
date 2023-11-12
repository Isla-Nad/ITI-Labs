((num1, num2) => {
  alert(`The Sum of ${num1} and ${num2} is:  ${num1 + num2}`);
})(5, 6);

// ============================================================

let arr = [1, 2, 3, 8, 9];
console.log(arr);
console.log(`the odd nums are: ${arr.filter((num) => num % 2 !== 0)}`);

// // =============================================================

console.log(`the even nums are:`);
arr.forEach((num) => {
  if (num % 2 == 0) console.log(num);
});

// // =============================================================

console.log(`the squares are: ${arr.map((num) => num * num)}`);

// // =============================================================

for (let num of arr) {
  console.log(num);
}

arr.forEach((num) => console.log(num));

for (let num in arr) {
    console.log(num);
  }

let obj = { a: 1, b: 2, c: 3 };
for (const key in obj) {
  console.log(key, obj[key]);
}
// // =============================================================

document.getElementById("regularButton").addEventListener("click", function () {
  console.log(this);
});

document.getElementById("arrowButton").addEventListener("click", () => {
  console.log(this);
});
