async function registerUser() {
    const email = document.getElementById("regEmail").value;
    const password = document.getElementById("regPassword").value;

    const res = await fetch('/auth/register', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({email, password})
    });

    const data = await res.json();
    alert(data.message || data.error);
}

async function loginUser() {
    const email = document.getElementById("logEmail").value;
    const password = document.getElementById("logPassword").value;

    const res = await fetch('/auth/login', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({username: email, password})
    });

    const data = await res.json();
    if (data.access_token) {
        localStorage.setItem("token", data.access_token);
        window.location.href = "/dashboard.html";
    } else {
        alert("Invalid login");
    }
}
