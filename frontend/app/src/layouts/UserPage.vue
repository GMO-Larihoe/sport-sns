<template>
    <SideBar />
    <MainContent />
</template>
   
  <script>
import SideBar from '../components/SideBar.vue';
import MainContent from './MainContent.vue'
import { useRouter } from "vue-router"
  export default{
    components: {
      SideBar,
      MainContent,
    },
    mounted(){
        this.cheack()
    },
    methods : {
        cheack: async function(){
            const router = useRouter()
            let token = sessionStorage.getItem('access_token');
            if(!token){
                router.push('/login')
            }
        }
    }
  
  }
  </script>
  
  <style scoped>
  .maincontent_wrapper {
    width: 100%;
  }
  </style>