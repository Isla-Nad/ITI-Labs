$(".container1").append("<div class='black'>islam1</div>");

$(".container1").prepend("<div class='white'>islam2</div>");

$("p.pink").before("<p class='yellow'>islam3</p>");
// =========================================================
$(".container2 p").each(function (i) {
  $(this).replaceWith(`<a href="http://${$(this).text()}">${$(this).text()}</a>`);
});
// ===============================================================
$(".container3 img").wrap("<figure></figure>");

$("figure").append("<figcaption>Coffee</figcaption>");
// ===========================================================
$("td.col-age").text("");

$("td:contains(Mohsen)").addClass("man");

$("td").each(function () {
  if (!$(this).hasClass("your-email")) {
    $(this).addClass("your-email");
  } else {
    $(this).removeClass("your-email");
  }
});
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
// =================================================================
$(".container5 li")
  .filter((i) => i % 3 === 0)
  .css("color", "red");
// =================================================================
$(".container6 input[name=username]").val("Islam");
$("#remember").prop("checked", true);
