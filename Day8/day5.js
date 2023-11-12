//******************************* */ question n1

let currentIndex = 0;
let intervalId;
let images = [];

function fetchImages() {
  const xhr = new XMLHttpRequest();
  xhr.open("GET", "https://jsonplaceholder.typicode.com/albums/1/photos");
  xhr.onload = function () {
    if (xhr.status === 200) {
      images = JSON.parse(xhr.responseText);
      showImage(currentIndex);
    }
  };
  xhr.send();
}

function showImage(index) {
  const sliderImage = document.getElementById("slider-image");
  const sliderText = document.getElementById("slider-text");

  sliderImage.src = images[index].url;
  sliderText.textContent = images[index].title;
}

function playSlider(speed) {
  clearInterval(intervalId);
  intervalId = setInterval(() => {
    currentIndex = (currentIndex + 1) % images.length;
    showImage(currentIndex);
  }, speed);
}

document
  .getElementById("play-btn")
  .addEventListener("click", () => playSlider(6000));
document
  .getElementById("stop-btn")
  .addEventListener("click", () => clearInterval(intervalId));
document.getElementById("prev-btn").addEventListener("click", () => {
  currentIndex = (currentIndex - 1 + images.length) % images.length;
  showImage(currentIndex);
});
document.getElementById("next-btn").addEventListener("click", () => {
  currentIndex = (currentIndex + 1) % images.length;
  showImage(currentIndex);
});
document
  .getElementById("speed-6s-btn")
  .addEventListener("click", () => playSlider(6000));
document
  .getElementById("speed-4s-btn")
  .addEventListener("click", () => playSlider(4000));
document
  .getElementById("speed-2s-btn")
  .addEventListener("click", () => playSlider(2000));

fetchImages();
playSlider(6000);

//******************************* */ question n2

const contactTable = document.getElementById("contact-table");
const addBtn = document.getElementById("add-btn");
const updateBtn = document.getElementById("update-btn");
const searchInput = document.getElementById("search");

addBtn.addEventListener("click", addContact);
updateBtn.addEventListener("click", updateContact);
searchInput.addEventListener("input", searchContacts);

loadContacts();

function loadContacts() {
  const contacts = getContactsFromLocalStorage();
  renderContactTable(contacts);
}

function addContact() {
  const title = document.querySelector('input[name="gender"]:checked').value;
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const card = document.getElementById("card").value;
  const save = document.getElementById("save").checked;

  const newContact = {
    title: title,
    name: name,
    email: email,
    card: card,
    save: save,
  };

  const contacts = getContactsFromLocalStorage();
  contacts.push(newContact);
  saveContactsToLocalStorage(contacts);

  renderContactTable(contacts);
  updateNumberOfUsers(contacts.length);

  document.querySelector('input[name="gender"]:checked').checked = false;
  document.getElementById("name").value = "";
  document.getElementById("email").value = "";
}

function editContact(index) {
  const contacts = getContactsFromLocalStorage();
  const contact = contacts[index];

  document.querySelector(
    `input[name="gender"][value="${contact.title}"]`
  ).checked = true;
  document.getElementById("name").value = contact.name;
  document.getElementById("email").value = contact.email;
  document.getElementById("card").value = contact.card;
  document.getElementById("save").checked = contact.save;

  const editBtn = document.querySelector(
    `tr:nth-child(${index + 2}) button:nth-child(5)`
  );
  editBtn.disabled = true;

  const saveBtn = document.querySelector(
    `tr:nth-child(${index + 2}) button:nth-child(6)`
  );
  saveBtn.style.display = "block";

  addBtn.style.display = "none";

  updateBtn.style.display = "block";
  updateBtn.dataset.index = index.toString();
}

function updateContact() {
  const index = parseInt(updateBtn.dataset.index);
  const contacts = getContactsFromLocalStorage();
  const editedContact = {
    title: document.querySelector('input[name="gender"]:checked').value,
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    card: document.getElementById("card").value,
    save: document.getElementById("save").checked,
  };

  contacts.push(editedContact);
  saveContactsToLocalStorage(contacts);
  renderContactTable(contacts);
  updateNumberOfUsers(contacts.length);

  const editBtn = document.querySelector(
    `tr:nth-child(${contacts.length + 1}) button:nth-child(5)`
  );
  editBtn.disabled = false;

  const saveBtn = document.querySelector(
    `tr:nth-child(${contacts.length + 1}) button:nth-child(6)`
  );
  saveBtn.style.display = "none";

  addBtn.style.display = "block";
  updateBtn.style.display = "none";

  document.querySelector('input[name="gender"]:checked').checked = false;
  document.getElementById("name").value = "";
  document.getElementById("email").value = "";
}

function deleteContact(index) {
  const contacts = getContactsFromLocalStorage();
  contacts.splice(index, 1);
  saveContactsToLocalStorage(contacts);
  renderContactTable(contacts);
  updateNumberOfUsers(contacts.length);
}

function searchContacts() {
  const query = searchInput.value.toLowerCase();
  const contacts = getContactsFromLocalStorage();
  const filteredContacts = contacts.filter((contact) =>
    contact.name.toLowerCase().includes(query)
  );
  renderContactTable(filteredContacts);
}

function getContactsFromLocalStorage() {
  const contacts = JSON.parse(localStorage.getItem("contacts")) || [];
  return contacts;
}

function saveContactsToLocalStorage(contacts) {
  localStorage.setItem("contacts", JSON.stringify(contacts));
}

function renderContactTable(contacts) {
  const tbody = contactTable.querySelector("tbody");
  tbody.innerHTML = "";

  contacts.forEach((contact, index) => {
    const row = document.createElement("tr");
    const nameAndTitleCell = document.createElement("td");
    const emailCell = document.createElement("td");
    const cardCell = document.createElement("td");
    const saveCell = document.createElement("td");
    const editCell = document.createElement("td");
    const deleteCell = document.createElement("td");

    const nameAndTitle = document.createElement("span");
    nameAndTitle.textContent = `${contact.title}, ${contact.name}`;
    nameAndTitleCell.appendChild(nameAndTitle);
    nameAndTitleCell.classList.add("name-and-title");

    emailCell.innerHTML = `<input type="email" id="email-${index}" value="${contact.email}">`;

    const cardSelect = document.createElement("select");
    cardSelect.id = `card-${index}`;
    const visaOption = document.createElement("option");
    visaOption.value = "visa";
    visaOption.textContent = "Visa";
    cardSelect.appendChild(visaOption);
    cardSelect.value = contact.card;
    cardCell.appendChild(cardSelect);

    const saveCheckbox = document.createElement("input");
    saveCheckbox.type = "checkbox";
    saveCheckbox.id = `save-${index}`;
    saveCheckbox.checked = contact.save;
    saveCell.appendChild(saveCheckbox);

    const editBtn = document.createElement("button");
    editBtn.textContent = "📝 Edit";
    editBtn.addEventListener("click", () => editContact(index));
    editCell.appendChild(editBtn);

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "🗑️ Delete";
    deleteBtn.addEventListener("click", () => deleteContact(index));
    deleteCell.appendChild(deleteBtn);

    row.appendChild(nameAndTitleCell);
    row.appendChild(emailCell);
    row.appendChild(cardCell);
    row.appendChild(saveCell);
    row.appendChild(editCell);
    row.appendChild(deleteCell);
    tbody.appendChild(row);
  });

  updateNumberOfUsers(contacts.length);
}

function updateNumberOfUsers(count) {
  const footerRow = contactTable.querySelector("tfoot tr");
  footerRow.innerHTML = `<td colspan="6">Number of users is ${count}</td>`;
}
