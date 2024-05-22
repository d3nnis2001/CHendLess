import Start from "@/pages/Start.vue";
import Main from "@/pages/Main.Vue";
import {createRouter, createWebHistory} from "vue-router";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'start',
            component: Start
        },
        {
            path: '/main',
            name: 'main',
            component: Main
        },
    ]
})

router.beforeEach((to) => {
    // Something which should be executed before each routing
})

export default router