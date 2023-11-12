const canvas = document.querySelector("#my-canvas");
const context = canvas.getContext("2d");
const line = document.querySelector("#ab-line");
const freehand = document.querySelector("#ab-freehand");
const rect = document.querySelector("#ab-rect");
const circle = document.querySelector("#ab-circle");
const eraser = document.querySelector("#ab-eraser");
const fillColor = document.querySelector("#fill-color");
const strokeColor = document.querySelector("#stroke-color");
let fillChoosenColor;
let strokeChoosenColor;

fillColor.addEventListener("change", () => {
  fillChoosenColor = fillColor.value;
});

strokeColor.addEventListener("change", () => {
  strokeChoosenColor = strokeColor.value;
});

line.addEventListener("click", () => {
  let randomLine = Math.floor(Math.random() * 600);
  context.beginPath();
  context.moveTo(randomLine, 25);
  context.lineTo(150, randomLine);
  context.strokeStyle = strokeChoosenColor;
  context.stroke();
});

rect.addEventListener("click", () => {
  let randomLine = Math.floor(Math.random() * 600);
  context.beginPath();
  context.fillStyle = fillChoosenColor;
  context.fillRect(randomLine, randomLine, 150, 75);
  context.strokeStyle = strokeChoosenColor;
  context.lineWidth = 5;
  context.stroke();
});

circle.addEventListener("click", () => {
  let randomLine = Math.floor(Math.random() * 600);
  context.beginPath();
  context.arc(randomLine, randomLine, 40, 0, 2 * Math.PI);
  context.fillStyle = fillChoosenColor;
  context.fill();
  context.strokeStyle = strokeChoosenColor;
  context.stroke();
});

eraser.addEventListener("click", () => {
  context.clearRect(0, 0, 700, 450);
});

freehand.addEventListener("click", () => {
  let myFlag = false;
  canvas.addEventListener("mousedown", (e) => {
    startX = e.offsetX;
    startY = e.offsetY;
    context.moveTo(startX, startY);
    myFlag = true;
  });
  canvas.addEventListener("mousemove", (e) => {
    if (myFlag) {
      startX = e.offsetX;
      startY = e.offsetY;
      context.lineTo(startX, startY);
      context.stroke();
    }
  });
  canvas.addEventListener("mouseup", (e) => {
    myFlag = false;
  });
});

// ================================================
// not working

// let myFlag = false;
// function handleMouseDown(e) {
//   startX = e.offsetX;
//   startY = e.offsetY;
//   context.moveTo(startX, startY);
//   myFlag = true;
// }
// function handleMouseMove(e) {
//   if (myFlag) {
//     startX = e.offsetX;
//     startY = e.offsetY;
//     context.lineTo(startX, startY);
//     context.stroke();
//   }
// }
// function handleMouseUp(e) {
//   myFlag = false;
// }

// freehand.addEventListener("click", freehandHandler, false);

// function freehandHandler() {
//   canvas.addEventListener("mousedown", handleMouseDown);
//   canvas.addEventListener("mousemove", handleMouseMove);
//   canvas.addEventListener("mouseup", handleMouseUp);
// }

// function removeFreehandHandler() {
//   canvas.removeEventListener("mousedown", handleMouseDown);
//   canvas.removeEventListener("mousemove", handleMouseMove);
//   canvas.removeEventListener("mouseup", handleMouseUp);
// }

// freehand.addEventListener("click", removeFreehandHandler, false);
