# ckcsc RPG網頁

![系統架構圖](markdown/system_structure.png)

## 目錄


````
│   README.md               說明書
│   __init__.py             初始化(全域變數)
│   app.py                  啟動
│   requirements.txt        環境要求
│   
└───static                  css/js
│   │  main.css              
│   │  getscript.js        show_script.html 中用於取得劇本(ajax)
│   │  schedule.js         control_schedule.html 中用於顯示目前各小隊進度與調整表單內容
│   │  showscript.js       show_script.html 中用於調整後端傳來的劇本格式
│ 
└───templates               html
│   │  home.html            登入系統的主頁
│   │  login.html           登入頁面
│   │  useerPage.html       登入系統登入後顯示的頁面
│   │  show_script.html     顯示劇本給player
│   │  choose_script.html   顯示劇本的主頁，用於選擇劇本
│   │  control_schedule.html用於供admin管理各小隊進度
│   │  rpg_script.html      沒用到，測試用
│   │  The_progress_of_each_group.html 尚未實現功能，顯示各組進度
│ 
└───RPGscript               存放RPG劇本
│   ...
│
└───markdown                README用圖片
│   ...
│
└───script_player           對player部分系統
│   │   scriptControlter.py 劇本調用系統
│   │   scriptsystem.py     與player有關的route
│   │   showscript.py       與顯示劇本相關function
│ 
└───admin                   與admin有關系統
│   │   adminsystem.py      與admin有關的route
│   │   progressController.py 管理各小隊進度
│   │   schedule.py         進度管理相館function(格式轉換)
│
└───login
│   │   loginsystem.py      與登入有關的route
│   │   user.py             與登入有關的function
│
````
## Function規範

### 進度管理
* 查詢進度  (名子可以改)
```
名子: get_all_team_all_progress
功能: 取得所有的進度(進度的歷程)
輸入: -
輸出: [{隊伍0:str,全進度:dict},{隊伍1:str,全進度:dict}...]
```
```
名子: get_all_team_new_progress
功能: 取得所有player的最新的進度
輸入: -
輸出: [{隊伍0:str,最新進度:dict},{隊伍1:str,最新進度:dict}...]
```
```
名子: get_self_team_new_progress
功能: 取得該player的最新的進度
輸入: player小隊
輸出: {'event': 1, 'choise': 0}
```
```
名子: get_self_team_all_progress
功能: 取得該player的全部的進度
輸入: player小隊
輸出: {'兇靈線': ['1-0'], 'ㄎㄎ長線': ['1-0'], '大學長線': ['1-0'], '李日凱線': ['1-0', '2-0', '3-2', '3-1', '4-0', '5-0', '6-0'], '巫師線': ['1-0', '2-0']}
```
* 刪除進度
```
名子: delete
功能: 刪除該player小隊在該劇本的某個進度
輸入: player小隊、劇本名、欲刪除的進度
輸出: -
```
* 新增進度
```
名子: join
功能: 新增該player小隊在該劇本的某個進度
輸入: player小隊、劇本名、欲新增的進度
輸出: 是否成功增加 ex. success push '14' into line 巫師線
```
* 其他
```
名子: total
功能: 查詢完成度
輸入: player小隊
輸出: ["line '兇靈線' done0.0%", "line 'ㄎㄎ長線' done0.0%", "line '大學長線' done0.0%", "line '李日凱線' done0.0%", "line '巫師線' done0.0%"]
```


## 更新
### 已完成
* rwd
* ajax改為fetch
* 改進進度管理系統
* 增加兼容性(可適用其他劇本)
* longin與rpg系統整合
* 管理頁面使用ajax
* 完成度頁面
### 待完成
* 把劇本放到資料庫
