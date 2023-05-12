from script_player.scriptController import RPG_Script
from __init__ import script_finalgress

def show_old_script(team_all_progress:list,scriptName:str,team_progress_now:int)->dict:
    '''team_progress 完整走過的劇情紀錄 ["event":事件,"choise":選擇(無分支為0)]\n 
    \nscriptName 正在跑的劇本名
    \nteam_progress_now 現在的進度
    '''
    # [["event":1,"choise":0], ["event":2,"choise":0], ["event":3,"choise":0], ["event":4,"choise":0], ["event":5,"choise":0], ["event":6,"choise":0], ["event":7,"choise":0], ["event":8,"choise":1]] 
    team_progress_now = script_finalgress[scriptName]
    _packScript = RPG_Script[scriptName].get_before(team_progress_now)
    _script = {}
    for i in team_all_progress:
        # print(_packScript)
        # print(i["event"])
        # print(_packScript[str(i["event"])],_packScript[str(i["event"])]['event'],i["choise"])
        # print(_packScript[str(i["event"])]['event'][i["choise"]]["text"])
        _script[f"{i['event']}-{i['choise']}"]= _packScript[str(i["event"])]['event'][i["choise"]]["text"]
    return _script

def get_nextevent(script_all_progress:list,now_progress:dict)->dict:
    '''script_all_progress 完整的劇情紀錄 ["event":事件,"choise":選擇(無分支為0)]\n 
    \nprogress_now 正在更新的進度
    '''
    if script_all_progress.index(now_progress) >= len(script_all_progress)-1:
        return now_progress
    next_progress = script_all_progress[script_all_progress.index(now_progress)+1]
    return  next_progress
    