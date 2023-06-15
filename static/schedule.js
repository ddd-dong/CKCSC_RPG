const scriptSelect=document.querySelector('#first-select');
const progressSelect=document.querySelector('#second-select');
const teamselect = document.getElementById('team-select');
const actionselect = document.getElementById('action-select');
const showprogressbox = document.getElementById('show_progress');
const schedule_form = document.getElementById('schedule_form');
const submit_button  = document.getElementById('submit_button');
let allprogress;
function show_progress(){
    showprogressbox.innerHTML=''
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
function updateProgress(){
    send_fetch('',progress_path,(_data)=>{
        allprogress=_data;
        show_progress();
    })
}


setInterval(updateProgress,1000)

// 發送表單
submit_button.onclick = ()=>{
    let _data={}
    for(let i = 0;i<schedule_form.length;i++){
        console.log(schedule_form[i].name)
        _data[schedule_form[i].name]=schedule_form[i].value
    }
    console.log(_data)
    send_fetch(_data,update_path,(response)=>{
        console.log(response)
        alert(response);
    })
}

// 選單變化
/*
Cannot read properties of undefined (reading 'map')
這個erro只是更新的時候會發生teamselect.value或其他選項還是預設值(ex.'請選擇當前劇情線')而已，
理論上不會出什麼問題
*/
actionselect.addEventListener('change',()=>{
    progressSelect.innerHTML =''
    let options=[]
    if (actionselect.value == 'join'){
        options=script_wholeprogress[scriptSelect.value]
    }
    else{
        options=allprogress[teamselect.value][scriptSelect.value];
    }
    const html = options.map(option => `<option>${option}</option>`).join('');
    console.log(html)
    progressSelect.innerHTML = html;
})

scriptSelect.addEventListener('change',()=>{
    // console.log(teamselect.value,scriptSelect.value)
    progressSelect.innerHTML =''
    let options=[]
    if(actionselect.value == 'join'){
        options=script_wholeprogress[scriptSelect.value]
    }
    else{
        options=allprogress[teamselect.value][scriptSelect.value];
    }
    // console.log(options)
    const html = options.map(option => `<option>${option}</option>`).join('');
    progressSelect.innerHTML = html;
});

teamselect.addEventListener('change',()=>{
    progressSelect.innerHTML =''
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

