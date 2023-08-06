<template>
	<header><h1>Cases</h1></header>
	<section>
		<!-- MODALS -->
		<Case1 v-if="currentModal == 1" @close="currentModal=0"/>
		<Case2 v-if="currentModal == 2" @close="currentModal=0"/>
		<Case3 v-if="currentModal == 3" @close="currentModal=0"/>

		<article class="log4j-case">
			<div class="case-header">
				<h1>#4201</h1>
				<h1>Log4j Zero Day</h1>
			</div>

			<p>
				Colleague has discovered a new zero day has been found as of 3:00 AM. Your job is to research the current exploit and vulnerability. By now there should be a CVE available maybe start there.
			</p>
			<p>
				Once you think you have an understanding hunt down all the log ID's in the "Logs" tab, that have to do with the Log4j vulnerability. Enter each ID
			</p>

			<div class="case-footer">
				<button @click="currentModal = 1">Case Submission</button>
				<h1>Author: Neo</h1>
			</div>
		</article>
		<article>
			<div class="case-header">
				<h1>#4202</h1>
				<h1>Email URL Accessed</h1>
			</div>

			<p>
				Apologies I have no information other than that I know a user clicked on a link.
				<br><br>
				Go to the alerts tab and check out "User Interaction With Email Link"
			</p>

			<div class="case-footer">
				<button @click="currentModal = 2">Case Submission</button>
				<h1>Author: Elliot</h1>
			</div>
		</article>
		<article>
			<div class="case-header">
				<h1>#4203</h1>
				<h1>Sudden User Elevation</h1>
			</div>

			<p>
				Recently a large amount of users have changed their privileges and it is hard to tell if they are all legit.<br><br>I have been up all night doing on-call, I am really tired and exhausted could you please review my work and complete the last alarm.
			</p>

			<div class="case-footer">
				<button @click="currentModal = 3">Case Submission</button>
				<h1>Author: Radical Ed</h1>
			</div>
		</article>
		<article>
			<div class="case-header">
				<h1>#4204</h1>
				<h1>Rule Parser</h1>
			</div>

			<p>
				The team now needs to create a regex rule to parse out logs matching Log4j vulnerability attempts. This way we can be alerted when threat agents attempt to breach our clients. Move over to the <i>RULES</i> tab and create a regex string to filter out the log4j logs.
			</p>

			<div class="case-footer">
				<h1>Author: 4ndr3w</h1>
			</div>
		</article>
	</section>
</template>

<script setup lang='ts'>
	import { ref } from 'vue'
	import Case1 from '../components/Case1.vue'
	import Case2 from '../components/Case2.vue'
	import Case3 from '../components/Case3.vue'
	// Vars
	const currentModal = ref(0);
</script>

<style>
	.shadow{
		color: white;
		text-shadow: 4px 3px 0 #7A7A7A;
	}
</style>

<style scoped>
    section{
        display: flex;
        flex-flow: wrap;
        justify-content: center;
        align-items: center;
        padding: 1rem 10rem;
    }

    article{
    	display: flex;
    	flex-direction: column;
    	justify-content: space-between;

    	padding: 1rem;
    	margin: 1rem;
    	height: 25rem;
    	flex: 1 1 30rem;
    	
    	background: whitesmoke;
    	border: 0.5rem solid var(--si);
    	outline: 2px solid black;
    }

    article p{
    	font-family: "Press Start 2P", cursive;
    	text-align: justify;
    }

    .case-header{
    	display: flex;
    	justify-content: space-between;
    	flex-wrap: wrap;
    }

    .case-footer{
    	display: flex;
    	justify-content: space-around;
    	align-items: center;
    }

	.case-footer button{
		width: 15rem;
		height: 3rem;

		font-family: "Press Start 2P", cursive;
		text-transform: uppercase;

		border: 2px dashed black;
		background: none;
	}
	.case-footer button:hover{
		background: var(--si);
	}
	.case-footer button:active{
		color: white;
		background: black;
	}
/*////////////////////////////////////////////*/
</style>