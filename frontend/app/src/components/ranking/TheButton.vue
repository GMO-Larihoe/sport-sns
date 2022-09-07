<template>
    <div class="meaple"> meaple </div>

    <div id="wrap">
    <div class="btn_wrap">
    <a href="#none" class="lazer"><span>BUTTON</span></a>
    </div>
    </div>

    <!-- <div id="wrap1">
    <div class="btn_wrap">
    <a href="#none" class="lazer"><span>BUTTON</span></a>
    </div>
    </div> -->



</template>
<script>
  export default{
      // name:'Button',
  }
  </script>

<style scoped>
    
    html,
body {
  height: 100%;
  background: #f0002e;
}

#wrap {
  height: 50vh;/*ここでボタンの場所を指定*/
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


/* ==============================================
* Lazer Effect 
==============================================*/

/* .lazer:before {
  content: "";
  width: 100%;
  height: 0px;
  background: #FFF;
  position: absolute;
  top: -1px;
  right: 0;
  transition: .1s ease-in-out .1s;
} */

/* .lazer:after {
  content: "";
  width: 1px;
   height: 0%; /*変えると横棒が消える
  background: #FFF;
  position: absolute;
  bottom: 0;
  right: -1px;
  transition: .1s ease-in-out .2s;
} 
*/


.lazer span:before {
  content: "";
  width: 100%;
  height: 2px;/*ここが下線 */
  background: #FFF;
  position: absolute;
  bottom: -1px;
  left: 0;
  transition: .3s ease-in-out .0s;
}
/* 
 .lazer span:after {
  content: "";
  width: 1px;
  height: 0%;
  background: #FFF;
  position: absolute;
  top: 0;
  left: -1px;
  transition: .1s ease-in-out .1s;
} 

 .lazer:hover span:after {
  height: 0;
}

.lazer:hover:before {
  width: 0;
}

.lazer:hover:after {
  height: 0;
} 
*/
.lazer:hover span:before {
  height: 5px;/*下線*/
} 
</style>