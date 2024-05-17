import {createApp} from 'vue'
import {createPinia} from 'pinia'
import App from './App.vue'
import router from './router'
import {Quasar, Notify} from 'quasar'

import '@quasar/extras/material-icons/material-icons.css'
import 'quasar/src/css/index.sass'

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
