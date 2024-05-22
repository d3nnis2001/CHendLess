import {createApp} from 'vue'
import {createPinia} from 'pinia'
import App from './App.vue'
import router from './router'
import {Quasar, Notify} from 'quasar'

createApp(App)
    .use(router)
    .use(createPinia())
    .use(Quasar, {
        plugins: {Notify},
        config: {
            notify: {}
        }
    })
    .mount('#app')