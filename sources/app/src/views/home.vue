<template>
  <div class="home">

    <h1 class="main-headline">{{ $t('hello') }}</h1>
    <sl-icon class="icon" src="/logo-cube.svg"></sl-icon>
    <div>
      <sl-button-group>
    <sl-button @click="appStore.state.counter+=1" variant="success">+1</sl-button>
    <sl-button @click="appStore.state.counter-=1" variant="warning">-1</sl-button>
    <sl-button @click="appStore.state.counter=0" variant="danger">reset</sl-button>
        </sl-button-group>
    </div>
    <div class="output">{{appStore.state.counter}}</div>
  </div>
</template>

<script>
// @ts-nocheck
import {defineComponent, reactive,computed} from 'vue'
import {useAppStore} from "@/stores/app";

export default defineComponent({
  props: {},
  components: {},
  setup(props, context) {
    const appStore = useAppStore()


    const state = reactive({

    });

    return {
      state,
      appStore
    }
  }
})
</script>

<style scoped>
.home{
  display: grid;
      justify-items: center;
    align-items: center;
}
.output{
  padding: 50px;
  font-size: 2rem;
}

.icon{
  font-size: 5rem;
  padding:20px;
  color:firebrick;
}
</style>