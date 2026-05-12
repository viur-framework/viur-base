import { createRouter, createWebHashHistory } from "vue-router"
import { useUserStore } from "@viur/vue-utils/login/stores/user"
import pinia from "./pinia"

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("@/views/HomeView.vue"),
      meta: { layout: "default" },
    },
    {
      path: "/user/login",
      name: "login",
      component: () => import("@/views/LoginView.vue"),
      meta: { layout: "FullscreenLayout" },
    },
  ],
})

router.beforeEach(async (to, from, next) => {
  const userStore = useUserStore(pinia)

  if (to.name !== "login" && !userStore.state.user) {
    try {
      await userStore.updateUser()
    } catch (error) {
      userStore.state.user = null
      return next({ name: "login" })
    }
  } else if (to.name === "login" && !userStore.state.user) {
    return next()
  }
  next()
})

export default router
