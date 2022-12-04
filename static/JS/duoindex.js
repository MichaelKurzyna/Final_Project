$(document).ready(function () {
    let ranks = [
            {
            "name": "IRON I",
            "num": 0
            },
            {
            "name": "IRON II",
            "num": 1
            },
            {
            "name": "IRON III",
            "num": 2
            },
            {
            "name": "BRONZE I",
            "num": 3
            },
            {
            "name": "BRONZE II",
            "num": 4
            },
            {
            "name": "BRONZE III",
            "num": 5
            },
            {
            "name": "SILVER I",
            "num": 6
            },
            {
            "name": "SILVER II",
            "num": 7
            },
            {
            "name": "SILVER III",
            "num": 8
            },
            {
            "name": "GOLD I",
            "num": 9
            },{
            "name": "GOLD II",
            "num": 10
            },{
            "name": "GOLD III",
            "num": 11
            },{
            "name": "PLATINUM I",
            "num": 12
            },
            {
            "name": "PLATINUM II",
            "num": 13
            },
            {
            "name": "PLATINUM III",
            "num": 14
            },
            {
            "name": "DIAMOND I",
            "num": 15
            },
            {
            "name": "DIAMOND II",
            "num": 16
            },
            {
            "name": "DIAMOND III",
            "num": 17
            },
            {
            "name": "ASCENDANT I",
            "num": 18
            },
            {
            "name": "ASCENDANT II",
            "num": 19
            },
            {
            "name": "ASCENDANT III",
            "num": 20
            },
            {
            "name": "IMMORTAL I",
            "num": 21
            },
            {
            "name": "IMMORTAL II",
            "num": 22
            },
            {
            "name": "IMMORTAL III",
            "num": 23
            },
            {
            "name": "RADIANT",
            "num": 24
            }
        ]
    let agents = [
            {
            "name": "Brimstone",
            "num": 0
            },
            {
            "name": "Pheonix",
            "num": 1
            },
            {
            "name": "Sage",
            "num": 2
            },
            {
            "name": "Sova",
            "num": 3
            },
            {
            "name": "Viper",
            "num": 4
            },
            {
            "name": "Cypher",
            "num": 5
            },
            {
            "name": "Reyna",
            "num": 6
            },
            {
            "name": "Killjoy",
            "num": 7
            },
            {
            "name": "Breach",
            "num": 8
            },
            {
            "name": "Omen",
            "num": 9
            },{
            "name": "Jett",
            "num": 10
            },{
            "name": "Raze",
            "num": 11
            },{
            "name": "Skye",
            "num": 12
            },
            {
            "name": "Yoru",
            "num": 13
            },
            {
            "name": "Astra",
            "num": 14
            },
            {
            "name": "Kayo",
            "num": 15
            },
            {
            "name": "Chamber",
            "num": 16
            },
            {
            "name": "Neon",
            "num": 17
            },
            {
            "name": "Fade",
            "num": 18
            },
            {
            "name": "Harbor",
            "num": 19
            }
        ]
    //update rank picture
    $('.rank').each(function (){
        let thisrank = ($(this).attr('id'));
        let foundrank = ranks.find(rank => rank.name === thisrank);
        let number = foundrank.num;
        $(this).attr('src', images[number]);
    })
    //update agent pictures
    $('.agents').each(function (){
        let thisagent = ($(this).attr('id'));
        let agentArray = thisagent.split(",");
        let arrayLength = agentArray.length;
        //create array with list of agents to produce images equal to number of agents selected
        if (arrayLength === 1){
            let foundagent = agents.find(agent => agent.name === agentArray[0]);
            let number = foundagent.num;
            $(this).attr('src', agentsimages[number]);
        }
        if (arrayLength > 1){
            for (let i = 0; i < arrayLength; i++){
                    if (i === 0){
                        //Get first agent and trim excess character such as [] '' to match with array values
                        let thisagent = agentArray[0].slice(1);
                        thisagent = thisagent.slice(1,-1);
                        let foundagent = agents.find(agent => agent.name === thisagent);
                        let number = foundagent.num;
                        $(this).append($('<img>', {src: agentsimages[number], alt: foundagent.name}));
                    }
                    else if (i === (arrayLength - 1)){
                        //Get last agent and trim excess character such as [] '' to match with array values
                        let thisagent = agentArray[i].slice(2,-2);
                        let foundagent = agents.find(agent => agent.name === thisagent);
                        let number = foundagent.num;
                        $(this).append($('<img>', {src: agentsimages[number], alt: foundagent.name}));
                    }
                    else{
                        //Get current iterated agent and trim excess character such as [] '' to match with array values
                        let curragent = agentArray[i];
                        if (curragent.charAt(1) === "'"){
                             let current = agentArray[i].slice(2, -1);
                             let foundagent = agents.find(agent => agent.name === current);
                             let number = foundagent.num;
                             $(this).append($('<img>', {src: agentsimages[number], alt: foundagent.name}));
                        }
                        else {
                             let foundagent = agents.find(agent => agent.name === agentArray[i]);
                             let number = foundagent.num;
                             $(this).append($('<img>', {src: agentsimages[number], alt: foundagent.name}));
                        }

                    }

            }
        }
    })
})