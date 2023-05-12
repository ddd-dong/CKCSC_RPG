const scriptSelect=document.querySelector('#first-select');
const progressSelect=document.querySelector('#second-select');
const teamselect = document.getElementById('team-select')
const actionselect = document.getElementById('action-select')
const showprogressbox = document.getElementById('show_progress')

console.log(allprogress_dict)
let allprogress = {} //{team:int,{scriptName:str,["1-0",.....]}}
let script_wholeprogress={}//{scriptName:str,["1-0",.....]}

for(let teami=0;teami<3;teami++){
    allprogress[teami]={}
    for(let _scriptN in allprogress_dict[teami]){
        allprogress[teami][_scriptN]=[]
        for(let _progress in allprogress_dict[teami][_scriptN] ){
            allprogress[teami][_scriptN].push(`${allprogress_dict[teami][_scriptN][_progress]['event']}-${allprogress_dict[teami][_scriptN][_progress]['choise']}`)
        }
    }
}

for(let _scriptN in script_wholeprogress_dict){
    script_wholeprogress[_scriptN]=[]
    for(let _progress in script_wholeprogress_dict[_scriptN] ){
        script_wholeprogress[_scriptN].push(`${script_wholeprogress_dict[_scriptN][_progress]['event']}-${script_wholeprogress_dict[_scriptN][_progress]['choise']}`)
    }
}

function show_progress(){
    for(let i=0;i<3;i++){
        const teambox = document.createElement('div')
        teambox.className += "teambox"
        teambox.innerHTML +=`<h3>${i}</h3>`
        for(let _scriptN in allprogress[i]){
            const scriptbox = document.createElement('div')
            scriptbox.className +="scriptbox"
            teambox.innerHTML +=`<h3>${_scriptN}</h3>`
            for(let _progress in allprogress[i][_scriptN]){
                const progress_p = document.createElement('p')
                progress_p.className += "progress_p"
                progress_p.innerHTML += `${allprogress[i][_scriptN][_progress]}`
                scriptbox.appendChild(progress_p)
            }
            teambox.appendChild(scriptbox)
        }
        showprogressbox.appendChild(teambox)
    }
}
show_progress()
actionselect.addEventListener('change',()=>{
    let options=[]
    if (actionselect.value == 'join'){
        options=script_wholeprogress[scriptSelect.value]
    }
    else{
        options=allprogress[teamselect.value][scriptSelect.value];
    }
    const html = options.map(option => `<option>${option}</option>`).join('');
    progressSelect.innerHTML = html;
})

scriptSelect.addEventListener('change',()=>{
    console.log(teamselect.value,scriptSelect.value)
    let options=[]
    if(actionselect.value == 'join'){
        options=script_wholeprogress[scriptSelect.value]
    }
    else{
        options=allprogress[teamselect.value][scriptSelect.value];
    }
    console.log(options)
    const html = options.map(option => `<option>${option}</option>`).join('');
    progressSelect.innerHTML = html;
});

teamselect.addEventListener('change',()=>{
    let options=[]
    if(actionselect.value == 'join'){
        options=script_wholeprogress[scriptSelect.value]
    }
    else{
        options=allprogress[teamselect.value][scriptSelect.value];
    }
    const html = options.map(option => `<option>${option}</option>`).join('');
    progressSelect.innerHTML = html;
});

