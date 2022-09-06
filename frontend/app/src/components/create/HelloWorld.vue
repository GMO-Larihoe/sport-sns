<template>
<div class="side">
</div>
<div class="side2">
</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },

  data(){
    return{
      nowmsg : 'apple'
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
.flex{
  display:flex;
}
.side{
    position:absolute;
    background-color:#ff838b;
    width:15vw;
    height: 100vh;
    top:0vh;
    left:0vw;
}
</style>
