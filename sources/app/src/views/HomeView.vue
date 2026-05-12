<template>
</template>

<script setup>
import { computed, onMounted, reactive } from 'vue'
import { ListRequest } from '@viur/vue-utils'
import { useUserStore } from '@viur/vue-utils/login/stores/user'
import { useAppStore } from '@/stores/app'
import { useRouter } from 'vue-router'

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
