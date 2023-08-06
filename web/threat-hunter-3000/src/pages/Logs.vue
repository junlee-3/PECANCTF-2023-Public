<template>
    <section class="log-panel">
        <h1>Logs</h1>
        <h1>Log Inspector</h1>

        <div class="filter">
            <div class="search">
                <label>Filter</label>
                <input type="text" v-model="input">
            </div>

            <a href="https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/appendix-l--events-to-monitor" target="_blank">Windows Event IDs</a>
        </div>

        <div class="table">
            <div class="table-header">ID</div>
            <div class="table-header">Timestamp</div>
            <div class="table-header">Log Type</div>

            <div :class="{'active':active==i}" class="wrapper"
                v-for="log, i in FilterLogs" @click="activeLog=log;active=i">
                <div class="log-select table-cell">{{ i }}</div>
                <div class="log-time table-cell">{{ log["time"] }}</div>
                <div class="log-type table-cell">{{ log["type"] }}</div>
            </div>
        </div>

        <div class="drilldown">
            <div class="extra-info" v-if="activeLog">
                <template v-for="item, key in activeLog['log']">
                    <div class="info-title">{{key}}</div>
                    <div class="info">{{item}}</div>
                    <hr>
                </template>
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
    import { ref, onMounted, computed } from 'vue'
    import { useStore } from '../stores/main'
    
    const store = useStore();
    const active = ref(0);
    const activeLog = ref({"log":{"Missing Log": "Select a log"}});
    const input = ref("");

    const escapeRegExp = (input: string) => input.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

    const FilterLogs = computed(() => {
        const logs: any = store.store.logs;

        return logs.filter((x) => {
            const regexPattern = escapeRegExp(input.value);
            const regex = new RegExp(regexPattern, 'i');

            const values: (string|number)[] = [x["time"], x["type"], ...Object.values(x["log"])];
            const rawlog: string = values.join('');

            return regex.test(rawlog);
        });
    });

    onMounted(() => {
        window.addEventListener('keyup', function(event) {
            const lenOfLogs: any = store.getLogs;

            if(event.keyCode === 38)
                active.value -= 1;
            else if(event.keyCode === 40)
                active.value += 1;
            
            if(active.value > lenOfLogs.length-1)
                active.value = lenOfLogs.length-1;
            else if(active.value == -1)
                active.value = 0;

            activeLog.value = FilterLogs.value[active.value]
        });
    })
</script>

<style scoped>
    .log-panel{
        display: grid;
        grid-gap: 1rem;
        grid-template-columns: auto 1fr;
        grid-template-rows: repeat(3, auto);
        grid-template-areas:
            "title1 title2" 
            "filter filter"
            "table drilldown";
    }

    .log-panel h1{
        text-transform: uppercase;
        margin: 0.5rem 0;
    }

/* LOG TABLE */
    .table{
        display: grid;
        grid-gap: 0.5rem;
        grid-template-columns: auto 1fr 0.5fr;
        grid-auto-rows: min-content;
        padding: 1rem;
        background: whitesmoke;
    }

    .table-header{
        display: flex;
        justify-content: left;
        align-items: center;
        padding: 0.5rem;
        background: var(--si);
    }

    .table-cell{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 2rem;
        background: rgba(0, 0, 0, 0.1);
    }

    .wrapper{
        display: contents;
    }

    .log-select{
        margin: auto;
        width: 100%;
        height: 100%;
        grid-column: 1;
    }

    .wrapper:hover *{
        background: var(--si-alt);
        cursor: pointer;
    }
    .active *{
        background: var(--si-alt);
    }

    .log-time{
        font-size: 0.8rem;
        padding: 0 1rem;
    }
    .log-type{
        font-size: 0.8rem;
        text-align: center;
    }
    .log-status{

    }

/* FILTER */
    .filter{
        padding: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        grid-area: filter;
    }

    .filter label{
        margin-right: 2rem;
        text-transform: uppercase;
    }

    .filter a{
        color: black;
        text-decoration: underline;
        text-decoration-style: dashed;
        background: var(--contrast);
    }

    .filter input{
        padding: 0.5rem;
        font-family: "Press Start 2P", cursive;
        font-size: 1.33rem;
        color: black;

        background: none;
        outline: none;
        border: 2px dashed black;
        transition: 0.33s ease;
    }

    .filter button{
        padding: 0.5rem;
        margin-right: 2rem;
        font-family: "Press Start 2P", cursive;
        font-size: 1.33rem;
        color: black;
        background: none;
        border: 2px dashed black;
        transition: 0.33s ease;
        cursor: pointer;
    }

    .filter button:hover{
        color: black;
        border: 2px dashed black;
        background: var(--contrast);
    }

/* LOG INSPECTOR */
    .drilldown{
        padding: 1rem;
        background: whitesmoke;
    }

    .extra-info{
        position: -webkit-sticky; /* Safari */
        position: sticky;
        top: 1rem;
    }

    .extra-info .info-title{
        padding: 0.5rem 0;
        text-transform: uppercase;
        color: var(--si);
        text-shadow: 3px 1px 0 rgba(0, 182, 217, 0.33);
    }

    .extra-info .info{
        padding: 0.5rem 0;
        word-break: break-all;
    }

    .extra-info hr{
        margin: 0.5rem 0;
    }
</style>