<template>
    <div class="side">
    <MeapleAicon />
    <TheButton />
    </div>
</template>

<script setup>
    import TheButton from './ranking/TheButton.vue';
  </script>

<style scoped>
    .side{
        position:absolute;
        background-color:#ff9f04d5;
        width:15vw;
        margin-left:0;
        padding:0;
        height:100vh;
        /*marginss-top:100px;*/
        text-align:center;
        border-right:solid 0.1vw rgb(24, 19, 19);
        
    }    

</style>