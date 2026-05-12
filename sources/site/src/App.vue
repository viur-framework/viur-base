
<template>
  <HomeView />
</template>

<script setup>

import { useRouter } from "vue-router"
import { onBeforeMount, reactive } from "vue"
import { useUserStore } from "@viur/vue-utils/login/stores/user"
import HomeView from "./views/HomeView.vue";

const router = useRouter()
const userStore = useUserStore()

const state = reactive({
})

onBeforeMount(async () => {
})
</script>

<style scoped>
</style>
