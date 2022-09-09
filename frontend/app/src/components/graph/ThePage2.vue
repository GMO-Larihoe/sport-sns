<template>
    <div class="flame">
        <div class="today">
            <!-- <div id="title">
            レーダーチャート
            </div> -->
            <div id="radargurahu">
                <RadarChartEgg ></RadarChartEgg>
            </div>
        </div>
        <div class="score">
            <div id="scoretitle">
                スコア
            </div>
            <div id="scorecount">
                {{(score)}}
            </div>
        </div>
        <div class="eiyou">
            <!-- <div class="eiyoutitle">
                食品の栄養素
            </div> -->
            <div class="eiyoulist">
                <div v-for="(item,index) in items" v-bind:key="index">
                    〇{{(item.name)}}⇒{{(item.score)}}
                </div>
            </div>
        </div>
        <div class="kabusoku">
            <div class="kabusokutitle">
                過剰・不足な栄養素
            </div>
            <div class="kabusokulist">
                <div v-for="(kabusokuegg,index) in kabusokun" v-bind:key="index">
                    {{(kabusokuegg.name)}}⇒{{(kabusokuegg.eiyou)}}
                </div>
            </div>
        </div>
        <div class="osusume">
            <div class="osusumetitle">
                おすすめの食品
            </div>
            <div class="footer">
                <TweetEgg></TweetEgg> 
            <!-- ここ多分コンポーネントを三回分forで回す -->
            </div>
        </div>
        <div class="linegraph">
            <div class="linegraphtitle">
                1週間のグラフ
            </div>
            <div>
                <ChartEgg></ChartEgg>
            </div>
        </div>
        <!-- <div class="hikaku">
            <div class="hikakutitle">
                前週比
            </div>
            <div>
                スコア比較
            </div>
        </div> -->

    </div>
</template>

<script>
import RadarChartEgg from './RadarChartEgg.vue'
import ChartEgg from './ChartEgg.vue'
import TweetEgg from './TweetEgg.vue' //
import axios from 'axios';

var kajou = "未登録"
var husoku = "未登録"

var socores = [];

export default {
    data() {
        return {
            message: "Hello",
            items: [
                    { name: "炭水化物", score: "未登録" },
                    { name: "脂質", score: "未登録" },
                    { name: "タンパク質", score: "未登録" },
                    { name: "ミネラル", score: "未登録" },
                    { name: "ビタミン", score: "未登録" },
                ],
            
            kabusokun: [
                    {name:"過剰",eiyou:kajou},
                    {name:"不足",eiyou:husoku},
            ],
osusume: [""],
score: 0,
        };
    },
    mounted(){
        this.getscore();
this.getalleiyou();
        this.getalleiyou2();
    },
    components: {
        RadarChartEgg,
        ChartEgg,
        TweetEgg,
    },
    methods:{
        getalleiyou2: async function(){
            let url = process.env.VUE_APP_API_DEV + '/users/nutritions';
            const API_TOKEN = sessionStorage.getItem('access_token');
            const res = await axios.get(url, { headers: { Authorization: "Bearer " + API_TOKEN } });
            //console.log(res.data["carbohydrate"]);
            // x1 = res.data["carbohydrate"];
            // x2 = res.data["lipid"];
            // x3 = res.data["protein"];
            // x4 = res.data["mineral"];
            // x5 = res.data["vitamin"];
            this.items[0]["score"] = res.data["carbohydrate"];
            this.items[1]["score"] = res.data["lipid"];
            this.items[2]["score"] = res.data["protein"];
            this.items[3]["score"] = res.data["mineral"];
            this.items[4]["score"] = res.data["vitamin"];
            socores[0]= res.data["carbohydrate"];
            socores[1]= res.data["lipid"];
            socores[2]= res.data["protein"];
            socores[3]= res.data["mineral"];
            socores[4]= res.data["vitamin"];

      }
      ,   
        getscore: async function(){
            try {
                let url = process.env.VUE_APP_API_DEV + '/users/score';
                const API_TOKEN = sessionStorage.getItem('access_token');
                const res = await axios.get(url, { headers: { Authorization: "Bearer " + API_TOKEN } });
                //console.log(res.data["score"]);
                this.score = res.data["score"];
            } catch (error) {
                this.score = 0;
            }
            
        },
getalleiyou: async function () {
let url = process.env.VUE_APP_API_DEV + '/usersreco_menu';
const API_TOKEN = sessionStorage.getItem('access_token');
const res = await axios.get(url, { headers: { Authorization: "Bearer " + API_TOKEN } });
this.osusume = res.data;
// console.log(res.data[0].vitamin);

// ---------
var maxcount = -1;
var mincount = 9999;
var indexmax = -1;
var indexmin = -1;
    
    for(let i = 0; i<5; i++) {
if (socores[i] > maxcount) {
maxcount = socores[i];
indexmax = i;
}
if (socores[i] < mincount) {
    mincount = socores[i];
            indexmin = i;
    }
}


switch (indexmax) {
    case 0:
    this.kabusokun[0].eiyou="炭水化物"
    break;
  case 1:
  this.kabusokun[0].eiyou="脂質"
    break;
  case 2:
  this.kabusokun[0].eiyou="たんぱく質"
break;
case 3:
this.kabusokun[0].eiyou="ミネラル"
    break;
  case 4:
  this.kabusokun[0].eiyou="ビタミン"
    break;
  default:
    // console.log('その他の都市です');
}

switch (indexmin) {
    case 0:
    this.kabusokun[1].eiyou="炭水化物"
    break;
  case 1:
  this.kabusokun[1].eiyou="脂質"
    break;
  case 2:
  this.kabusokun[1].eiyou="たんぱく質"
break;
case 3:
this.kabusokun[1].eiyou="ミネラル"
    break;
  case 4:
  this.kabusokun[1].eiyou="ビタミン"
    break;
  default:
    // console.log('その他の都市です');
}

// ---------

        }


    }
}

</script>

<style scoped>
body{
        font-family:'Noto Sans JP',sans-serif;
        /* background-color:#f6f5f4; */
} 
.flame{
    position:absolute;
    width:85%;
    height:100%;
    background-color: #FFF186;  /* 今flameは縦が設定されてないので一次元(直線) */
    right:0%;
}
.today{
    position:absolute;
    /* background-color:#FFF186; */
    width:25%;
    height: 200px;
    left:0%;
}
.today #title{
    position:absolute;
    /* color:red; */
    left:30%;
}
#gurahu{
    position:absolute;
    /* background-color:#9283ff; */
    width:80%;
    height:80%;
    top:10%;
    left:10%;
}
.score{
    position:absolute;
    /* background-color:#3c00ff; */
    width:25%;
    height: 200px;
    left:25%;
}
.score #scoretitle{
    position:absolute;
    /* color:red; */
    left:38%;
    font-size:30px;
    /* text-decoration:underline;
    text-decoration-color:orange; */
}
.score #scorecount{
    position:absolute;
    left:30%;
    font-size:100px;
    top:15%;
    /* text-decoration:underline;
    text-decoration-color:orange; */
}
.eiyou{
    position:absolute;
    /* background-color:#fbff00; */
    width:25%;
    height: 200px;
    left:50%;
    font-size:20px;
}
.eiyou .eiyoulist{
    margin-top:7%;
    margin-left:10%
}
.eiyou .eiyoulist ul{
    margin-top:50%;/*リスト上の余白*/
    margin-bottom:50%;/*リスト下の余白*/
    
}
.kabusoku{
    position:absolute;
    /* background-color:#00ff51; */
    width:25%;
    height: 200px;
    left:75%;
}
.kabusoku .kabusokutitle{
    font-size:25px;
    /* text-decoration:underline;
    text-decoration-color:orange; */
}
.kabusoku .kabusokulist{
    margin-top:20px;
    margin-bottom:5px;
    margin-left:5px;
    font-size:30px;
}
.osusume{
    position:absolute;
    /* background-color: red; */
    border:4px solid;
    border-color:pink;
    width:100%;
    height:30vh;
    left:0%;
    top:200px;
    z-index: 100
}
.osusume .osusumetitle{
    text-align:  center;
    font-size:30px;
    text-decoration:underline;
    text-decoration-color:orange;
}
.linegraph{
    position:absolute;
    /* background-color: #FFF186; */
    width:100%;
    height:270px;
    left:0%;
    top:440px;
}
.linegraph .linegraphtitle{
    position:absolute;
    left:5%;
    top:10%;
    font-size:50px;
    text-decoration:underline;
    text-decoration-color:orange;
}

</style>