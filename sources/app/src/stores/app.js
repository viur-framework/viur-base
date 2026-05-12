import { reactive } from "vue"
import { defineStore } from "pinia"
import { Request } from "@viur/vue-utils"

export const useAppStore = defineStore("appStore", () => {
  const state = reactive({
    user: null,
    ready: false,
    selectedLedgerentryKey: null,
    background: publicAsset("login-background.jpg", "/app/images"),
    logo: publicAsset("mb-clock.svg", "/app/logos"),
  })

  function publicAsset(path, prefix = "static") {
    return `${prefix}/${path}`
    if (import.meta.env.DEV) {
      return `${prefix}/${path}`
    }
    return `../${path}`
  }

  function getCurrentUser() {
    Request.view("user", "self").then(async (resp) => {
      const data = await resp.json()
      state.user = data["values"]
      state.ready = true
    })
  }

  function getUserKey(user) {
    return user?.key || user?.["key"] || ""
  }


  return {
    state,
    getCurrentUser,
    getUserKey,
  }
})
