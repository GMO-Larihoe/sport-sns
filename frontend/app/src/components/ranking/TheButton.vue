<template>
  <div class="meaple"> meaple </div>

  
  <div id="wrap">
  <div class="btn_wrap">
  <a href="/home/page1" class="lazer"><span>入力</span></a>
  </div>
  </div>

   <div id="wrap1">
  <div class="btn_wrap">
  <a href="/home/page2" class="lazer"><span>分析</span></a>
  </div>
  </div> 

  <div id="wrap2">
  <div class="btn_wrap">
  <a href="/home/page3" class="lazer"><span>ランキング</span></a>
  </div>
  </div> 

  <div id="wrap3">
  <div class="btn_wrap">
  <a href="#" @click="linkClick" class="lazer"><span>ログアウト</span></a>
  </div>
  </div> 

</template>
<script scoped>
  import router from '../../router/router.js'
export default{
    // name:'Button',
    methods: {
      linkClick: function(){
        console.log(1);
        sessionStorage.clear();
        router.push("/login")

      }
    }
}
</script>



<style scoped>

.meaple{
margin-top:10vh;
height:5vh;
}

  html,
body {
height: 100%;
/* background: #f0002e; */
}
/*ボタン1つ目*/
#wrap {
/* background-color: #f0002e; */
height: 00vh;/*ここでボタンの場所を指定*/
margin-top:10vh;
}

/*ボタン2つ目 */
#wrap1 {
/* background-color: aqua; */
height: 0vh;/*ここでボタンの場所を指定*/
margin-top:10vh;
}

/*ボタン3つ目*/
#wrap2 {
/* background-color: rgb(43, 228, 11); */
height: 0vh;/*ここでボタンの場所を指定*/
margin-top:10vh;
}

/*ログアウト*/
#wrap3 {
/* background-color: rgb(43, 228, 11); */
height: 0vh;/*ここでボタンの場所を指定*/
margin-top:40vh;
}

.btn_wrap {
height: 100%;
display: -webkit-flex;
display: flex;
-webkit-align-items: center;
align-items: center;
-webkit-justify-content: center;
justify-content: center;
}

a {
display: block;
 margin: 0 10px;
padding: 15px 0; 
 width: 130px; 
font-weight: bold;
color: #FFF;
text-align: center;
text-decoration: none;
position: relative;
transition: .2s ease-in-out;
}

a:active {
  background: rgba(255, 255, 255, .5);
}

/*ここから*/
 .lazer:before {
  content: "";
  width: 100%;
  height: 0vh;
  background: #FFF;
  position: absolute;
  top: -1px;
  right: 0;
  transition: .1s ease-in-out .1s;
}
.lazer:after {
  content: "";
  width: 0vh;
  height: 100%;
  background: #FFF;
  position: absolute;
  bottom: 0;
  right: -1px;
  transition: .1s ease-in-out .2s;
} 
.lazer span:before {
content: "";
width: 100%;
height: 0.2vh;/*ここが下線 */
background: #FFF;
position: absolute;
bottom: -1px;
left: 0;
transition: .3s ease-in-out .0s;
}

 .lazer span:after {
  content: "";
  width: 0vh;
  height: 100%;
  background: #FFF;
  position: absolute;
  top: 0;
  left: -1px;
  transition: .1s ease-in-out;
} 
/*ここまで*/


.lazer:hover span:after {
  height: 0.5vh;
}
.lazer:hover:before {
  width: 0.5vh;
}
.lazer:hover:after {
  height: 0.5vh;
}

.lazer:hover span:before {
height: 0.5vh;/*下線*/
} 

</style>

