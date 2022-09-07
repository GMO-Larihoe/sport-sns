<template>
  <div>
  <a class="btn btn--yellow btn--cubic" v-on:click="add">食品追加</a>
<div class="noweat">
  <PullDown />
</div>
<p id="ttext">今日の食事</p>
<div class="today">
<TodayEat />
  </div>
  </div>
</template>

<script>
import PullDown from './PullDown.vue';
import TodayEat from './TodayEat.vue';
export default {
  name: 'ThePage1',
  components:{PullDown,TodayEat,},

  data(){
    return{
    };
 
  },
  computed: {
    test() {
      switch(this.nowmsg){
        case 'apple': 
        case 'melon':
        case 'orange':
          return this.nowmsg;
        default:
          return 'test';
      }
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body{
        font-family:'Noto Sans JP',sans-serif;
        background-color:#f6f5f4;
}
.today{
  position:absolute;
  background-color:coral;
  overflow: auto;
  width:75vw;
  height:50vh;
  margin-top:45vh;
  margin-left:20vw;
} 
.noweat{
  position:absolute;
  background-color: chocolate;
  width:75vw;
  height:30vh;
  margin-top:7vh;
  margin-left:20vw;
}
#ttext{
  position:absolute;
  font-size:120%;
  width:auto;
  height:auto;
  background-color:chartreuse;
  margin-top:40vh;
  margin-left:20vw;
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
  left:83.5vw;
  top:1vh;
  color: #000;
  background-color: #fff100;
  border-bottom: 5px solid #ccc100;
}
a.btn--yellow:hover {
  margin-top: 3px;
  color: #000;
  background: #fff20a;
  border-bottom: 2px solid #ccc100;
}
</style>
