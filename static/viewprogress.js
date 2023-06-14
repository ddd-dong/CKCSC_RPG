const progress_box = document.getElementById('progress_box');
let old_data;

function show_total(_data){
    progress_box.innerHTML=''
    for(let _team in _data){
        progress_box.innerHTML +=`<h1>${_team}小進度</h1>`
        let _inn_html='';
        for(let _script in _data[_team]){
            _inn_html +=`<div class="progress-label">
            ${_script}&nbsp;&nbsp;&nbsp;完成度:${_data[_team][_script]}%
        </div>
        <div class="progress-bar-container">
            <div class="progress">
                <div class="progress-bar" role="progressbar" style="width: ${_data[_team][_script]}%; background-color: rgb(136, 136, 136)"></div>
            </div>
        </div>`
        }
        progress_box.innerHTML += '<div class="container">'+_inn_html+'</div>'
    }
}

        
setInterval(send_fetch('',update_progress_path,(_data)=>{
    if (old_data === _data){
        console.log('same');
        return
    }
    console.log(_data)
    show_total(_data);
}))