<template>
    <div class="home">
        View {{route.path}} is missing.
    </div>
</template>

<script>
// @ is an alias to /src
import {reactive} from 'vue'
import {useRoute} from "vue-router";

export default {
    name: 'Home',
    components: {
    },
    setup(props, context) {
        const route = useRoute()
        const state = reactive({})

        return {
            state,
            route
        }
    }
}
</script>
