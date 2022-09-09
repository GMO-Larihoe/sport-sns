<template>
  <!-- <div style="position:absolute;top:10; left:10; z-index: 100; "> -->
  <div style="position:relative;width:200px;height:200px;z-index: 9999; left:10%;">
    <canvas id="chartchart"></canvas>
  </div>
</template>





<script>

//記事末尾で補足
import Chart from 'chart.js/auto';
import axios from 'axios';

export default {
data() {
return {
    x1: 0,
    x2: 0,
    x3: 0,
    x4: 0,
    x5: 0,
      
    }
    
  },
  methods: {
    getalleiyou: async function(){
            let url = process.env.VUE_APP_API_DEV + '/users/nutritions';
            const API_TOKEN = sessionStorage.getItem('access_token');
axios.get(url, { headers: { Authorization: "Bearer " + API_TOKEN } }).then(res => {
            this.x1 = res.data["carbohydrate"];
            this.x2 = res.data["lipid"];
            this.x3 = res.data["protein"];
            this.x4 = res.data["mineral"];
            this.x5 = res.data["vitamin"];
            this.renderChart()
            // console.log("magic2")
          });


            // this.items[0]["score"] = res.data["carbohydrate"];
            // this.items[1]["score"] = res.data["lipid"];
            // this.items[2]["score"] = res.data["protein"];
            // this.items[3]["score"] = res.data["mineral"];
            // this.items[4]["score"] = res.data["vitamin"];
            
      }
      ,  
    renderChart() {
      let ctx = document.getElementById("chartchart");
//       var carbohydrate = this.x1;
//       console.log("magic");
// console.log(this.x1);
      new Chart(ctx, {
        type: 'radar',
        data:{
          labels: ["た", "脂質", "黄色", "緑", "紫"],
          datasets: [{
            label: '得票数',
            // data: [12, 19, 3, 5, 2],
            data: [this.x1, this.x2, this.x3, this.x4, this.x5],
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
    this.getalleiyou();
},
created(){
  
}
};
</script>
