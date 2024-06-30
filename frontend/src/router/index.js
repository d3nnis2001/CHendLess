import { createRouter, createWebHistory } from 'vue-router';
import Upload from '../pages/Upload.vue';
import Start from '../pages/Start.vue';
import Results from '../pages/Results.vue';
import User from '../pages/User.vue';


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
            path: '/results',
            name: 'Results',
            component: Results
        },
        {
            path: '/user/:id',
            component: User
        }
    ]
})


export default router
