// var googleMapSrc = "http://maps.googleapis.com/maps/api/staticmap?center="+latlon+"&zoom=14&size=400x300&sensor=false";
const getLoction = document.querySelector("#get-loc");
const gotoLoction = document.querySelector("#go-loc");
const showLat = document.querySelector("#lat");
const showLon = document.querySelector("#lon");
let latitude;
let longitude;

getLoction.addEventListener("click", () => {
  navigator.geolocation.getCurrentPosition(function (pos) {
    latitude = pos.coords.latitude;
    longitude = pos.coords.longitude;
    showLat.textContent = latitude;
    showLon.textContent = longitude;
  });
});

gotoLoction.addEventListener("click", () => {
  let googleMap = `https://maps.google.com/maps?q=${latitude},${longitude}`;
  open(googleMap);
});
