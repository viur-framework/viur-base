import './shoelace.config'
import './webawesome.config'
import './style/style.css'

import { createApp } from 'vue'
import { createI18n } from "vue-i18n"

import bone from "@viur/vue-utils/bones/edit/bone.vue"
import Wrapper_nested from "@viur/vue-utils/bones/edit/wrapper_nested.vue"
import App from './App.vue'
import pinia from './pinia'
import router from './router'
import { de_translations } from "@viur/vue-utils"



const app = createApp({
  setup() {
  },
  mounted: function () {
    console.debug("mounted Vue.js app", document.readyState);
  },
});

app.use(pinia)

app.component('Bone', bone);
app.component('WrapperNested', Wrapper_nested);


const i18n = createI18n({
  legacy:false,
  locale: 'de',
  fallbackLocale: 'de',
  messages: {  de: de_translations }
})

app.use(i18n);
app.use(router)
app.mount('#app')
