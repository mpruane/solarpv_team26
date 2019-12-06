$.validator.setDefaults({
  submitHandler: function() {
    alert("submitted!");
  }
});

$(document).ready(function()
{
  $("#registrationForm").validate({
      rules: {
        rusername: {
            required: true,
            maxlength: 8
          },
        rpassword: {
            required: true,
            passwordCheck: true
        },
        rlastname: "required",
        gender: {required: true},
        raddress: "required",
        rcity: "required",
        rstate: "required",
        rzip: {
          required: true,
          minlength: 5,
          maxlength: 5
        },
        remail: "required",
        rcell: {
          required: true,
          minlength: 10,
          maxlength: 10
        },
        rcompany: "required"
      },
      messages: {
        rusername: {
          required: "Enter Username",
          maxlength: "Under 8 Characters"
        },
        rpassword: { required: "Enter Password"},
        rlastname: "Enter Last Name",
        gender: "Select Gender",
        raddress: "Enter Address",
        rcity: "Enter City",
        rstate: "Select State",
        rzip: {
          required: "Enter A Zip Code",
          minlength: "Enter 5 Digits",
          maxlength: "Enter 5 Digits"
        },
        remail: "Enter E-mail Address",
        rcell: {
          required: "Enter Cell Phone Number",
          minlength: "Enter 10 Digit Number",
          maxlength: "Enter 10 Digit Number"          
        },
        rcompany: "Enter Company Name"
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
