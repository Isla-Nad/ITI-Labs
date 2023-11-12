$(".container1 div").each(function () {
  $(this).css("background", $(this).attr("class"));
});
$(".container1 p").each(function () {
  $(this).css("color", $(this).attr("class"));
});
// ========================================================
$("a[href*='google']").text("Google");
$("a[href$='org']").text("IEEE");
$("a[href^='https']").text("Facebook");
$("a[href^='http']").append(" Official Website");
// ===========================================
$("img[src='img/Lemon.png']").attr("src", "img/orange.png").next().text("fig.3 - Orange Juice");
// =======================================================
$("td.my-name").attr("style", "color: blue;");
$("td:odd").css("background", "pink");
$("table tr:last td:nth-child(2)").css("font-weight", "bold");
// ===============================================================
$("ul>li:nth-child(2)").css("font-style", "italic")
$("ol>li:nth-child(2)+li").css("color", "red")

