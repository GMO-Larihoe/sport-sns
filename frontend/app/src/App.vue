<template>
<router-view></router-view>
  <SideBar />
  
</template>
<script setup>
  import SideBar from './components/SideBar.vue';
</script>

<script>
  import MainContent from './components/ranking/ThePage3.vue';
  import SideBar from './components/SideBar.vue';
</script>

<style>
  /* body{
    background-color:#b3b1af;
  } */
</style>