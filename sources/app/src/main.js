import './shoelaceConfig';

import {createApp} from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import {createI18n} from "vue-i18n"
import en from "./translations/en"
import de from "./translations/de"
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue'

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

const app = createApp(App)

app.use(pinia)

app.use(router)

const i18n = createI18n({
    locale: "de",
    fallbackLocale: "en",
    messages: {"en": en, "de": de}
})

app.use(i18n)

app.mount('#app')
