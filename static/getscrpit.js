// const request_ajax = new XMLHttpRequest()
// const add_button = document.getElementById("add_button")
let add_count = 0
let scriptAllprogres =[]

for(let _progress in scriptAllprogress_dict ){
    console.log(`${scriptAllprogress_dict[_progress]['event']}-${scriptAllprogress_dict[_progress]['choise']}`)
    scriptAllprogres.push(`${scriptAllprogress_dict[_progress]['event']}-${scriptAllprogress_dict[_progress]['choise']}`)
}

function typing(ele_text_p,Stext,count,delay){
    if (count>=Stext.length){
       return
    }
    ele_text_p.innerHTML+=Stext[count];
    setTimeout(typing ,delay,ele_text_p,Stext,count+1)
}

/**
 * send fetch POST method
 * 
 * @param {dictionary} _data 要傳送的資料
 * @param {string} _path 發送路徑
 * @param {function}  _fu 收到response後執行的function
 */
function send_fetch(_data,_path,_fu){
    fetch(_path,{ 
        method: "POST",
        headers:{
            'Content-Type': "application/json"
        },
        body:JSON.stringify(_data)
    })
        .then((response) =>{
            console.log(response)
            if (response.status >= 200 && response.status < 300) {
                return response.json();
            } else {
                var error = new Error(response.statusText)
                error.response = response; 
                throw error;
            }
        })
        .then((data)=>{
            _fu(data);
        })
        .catch((erro)=>{
            console.log('Erro:',erro)
            return erro.response.json()
        });
}

// request_ajax.onload = function (){
//     const responseScript = JSON.parse(request_ajax.response)
//     console.log(responseScript)
//     console.log("AAA")
//     if(responseScript['chapter'] == scriptAllprogres[scriptAllprogres.length-1]){
//         console.log('same')
//         return
//     }
//     if(responseScript['chapter'] == undefined){
//         console.log(undefined)
//         return
//     }
//     const text_div = document.createElement('div')
//     const text_p = document.createElement('p')
//     const text_title = document.createElement('h3')
//     text_div.id = `text${add_count}`
//     text_title.className = 'chapter'
//     // text_p.innerText = responseScript['text']
//     text_title.innerHTML = responseScript['chapter']
//     text_div.appendChild(text_title)
//     text_div.appendChild(text_p)
//     text_box.appendChild(text_div)
//     scriptAllprogres.push(responseScript['chapter'])
//     typing(text_p,responseScript['text'],0,2000)

//     console.log(request_ajax.responseText)
// }
// request_ajax.open("POST","/api/script")
// request_ajax.send("兇靈線")
// setInterval(()=>{
//     request_ajax.open("POST",`/api/script?scriptName=${scriptName}&updateChapter=${scriptAllprogres[scriptAllprogres.length-1]}`, true)
//     request_ajax.send()},3000)
setInterval(()=>{send_fetch({'scriptName':scriptName,'updateChapter':scriptAllprogres[scriptAllprogres.length-1]}
,"/api/script",(responseScript)=>{
    console.log(responseScript)
    console.log("AAA")
    if(responseScript['chapter'] == scriptAllprogres[scriptAllprogres.length-1]){
        console.log('same')
        return
    }
    if(responseScript['chapter'] == undefined){
        console.log(undefined)
        return
    }
    const text_div = document.createElement('div')
    const text_p = document.createElement('p')
    const text_title = document.createElement('h3')
    text_div.id = `text${add_count}`
    text_title.className = 'chapter'
    // text_p.innerText = responseScript['text']
    text_title.innerHTML = responseScript['chapter']
    text_div.appendChild(text_title)
    text_div.appendChild(text_p)
    text_box.appendChild(text_div)
    scriptAllprogres.push(responseScript['chapter'])
    typing(text_p,responseScript['text'],0,2000)
})},2000)
// add_button.addEventListener("click",()=>{
//     request_ajax.open("POST",`/api/script?scriptName=${scriptName}&updateChapter=${scriptAllprogres[scriptAllprogres.length-1]}`, true)
//     // request_ajax.setRequestHeader('Content-type','application/json')
//     request_ajax.send("data=555")
// })