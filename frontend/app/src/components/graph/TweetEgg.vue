<template>
	<div>
		<div class="wrapper">
    <div v-for="n in 3" v-bind:key="n">
    <div class="todayeat">
	<div class="picture">
		{{picture}}
	</div>
    <!-- <div class="genre">
		ジャンル：{{genre}}
	</div>
    <div class="food">
		食べ物:{{food}}
	</div> -->
    <div class="godai">
		〇炭水化物⇒⇒{{tans}}<br>
        〇脂質⇒⇒⇒⇒{{si}}<br>
        〇タンパク質⇒{{tanp}}<br>
        〇ミネラル⇒⇒{{mine}}<br>
        〇ビタミン⇒⇒{{bita}}
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
.todayeat{
    margin-top:0vh;
    margin-left:2vw;
    background-color:chartreuse;
    width:25vw;
    height:25vh;
}
.picture{
    position:absolute;
	margin-top:2vh;
	margin-left:1vw;
    width:10vw;
    height:20vh;
    text-align: center;
    background-color:red;
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