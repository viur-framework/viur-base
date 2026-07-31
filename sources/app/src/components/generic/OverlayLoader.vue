<template>
  <div class="overlay" v-if="active">
    <div class="bg"></div>
    <slot>
      <sl-spinner></sl-spinner>
    </slot>
  </div>
</template>
<script setup>
const props = defineProps({
  active: {
    type: Boolean,
    defaultValue: true,
  },
})
</script>

<style scoped>
.overlay {
  position: absolute;
  display: flex;
  width: 100%;
  height: 100%;
  align-items: center;
  justify-content: center;
  z-index: 99;

  .bg {
    position: absolute;
    background-color: white;
    opacity: 0.7;
    width: 100%;
    height: 100%;
  }

  & sl-spinner,
  sl-icon {
    font-size: 3rem;
    z-index: 99;
  }
}
</style>
