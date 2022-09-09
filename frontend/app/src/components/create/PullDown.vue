<template>
	<div>
	<div class="noweat">
	<div id="eat">
	<div id="E11">ジャンル</div>
	<div id="E12">食べ物</div>
	<div id="E21">
	<div class="cp_ipselect cp_sl05">
        <select v-model="Gselected" name="genre" v-on:change="Goutput">
            <option value="" hidden>選択して下さい</option>
            <option v-for="genre in genres" v-bind:value="genre.name" v-bind:key="genre.id">
                {{ genre.name }}
            </option>
        </select>
    </div>
	</div>
	<div id="E22">
	<div class="cp_ipselect cp_sl05">
        <select v-model="Fselected" name="food" v-on:change="Foutput">
            <option value="" hidden>選択して下さい</option>
            <option v-for="food in foods" v-bind:value="food.name" v-bind:key="food.id">
            {{ food.name }}
            </option>
        </select>
    </div>
	</div>
	</div>
	<img v-bind:src="imgSrc" id="selectimg">
	<div id="godai">
		<div id="G11">〇炭水化物</div>
		<div id="G12">〇脂質</div>
		<div id="G13">〇タンパク質</div>
		<div id="G14">〇ミネラル</div>
		<div id="G15">〇ビタミン</div>
		<div id="G21">{{godai.carbohydrate}}</div>
		<div id="G22">{{godai.lipid}}</div>
		<div id="G23">{{godai.protein}}</div>
		<div id="G24">{{godai.mineral}}</div>
		<div id="G25">{{godai.vitamin}}</div>
	</div>
		<a class="btn btn--yellow2 btn--cubic" v-on:click="insert">投稿</a>
	</div>
</div>
</template>
<script>
	import axios from 'axios';
	import swal from 'sweetalert';
	export default{
		
		name:'PullDown',
		data(){
			return {
				Gselected: '',
				text : "",
				allgenres:[],
				genres: [
						{ id: 1, name: '和食' },
						{ id: 2, name: '洋食' },
						{ id: 3, name: '中華' }
				],
				Fselected: '',
				foods: [
						{ id: 1, name: 'ジャンルを選択してください' },
				],
				// imgSrc:"",
				img:"",
				imgSrc:"./leftselect.png",
				godai:[],
			} 

		},
		mounted(){
			this.getData();
		},
		// computed:{
		// 	imgSrc(){
		// 		console.log(this.allgenres.data[this.Gselected][0].img);
		// 		return "data:image/png;base64,"+this.allgenres.data[this.Gselected][0].img;
		// 	},
		// },
		methods:{
			getData: async function(){
				console.log(1);
				let url = process.env.VUE_APP_API_DEV + "/users/genres";
				const API_TOKEN = sessionStorage.getItem('access_token');
				let response = await axios.get(url, { headers: { Authorization: "Bearer " + API_TOKEN } });
				console.log(response.data[0].name);
				this.genres=response.data;

				url = process.env.VUE_APP_API_DEV + "/users/genres_food";
				response = await axios.get(url, { headers: { Authorization: "Bearer " + API_TOKEN } });
				console.log(response.data['日本食'][0].name);
				this.allgenres=response;
				// this.imgSrc=require("./leftselect.png");
				if(this.Gselected=="" || this.Fselected!=""){
					this.imgSrc=require("./leftselect.png");
				}
			},
			insert: async function(){
				try{
				let url = process.env.VUE_APP_API_DEV + "/users/food_post";
				const API_TOKEN = sessionStorage.getItem('access_token');
				let x=0;
				for(let i=0;i<this.allgenres.data[this.Gselected].length;i++){
					if(this.allgenres.data[this.Gselected][i].name==this.Fselected){
						x=i;
					}
				}
				let genres = {
					"genre_id" : this.allgenres.data[this.Gselected][x].genre_id,
					"food_id" : this.allgenres.data[this.Gselected][x].id,
				}
				//this.$emit('parent', this.allgenres.data[this.Gselected][x]);
				console.log(this.allgenres.data);
				let response = await axios.post(url, genres, { headers: { Authorization: "Bearer " + API_TOKEN } });
				console.log(response.data);
				swal("登録完了！", "ジャンル:"+this.Gselected+"　食べ物:"+this.allgenres.data[this.Gselected][x].name, "success")
				.then( () =>  { 
					location.reload();
				} ) ;
				}catch(error){
					swal("登録失敗", "ジャンルと食べ物を選択して投稿してください", "error")
				}
			},
			Goutput: function(e){
				console.log(e.target.value);
				this.foods=this.allgenres.data[this.Gselected];
				console.log(this.foods);
				let nowfood;
				if(this.Gselected != ""){
					this.Fselected = this.foods[0].name;
					console.log("food selected"+this.Fselected);
				}

				for(let i=0;i<this.foods.length;i++){
					if(this.foods[i].name==this.Fselected){
						nowfood=i;
					}
				}

				if(this.Gselected!="" && this.Fselected!=""){
					this.imgSrc="data:image/png;base64,"+this.allgenres.data[this.Gselected][nowfood].img;
					this.godai={
						carbohydrate:this.allgenres.data[this.Gselected][nowfood].carbohydrate,
						lipid:this.allgenres.data[this.Gselected][nowfood].lipid,
						protein:this.allgenres.data[this.Gselected][nowfood].protein,
						mineral:this.allgenres.data[this.Gselected][nowfood].mineral,
						vitamin:this.allgenres.data[this.Gselected][nowfood].vitamin
					}
				}else{
					this.imgSrc=require("./leftselect.png");
				}
				console.log(this.allgenres.data[this.Gselected][nowfood].name);
				// this.Fselected=this.allgenres.data[this.Gselected][nowfood].name;
			},
			Foutput: function(e){
				console.log(e.target.value);
				this.foods=this.allgenres.data[this.Gselected];
				console.log(this.foods);
				let nowfood;

				for(let i=0;i<this.foods.length;i++){
					if(this.foods[i].name==this.Fselected){
						nowfood=i;
					}
				}

				if(this.Gselected!="" && this.Fselected!=""){
					this.imgSrc="data:image/png;base64,"+this.allgenres.data[this.Gselected][nowfood].img;
					this.godai={
						carbohydrate:this.allgenres.data[this.Gselected][nowfood].carbohydrate,
						lipid:this.allgenres.data[this.Gselected][nowfood].lipid,
						protein:this.allgenres.data[this.Gselected][nowfood].protein,
						mineral:this.allgenres.data[this.Gselected][nowfood].mineral,
						vitamin:this.allgenres.data[this.Gselected][nowfood].vitamin
					}
				}else{
					this.imgSrc=require("./leftselect.png");
				}
				console.log(this.allgenres.data[this.Gselected][nowfood].name);
				// this.Fselected=this.allgenres.data[this.Gselected][nowfood].name;
			}

		}
	}
</script>
<style scoped>
.noweat{
	display:grid;
    grid-template-rows:150px;
    grid-template-columns:400px 250px 300px 200px;
  position:absolute;
  width:78vw;
  height:30vh;
  margin-top:9vh;
  margin-left:20vw;
    background: #fff0cd;
    box-shadow: 0px 0px 0px 5px #fff0cd;
    border: dashed 2px white;
    padding-top:40px;
	padding-left:50px;
    color: #454545;
}
.noweat:after{
    position: absolute;
    content: '';
    right: -7px;
    top: -7px;
    border-width: 0 15px 15px 0;
    border-style: solid;
    border-color: #ffdb88 #fff #ffdb88;
    box-shadow: -1px 1px 1px rgba(0, 0, 0, 0.15);
}
#selectimg{
	position:absolute;
    width:180px;
    height:180px;
	margin-top:-20px;
	grid-row: 1 / 2;
    grid-column: 2 / 3;
}
#eat{
    display:grid;
    grid-template-rows:60px 60px 15px;
    grid-template-columns:90px 200px;
	position:absolute;
	font-size:120%;
    width:20vw;
	background: #f4f4f4;
    border-left: solid 6px #ffb700;
    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.33);
	grid-row: 1 / 2;
    grid-column: 1 / 2;
}
#E11 {
    grid-row: 1 / 2;
    grid-column: 1 / 2;
	padding-top:20%;
	text-align: center;
}
#E12 {
    grid-row: 2 / 3;
    grid-column: 1 / 2;
	padding-top:20%;
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
    width:auto;
	background: #f4f4f4;
    border-left: solid 6px #ffb700;
    box-shadow: 0px 2px 3px rgba(0, 0, 0, 0.33);
	grid-row: 1 / 2;
    grid-column: 3 / 4;
	margin-top:-15px;
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
  color: #000;
  background-color: #fff100;
  border-bottom: 5px solid #ccc100;
  grid-row: 1 / 2;
  grid-column: 4 / 5;
  top:50px;
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
	color: #ffffff;
	background-color:#d88e16;
}
</style>