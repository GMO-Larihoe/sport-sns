import { createRouter, createWebHistory } from 'vue-router'
import HelloWorld from '../components/create/HelloWorld.vue';
import ApplePage from '../components/create/ApplePage.vue';
import MelonPage from '../components/create/MelonPage.vue';
import OrangePage from '../components/create/OrangePage.vue';


const routes = [
    {
        path: '/',
        component: HelloWorld,
    },
    {
        path: '/apple',
        component: ApplePage,
    },
    {
        path: '/melon',
        component: MelonPage,
    },
    {
        path: '/orange',
        component: OrangePage,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router;