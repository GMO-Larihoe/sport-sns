import { createRouter, createWebHistory } from 'vue-router'
import ThePage3 from '../components/ranking/ThePage3';
import ThePage2 from '../components/graph/ThePage2';


import ThePage1 from '../components/create/ThePage1.vue';

const routes = [
  {
    path: '/',
    component: ThePage1,
},

  {
    path : '/pae2',
    component: ThePage2,
  },
  {
    path : '/pae3',
    component: ThePage3,
  },
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router