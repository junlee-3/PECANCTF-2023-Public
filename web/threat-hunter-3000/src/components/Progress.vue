<template>
	<div class="progress-bar" v-if="!caseOne || !caseTwo || !caseThree || !caseFour">
		<div class="bracket">[</div>

		<div :class="{'hunted': caseOne}" class="check">
			{{caseOne ? 1 : 0}}
		</div>

		<div :class="{'hunted': caseTwo}" class="check">
			{{caseTwo ? 1 : 0}}
		</div>

		<div :class="{'hunted': caseThree}" class="check">
			{{caseThree ? 1 : 0}}
		</div>

		<div :class="{'hunted': caseFour}" class="check">
			{{caseFour ? 1 : 0}}
		</div>

		<div class="bracket">]</div>
	</div>
	<button class="victory-btn" v-else @click="store.VictoryFlag()">!! FLAG !!</button>
</template>

<script setup lang="ts">
	import { computed } from 'vue'
    import { useStore } from '../stores/main'
    
    const store = useStore();

    const checkForFalse = (array) => {
    	let result = true;

    	array.forEach(x => {
    		if(x["caught"] === false){
    			result = false;
    		}
    	})

    	return result
    }

    const caseOne = computed(() => {
    	const flags = store.store["flags"]["log4j"];
    	return checkForFalse(flags)
    })

    const caseTwo = computed(() => {
    	const flags = store.store["flags"]["email"];
		return checkForFalse(flags)
    })

    const caseThree = computed(() => {
    	const flags = store.store["flags"]["enum"];
    	return checkForFalse(flags)
    })

    const caseFour = computed(() => {
    	const flags = store.store["flags"]["rule"];
    	return checkForFalse(flags)
    })
</script>

<style scoped>
	.progress-bar{
		width: 100%;
		height: var(--headingHeight);
		margin-right: 4rem;

		display: flex;
		justify-content: center;
		align-items: center;
		gap: 2rem;
	}

	.bracket, .check{
		font-family: "Press Start 2P", cursive;
		font-weight: bold;
		font-size: 2rem;
		text-shadow: 4px 3px 0 #7A7A7A;
	}

	.hunted{
		color: var(--green);
	}

	.victory-btn{
		padding: 0.5rem 1rem;
		color: var(--contrast);
		font-family: "Press Start 2P", cursive;
		font-weight: bold;
		font-size: 2rem;
		text-shadow: 4px 3px 0 #7A7A7A;

        background: none;
        outline: none;
        border: 2px dashed white;
        transition: 0.33s ease;
        cursor: pointer;
	}

	.victory-btn:hover{
		border-color: black;
		color: white;
		background: var(--contrast);
	}
</style>