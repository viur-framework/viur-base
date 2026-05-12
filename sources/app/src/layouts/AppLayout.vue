<template>
  <div class="page">
    <slot></slot>
  </div>
</template>
<script setup>

import { useAppStore } from "@/stores/app"

const appStore = useAppStore()

</script>
<style scoped>
.page {
  flex: 1;
  min-height: 0;
  padding: 0;
  overflow-y: auto;
}

</style>
