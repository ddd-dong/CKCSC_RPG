from admin.progressController import progress_tracker 
from login.user import isLogin

# def getteamsprogress(teamNumber:int=3)->dict:
#     '''
#     所有隊伍的目前進度，結構:{隊伍:str,進度:dict}
#     '''
#     _ALLprogress = {}
#     for i in range(teamNumber):
#         _ALLprogress[str(i)]=progress_tracker.get_progress(i)
#     return _ALLprogress

# def getAllteam_Allprogress(teamNumber:int=3)->dict:
#     '''
#     所有隊伍目前的所有進度，結構:{隊伍:str,全進度:dict}
#     '''
#     _ALLprogress = {}
#     for i in range(teamNumber):
#         _ALLprogress[str(i)]=progress_tracker.get_all_progress(i)
#     return _ALLprogress

def progress_update(request_values)->dict:
    '''
    管理對進度的操作，並回傳推送狀態訊息
    '''
    join_delete=str(request_values['join_delete'])
    select_team=int(request_values['select_team'])
    plot_line=str(request_values['plot_line'])
    modified_progress=str(request_values['level'])
    if join_delete=="join":
        _message = progress_tracker.join(select_team,modified_progress,plot_line)
    elif join_delete=="delete":
        _message = progress_tracker.delete(select_team,modified_progress,plot_line)
    return _message

def requestcheck(request_values)->dict:
    '''
    回復和檢查request
    '''
    if not isLogin():
        return {'state':False,'message':'未登入'}
    if not request_values['select_team'].isdigit() or request_values['join_delete'] == '加入進度還是移出進度' or request_values['select_team'] == '請選擇小分隊'\
    or request_values['plot_line'] == '請選擇當前劇情線' or request_values['level']==None or (request_values['join_delete']!="join" and\
        request_values['join_delete']!="delete"):
        return {'state':False,'message':'請完整填寫表單'}
    
    if request_values['level']=='1-0' and request_values['join_delete']=="delete":
        return {'state':False,'message':'不可刪除1-0'}
    
    return {'state':True,'message':progress_update(request_values)}
