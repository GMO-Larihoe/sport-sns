<template>
    <div style="position:relative;width:500px;height:200px;left:50%;top:100%">
        <canvas id="chart"></canvas>
    </div>
</template>

<script>

//記事末尾で補足
import Chart from 'chart.js/auto';
import axios from 'axios';

const day = [];
const month = [];

var objDate = new Date()
for (let step = 0; step < 7; step++) {
  var subDay = objDate.setDate(objDate.getDate() - 1);
  var yesterday = new Date(subDay);
  month[step] = yesterday.getMonth() + 1
  day[step] = yesterday.getDate()
}
//console.log('/users/scores?start=2022-'+String(month[0])+'-'+String(day[0])+'&end2022-'+String(month[6])+'-'+String(day[6]));これじゃ逆
console.log('/users/scores?start=2022-'+String(month[6])+'-'+String(day[6])+'&end2022-'+String(month[0])+'-'+String(day[0]+1));
export default {
  data() {
return {
    x1: 0,
    x2: 0,
    x3: 0,
    x4: 0,
    x5: 0,
    x6: 0,
    x7: 0,
    }
  },
methods: {
  getalleiyou: async function(){
let url = process.env.VUE_APP_API_DEV + '/users/scores?start=2022-'+String(month[6])+'-'+String(day[6]+1)+'&end=2022-'+String(month[0])+'-'+String(day[0]+1);
// /users/scores?start=2022-9-7&end2022-9-1
//'/users/scores?start=2022-9-2&end=2022-9-8';動いた
            const API_TOKEN = sessionStorage.getItem('access_token');
axios.get(url, { headers: { Authorization: "Bearer " + API_TOKEN } }).then(res => {

var rail = [];

console.log(res.data.length);
for (let p = 0; p < res.data.length; p++) {
let found = res.data[p]["date"].match(/\d+/g).map(Number);
let total = found.reduce(function (sum, element) { return sum + element; }, 0);
console.log(total);//2039
for (let j = 0; j < 7; j++) {
if (total == 2022 + month[j] + day[j] + 1) {
rail[j] = res.data[0]["score"];
switch (j) {
case 0:
this.x1 = rail[j]
break;
case 1:
this.x2 = rail[j]
break;
case 2:
this.x3 = rail[j]
break;
case 3:
this.x4 = rail[j]
break;
case 4:
this.x5 = rail[j]
break;
case 5:
this.x6 = rail[j]
break;
case 6:
this.x7 = rail[j]
break;
}
console.log("成功")
}
}
}

// this.x1 = res.data[0]["score"];
// this.x2 = res.data[0]["score"];
// this.x3 = res.data[0]["score"];
// this.x4 = res.data[0]["score"];
// this.x5 = res.data[0]["score"];
// this.x6 = res.data[0]["score"];
// this.x7 = res.data[0]["score"];
this.renderChart();
// console.log("magic")
});
      }
      ,       
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
            data: [this.x7, this.x6, this.x5, this.x4, this.x3, this.x2,this.x1],
            // data:[7,6,4,8,1,9,2],
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
    this.getalleiyou();
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