<template>
      <link href="https://fonts.googleapis.com/css?family=Noto+Sans+JP" rel="stylesheet">
    <div>
       
        
            <div  v-for="(dataindex,index) in dataList" v-bind:key="index">
                <div class="ranking">
                <div class="rankinglist"> {{index+1}}<!--表示--></div>
                <div class="namelist">{{(dataindex.name)}}</div>
                <div class="scorelist"> {{(dataindex.score)}}</div>
                </div>
            </div>
        

           <!-- <div class="namelist">
            <div v-for="(dataname,index) in dataList" v-bind:key="index">
                {{(dataname.name)}}
            </div>
        </div> 

         <div class="scorelist">
            <div v-for="(datascore,index) in dataList" v-bind:key="index">
                {{(datascore.score)}}
            </div>
        </div>   -->

    </div>
</template>

<script>
    import axios from 'axios'; 
    export default{
        data(){
            return {
                dataList:[
                // {name:'kanno',score:50},
                // {name:'suzuki',score:80},
                // {name:'suzuki',score:70},
                // {name:'nii',score:60},
                // {name:'ueda',score:60},
                // {name:'kanno',score:50},
                // {name:'suzuki',score:80},
                // {name:'suzuki',score:70},
                // {name:'nii',score:60},
                // {name:'ueda',score:60},
                // {name:'kanno',score:50},
                // {name:'suzuki',score:80},
                // {name:'suzuki',score:70},
                // {name:'nii',score:60},
                // {name:'ueda',score:60},
                // {name:'kanno',score:50},
                // {name:'suzuki',score:80},
                // {name:'suzuki',score:70},
                // {name:'nii',score:60},
                // {name:'ueda',score:60},
                // {name:'kanno',score:50},
                // {name:'suzuki',score:80},
                // {name:'suzuki',score:70},
                // {name:'nii',score:60},
                // {name:'ueda',score:60},
                // {name:'kanno',score:50},
                // {name:'suzuki',score:80},
                // {name:'suzuki',score:70},
                // {name:'nii',score:60},
                // {name:'ueda',score:60},
                
               
                
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
                this.dataList=res.data;
            }
        }
    }
</script>

<style scoped>
  .ranking{    
    display:flex;
    font-size:120%;
	margin-left:0vw;
    width:100%;
    border-bottom:1px dashed gray;
    

  }

     .rankinglist{ 
       
    font-family: 'Noto Sans JP', sans-serif;
     /* position: absolute;  */
     margin-left:0vw; 
     margin-top:0vh;
     height:30px;
     width:33.3% ;
     /* padding-left:0;  */
    /* background: white; */
} 

    .namelist{
        font-family: 'Noto Sans JP', sans-serif;
        /* position:absolute; */
        margin-left:0vw;
        margin-top:0vh;
        height:30px;
     width:33.3%;
        /* background-color: white; */
    }
 
    .scorelist{ 
        font-family: 'Noto Sans JP', sans-serif;
    /* position: absolute; */
     margin-left:0vw; 
     margin-top:0vh;
     height:30px;
     width:33.3%;
    /* padding-left:0; */
    /* background: white; */
}
</style>