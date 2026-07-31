
<template>
  <div class="wa-stack wa-gap-0 wrapper" v-if="state.webReady">
    <router-view v-slot="mainprops">
      <component :is="getLayout(mainprops)">
        <component :is="mainprops.Component"></component>
      </component>
    </router-view>
  </div>
</template>

<script setup>

import { RouterView, useRouter } from "vue-router"
import layouts from "./layouts/index"
import { allDefinedShoelace } from "./shoelace.config"
import { onBeforeMount, onMounted, onUnmounted, reactive } from "vue"
import { allDefined } from "@viur/webawesome"
import { useUserStore } from "@viur/vue-utils/login/stores/user"

const router = useRouter()
const userStore = useUserStore()
const state = reactive({
  webReady: false,
  webError: false,
})

async function checkSession() {
  if (document.visibilityState !== 'visible') return
  try {
    await userStore.updateUser()
  } catch {
    userStore.state.user = null
    router.push({ name: 'login' })
  }
}

onMounted(() => document.addEventListener('visibilitychange', checkSession))
onUnmounted(() => document.removeEventListener('visibilitychange', checkSession))

function getLayout(mainprops) {
  if (mainprops.route.matched.length === 0) {
    return layouts.FullscreenLayout
  }
  return layouts?.[mainprops.route.meta.layout] || layouts.default
}

onBeforeMount(async () => {
  try {
    await allDefinedShoelace()
    await allDefined()
    state.webReady = true
  } catch (err) {
    state.webError = true
  }
})
</script>

<style scoped>
.wrapper{
  height: 100vh;
}

:deep(.login-card){
  background-color: #fff !important;
}


</style>
