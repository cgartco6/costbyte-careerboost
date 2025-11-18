// Dashboard JS
function updateDashboard(data){
    document.getElementById('totalUsers').innerText = data.users || 0;
    document.getElementById('totalRevenue').innerText = `R${data.revenue || 0}`;
    document.getElementById('paidApplicants').innerText = data.payments || 0;
    document.getElementById('aiStatus').innerText = data.ai_status || "Operational";
}
