<template>
    <div class="meaple"> meaple </div>

    <div id="wrap">
    <div class="btn_wrap">
    <a href="#none" class="lazer"><span>BUTTON</span></a>
    </div>
    </div>
</template>

<script>
  export default{
      // name:'Button',
  }
  </script>

<style scoped>
    .button{
        margin:0;
        padding:0;
    }

    html,
body {
  height: 100%;
  background: #f0002e;
}

#wrap {
  height: 100%;
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

.lazer:before {
  content: "";
  width: 100%;
  height: 1px;
  background: #FFF;
  position: absolute;
  top: -1px;
  right: 0;
  transition: .1s ease-in-out .1s;
}

.lazer:after {
  content: "";
  width: 1px;
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
  height: 1px;
  background: #FFF;
  position: absolute;
  bottom: -1px;
  left: 0;
  transition: .1s ease-in-out .3s;
}

.lazer span:after {
  content: "";
  width: 1px;
  height: 100%;
  background: #FFF;
  position: absolute;
  top: 0;
  left: -1px;
  transition: .1s ease-in-out;
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

.lazer:hover span:before {
  height: 5px;
}


/* ==============================================
* Light Effect
==============================================*/

.light {
  border: 1px solid #FFF;
  overflow: hidden;
}

.light:before {
  content: "";
  width: 200%;
  height: 200%;
  background: rgba(255, 255, 255, .2);
  transform: rotate(-45deg);
  position: absolute;
  top: -10%;
  left: -180%;
  transition: .3s ease-in-out;
}

.light:hover:before {
  left: 60%;
}


/* ==============================================
* Spin Effect
==============================================*/

.spin {
  border: 1px solid #FFF;
  overflow: hidden;
  transition: none;
}

.spin:hover {
  transform: rotateX(360deg);
  transition: .8s ease-in-out;
}


/* ==============================================
* Spin Text Effect
==============================================*/

.spin_text {
  border: 1px solid #FFF;
  overflow: hidden;
}

.spin_text:hover span {
  display: block;
  transform: rotateY(360deg);
  transition: .8s ease-in-out;
}


/* ==============================================
*  Effect
==============================================*/

.push {
  text-indent: -9999em;
}

.push:before {
  content: "BUTTON";
  padding-top: 16px;
  width: 100%;
  height: 100%;
  color: #FFF;
  text-indent: 0;
  background: #b40023;
  box-sizing: border-box;
  box-shadow: 10px 10px 0 #90001c;
  position: absolute;
  top: -5px;
  left: -5px;
  z-index: 2;
  transition: .2s ease-in-out;
}

.push:hover:before {
  top: 0;
  left: 0;
  box-shadow: 0 0 0 #90001c;
}

</style>