function validateForm() {
    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let mobile = document.getElementById("mobile").value.trim();
    let dept = document.getElementById("department").value;
    let feedback = document.getElementById("feedback").value.trim();
    let gender = document.getElementsByName("gender");

    let error = "";

    if (name === "") error = "Name cannot be empty";
    else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) error = "Invalid email";
    else if (!/^\d{10}$/.test(mobile)) error = "Mobile must be 10 digits";
    else if (dept === "") error = "Select department";
    else if (![...gender].some(g => g.checked)) error = "Select gender";
    else if (feedback.split(" ").length < 10) error = "Minimum 10 words required";

    if (error !== "") {
        document.getElementById("error").innerText = error;
        return false;
    }

    alert("Form submitted successfully!");
    return true;
}
