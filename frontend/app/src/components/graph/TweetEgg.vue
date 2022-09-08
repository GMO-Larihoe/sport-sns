<template>
	<div>
		<div class="wrapper">
    <div v-for="(n,index) in osusume" v-bind:key="index">
    <div class="todayeat">

			<img v-bind:src="pictures[index]" class="picture">
    <!-- <div class="genre">
		ジャンル：{{genre}}
	</div> -->
    <div class="food">
		食べ物:{{n.name}}
	</div>
    <div class="godai">
		〇炭水化物⇒⇒{{n.carbohydrate}}<br>
        〇脂質⇒⇒⇒⇒{{n.lipid}}<br>
        〇タンパク質⇒{{n.protein}}<br>
        〇ミネラル⇒⇒{{n.mineral}}<br>
        〇ビタミン⇒⇒{{n.vitamin}}
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
// if (this.picutures.length!=0) {
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
	margin-top:2vh;
	margin-left:1vw;
    width:100px;
    height:100px;
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
	margin-top:15vh;
	margin-left:20vw;
}
.godai{
    position:absolute;
    font-size:120%;
	margin-top:2vh;
	margin-left:12vw;
}
.wrapper{
    display: -webkit-flex;
    display: -moz-flex;
    display: -ms-flex;
    display: -o-flex;
    display: flex;
}
</style>