<template>
  <overlay-loader v-if="state.waitForInit"></overlay-loader>
  <div v-else class="login">
    <the-login-screen
      :backgroundImage="appStore.state['background']"
      :logo="appStore.state.logo"
    ></the-login-screen>
  </div>
</template>
<script setup>
import { onBeforeMount, reactive, watch } from "vue"
import TheLoginScreen from "@viur/vue-utils/login/TheLoginScreen.vue"
import OverlayLoader from "@/components/generic/OverlayLoader.vue"
import { useUserStore } from "@viur/vue-utils/login/stores/user"
import { Request } from "@viur/vue-utils"
import { useRouter } from "vue-router"
import { useAppStore } from "@/stores/app"

const userStore = useUserStore()
const router = useRouter()
const appStore = useAppStore()
const state = reactive({
  waitForInit: true,
})

function checkUser() {
  userStore
    .updateUser()
    .then(() => {
      state.waitForInit = false
      router.push("/")
    })
    .catch((error) => {
      state.waitForInit = false
    })
}

watch(
  () => userStore.state.user?.key,
  (newVal, oldVal) => {
    checkUser()
  }
)

onBeforeMount(() => {
  Request.get("/vi/settings")
    .then(async (resp) => {
      let data = await resp.json()
      userStore.googleInit(data["admin.user.google.clientID"]).catch(() => {
        throw new Error("clientId is required since the plugin is not initialized with a Client Id")
      })
      checkUser()
    })
    .catch(() => {
      console.log("Viur settings not Found")
    })
})
</script>
<style scoped>
.login {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
}
</style>
