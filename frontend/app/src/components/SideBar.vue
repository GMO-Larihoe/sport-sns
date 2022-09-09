<template>
    <div class="side">
    <img src="./meaple8.png" id="meapleimg">

    <TheButton />
    </div>
</template>

<script setup>
    import TheButton from './ranking/TheButton.vue';
  </script>

<style scoped>
    #meapleimg{
        margin-left:0;
        margin-top:5vh;
        width:80%;
        height:20%;

        background-color:#fff6ec;
    }

    .side{
        position:absolute;
        background-color:#FF9F04;
        width:15vw;
        margin-left:0;
        padding:0;
        height:100vh;
        /*marginss-top:100px;*/
        text-align:center;
        border-right:solid 0.1vw rgb(24, 19, 19);
        
    }    

</style>