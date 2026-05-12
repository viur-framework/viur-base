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

import { useAccessabilityStore } from "@/stores/accessabilityStore";


const app = createApp({
  setup() {
    const appElement = document.getElementById("vite_context");
    const accessabilityStore = useAccessabilityStore();
    // Setting Classes vor Accessability Functions
    appElement.classList.add('app-cursor-size-' + accessabilityStore.state.cursorSize)
    appElement.classList.add('app-font-size-' + accessabilityStore.state.fontSize)
    appElement.classList.add('app-line-height-' + accessabilityStore.state.lineHeight)
    appElement.classList.add('app-links-highlighted-' + accessabilityStore.state.linksHighlighted)
    appElement.classList.add('app-font-family-' + accessabilityStore.state.fontFamily)
    appElement.classList.add('app-contrast-mode-' + accessabilityStore.state.contrastMode)
    appElement.classList.add('app-hide-images-' + accessabilityStore.state.hideImages)
    appElement.classList.add('app-text-align-' + accessabilityStore.state.textAlign)
    appElement.classList.add('app-info-hints-' + accessabilityStore.state.infoHints)

  },
  mounted: function () {
    console.debug("mounted Vue.js app", document.readyState);
    boot();
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
