<template>
    <section class="rule-panel">
    	<h1>Regex Parser</h1>

        <div class="filter-wrap">
            <div class="filter">
                <input type="text" v-model="store.store.rule">
            </div>
        </div>

        <div class="logs" v-for="log in regexOutput">
        	<div class="log-line">{{ log }}</div>
        </div>

        {{foo}}
    </section>
</template>

<script setup lang='ts'>
    import { ref, onMounted, computed } from 'vue'
    import { useStore } from '../stores/main'
    
    const store = useStore();

    const regexOutput = computed(() => {
    	let regex = new RegExp(store.getRule);
        const apacheLogs: any = store.getApacheLogs;
    	return apacheLogs.filter(x => regex.test(x))
    })

    const foo = computed(() => {
        const result = regexOutput;
        if(result.value.length == 1){
            store.setRule(result.value[0])
            store.checkAnswer('rule', 0);
        }
    })
</script>

<style scoped>
    .rule-panel{
        display: grid;
        grid-gap: 2rem;
        justify-content: center;
        align-items: center;
        grid-template-columns: 1fr;
        grid-template-rows: 5vh 5vh 1fr;
    }

    .filter-wrap{
    	display: flex;
    	justify-content: center;
    	align-content: center;
    }

    .filter input{
        width: 50vw;
        font-size: 1.5rem;
        text-align: center;
        padding: 0.5rem;
        border: 2px dashed black;
        background: white;
        outline: none;
    }

    .filter input:active, .filter input:focus{
        outline: 4px solid var(--si-alt);
    }

    .logs{
    	display: flex;
    	flex-direction: column;
    	gap: 1rem;
    	text-align: center;
    }

    .log-line{
    	padding: 1rem;
    	background: rgba(0, 0, 0, 0.1);
    }
</style>