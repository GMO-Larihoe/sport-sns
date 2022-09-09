<template>
     <link href="https://fonts.googleapis.com/earlyaccess/kokoro.css" rel="stylesheet">
    <div>
        <div class="rankinglist">
            <div v-for="(dataindex,index) in dataList" v-bind:key="index">
                {{index+1}}<!--表示-->
            </div>
        </div>

           <div class="namelist">
            <div v-for="(dataname,index) in dataList" v-bind:key="index">
                {{(dataname.name)}}
            </div>
        </div> 

         <div class="scorelist">
            <div v-for="(datascore,index) in dataList" v-bind:key="index">
                {{(datascore.score)}}
            </div>
        </div>  

    </div>
</template>

<script>
    import axios from 'axios'; 
    export default{
        data(){
            return {
                dataList:[
                {name:'kanno',score:50},
                {name:'suzuki',score:80},
                {name:'suzuki',score:70},
                {name:'nii',score:60},
                {name:'ueda',score:60},
                {name:'kanno',score:50},
                {name:'suzuki',score:80},
                {name:'suzuki',score:70},
                {name:'nii',score:60},
                {name:'ueda',score:60},
                {name:'kanno',score:50},
                {name:'suzuki',score:80},
                {name:'suzuki',score:70},
                {name:'nii',score:60},
                {name:'ueda',score:60},
                {name:'kanno',score:50},
                {name:'suzuki',score:80},
                {name:'suzuki',score:70},
                {name:'nii',score:60},
                {name:'ueda',score:60},
                {name:'kanno',score:50},
                {name:'suzuki',score:80},
                {name:'suzuki',score:70},
                {name:'nii',score:60},
                {name:'ueda',score:60},
                {name:'kanno',score:50},
                {name:'suzuki',score:80},
                {name:'suzuki',score:70},
                {name:'nii',score:60},
                {name:'ueda',score:60},
                
               
                
                ],
            }
        },
        mounted(){
            this.getRank();
        },
        methods: {
            getRank: async function(){
                let url = process.env.VUE_APP_API_DEV + '/users/rank';
                const API_TOKEN = sessionStorage.getItem('access_token');
                const res = await axios.get(url, { headers: { Authorization: "Bearer " + API_TOKEN } });
                console.log(res.data);
            }
        }
    }
</script>

<style scoped>
    .rankinglist{ 
        font-family: "Kokoro";
    position: absolute;
     margin-left:7vw; 
     margin-top:0vh;
    /* padding-left:0; */
}
    .namelist{
        
        font-family: "Kokoro";
        position:absolute;
        margin-left:25vw;
        margin-top:0vh;
    }
 
    .scorelist{ 
        font-family: "Kokoro";
    position: absolute;
     margin-left:45vw; 
     margin-top:0vh;
    /* padding-left:0; */
}
</style>