<template>
  <div class="wa-stack wa-align-items-center wa-justify-content-center">
    <h1 class="headline">Welcome to your first ViUR Vue-Site</h1>
  </div>
  <AccessibilityDrawer />
</template>

<script setup>
import { computed, onMounted, reactive } from 'vue'
import { useUserStore } from '@viur/vue-utils/login/stores/user'
import { useAppStore } from '@/stores/app'
import { useRouter } from 'vue-router'

import AccessibilityDrawer from "../components/generic/AccessibilityDrawer.vue";

const userStore = useUserStore()
const appStore = useAppStore()
const router = useRouter()



const state = reactive({
    loading: true,
})

onMounted(async () => {
})

</script>

<style scoped>

</style>
