import { createRouter, createWebHistory } from 'vue-router'
import ThePage3 from '../components/ranking/ThePage3';


const routes = [
  {
    path:'/',
    component:ThePage3,
  }
  
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router