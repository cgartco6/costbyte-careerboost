async function checkAIStatus() {
    let res = await fetch("/api/ai/status");
    let data = await res.json();
    document.getElementById("ai-state").textContent = data.state;
    document.getElementById("ai-tasks").textContent = data.active_tasks;
}
setInterval(checkAIStatus, 5000);
