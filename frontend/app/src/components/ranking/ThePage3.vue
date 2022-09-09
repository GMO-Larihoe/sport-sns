<template>
    <div class="content">
        <DayRanking />
    </div>
</template>

<script>
    import DayRanking from './DayRanking.vue';
    export default{
        name:'ThePage3',
       components:{DayRanking}
    };
</script> 

<style>
    
.content{
    position: absolute;
    background-color:#fff1b6;
    width:85vw;
    height:100vh;
margin-left: 15vw;
    /* margin-left:200px; */
}
</style>