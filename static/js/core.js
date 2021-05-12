$(document).ready(function() {

  // Check for click events on the navbar burger icon
  $(".navbar-burger").click(function() {
      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      $(".navbar-burger").toggleClass("is-active");
      $(".navbar-menu").toggleClass("is-active");

  });
});

var col = document.getElementsByClassName("collapsible")
var i;

for (i = 0; i < col.length; i++) {
    col[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display == "grid") {
            content.style.display = "none";
        } else {
            content.style.display = "grid";
        }
    });
}