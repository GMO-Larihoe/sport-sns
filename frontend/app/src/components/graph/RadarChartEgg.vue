<template>
  <!-- <div style="position:absolute;top:10; left:10; z-index: 100; "> -->
  <div style="position:relative;width:200px;height:200px;z-index: 9999; left:10%;">
    <canvas id="chartchart"></canvas>
  </div>
</template>





<script>

//記事末尾で補足
import Chart from 'chart.js/auto';

export default {
  methods: {
    renderChart() {
      let ctx = document.getElementById("chartchart");
      new Chart(ctx, {
        type: 'radar',
        data:{
          labels: ["た", "脂質", "黄色", "緑", "紫"],
          datasets: [{
            label: '得票数',
            data: [12, 19, 3, 5, 2],
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(153, 102, 255, 0.2)'
            ],
            borderColor: [
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
              'rgba(255, 159, 64, 1)',
            ],
            borderWidth: 2
          }]
        },
        options: {
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
