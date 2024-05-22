import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { Quasar } from 'quasar'
import quasarUserOptions from './quasar-user-options'
import App from './pages/App.vue'
import router from './router'
const app = createApp(App)
app.use(createPinia())
app.use(router)
app.use(Quasar, quasarUserOptions)
app.mount('#app')