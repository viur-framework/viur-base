<template>
  <router-view :key="route.params.key"/>
</template>

<script>
import {computed, defineComponent, onBeforeMount} from "vue"
import {useRoute} from "vue-router";

export default defineComponent({
  components: { },
  setup() {
    const route = useRoute()

    return {
      route
    }

  }
})
</script>

<style>

</style>
