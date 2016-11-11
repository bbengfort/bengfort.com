/*
 * bengfort.js
 * Main javascript function that should be run first thing on Bengfort.com.
 *
 * Author:  Benjamin Bengfort <benjamin@bengfort.com>
 * Created: Fri Nov 11 11:00:35 2016 -0500
 *
 * Dependencies:
 *  - jquery
 */

(function($) {

  // Do the CSRf AJAX Modification
  // var csrfToken   = $('input[name="csrfmiddlewaretoken"]').val();
  // $.ajaxSetup({headers: {"X-CSRFToken": csrfToken}});

  // Update the status and the version from the API.
  var statusURL = "/api/status/";
  $.get(statusURL)
    .success(function(data) {
      $("#footerVersion").text(data.version);
      if (data.status == "ok") {
        $("#footerStatus").addClass("text-success");
      } else {
        $("#footerStatus").addClass("text-warning");
      }
    })
    .fail(function() {
      $("#footerVersion").text("X.X");
      $("#footerStatus").addClass("text-danger");
    });

  // Add the hotkeys for easy management
  $(document).ready(function() {
    $(document).keyup(function(e) {
      if (e.keyCode == 27) {
        e.preventDefault();
        window.location = "/admin/";
      }
    });
  });

  console.log("The Bengfort.com App is started and ready");

})(jQuery);
