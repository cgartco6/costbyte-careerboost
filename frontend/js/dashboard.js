async function loadDashboard() {
    let res = await fetch("/dashboard/data");
    let data = await res.json();

    document.getElementById("total-users").textContent = data.users;
    document.getElementById("total-revenue").textContent = "R" + data.revenue;
    document.getElementById("jobs-found").textContent = data.jobs;

    new Chart(document.getElementById("revChart"), {
        type: "line",
        data: {
            labels: data.rev_labels,
            datasets: [{
                label: "Revenue",
                data: data.rev_data
            }]
        }
    });

    new Chart(document.getElementById("userChart"), {
        type: "bar",
        data: {
            labels: data.user_labels,
            datasets: [{
                label: "Registrations",
                data: data.user_data
            }]
        }
    });
}

loadDashboard();
