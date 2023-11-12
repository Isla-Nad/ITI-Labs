// var shape = document.createElementNS("http://www.w3.org/2000/svg","path");
const svg = document.querySelector("#my-svg");
const line = document.querySelector("#ab-line");
const rect = document.querySelector("#ab-rect");
const circle = document.querySelector("#ab-circle");

line.addEventListener("click", () => {
  let randomLine = Math.floor(Math.random() * 600);
  svg.innerHTML += `<g fill="none" stroke="black">
                    <path stroke-width="2" d="M${randomLine} 20 L20 ${randomLine}" />
                    </g>`;
});

rect.addEventListener("click", () => {
  let randomLine = Math.floor(Math.random() * 600);
  svg.innerHTML += `<rect width="200" height="100" x="${randomLine}" y="${randomLine}" style="fill:rgb(0,0,255);stroke-width:10;"/>`;
});

circle.addEventListener("click", () => {
  let randomLine = Math.floor(Math.random() * 600);
  svg.innerHTML += `<circle cx="${randomLine}" cy="${randomLine}" r="40" stroke="orange" stroke-width="4" fill="blue" />`;
});
