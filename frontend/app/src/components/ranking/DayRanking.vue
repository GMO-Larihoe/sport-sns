<template>
    <div class="rankingword">
       前日ランキング

    </div>
    <div class="wordframe">
        <TheWord />
    </div>



    <div class="rankingframe"> 
        <!-- <TheNumber /> -->
        <TheData />
    </div>
     <!--   <frame />-->
     
    <div class="pagenumber">

    </div>

    <!-- 
    <div id="ranking1"><router-link :to='/ranking1'>1</router-link></div>
    <div id="ranking2"><router-link :to='/ranking2'>2</router-link></div>
    <div id="ranking3"><router-link :to='/ranking3'>3</router-link></div>
    <div id="ranking4"><router-link :to='/ranking4'>4</router-link></div>
    <div id="ranking5"><router-link :to='/ranking5'>5</router-link></div>  -->  
</template>

<script>
    import TheWord from './details/TheWord.vue';
    import TheData from './details/TheData.vue';
    export default{
    components: {
        TheWord,
        TheData,
    }
}
</script>

<style scoped>
    .rankingword{
        text-align:center;
        /* margin-top:10vw;  */
        padding-top: 2vw;
        font-size:20px;
    }
    .wordframe{
        position:absolute;
        background-color:#ffffff;
        margin-left:10vw;
        margin-top:5vh;
        width:65vw;
        height:3vh;
    }
    .rankingframe{
        position:absolute;
        overflow: auto;
        background-color:#ffffff;
        text-align:center;
        /* margin-left:25vw;*/
        margin-left:10vw;
        margin-top:9vh;
        width:65vw;
        height:80vh;
    } 
    .pagenumber{
        text-align:center;
    }
</style>