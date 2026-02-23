function validateForm() {
    var fname = document.forms["regForm"]["fname"].value;
    var lname = document.forms["regForm"]["lname"].value;
    var password = document.forms["regForm"]["password"].value;
    var email = document.forms["regForm"]["email"].value;
    var mobile = document.forms["regForm"]["mobile"].value;
    var address = document.forms["regForm"]["address"].value;
    var msg = "";
    if (!/^[A-Za-z]{6,}$/.test(fname)) msg += "First name must be at least 6 letters.\n";
    if (lname.trim() === "") msg += "Last name cannot be empty.\n";
    if (password.length < 6) msg += "Password must be at least 6 characters.\n";
    if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)) msg += "Invalid email.\n";
    if (!/^\d{10}$/.test(mobile)) msg += "Mobile must be 10 digits.\n";
    if (address.trim() === "") msg += "Address cannot be empty.\n";
    if (msg) {
        document.getElementById("regMsg").innerText = msg;
        return false;
    }
    return true;
}
