import { createRouter, createWebHistory } from 'vue-router'
import ThePage3 from '../components/ranking/ThePage3.vue';
import ThePage2 from '../components/graph/ThePage2.vue';
import ThePage1 from '../components/create/ThePage1.vue';
import UserPage from '../layouts/UserPage.vue'
import LoginPage from '../LoginPage.vue'
import SignUp from '../SignUp.vue'

const routes = [
  {
    path: '/home',
    component: UserPage,
    children: [
      {
        path: 'page1',
        component: ThePage1
      },
      {
        // /user/:id/posts がマッチした時に
        // UserPosts は User の <router-view> 内部で描画されます
        path: 'page2',
        component: ThePage2
      },
      {
        // /user/:id/posts がマッチした時に
        // UserPosts は User の <router-view> 内部で描画されます
        path: 'page3',
        component: ThePage3
      }
    ]
  },
  {
    path: '/login',
    component: LoginPage,
  },
  {
    path: '/signup',
    component: SignUp,
  },
  {
    path: '/:catchAll(.*)',
    redirect: '/home'
  }
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router