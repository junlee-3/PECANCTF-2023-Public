<template>
	<div id="case1-modal" class="modal">
		<div class="background" @click="$emit('close')"></div>

		<div class="case-submit">
            <div class="case-head">
                <h2 class="shadow">CASE #4203</h2>
                <h2 class="shadow">Sudden User Elevation</h2>
            </div>

            <!-- Question 1 -->
            <div class="question" v-if="question==0">
                <h3 class="shadow">It seems your colleague missed something!</h3>
                <label>Enter the user that has raised suspicions</label>
                <span>
                    <input v-model="main.getFlags['enum'][0]['value']">
                    <button @click="main.checkAnswer('enum', 0)">Submit</button>
                </span>
            </div>

            <!-- Finish -->
            <div class="question" v-else>
                <h3 class="shadow hunted">~ Threat Hunted ~</h3>
            </div>

            <!-- Question Counter -->
            <div class="paginator" >
                <template v-for="key, i in main.getFlags['enum'].length">
                    <div :class="{done: main.getFlags['enum'][i]['caught']}"></div>
                </template>
            </div>
		</div>
	</div>
</template>

<script setup lang='ts'>
    import { computed } from 'vue'
    import { useStore } from '../stores/main'

    // Vars
    const main = useStore();

    // Computed
    const question = computed(() => {
        let count = 0;
        for(let i=0;i < main.getFlags['enum'].length;i++){
            if(main.getFlags['enum'][i]['caught']){
                count += 1;
            }
        }

        return count;
    });
</script>

<style scoped>
    .case-head{
        display: flex;
        justify-content: space-between;
        margin-bottom: 2rem;
    }

    .case-submit{
        position: relative;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        padding: 2rem;
        width: 50vw;
        background: var(--si);
        border: 2px solid black;
    }

    hr{
        border: 2px dotted black;
        margin-bottom: 1rem;
    }

    .hunted{
        color: var(--green);
        text-align: center;
        text-transform: uppercase;
    }

    .question{
        display: flex;
        justify-content: left;
        align-items: left;
        flex-direction: column;
        color: white;
    }
    .question *{
        margin: 1rem 0;
    }

    span{
        display: grid;
        justify-items: center;
        grid-gap: 2rem;
        grid-template-columns: 1fr 1fr;
        grid-template-rows: 1fr;
    }

    input{
        width: 75%;
        font-size: 1rem;
        text-align: center;
        padding: 0.5rem;
        border: 2px dashed black;
        background: white;
        outline: none;
    }

    input:active, input:focus{
        outline: 4px solid var(--si-alt);
    }

    button{
        width: 75%;
        padding: 0 1rem;
        font-family: "Press Start 2P", cursive;
        border: 2px solid black;
        background: lightgrey;
        cursor: pointer;
    }

    button:active{
        color: white;
        background: black;
    }

    .paginator{
        display: flex;
        justify-content: center;
        align-content: center;
        gap: 1rem;
        margin-top: 1rem;
    }

    .paginator div{
        width: 1rem;
        height: 1rem;
        background: whitesmoke;
    }

    .paginator .done{
        background: var(--green);
    }
</style>