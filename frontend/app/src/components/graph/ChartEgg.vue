<template>
    <div style="position:relative;width:500px;height:200px;left:20%;margin-top:4%;">
        <canvas id="chart"></canvas>
    </div>
</template>

<script>

//記事末尾で補足
import Chart from 'chart.js/auto';

const day = [];
const month = [];

var objDate = new Date()
for (let step = 0; step < 7; step++) {
  var subDay = objDate.setDate(objDate.getDate() - 1);
  var yesterday = new Date(subDay);
  month[step] = yesterday.getMonth() + 1
  day[step] = yesterday.getDate()
}

export default {
  methods: {
    renderChart() {
      let ctx = document.getElementById("chart");
      new Chart(ctx, {
        type: 'line',
        data:{
            labels: [
            month[6] + "/" + day[6],
            month[5] + "/" + day[5],
            month[4] + "/" + day[4],
            month[3] + "/" + day[3],
            month[2] + "/" + day[2],
            month[1] + "/" + day[1],
            month[0] + "/" + day[0]
            ],
          datasets: [{
            label: '得票数',
            data: [7, 8, 3, 5, 2, 3, 4],
            backgroundColor: [
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
            ],
            borderColor: [
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
            ],
            borderWidth: 4
          }]
        },
        options: {
          plugins: {
    legend: {
      display: false,
    },
  },
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero:true
              }
            }]
          }
        }
      });
    }
  },
  mounted() {
    this.renderChart();
  }
};
</script>

<!-- <style scoped>
.radar {
 height:200px
}
.chart {
 width: auto; 
 max-height: 100%; 
}
</style> -->