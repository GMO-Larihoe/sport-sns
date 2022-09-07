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
  .allpage{
    position: absolute;
  }
  /* body{
    background-color:#b3b1af;
  } */
</style>