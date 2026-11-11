import './shoelace.config'
import './webawesome.config'
import './style/style.css'

import { createApp } from 'vue'
import { createI18n } from "vue-i18n"

import bone from "@viur/vue-utils/bones/edit/bone.vue"
import Wrapper_nested from "@viur/vue-utils/bones/edit/wrapper_nested.vue"
import pinia from './pinia'
import { de_translations } from "@viur/vue-utils"

import { useAccessibilityStore } from "@/stores/accessibilityStore";
import AccessibilityDrawer from "@/components/generic/AccessibilityDrawer.vue";


const app = createApp({
  setup() {
    const appElement = document.getElementById("vite_context");
    const accessibilityStore = useAccessibilityStore();
    // Setting Classes vor Accessibility Functions
    appElement.classList.add('app-cursor-size-' + accessibilityStore.state.cursorSize)
    appElement.classList.add('app-font-size-' + accessibilityStore.state.fontSize)
    appElement.classList.add('app-line-height-' + accessibilityStore.state.lineHeight)
    appElement.classList.add('app-links-highlighted-' + accessibilityStore.state.linksHighlighted)
    appElement.classList.add('app-font-family-' + accessibilityStore.state.fontFamily)
    appElement.classList.add('app-contrast-mode-' + accessibilityStore.state.contrastMode)
    appElement.classList.add('app-hide-images-' + accessibilityStore.state.hideImages)
    appElement.classList.add('app-text-align-' + accessibilityStore.state.textAlign)
    appElement.classList.add('app-info-hints-' + accessibilityStore.state.infoHints)

  },
  mounted: function () {
    console.debug("mounted Vue.js app", document.readyState);
  },
});

app.use(pinia)

// The app is mounted on the server-rendered `#vite_context`, whose markup Vue compiles at runtime.
// Components registered here can be used in the Jinja templates (in kebab-case, e.g. `<accessibility-drawer>`).
app.config.compilerOptions.isCustomElement = (tag) => tag.startsWith('sl-') || tag.startsWith('wa-');

app.component('Bone', bone);
app.component('WrapperNested', Wrapper_nested);
app.component('AccessibilityDrawer', AccessibilityDrawer);

const i18n = createI18n({
  legacy:false,
  locale: 'de',
  fallbackLocale: 'de',
  messages: {  de: de_translations }
})

app.use(i18n);
app.mount('#vite_context')
