<template>
    <div class="flame">
        <div class="today">
            <div id="title">
            レーダーチャート
            </div>
            <div id="radargurahu">
                <RadarChartEgg></RadarChartEgg>
            </div>
        </div>
        <div class="score">
            <div id="scoretitle">
                スコア
            </div>
            <div id="scorecount">
                <!-- ここにスコアを入れる -->
            </div>
        </div>
        <div class="eiyou">
            <div class="eiyoutitle">
                食品の栄養素
            </div>
            <!-- <div>
                {{ message }}
            </div> -->
            <div class="eiyoulist">
                <!-- <ul v-for="(item, key) in items" :key="key">
                    <li>{{item.name}},{{item.score}}</li>
                </ul> -->
                <div v-for="(item,index) in items" v-bind:key="index">
                    {{(item.name)}},{{(item.score)}}
                </div>

            </div>
        </div>
        <div class="kabusoku">
            <!-- <ul v-for="(kabusokuegg, key) in kabusokun" :key="key">
                    <li>{{kabusokuegg.name}},{{kabusokuegg.eiyou}}</li>
                </ul> -->
                <div v-for="(kabusokuegg,index) in kabusokun" v-bind:key="index">
                    {{(kabusokuegg.name)}},{{(kabusokuegg.eiyou)}}
                </div>
        </div>
        <div class="osusume">
            <div class="osusumetitle">
                おすすめの食品
            </div>
            <div class="footer">
                <TweetEgg></TweetEgg> //
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
        <div class="hikaku">
            <div class="hikakutitle">
                前週比
            </div>
            <div>
                スコア比較
            </div>
        </div>

    </div>
</template>

<script>
import RadarChartEgg from './RadarChartEgg.vue'
import ChartEgg from './ChartEgg.vue'
import TweetEgg from './TweetEgg.vue' //


export default {
    data() {
        return {
            message: "Hello",
            items: [
                    { name: "タンパク質", score: 81 },
                    { name: "脂質", score: 78 },
                    { name: "野菜", score: 64 },
                    { name: "ニンニク", score: 92 },
                    { name: "マシマシ", score: 73 },
                ],
            
            kabusokun: [
                    {name:"過剰",eiyou:"たんぱく"},
                    {name:"不足",eiyou:"脂質"},
            ]
        };
    },
    components: {
        RadarChartEgg,
        ChartEgg,
        TweetEgg //
},
}

</script>

<style scoped>
body{
        font-family:'Noto Sans JP',sans-serif;
        background-color:#f6f5f4;
} 
.flame{
    position:absolute;
    width:85%;
    background-color: red;  /* 今flameは縦が設定されてないので一次元(直線) */
    right:0%;
}
.today{
    position:absolute;
    background-color:#FFF186;
    width:25%;
    height: 200px;
    left:0%;
}
.today #title{
    position:absolute;
    color:red;
    left:20%;
}
#gurahu{
    position:absolute;
    background-color:#9283ff;
    width:80%;
    height:80%;
    top:10%;
    left:10%;
}
.score{
    position:absolute;
    background-color:#3c00ff;
    width:25%;
    height: 200px;
    left:25%;
}
.eiyou{
    position:absolute;
    background-color:#fbff00;
    width:25%;
    height: 200px;
    left:50%;
}
.eiyou .eiyoulist ul{
    margin-top:0%;/*リスト上の余白*/
    margin-bottom:0%;/*リスト下の余白*/
}
.kabusoku{
    position:absolute;
    background-color:#00ff51;
    width:25%;
    height: 200px;
    left:75%;
}
.osusume{
    position:absolute;
    background-color: red;
    width:100%;
    height:25vh;
    left:0%;
    top:200px;
    z-index: 100;
}
.linegraph{
    position:absolute;
    background-color: #FFF186;
    width:75%;
    height:270px;
    left:0%;
    top:410px;
}
.hikaku{
    position:absolute;
    background-color: purple;
    width:25%;
    height:270px;
    left:75%;
    top:410px;
}
</style>