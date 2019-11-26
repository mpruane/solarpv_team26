$.validator.setDefaults({
  submitHandler: function() {
    alert("submitted!");
  }
});

function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
  $('.loginsub').removeAttr('disabled');
}

$(document).ready(function()
{
  $("#loginForm").validate({
      rules: {
        lusername: {
            required: true,
            maxlength: 8
          },
        lpassword: {
            required: true,
            passwordCheck: true
        }
      },
      messages: {
        lusername: {
          required: "Enter Username",
          maxlength: "Under 8 Characters"
        },
        lpassword: { required: "Enter Password"}
      }
  });
});
jQuery.validator.addMethod("passwordCheck",
        function(value, element, param) {
            if (this.optional(element)) {
                return true;
            } else if (!/[A-Z]/.test(value)) {
                return false;
            } else if (!/[a-z]/.test(value)) {
                return false;
            } else if (!/[0-9]/.test(value)) {
                return false;
            }
            return true;
        },
        "Uppercase Letter, Lowercase Letter, and Number Needed");
