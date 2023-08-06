import { ref, computed } from 'vue'
import { defineStore, acceptHMRUpdate } from 'pinia'
import sjcl from 'sjcl'

export const useStore = defineStore('main', () => {
    // State
    const store = ref({
        salt: ":dothechallengelazybones",
        rule: "",
        flags: {
            log4j:[
                {
                    value: "",
                    hash: "e9533c40becc22b75ad99b17aecc784157ae2cee40b2e6ff5f497c28541ce81b",
                    caught: false
                },
                {
                    value: "",
                    hash: "62bbcba0aaecca8ee69689d71e8012dc82b703f5efe0ff7df65c0c2a4dbae2b2",
                    caught: false
                },
                {
                    value: "",
                    hash: "a675da970e08d878c4bdabccaa2c9b6cb27f1e4eadb40be9742e5baf628cd3df",
                    caught: false
                },
                {
                    value: "",
                    hash: "28f016edd8fc3b8a525a2c60d39634f04183c46bfc313e30adfef60cae463fa2",
                    caught: false
                }
            ],
            email:[
                {
                    value: "",
                    hash: "0085006f38aa476fa41e82737801fa6b2750443a5868b67c6bf0b4d5c9b2b050",
                    caught: false
                },
                {
                    value: "",
                    hash: "0beaf5524996925eba569b6b45986881002012eb65e77287ee717bfb497f375e",
                    caught: false
                },
                {
                    value: "",
                    hash: "8e269d6ccd0dad203d3f78ce3675b09da2b058633e4705abbb74eda5e24b988e",
                    caught: false
                }
            ],
            enum:[
                {
                    value: "",
                    hash: "21e7dbae486d62943f922778d178721e95edeab84f5a1fee3e289669600b9784",
                    caught: false
                }
            ],
            rule:[
                {
                    value: "",
                    hash: "ad21172cdfa4a4e380052773da6babdcb8adf6d5a1217a92bbb1426a1bf950d0",
                    caught: false
                }
            ]
        },
        logs:{}
    });

    // Getters
    const getFlags = computed(() => store.value.flags)
    const getRule = computed(() => store.value.rule)
    const getLogs = computed(() => store.value.logs)

    const getApacheLogs = computed(() => {
        if(typeof store.value.logs === 'undefined')
            return false

        const logs: any = store.value.logs;
        let logsObject: any = logs.filter(set => set["type"].includes("Apache"))
        let logsArray = []
        for(let x in logsObject){
            let log = ""
            for(let y in logsObject[x]["log"]){
                log += `${logsObject[x]["log"][y]} `
            }
            logsArray.push(log.trim())
        }
        return logsArray
    })

    // Actions
    const setRule = (rule) => store.value.flags["rule"][0]["value"] = rule;

    const checkAnswer = (challenge, question) => {
        const bitArray = sjcl.hash.sha256.hash(
            store.value.flags[challenge][question]["value"].toLowerCase()+store.value.salt
        );
        const hash = sjcl.codec.hex.fromBits(bitArray)

        if(store.value.flags[challenge][question]["hash"] == hash)
            store.value.flags[challenge][question]["caught"] = true;
        else
            store.value.flags[challenge][question]["caught"] = false;
    }

    const VictoryFlag = () => {
        let values = [":dothechallengelazybones"];
        const flags = store.value.flags;

        for(let challenge in flags){
            for(let flag of flags[challenge]){
                if(flag["caught"]===false){return}
                values.unshift(flag["value"])
            }
        }

        const FinalFlag: string = values.join('').toLowerCase()
        const bitArray = sjcl.hash.sha256.hash(FinalFlag);
        const hash = sjcl.codec.hex.fromBits(bitArray)

        alert(`pecan{${hash}}`)
    }

    const randNum = (min, max) => {
        return (Math.floor(
            Math.pow(10,14)*Math.random()*Math.random())%(max-min+1)        
        )+min;
    }

    const randDate = () => {
        const max = 1662897600
        const min = 1640995200

        // Randomizer
        const time = new Date(
            (
                (Math.floor(
                    Math.pow(10,14)*Math.random()*Math.random())%(max-min+1)
                )+min
            )*1000
        );

        return `${time.getDay()+1}/${time.getMonth()+1}/${time.getFullYear()}`;
    }

    return{
        store,
        getFlags,
        getRule,
        getLogs,
        getApacheLogs,
        // Actions
        setRule,
        checkAnswer,
        VictoryFlag,
        randNum,
        randDate
    }
})