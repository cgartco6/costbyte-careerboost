// Charts using Chart.js placeholder
function renderRevenueChart(ctx, data){
    new Chart(ctx, {
        type:'line',
        data:{
            labels:data.labels,
            datasets:[{label:'Revenue', data:data.values, borderColor:'#0d6efd', fill:false}]
        },
        options:{responsive:true, maintainAspectRatio:false}
    });
}
