// Set jQuery XHR header for CSRF requests
var csrftoken = $("[name=csrfmiddlewaretoken]").val();

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function() {

  // Check for click events on the navbar burger icon
  $(".navbar-burger").click(function() {
      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      $(".navbar-burger").toggleClass("is-active");
      $(".navbar-menu").toggleClass("is-active");

  });

  // Check for click events on the user profile dropdown
  $(".user-dropdown").click(function() {
      // Toggle the "is-active" class on the "user-dropdown" class
      $(".user-dropdown").toggleClass("is-active");

  });

  $("#webtheme-auto").click(function () {
        $.post(
            '/accounts/settheme/',
            {
                'theme': "auto"
            },
            function () {
                location.reload();
            }, 'text');
    });
    $("#webtheme-light").click(function () {
        $.post(
            '/accounts/settheme/',
            {
                'theme': "light"
            },
            function () {
                location.reload();
            }, 'text');
    });
    $("#webtheme-dark").click(function () {
        $.post(
            '/accounts/settheme/',
            {
                'theme': "dark"
            },
            function () {
                location.reload();
            }, 'text');
    });

  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      $('#breadcrumbs-section').removeClass('has-background-light-scheme');
      $('#breadcrumbs-section').addClass('has-background-dark-scheme');
  }
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