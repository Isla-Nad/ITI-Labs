let usernameInput = document.getElementById("username");
let passwordInput = document.getElementById("password");
let checkbox = document.getElementById("remember");
let btn = document.getElementById("loginButton");
btn.addEventListener("click", () => {
  let username = usernameInput.value;
  let password = passwordInput.value;
  let isRemembered = checkbox.checked;
  if (username && password && isRemembered) {
    localStorage.setItem("username", username);
    localStorage.setItem("password", password);
    localStorage.setItem("remembered", "true");
  } else {
    localStorage.clear();
  }
});
let isRemembered = localStorage.getItem("remembered") === "true";
let savedUsername = localStorage.getItem("username");
let savedPassword = localStorage.getItem("password");
usernameInput.value = savedUsername;
passwordInput.value = savedPassword;
checkbox.checked = true;

// ===============================================================

let students = [
  {
    ID: "12345756",
    name: "John Doe",
    age: 20,
    skills: ["JavaScript", "HTML", "CSS"],
    isLeader: true,
    address: "123 Main Street, City, Country",
  },
  {
    ID: "123454534536",
    name: "ahmed Doe",
    age: 20,
    skills: ["JavaScript", "HTML", "CSS"],
    isLeader: true,
    address: null,
  },
  {
    ID: "1234dghf56",
    name: "islam Doe",
    age: 20,
    skills: ["JavaScript", "HTML", "CSS"],
    isLeader: true,
    address: "123 Main Street, City, Country",
  },
];
console.log(JSON.stringify(students));

students.forEach((student) => {
  console.log(`${student.name}'s skills: ${student.skills.join(", ")}`);
});

// ======================================================

function getData() {
  let request = new XMLHttpRequest();
  request.open("GET", "https://reqres.in/api/users/1", true);
  request.send();
  request.onreadystatechange = () => {
    if (request.status == 200 && request.readyState == 4) {
      let data = JSON.parse(request.responseText);
      //   console.log(data.data.first_name, data.data.last_name, data.data.avatar);
      let myimg = document.querySelector("#avatar img");
      myimg.setAttribute("src", data.data.avatar);
      let text = document.querySelector("#avatar p");
      text.textContent = data.data.first_name + " " + data.data.last_name;
      return data;
    }
  };
}
getData();

// ===================================================================

document.addEventListener("DOMContentLoaded", function () {
  let userListDiv = document.getElementById("userList");
  fetch("https://reqres.in/api/users")
    .then((response) => response.json())
    .then((data) => {
      displayUsers(data.data);
    });
  function displayUsers(users) {
    userListDiv.innerHTML = "";
    users.forEach((user) => {
      const userDiv = document.createElement("div");
      userDiv.innerHTML = `
          <p>ID: ${user.id}</p>
          <p>Name: ${user.first_name} ${user.last_name}</p>
          <img src="${user.avatar}" alt="User Avatar">
          <hr>
        `;
      userListDiv.appendChild(userDiv);
    });
  }
});

// =============================================================

document.addEventListener("DOMContentLoaded", function () {
  let userSelect = document.getElementById("userSelect");
  let userDataDiv = document.getElementById("userData");
  let apiUrl = "https://reqres.in/api/users/";
  userSelect.addEventListener("change", () => {
    const selectedUserId = userSelect.value;
    fetch(apiUrl + selectedUserId)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        displayUserData(data.data);
      });
  });
  function displayUserData(user) {
    userDataDiv.innerHTML = "";

    let userDiv = document.createElement("div");
    userDiv.innerHTML = `
        <p>ID: ${user.id}</p>
        <p>Name: ${user.first_name} ${user.last_name}</p>
        <img src="${user.avatar}" alt="User Avatar">
      `;
    userDataDiv.appendChild(userDiv);
  }
  let userDataDiv2 = document.getElementById("userData2");
  let userSearch = document.getElementById("search");
  let btn2 =document.getElementById("jake")
  btn2.addEventListener("click", () => {
    const selectedUserId = userSearch.value;
    fetch(apiUrl + selectedUserId)
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        displayUserData2(data.data);
      });
  });
  function displayUserData2(user) {
    userDataDiv2.innerHTML = "";

    let userDiv = document.createElement("div");
    userDataDiv2.innerHTML = `
        <p>ID: ${user.id}</p>
        <p>Name: ${user.first_name} ${user.last_name}</p>
        <img src="${user.avatar}" alt="User Avatar">
      `;
    userDataDiv2.appendChild(userDiv);
  }
});

// =============================================================
