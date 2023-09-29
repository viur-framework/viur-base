//@ts-nocheck

import {reactive, computed, Component, getCurrentInstance} from 'vue';
import {defineStore, StoreDefinition} from "pinia";
import {useRouter} from "vue-router";
import {useUserStore} from "./user";

export const useAppStore = defineStore("app", () => {
    const router = useRouter()
    const state = reactive({
        counter:0

    })

    return {
        state
    }
}, { persist: true })
