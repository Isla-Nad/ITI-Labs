// ******************************* 1st question
document.addEventListener("DOMContentLoaded", function () {
  let text = document.querySelector(".text");
  let mybtn = document.querySelector("#mybtn");
  mybtn.addEventListener("click", function () {
    let username = document.querySelector(".username").value;
    let password = document.querySelector(".password").value;
    let login = {
      username: username,
      password: password,
    };
    if (login.username === "admin" && login.password === "123") {
      text.textContent = "welcome";
      text.style.color = "green";
    } else {
      text.textContent = "Not registered";
      text.style.color = "red";
    }
  });
});

// ******************************* 2nd question
let mybtn2 = document.querySelector("#mybtn2");
mybtn2.addEventListener("click", function () {
  let arr1 = document.querySelector(".aar1").value;
  let arr2 = document.querySelector(".arr2").value;
  let array1 = arr1.split(",").map(Number);
  let array2 = arr2.split(",").map(Number);
  let newArr = array1
    .concat(array2)
    .filter((item, index, arr) => arr.indexOf(item) === index);
  document.querySelector(".text2").textContent = newArr;
});

// ******************************* 3rd question
const taskInput = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const taskList = document.getElementById("taskList");

let tasks = [];

function addTask() {
  const taskName = taskInput.value.trim();
  if (taskName === "") {
    alert("Please enter a valid task name.");
    return;
  }

  const task = {
    name: taskName,
    status: "pending",
  };

  tasks.push(task);
  saveTasksToLocalStorage();
  renderTaskList();
  taskInput.value = "";
}

function toggleTaskStatus(index) {
  tasks[index].status = tasks[index].status === "pending" ? "done" : "pending";
  saveTasksToLocalStorage();
  renderTaskList();
}

function deleteTask(index) {
  tasks.splice(index, 1);
  saveTasksToLocalStorage();
  renderTaskList();
}

function saveTasksToLocalStorage() {
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasksFromLocalStorage() {
  const storedTasks = localStorage.getItem("tasks");
  if (storedTasks) {
    tasks = JSON.parse(storedTasks);
  }
}

function renderTaskList() {
  taskList.innerHTML = "";
  tasks.forEach((task, index) => {
    const li = document.createElement("li");
    li.textContent = task.name;

    if (task.status === "done") {
      li.classList.add("done");
    }

    const doneBtn = document.createElement("button");
    doneBtn.textContent = "Done";
    doneBtn.classList.add("done");
    doneBtn.addEventListener("click", () => toggleTaskStatus(index));

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.addEventListener("click", () => deleteTask(index));

    li.appendChild(doneBtn);
    li.appendChild(deleteBtn);
    taskList.appendChild(li);
  });
}

addBtn.addEventListener("click", addTask);
loadTasksFromLocalStorage();
renderTaskList();
