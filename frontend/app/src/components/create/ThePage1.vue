<template>
  <div>
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
</style>
