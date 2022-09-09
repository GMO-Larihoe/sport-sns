<template>
  <div>
    <router-view />
  </div>
</template>


<script>

  export default {
    data () {
      return {
        isLogin: false
      }
    },
    methods : {
      changeLogin: function(val) {
        this.isLogin = val
      }
    }
  }
</script>

<style>
  body{
    background-color:#fff6ec;
    margin:0;
  } 
</style>