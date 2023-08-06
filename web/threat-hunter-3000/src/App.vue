<template>
    <CRT/>
    <Heading/>
    <router-view></router-view>
</template>

<script setup lang='ts'>
    import Heading from './components/Heading.vue'
    import CRT from './components/CRT.vue'
    import { useStore } from './stores/main'
    import axios from 'axios'
    // Fonts
    import '@fontsource/press-start-2p'
    import '@fontsource/open-sans'

    const store = useStore();
    axios({method: "get", url: "logs.json"}).then(response => {
        store.store.logs = response.data;
    }).catch(error => {
        console.log(error)
    })
</script>

<style>
    :root{
        --si: #00b6d9;
        --si-alt: #03D7FF;
        --contrast: #FFE800;
        --green: #A5F800;

        --headingHeight: 10vh;
    }

    *{
        margin: 0;
        padding: 0;
    }
    *::selection{
        color: blue;
        background: var(--contrast);
    }

    #app{
        display: grid;
        grid-template-rows: var(--headingHeight) 1fr;
        color: white;
    }

    h1,h2,h3,h4,input{ font-family: "Press Start 2P", cursive; }
    p{ font-family: "Open Sans", sans-serif; }

    .modal{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 10;
    }

    .background{
        position: absolute;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.75);
    }
</style>
