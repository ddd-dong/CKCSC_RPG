const request_ajax = new XMLHttpRequest()
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

request_ajax.onload = function (){
    const responseScript = JSON.parse(request_ajax.response)
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

    console.log(request_ajax.responseText)
}
// request_ajax.open("POST","/api/script")
// request_ajax.send("兇靈線")
setInterval(()=>{
    request_ajax.open("POST",`/api/script?scriptName=${scriptName}&updateChapter=${scriptAllprogres[scriptAllprogres.length-1]}`, true)
    request_ajax.send()},3000)

// add_button.addEventListener("click",()=>{
//     request_ajax.open("POST",`/api/script?scriptName=${scriptName}&updateChapter=${scriptAllprogres[scriptAllprogres.length-1]}`, true)
//     // request_ajax.setRequestHeader('Content-type','application/json')
//     request_ajax.send("data=555")
// })