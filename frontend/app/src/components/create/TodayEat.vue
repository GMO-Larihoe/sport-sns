<template>
	<div>
    <div v-for="n in 3" v-bind:key="n">
    <div class="todayeat">
	<div class="picture">
		{{picture}}
	</div>
	<div id="eat">
    <div id="E11">ジャンル</div>
    <div id="E12">食べ物</div>
	<div id="E21">：</div>
	<div id="E22">：</div>
	<div id="E31">{{genre}}</div>
	<div id="E32">{{food}}</div>
	</div>
	<div id="godai">
		<div id="G11">〇炭水化物</div>
		<div id="G12">〇脂質</div>
		<div id="G13">〇タンパク質</div>
		<div id="G14">〇ミネラル</div>
		<div id="G15">〇ビタミン</div>
		<div id="G21">{{tans}}</div>
		<div id="G22">{{si}}</div>
		<div id="G23">{{tanp}}</div>
		<div id="G24">{{mine}}</div>
		<div id="G25">{{bita}}</div>
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
				picture:'写真だよ',
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
			this.getData();
		},
		methods:{
			getData: async function(){
				console.log(1);
				const response = await axios.get(process.env.VUE_APP_API_DEV + "/authers");
				console.log(response.data[0]);
				//const response = await axios.post(process.env.VUE_APP_API_DEV + "/authers",JSONが入っている変数);
				//parms
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
#eat{
    display:grid;
    grid-template-rows:50px 50px;
    grid-template-columns:80px 20px 100px;
	position:absolute;
    font-size:120%;
	padding-top:8vh;
	margin-left:22vw;
}
#E11 {
    grid-row: 1 / 2;
    grid-column: 1 / 2;
    background: #f88;
}
#E12 {
    grid-row: 2 / 3;
    grid-column: 1 / 2;
    background: #88f;
}
#E21 {
    grid-row: 1 / 2;
    grid-column: 2 / 3;
    background: #f88;
}
#E22 {
    grid-row: 2 / 3;
    grid-column: 2 / 3;
    background: #88f;
}
#E31 {
    grid-row: 1 / 2;
    grid-column: 3 / 4;
    background: #f88;
}
#E32 {
    grid-row: 2 / 3;
    grid-column: 3 / 4;
    background: #88f;
}
#godai{
    display:grid;
    grid-template-rows:30px 30px 30px 30px 30px;
    grid-template-columns:100px 100px;
	position:absolute;
    font-size:120%;
	margin-top:4vh;
	margin-left:40vw;
}
#G11 {
    grid-row: 1 / 2;
    grid-column: 1 / 2;
    background: #f88;
}
#G12 {
    grid-row: 2 / 3;
    grid-column: 1 / 2;
    background: #8f8;
}
#G13 {
    grid-row: 3 / 4;
    grid-column: 1 / 2;
    background: #88f;
}
#G14 {
    grid-row: 4 / 5;
    grid-column: 1 / 2;
    background: #8f8;
}
#G15 {
    grid-row: 5 / 6;
    grid-column: 1 / 2;
    background: #f88;
}
#G21 {
	text-align: center;
    grid-row: 1 / 2;
    grid-column: 2 / 3;
    background: #f88;
}
#G22 {
	text-align: center;
    grid-row: 2 / 3;
    grid-column: 2 / 3;
    background: #8f8;
}
#G23 {
	text-align: center;
    grid-row: 3 / 4;
    grid-column: 2 / 3;
    background: #88f;
}
#G24 {
	text-align: center;
    grid-row: 4 / 5;
    grid-column: 2 / 3;
    background: #8f8;
}
#G25 {
	text-align: center;
    grid-row: 5 / 6;
    grid-column: 2 / 3;
    background: #f88;
}

.todayeat{
    margin-top:2vh;
    margin-left:7vw;
    background-color:chartreuse;
    width:60vw;
    height:30vh;
}
.picture{
    position:absolute;
	margin-top:5vh;
	margin-left:7vw;
    width:10vw;
    height:20vh;
    padding-top:55px;
	padding-left:45px;
    background-color:red;
}
</style>