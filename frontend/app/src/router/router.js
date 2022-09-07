import { createRouter, createWebHistory } from 'vue-router'
import ThePage1 from '../components/create/ThePage1.vue';

const routes = [
  {
    path: '/',
    component: ThePage1,
},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router