<template>
    <section>
        <div class="alert active">
            <div class="card">
                <div class="card-header">
                    <h2>User Interaction With Email Link</h2>
                    <h3 class="new">New</h3>
                </div>
                <div class="card-text">
                    <p>ID: {{ main.randNum(4000,5000) }}</p>
                    <p>Date: 12/Sep/2022 11:00 AM</p>
                    <p>Link: hxxp://void[.]xyz/keylogger.pdf?download=true</p>
                    <p>
                        A link has been clicked on within an email, and the link matched with an <i>indicator of compromise</i>.
                    </p>
                </div>
            </div>
        </div>
        <div class="alert active">
            <div class="card">
                <div class="card-header">
                    <h2>User Elevated To Administrator</h2>
                    <h3 class="new">New</h3>
                </div>
                <div class="card-text">
                    <p>ID: {{ main.randNum(4000,5000) }}</p>
                    <p>Date: 16/Sep/2022 10:04 PM</p>
                    <p>Event: #4728</p>
                    <p>A change in the administrators group has been detected.</p>
                </div>
            </div>
        </div>
        <div class="alert" v-for="i in 4">
            <div class="card">
                <div class="card-header">
                    <h2>{{ alarmNames[Math.floor(Math.random()*alarmNames.length)]}}</h2>
                    <h3 class="closed">Closed</h3>
                </div>
                <div>
                    ID: {{ main.randNum(4000,5000) }}<br>
                    Date: {{ main.randDate() }}<br>
                    ...
                </div>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
    import { useStore } from '../stores/main'
    const main = useStore();
    const alarmNames = [
        "Remote User Login Fail", "Port Scanning In Progress", 
        "Overseas Access", "Malicious Web Traffic"
    ]
</script>

<style scoped>
    section{
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 2rem;
        padding: 1rem 10rem;
    }

    .alert{
        padding: 1rem;
        width: 33rem;
        height: auto;

        background: whitesmoke;
        border: 4px dashed rgba(0, 0, 0, 0.33);
        color: rgba(0, 0, 0, 0.33);
    }

    .active{
        border: 4px solid var(--si);
        color: black;
    }

    .card *{
        margin-bottom: 0.5rem;
    }

    .card-header{
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .card h2{
        font-size: 1rem;
    }

    .card h3{
        font-size: 0.8rem;
    }

    .card-text p{
        font-family: "Press Start 2P", cursive;
        font-size: 0.8rem;
    }

    .card .new{ color: var(--si); }

    .card .closed{ color: rgba(255, 0, 0, 0.33); }
</style>