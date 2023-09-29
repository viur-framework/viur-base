<template>

    <picture v-if="srcset">
        <source type="image/webp" :srcset="srcset"/>

        <img class="image"
             draggable="false"
             :title="alt?alt:null"
             :alt="alt?alt:null"
             :src="state.image"
             @error="onError"
        />
    </picture>

    <img v-else
         draggable="false"
         :title="alt?alt:null"
         :alt="alt?alt:null"
         :src="state.image"
         @load="updateLoading(false)"
         class="image"
         @click="state.opened=!state.opened"
         @error="onError"
    />

    <sl-dialog v-if="popup" :open="state.opened">
        <img style="display:block"
         draggable="false"
         :title="alt?alt:null"
         :alt="alt?alt:null"
         :src="state.image"
         @load="updateLoading(false)"

    />
        <sl-button :download="alt+'.jpg'" :href="src" variant="primary" target="_blank">Download</sl-button>
    </sl-dialog>

</template>

<script>
/**
 * Image wrapper mit fallback
 * **/

import {reactive, inject,computed} from 'vue'

export default {
    components: {},
    props: {
        src: {
            type: String
        },
        alt: {
            type: String
        },
        srcset: {
            default: null
        },
        fallback: {
            type: String,
            default: 'static/image-fallback.webp'
        },
        popup:{
            type:Boolean,
            default:false
        }
    },

    setup(props, context) {
        const state = reactive({
            loading: true,
            background:computed(()=>{
                /*if(Object.keys(global.state).includes("fallback_image")){
                    return `url(${global.state.fallback_image})`
                }*/
                return ""
            }),
            opened:false,
            image: props.src?props.src:props.fallback
        })

        function updateLoading(loading) {
            state.loading = loading
        }

        function onError(e){
          state.image = props.fallback
        }

        return {updateLoading, state, onError}
    }
}
</script>

<style scoped>
img {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: contain;
    object-position: center;
    background-color: var(--sl-color-neutral-200);
    transition: opacity 2s ease-in-out;

}

img.is-loading {
    filter: blur(4px);
}

.image {
    width: 100%;
    background-image: v-bind('state.background');
    background-repeat: no-repeat;
    background-position: center center;
    background-size: contain;
}
.image:hover{
  object-fit: cover;
}

sl-dialog::part(panel){
  width:100%;
}

sl-dialog{
  img{
    width:auto;
  }
}
</style>
