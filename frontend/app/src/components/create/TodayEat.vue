<template>
	<div>
	<!-- <Child v-bind="child"></Child> -->
	<p id="ttext">今日の食事</p>
	<div class="today">
    <div v-for="(today,index) in todays" v-bind:key="index">
    <div class="todayeat">
	<img v-bind:src="pictures[index]" class="picture">
	<div id="eat">
    <div id="E11">ジャンル</div>
    <div id="E12">食べ物</div>
	<div id="E21">：</div>
	<div id="E22">：</div>
	<div id="E31">{{today.genre_name}}</div>
	<div id="E32">{{today.name}}</div>
	</div>
	<div id="godai">
		<div id="G11">〇炭水化物</div>
		<div id="G12">〇脂質</div>
		<div id="G13">〇タンパク質</div>
		<div id="G14">〇ミネラル</div>
		<div id="G15">〇ビタミン</div>
		<div id="G21">{{today.carbohydrate}}</div>
		<div id="G22">{{today.lipid}}</div>
		<div id="G23">{{today.protein}}</div>
		<div id="G24">{{today.mineral}}</div>
		<div id="G25">{{today.vitamin}}</div>
	</div>
    </div>
    </div>
</div>
    </div>
</template>
<script>
	import axios from 'axios';
	export default{
		
		name:'TodayEat',
		// props:["child"],
		data(){
			return {
				genres: [
						{ id: 1, name: '和食' },
						{ id: 2, name: '洋食' },
						{ id: 3, name: '中華' }
				],
				foods: [
						{ id: 1, name: '煮魚' },
						{ id: 2, name: 'おしるこ' },
						{ id: 3, name: 'おにぎり' }
				],
				pictures:[],
				todays:[],
			} 

		},
		mounted(){
			this.getData();
		},
		methods:{
			getData: async function(){
				let url = process.env.VUE_APP_API_DEV + "/users/genres";
				const API_TOKEN = sessionStorage.getItem('access_token');
				let response = await axios.get(url, { headers: { Authorization: "Bearer " + API_TOKEN } });
				console.log(response.data[0].name);
				this.genres=response.data;

				url = process.env.VUE_APP_API_DEV + "/users/food_post";
				response = await axios.get(url, { headers: { Authorization: "Bearer " + API_TOKEN } });
				console.log(response.data[0].name);
				this.todays=response.data;

				for(let i=0;i<this.todays.length;i++){
					console.log(this.todays[0].img)
					this.pictures[i]="data:image/png;base64,"+this.todays[i].img;
				}

				//this.todays[this.todays.length]=this.child;
			},
			output: function(e){
				console.log(e.target.value);
				switch(this.Gselected){
					case "和食":
						this.foods=[
						{ id: 1, name: '煮魚' },
						{ id: 2, name: 'おしるこ' },
						{ id: 3, name: 'おにぎり' }
						];
					return;
					case "洋食":
						this.foods=[
						{ id: 1, name: 'ハンバーグ' },
						{ id: 2, name: 'ステーキ' },
						{ id: 3, name: 'パスタ' }
						]
					return;
					case "中華":
						this.foods=[
						{ id: 1, name: 'エビチリ' },
						{ id: 2, name: '麻婆豆腐' },
						{ id: 3, name: '杏仁豆腐' }
						]
					return;
				}
			}

		}
	}
</script>
<style scoped>
.today{
  position:absolute;
  background-color:coral;
  overflow: auto;
  width:78vw;
  height:50vh;
  margin-top:45vh;
  margin-left:20vw;
  background: #fff0cd;
    box-shadow: 0px 0px 0px 5px #fff0cd;
    border: dashed 2px white;
    color: #454545;
} 
#ttext{
  position:absolute;
  font-size:120%;
  width:auto;
  height:auto;
  color: #ffffff;/*文字色*/
  padding: 0.5em;/*文字周りの余白*/
  display: inline-block;/*おまじない*/
  line-height: 1.3;/*行高*/
  background: #ffd350;/*背景色*/
  vertical-align: middle;
  border-radius: 25px 0px 0px 25px;/*左側の角を丸く*/
  margin-left:21vw;
  margin-top:49vh;
  z-index: 100;
}
#eat{
    display:grid;
    grid-template-rows:50px 50px;
    grid-template-columns:80px 20px 150px;
	position:absolute;
    font-size:120%;
	margin-top:60px;
	margin-left:20vw;
	background: #f4f4f4;
    border-left: solid 6px #ffb700;
    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.33);
	padding-top:20px;
}
#E11 {
    grid-row: 1 / 2;
    grid-column: 1 / 2;
	text-align: center;
}
#E12 {
    grid-row: 2 / 3;
    grid-column: 1 / 2;
	text-align:center;
}
#E21 {
    grid-row: 1 / 2;
    grid-column: 2 / 3;
}
#E22 {
    grid-row: 2 / 3;
    grid-column: 2 / 3;
}
#godai{
    display:grid;
    grid-template-rows:10px 30px 30px 30px 30px 30px 10px;
    grid-template-columns:10px 100px 100px 10px;
	position:absolute;
	background: #f4f4f4;
    border-left: solid 6px #ffb700;
    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.33);
	margin-top:4vh;
	margin-left:40vw;
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

.todayeat{
    margin-top:2vh;
    margin-left:10vw;
    background: #f4f4f4;
    border-left: solid 6px #ffb700;
    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.33);
    width:60vw;
    height:30vh;
}
.picture{
    position:absolute;
	width:10vw;
    height:20vh;
    margin-top:5vh;
	margin-left:5vw;
    width:10vw;
    height:20vh;
}
</style>