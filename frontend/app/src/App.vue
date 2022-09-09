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

<!-- <style>
  /body{
    background-color:#b3b1af;
  } 
</style> -->