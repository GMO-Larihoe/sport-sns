<template>
    <div class="rankingword">
       <div class="ranking"> 前日ランキング</div>
    </div>

    <div class="border">
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
        margin-left:27vw;
        margin-top:5vh;
        /* margin-top:10vw;  */
        padding-top: 2vh;
        font-size:20px;
         width:30vw;
         height:4vh;
         border-radius: 0%;
        background-color:#ff9f04d5;
    }
    .ranking{
        margin-top:-2vh;
         color:white; 
        text-align:center;   
    }

    .border{
        margin-left:5vh;
        margin-top:5vh;
        background-color:rgb(140, 137, 137);
        height:0.1vh;
        width:78vw;
        
    }
    .wordframe{
        /* border: 1px solid; */
        /* border-bottom: transparent; */
        
        border-left:solid 1px gray;
        border-right:solid 1px gray ; 
         border-top:solid 1px gray;
        position:absolute;
        background-color:#ffe4a9d5;
        margin-left:10vw;
        margin-top:6vh;
        width:65vw;
        height:3vh;
    }
    .rankingframe{
        border-top:solid 1px gray;
        border-left:solid 1px gray;
        border-right:solid 1px gray;
        border-bottom:solid 1px  gray;
        /*dashed */
        /* border: 1px solid; */
        /* border-top: transparent; */
        position:absolute;
        overflow: auto;

        background-color:rgb(253, 248, 248);
        text-align:center;
        /* margin-left:25vw;*/
        margin-left:10vw;
        margin-top:9vh;
        width:65vw;
        height:70vh;

    } 
    .pagenumber{
        text-align:center;
    }
</style>