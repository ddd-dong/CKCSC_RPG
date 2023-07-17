
/**
 * send fetch POST method
 * 
 * @param {dictionary} _data 要傳送的資料
 * @param {string} _path 發送路徑
 * @param {function}  _fu 收到response後執行的function, imput一個responsedata
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
            // console.log(response)
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





