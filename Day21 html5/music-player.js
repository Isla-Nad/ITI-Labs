const player = document.querySelector("#audio-player");
const play = document.querySelector("#mp-play-mode");
const list = document.querySelector("#al-list");
const repeat = document.querySelector("#mp-repeat-mode");
const shuffle = document.querySelector("#mp-shuffle-mode");

play.addEventListener("click", () => {
  if (play.value === "Play") {
    player.play();
    play.setAttribute("value", "Pause");
  } else {
    player.pause();
    play.setAttribute("value", "Play");
  }
});
// player.addEventListener("ended", () => {
//   const items = Array.from(list.children);
//   items.forEach((item) => {
//     let next = item.nextElementSibling.getAttribute("href");
//     player.setAttribute("src", next);
//   });
// });
player.addEventListener("ended", () => {
  const items = Array.from(list.children);
  const currentItem = document.querySelector(`[href="${player.getAttribute("src")}"]`);
  const i = items.indexOf(currentItem);
  if (i !== -1 && i < items.length - 1) {
    const next = items[i + 1].getAttribute("href");
    player.setAttribute("src", next);
    player.load();
    player.play();
  }
});

list.addEventListener("click", (e) => {
  if (e.target.tagName === "LI") {
    player.setAttribute("src", e.target.getAttribute("href"));
    player.play();
  }
  if (e.target.tagName === "SPAN") {
    document.querySelector("span").parentElement.remove();
  }
});

repeat.addEventListener("click", () => {
  player.load();
  player.play();
});

shuffle.addEventListener("click", () => {
  const items = Array.from(list.children);
  list.innerHTML = "";
  for (let i = 0; i < items.length; i++) {
    const j = Math.floor(Math.random() * i);
    [items[i], items[j]] = [items[j], items[i]];
  }
  items.forEach((item) => list.appendChild(item));
});
// ====================================================
let add = document.querySelector("#al-add");
add.addEventListener("change", (e) => {
  if (add.files[0]) {
    list.innerHTML += `<li style="cursor: pointer" href="${URL.createObjectURL(add.files[0])}">${e.target.files[0].name}</li>`;
  }
});
