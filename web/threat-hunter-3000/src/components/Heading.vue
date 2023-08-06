<template>
    <header>
        <h1 class="title">Threat Hunter 3000</h1>
        <nav>
<!--             <div class="flag-submit">
                <button @click="flagModal = !flagModal">FLAGS</button>
                <FlagSubmit @close="flagModal = !flagModal" v-if="flagModal"/>
            </div> -->
            <ProgressBar />
            
            <div class="help">
                <p @click="helpModal = !helpModal">?</p>
                <Help @close="helpModal = !helpModal" v-if="helpModal"/>
            </div>
        </nav>
    </header>
</template>

<script setup lang='ts'>
    import { ref } from 'vue'
    import FlagSubmit from './FlagSubmit.vue'
    import ProgressBar from './Progress.vue'
    import Help from './Help.vue'

    // Vars
    const flagModal = ref(false);
    const helpModal = ref(false);
</script>

<style scoped>
    header{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 2rem;
        background: var(--si);
        border-bottom: 2px solid black;
    }

    h1{
        font-size: 2rem;
        font-weight: bold;
        text-transform: uppercase;
        text-shadow: 4px 3px 0 #7A7A7A;
    }

    nav{
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .flag-submit{
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .flag-submit button{
        padding: 0.5rem;

        font-family: "Press Start 2P", cursive;
        font-size: 1.33rem;
        color: white;
        background: none;
        border: 2px dashed white;
        transition: 0.33s ease;
    }

    .flag-submit:hover button{
        color: black;
        border: 2px dashed black;
        background: var(--contrast);
    }

    .help{
        display: flex;
        justify-content: center;
        align-content: center;
        width: 3rem;
        height: 3rem;
        margin: 0 0 0 1.5rem;
    }
    .help p{
        font-size: 2.5rem;
        font-family: "Press Start 2P", cursive;
        transition: 0.33s ease;
        text-shadow: 4px 3px 0 #7A7A7A;
    }
    .help:hover p{
        color: var(--contrast);
        cursor: pointer;
    }
</style>