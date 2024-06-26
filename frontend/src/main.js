import { createApp } from 'vue'
import App from './pages/App.vue'
import { createPinia } from 'pinia'
import './index.css'
import router from './router'

const app = createApp(App);
app.use(createPinia)
app.use(router);
app.mount('#app');