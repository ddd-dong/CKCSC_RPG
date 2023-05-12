const text_box = document.getElementById("showscript")

function load_old_script(_script_long,_script){
    let Selement = []
    let count=0
    for(let i in _script){
        Selement.push(document.createElement('div'))
        Selement[count].id = `text${count}`
        const text_p = document.createElement('p')
        const text_title = document.createElement('h3')
        text_title.className = 'chapter'
        text_p.innerHTML = `${_script[i]}`
        text_title.innerHTML = `${i}`
        Selement[count].appendChild(text_title)
        Selement[count].appendChild(text_p)
        
        text_box.appendChild(Selement[count])
        // typing(text_p,_script[i],0,1000)
        count +=1
    }
}



load_old_script(old_script.length,old_script)