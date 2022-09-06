<script>
    import TheButton from './TheButton.vue';
    export default {
        name: 'SideBar',
        components: 'TheButton',
    }
  </script>

<template>
   
<div class="side">
    <TheButton />
</div>
</template>

<style scoped>
    .side{
        position:absolute;
        background-color:#727272;
        width:15%;
        margin-left:0;
        padding:0;
        height:100vh;
        /*marginss-top:100px;*/
        text-align:center;
        
    }
     /* #meaple{ 
        position: absolute;
        text-align:center;
    } */
</style>