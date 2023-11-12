const numbers1 = [1, 2, 3, 4, 5];
const numbers2 = [6, 7, 8];
const mergedNumbers = [...numbers1, ...numbers2];
console.log("numbers1:", numbers1);
console.log("numbers2:", numbers2);
console.log("Merged numbers:", mergedNumbers);


// ========================================================



function Student(name, university, faculty, finalGrade) {
  this.name = name;
  this.university = university;
  this.faculty = faculty;
  this.finalGrade = finalGrade;
}
const student1 = new Student("Islam", " beni-suef", "sceince", 79.4);






// ==================================================================



console.log(`${student1.name} is a student in faculty of ${student1.faculty} in university ${student1.university}, and his final grade is ${student1.finalGrade}.`);


// ==================================================================




const studentNames = new Set();
studentNames.add("Islam");
studentNames.add("Ahmed");
studentNames.add("Mohamed");
studentNames.add("Islam");
console.log([...studentNames]);
for (const name of studentNames) {
  console.log(name);
}




// ==================================================================





const tipDisplay = document.getElementById("tip");
const generateBtn = document.getElementById("generateBtn");
const intervalBtn = document.getElementById("intervalBtn");

function* tipGenerator() {
  const tips = ["Drink plenty of water.", "Get enough sleep.", "Eat a balanced diet.", "Exercise regularly.", "Take breaks during work.", "Practice mindfulness.", "Keep a positive attitude.", "Spend time with loved ones.", "Read a good book.", "Learn something new each day."];
  for (let i = 0; i < tips.length; i++) {
    yield tips[i];
  }
}

const tipsGenerator = tipGenerator();
generateBtn.addEventListener("click", () => {
  let allTips = ""; 
  for (const tip of tipsGenerator) {
    allTips += tip + "<br>";
  }
  tipDisplay.innerHTML = allTips;
});

let intervalId;
intervalBtn.addEventListener("click", () => {
  tipDisplay.textContent = "";
  intervalId = setInterval(() => {
    const { value, done } = tipsGenerator.next();
    if (done) {
      clearInterval(intervalId);
    } else {
      tipDisplay.textContent = value;
    }
  }, 3000);
});






// =================================================================
const arr = [1, 2, [3, 4], [5, [6, 7]], 8];
const arr2 = arr.flat();
console.log(arr2);
const arr3 = arr2.flat();
console.log(arr3);
// ==============================================================================
const student = [
  ['name', 'islam'],
  ['age', 27],
  ['city', 'beni seuf']
];
const person = Object.fromEntries(student);
console.log(person);
// =================================================================
const student2 = {
  name: "islam",
  age: 27,
  city: "minia"
};
const array = Object.values(student2);
console.log(array); 