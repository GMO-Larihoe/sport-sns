import { createRouter, createWebHistory } from 'vue-router'
import ThePage2 from '../components/graph/ThePage2';


const routes = [
  {
    path : '/',
    component: ThePage2,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router