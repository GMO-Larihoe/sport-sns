<template>
  <div class="allpage">
  <SideBar />
  <router-view></router-view>
</div>
</template>


<script setup>
  import SideBar from './components/SideBar.vue';
</script>

<style>
  /* body{
    background-color:#b3b1af;
  } */
</style>