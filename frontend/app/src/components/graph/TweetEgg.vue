<template>
	<div>
		<div class="wrapper">
    <div v-for="(n,index) in osusume" v-bind:key="index">
    <div class="todayeat">
	<p v-if="n.carbohydrate==null">未登録</p>
	<p v-else>
			<img v-bind:src="pictures[index]" class="picture">
	</p>
    <!-- <div class="genre">
		ジャンル：{{genre}}
	</div> -->
    <div class="food">
		{{n.name}}
	</div>
    <!-- <div class="godai">
		<p v-if="n.carbohydrate==null">未登録</p>
		<p v-else>
			〇炭水化物⇒{{n.carbohydrate}}<br>
			〇脂質⇒{{n.lipid}}<br>
			〇タンパク質⇒{{n.protein}}<br>
			〇ミネラル⇒{{n.mineral}}<br>
			〇ビタミン⇒{{n.vitamin}}
		</p>
	</div> -->
	<p v-if="n.carbohydrate==null">未登録</p>
	<p v-else>
	<div id="godai">
			<div id="G11">〇炭水化物</div>
			<div id="G12">〇脂質</div>
			<div id="G13">〇タンパク質</div>
			<div id="G14">〇ミネラル</div>
			<div id="G15">〇ビタミン</div>
			<div id="G21">{{n.carbohydrate}}</div>
			<div id="G22">{{n.lipid}}</div>
			<div id="G23">{{n.protein}}</div>
			<div id="G24">{{n.mineral}}</div>
			<div id="G25">{{n.vitamin}}</div>
		</div>
		</p>

    </div>
    </div>
    </div>
	</div>
</template>
<script>
	import axios from 'axios';
	export default{
		
		name:'TodayEat',
		data(){
			return {
				osusume:[""],
				foods: "食べ物の名前",
				pictures: [],
                genre:'和食',
                food:'煮魚',
                tans:50,
                si:50,
                tanp:50,
                mine:50,
                bita:50,
			} 

		},
		mounted(){
			this.getalleiyou();
		},
methods: {
getalleiyou: async function () {
let url = process.env.VUE_APP_API_DEV + '/usersreco_menu';
const API_TOKEN = sessionStorage.getItem('access_token');
const res = await axios.get(url, { headers: { Authorization: "Bearer " + API_TOKEN } });
this.osusume = res.data;
for (let i = 0; i < 3; i++){
console.log(this.osusume[0].img);
this.pictures[i] = "data:image/png;base64,"+this.osusume[i].img;
}
// }
// console.log(res.data[0].name);
},
			// output: function(e){
			// 	// console.log(e.target.value);
			// 	switch(this.Gselected){
			// 		case "和食":
			// 			this.foods=[
			// 			{ id: 1, name: '煮魚' },
			// 			{ id: 2, name: 'おしるこ' },
			// 			{ id: 3, name: 'おにぎり' }
			// 			];
			// 		return;
			// 		case "洋食":
			// 			this.foods=[
			// 			{ id: 1, name: 'ハンバーグ' },
			// 			{ id: 2, name: 'ステーキ' },
			// 			{ id: 3, name: 'パスタ' }
			// 			]
			// 		return;
			// 		case "中華":
			// 			this.foods=[
			// 			{ id: 1, name: 'エビチリ' },
			// 			{ id: 2, name: '麻婆豆腐' },
			// 			{ id: 3, name: '杏仁豆腐' }
			// 			]
			// 		return;
			// 	}
			// }

		}
	}
</script>
<style scoped>
.todayeat{
    margin-top:0vh;
    margin-left:2vw;
    /* background-color:chartreuse; */
    width:25vw;
    height:25vh;
}
.picture{
    position:absolute;
	margin-top:5vh;
	margin-left:0vw;
    width:120px;
    height:120px;
    text-align: center;
    /* background-color:red; */
}
.genre{
    position:absolute;
    font-size:120%;
	padding-top:5vh;
	margin-left:20vw;
}
.food{
    position:absolute;
    font-size:120%;
	margin-top:0vh;
	margin-left:2vw;
}
/* .godai{
    position:absolute;
    font-size:120%;
	margin-top:2vh;
	margin-left:12vw;
} */
#godai{
    display:grid;
    grid-template-rows:10px 30px 30px 30px 30px 30px 10px;
    grid-template-columns:10px 100px 100px 10px;
	background: #f4f4f4;
    border-left: solid 6px #ffb700;
    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.33);
}
#G11 {
    grid-row: 2 / 3;
    grid-column: 2 / 3;
}
#G12 {
    grid-row: 3 / 4;
    grid-column: 2 / 3;
}
#G13 {
    grid-row: 4 / 5;
    grid-column: 2 / 3;
}
#G14 {
    grid-row: 5 / 6;
    grid-column: 2 / 3;
}
#G15 {
    grid-row: 6 / 7;
    grid-column: 2 / 3;
}
#G21 {
	text-align: center;
    grid-row: 2 / 3;
    grid-column: 3 / 4;
	border-bottom: 1px solid #000;
}
#G22 {
	text-align: center;
    grid-row: 3 / 4;
    grid-column: 3 / 4;
	border-bottom: 1px solid #000;
}
#G23 {
	text-align: center;
    grid-row: 4 / 5;
    grid-column: 3 / 4;
	border-bottom: 1px solid #000;
}
#G24 {
	text-align: center;
    grid-row: 5 / 6;
    grid-column: 3 / 4;
	border-bottom: 1px solid #000;
}
#G25 {
	text-align: center;
    grid-row: 6 / 7;
    grid-column: 3 / 4;
	border-bottom: 1px solid #000;
}
.wrapper{
    display: -webkit-flex;
    display: -moz-flex;
    display: -ms-flex;
    display: -o-flex;
    display: flex;
}
</style>