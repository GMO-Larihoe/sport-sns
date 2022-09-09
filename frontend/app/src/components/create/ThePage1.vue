<template>
  <div>
  <div class="addeat">
    <AddEat />
  </div>
  <PullDown v-on:parent="text = $event"></PullDown>
<TodayEat v-bind:child="text"></TodayEat>
  </div>
</template>

<script>
import axios from 'axios';
import PullDown from './PullDown.vue';
import TodayEat from './TodayEat.vue';
import AddEat from './AddEat.vue';
export default {
  name: 'ThePage1',
  components:{PullDown,TodayEat,AddEat},

  data(){
    return{
      text : "",
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
  },
  methods: {
    add : function(){
      const modal = document.getElementById('easyModal');
      modal.style.display = 'block';
    },
    close : function(){
      const modal = document.getElementById('easyModal');
      modal.style.display = 'none';
    },
    aaaaaaaaaaaaaaa : async function(){
        let url = process.env.VUE_APP_API_DEV + "/users/genres";
        const API_TOKEN = sessionStorage.getItem('access_token');
        let response = await axios.post(url, url, { headers: { Authorization: "Bearer " + API_TOKEN } });
        console.log(response.data);
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
</style>
