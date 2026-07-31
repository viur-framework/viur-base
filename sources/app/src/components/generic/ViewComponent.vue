<template>
  <header class="view-header wa-split wa-gap-xs wa-justify-content-space-between wa-align-items-start">
    <div class="view-header__content wa-stack wa-gap-xs">
      <h1 class="view-header__title">{{ title }}</h1>
      <div v-if="$slots.default" class="view-header__subtitle">
        <slot></slot>
      </div>
    </div>
    <div v-if="$slots.actions" class="wa-cluster wa-gap-xs view-header__actions">
      <slot name="actions"></slot>
    </div>
  </header>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true,
  },
})
</script>

<style scoped>
.view-header {
  margin-top: 1rem;
}

.view-header__title {
  margin: 0;
  font-size: 2.2em;
  font-weight: 700;
}

.view-header__subtitle:empty {
  display: none;
}

.view-header__subtitle :deep(p),
.view-header__subtitle :deep(h2),
.view-header__subtitle :deep(h3),
.view-header__subtitle :deep(h4),
.view-header__subtitle :deep(h5),
.view-header__subtitle :deep(h6) {
  margin: 0;
}

.view-header__actions {
  flex: 0 0 auto;
}
</style>
