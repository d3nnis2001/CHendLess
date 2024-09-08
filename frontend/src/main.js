import { createApp } from 'vue'
import App from './pages/App.vue'
import { createPinia } from 'pinia'
import './index.css'
import router from './router'
import Aura from '@primevue/themes/aura';
import PrimeVue from 'primevue/config';
import ToastService from 'primevue/toastservice';
import "primeicons/primeicons.css";

const app = createApp(App);
app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
});
app.use(ToastService);
app.use(createPinia)
app.use(router);
app.mount('#app');

