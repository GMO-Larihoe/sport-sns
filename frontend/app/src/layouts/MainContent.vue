<template>
  <router-view />
</template>
 
<script>
export default{
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

<style scoped>
.maincontent_wrapper {
  width: 100%;
}
</style>