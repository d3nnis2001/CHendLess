import Start from "./pages/Start.vue";
import {createRouter, createWebHistory} from "vue-router";

const routes = [
    {
        path: '/',
        component: Start
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
