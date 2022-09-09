<template>
    <div class="meaple"> meaple </div>

    <div id="wrap">
    <div class="btn_wrap">
    <a href="#none" class="lazer"><span>入力</span></a>
    </div>
    </div>

     <div id="wrap1">
    <div class="btn_wrap">
    <a href="#none" class="lazer"><span>分析</span></a>
    </div>
    </div> 

    <div id="wrap2">
    <div class="btn_wrap">
    <a href="#none" class="lazer"><span>ランキング</span></a>
    </div>
    </div> 

    <div id="wrap3">
    <div class="btn_wrap">
    <a href="#none" class="lazer"><span>ログアウト</span></a>
    </div>
    </div> 

</template>
<script scoped>
  export default{
      // name:'Button',
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
  height: 10vh;/*ここでボタンの場所を指定*/
  margin-top:10vh;
}

/*ボタン2つ目 */
#wrap1 {
  /* background-color: aqua; */
  height: 10vh;/*ここでボタンの場所を指定*/
  margin-top:0vh;
}

/*ボタン3つ目*/
#wrap2 {
  /* background-color: rgb(43, 228, 11); */
  height: 10vh;/*ここでボタンの場所を指定*/
  margin-top:0vh;
}

/*ログアウト*/
#wrap3 {
  /* background-color: rgb(43, 228, 11); */
  height: 10vh;/*ここでボタンの場所を指定*/
  margin-top:30vh;
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

.lazer span:before {
  content: "";
  width: 100%;
  height: 2.5px;/*ここが下線 */
  background: #FFF;
  position: absolute;
  bottom: -1px;
  left: 0;
  transition: .3s ease-in-out .0s;
}

.lazer:hover span:before {
  height: 5px;/*下線*/
} 
</style>

