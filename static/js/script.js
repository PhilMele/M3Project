// Register Page
function validatePassword() {
    const password = document.getElementById("password").value;
    const confirm_password = document.getElementById("confirm_password").value;
    const message = document.getElementById("message");
    const confirmMessage = document.getElementById("confirm_message");

    let strengthMessage = "";

    if (password.length < 8) {
        strengthMessage = "Password must be at least 8 characters long.";
    } else if (!/[A-Z]/.test(password)) {
        strengthMessage = "Password must contain at least one uppercase letter.";
    } else if (!/[a-z]/.test(password)) {
        strengthMessage = "Password must contain at least one lowercase letter.";
    } else if (!/\d/.test(password)) {
        strengthMessage = "Password must contain at least one number.";
    } else {
        strengthMessage = "Password is strong.";
    }

    message.textContent = strengthMessage;
    message.style.color = strengthMessage === "Password is strong." ? "#2ecc71" : "#e74c3c";

    if (password !== confirm_password) {
        confirmMessage.textContent = "Passwords do not match.";
        confirmMessage.style.color = "#e74c3c"; 
    } else {
        confirmMessage.textContent = "Passwords match.";
        confirmMessage.style.color = "#2ecc71";
    }
}
// Apply to Grant page  - Manages drop down of edit input filed
function toggleEditForm(questionId) {
    var form = document.getElementById('edit-form-' + questionId);
    if (form.style.display === 'none' || form.style.display === '') {
        form.style.display = 'block';
    } else {
        form.style.display = 'none';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    console.log("Active");

    // Create New Grant Page

    const grantFundInput = document.getElementById('grant_fund');  // Replace with actual ID
    const errorMessage = document.getElementById('error-message');
    const submitBtn = document.getElementById('submitBtn');

    const minInt = -2147483648;
    const maxInt = 2147483647;

    if (grantFundInput) {
        grantFundInput.addEventListener('input', function() {
            const value = parseInt(grantFundInput.value, 10);

            if (isNaN(value) || value < minInt || value > maxInt) {
                errorMessage.style.display = 'inline';
                submitBtn.disabled = true;
            } else {
                errorMessage.style.display = 'none';
                submitBtn.disabled = false;
            }
        });
    }
});