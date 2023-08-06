<template>
    <div id="help-modal" class="modal">
        <div class="background" @click="$emit('close')"></div>
        <div class="help">
            <h2>Help</h2><br>
            
            <h3>About</h3>
            <h4>
                Welcome to the Threat Hunter 3000. This device is a <span class="blue">BLUE</span> team simulator. Representing a product called a SIEM (Security information and event management). There are a total of 4 mini challenges once complete will unlock the flag. 

                You can track your progress from via the progress tracker next to the help button. Use the <i>CASES</i> tab to get the info you need to hunt those threats.
            </h4><br>
            <h4 class="shadow" style="color: var(--contrast);text-align: center;">WARNING: Refreshing the page will cause the challenge to restart!</h4><br>

            <h3>Alerts</h3>
            <h4>
                2 Cases have been made for the <i>ALERTS</i> tab. Alerts are pre-defined rules that automatically locate malicious activity within the logs. Use the alerts and <i>Open Source Intelligence</i> to find answers to the questions being asked by your team.
            </h4><br>

            <h3>Logs</h3>
            <h4>
                Use the <i>LOGS</i> tab to locate individual events created within the network. The logs panel has many filters that can be used to hone in on your desired output. Keep in mind the more filters and the more specific you are, the less logs will appear.
            </h4><br>

            <h3>Rules</h3>
            <h4>
                The zero day that you dealt with earlier does not have a way of detecting it in the current SEIM. Your task will be to learn "Regex" and create a string that can be used by the parser to digest future logs with the zero day
            </h4>
        </div>
    </div>
</template>

<style scoped>
    .help{
        position: relative;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        padding: 1rem;
        width: 80%;
        background: var(--si);
        border: 2px solid black;
        overflow: auto;
    }

    .blue{
        color: blue;
    }

    h3{
        margin-bottom: 0.5rem;
        text-shadow: 4px 3px 0 #7A7A7A;
    }

    h4{
        text-align: justify;
    }
</style>