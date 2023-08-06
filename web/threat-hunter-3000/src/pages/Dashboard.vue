<template>
	<main>
		<nav>
			<a @click="changeMenu('cases')"
				:class="{active: menu==='cases'}">Cases</a>

			<a @click="changeMenu('alerts')"
				:class="{active: menu==='alerts'}">Alerts</a>
				
			<a @click="changeMenu('logs')"
				:class="{active: menu==='logs'}">Logs</a>
				
			<a @click="changeMenu('rules')"
				:class="{active: menu==='rules'}">Rules</a>
		</nav>
		<section>
			<Logs v-if="menu==='logs'"/>
			<Alerts v-if="menu==='alerts'"/>
			<Cases v-if="menu==='cases'"/>
			<Rules v-if="menu==='rules'"/>
		</section>
	</main>
</template>

<script setup lang='ts'>
	import { ref } from 'vue'
	import Logs from './Logs.vue'
	import Alerts from './Alerts.vue'
	import Cases from './Cases.vue'
	import Rules from './Rules.vue'

	// Vars
	const menu = ref('cases');

    // Methods
    const changeMenu = (menuOption) => {
        menu.value = menuOption;
    }
</script>

<style scoped>
	main{
		color: black;
		font-family: "Press Start 2P", cursive;
	}

	nav{
		display: flex;
		justify-content: center;
		align-items: center;
	}

	nav a{
		width: 100%;
		height: 100%;
		
		padding: 1rem;
		margin: 0 1rem;

		text-align: center;
		text-transform: uppercase;
		border: 2px dashed black;
		border-top: none;
		transition: 0.15s ease;
	}
	nav a:hover{
		color: var(--contrast);
		background: var(--si);
		cursor: pointer;
	}

	nav .active{
		background: var(--si);
		border-style: solid;
		border-top: none;
	}

	section{
		padding: 1rem;
	}
</style>