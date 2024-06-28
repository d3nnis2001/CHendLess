import { createRouter, createWebHistory } from 'vue-router';
import Upload from '../pages/Upload.vue';
import Start from '../pages/Start.vue';
import Result from '../pages/Results.vue';


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'Start',
            component: Start
        },
        {
            path: '/upload',
            name: 'Upload',
            component: Upload
        },
        {
            path: '/result',
            name: 'Result',
            component: Result
        }
    ]
})


export default router
