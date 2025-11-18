// Autoposter JS placeholder
function showAppliedJobs(jobs){
    const container = document.getElementById('appliedJobs');
    container.innerHTML = "";
    jobs.forEach(job=>{
        const div = document.createElement('div');
        div.className = 'card';
        div.innerText = `Applied: ${job.job_title} at ${job.submitted_to}`;
        container.appendChild(div);
    });
}
