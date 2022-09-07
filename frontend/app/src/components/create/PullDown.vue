<template>
	<div>
	<div id="eat">
	<div id="E11">ジャンル</div>
	<div id="E12">食べ物</div>
	<div id="E21">
	<div class="cp_ipselect cp_sl05">
        <select v-model="Gselected" name="genre" v-on:change="output">
            <option value="" hidden>選択して下さい</option>
            <option v-for="genre in genres" v-bind:value="genre.name" v-bind:key="genre.id">
                {{ genre.name }}
            </option>
        </select>
    </div>
	</div>
	<div id="E22">
	<div class="cp_ipselect cp_sl05">
        <select v-model="Fselected" name="food">
            <option value="" hidden>選択して下さい</option>
            <option v-for="food in foods" v-bind:value="food.name" v-bind:key="food.id">
            {{ food.name }}
            </option>
        </select>
    </div>
	</div>
	</div>
	<div class="picture">
		{{picture}}
	</div>
	<div id="godai">
		<div id="G11">〇炭水化物</div>
		<div id="G12">〇脂質</div>
		<div id="G13">〇タンパク質</div>
		<div id="G14">〇ミネラル</div>
		<div id="G15">〇ビタミン</div>
		<div id="G21"><input type="number" id="tansui" size="10" min="0" max="2000"></div>
		<div id="G22"><input type="number" id="sisitu" size="10" min="0" max="2000"></div>
		<div id="G23"><input type="number" id="tanpaku" size="10" min="0" max="2000"></div>
		<div id="G24"><input type="number" id="mineraru" size="10" min="0" max="2000"></div>
		<div id="G25"><input type="number" id="bitamin" size="10" min="0" max="2000"></div>
	</div>
		<a class="btn btn--yellow btn--cubic">追加</a>
		<a class="btn btn--yellow2 btn--cubic">投稿</a>
</div>
</template>
<script>
	import axios from 'axios';
	export default{
		
		name:'PullDown',
		data(){
			return {
				Gselected: '',
				genres: [
						{ id: 1, name: '和食' },
						{ id: 2, name: '洋食' },
						{ id: 3, name: '中華' }
				],
				Fselected: '',
				foods: [
						{ id: 1, name: '煮魚' },
						{ id: 2, name: 'おしるこ' },
						{ id: 3, name: 'おにぎり' }
				],
				picture:'写真だよ',
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
				//const response = await axios.post(process.env.VUE_APP_API_DEV + "/users/genres",JSONが入っている変数);
				//parms
			},
			postData: async function(){
				const response = await axios.post(process.env.VUE_APP_API_DEV + "/users/genres",this.genres[0].name);
				console.log(response);
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
.picture{
    position:absolute;
	margin-top:5vh;
	margin-left:30vw;
    width:10vw;
    height:20vh;
    padding-top:55px;
	padding-left:45px;
    background-color:red;
}
#eat{
    display:grid;
    grid-template-rows:60px 60px ;
    grid-template-columns:80px 200px;
	position:absolute;
	font-size:120%;
    width:20vw;
	margin-left:5vw;
	margin-top:6vh;
}
#E11 {
    grid-row: 1 / 2;
    grid-column: 1 / 2;
    background: #f88;
	padding-top:20%;
}
#E12 {
    grid-row: 2 / 3;
    grid-column: 1 / 2;
    background: #8f8;
	padding-top:20%;
}
#E21 {
    grid-row: 1 / 2;
    grid-column: 2 / 3;
    background: #f88;
}
#E22 {
    grid-row: 2 / 3;
    grid-column: 2 / 3;
    background: #8f8;
}

#godai{
    display:grid;
    grid-template-rows:30px 30px 30px 30px 30px;
    grid-template-columns:100px 100px;
	position:absolute;
    width:20vw;
	margin-left:45vw;
	margin-top:4vh;
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
*,
*:before,
*:after {
  -webkit-box-sizing: inherit;
  box-sizing: inherit;
}

.btn,
a.btn,
button.btn {
  font-size: 1rem;
  font-weight: 700;
  line-height: 0.5;
  position: relative;
  display: inline-block;
  padding: 1rem 4rem;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  text-align: center;
  vertical-align: middle;
  text-decoration: none;
  letter-spacing: 0.1em;
  color: #212529;
  border-radius: 0.5rem;
}

a.btn--yellow {
  position: absolute;
  left:63vw;
  top:5vh;
  color: #000;
  background-color: #fff100;
  border-bottom: 5px solid #ccc100;
}
a.btn--yellow2 {
  position: absolute;
  left:63vw;
  top:18vh;
  color: #000;
  background-color: #fff100;
  border-bottom: 5px solid #ccc100;
}
a.btn--yellow2:hover {
  margin-top: 3px;
  color: #000;
  background: #fff20a;
  border-bottom: 2px solid #ccc100;
}
a.btn--yellow:hover {
  margin-top: 3px;
  color: #000;
  background: #fff20a;
  border-bottom: 2px solid #ccc100;
}

.cp_ipselect {
	overflow: hidden;
	width: 80%;
	left:10%;
	top:20%;
}
.cp_ipselect select {
	width: 100%;
	padding-right: 1em;
	cursor: pointer;
	text-indent: 0.01px;
	text-overflow: ellipsis;
	border: none;
	outline: none;
	background: transparent;
	background-image: none;
	box-shadow: none;
	-webkit-appearance: none;
	appearance: none;
}
.cp_ipselect select::-ms-expand {
    display: none;
}
.cp_ipselect.cp_sl05 {
	position: relative;
	border-radius: 2px;
  border-radius: 50px;
	background: #da3c41;
}
.cp_ipselect.cp_sl05::before {
	position: absolute;
	top: 0.8em;
	right: 0.8em;
	width: 0;
	height: 0;
	padding: 0;
	content: '';
	border-left: 6px solid transparent;
	border-right: 6px solid transparent;
	border-top: 6px solid #ffffff;
	pointer-events: none;
}
.cp_ipselect.cp_sl05 select {
	padding: 8px 38px 8px 8px;
	color: #ddff00;
	background-color:#da3c41;
}
</style>