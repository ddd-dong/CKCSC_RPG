from script_player.scriptController import RPG_Script
from __init__ import script_finalgress

def show_old_script(team_all_progress:list,scriptName:str)->dict:
    '''team_progress 完整走過的劇情紀錄 ['1-0', '2-0', '3-2', '3-1', '4-0', '5-0', '6-0']\n 
    \nscriptName 正在跑的劇本名
    \nteam_progress_now 現在的進度
    '''
    team_progress_now = script_finalgress[scriptName]
    print(team_progress_now)
    _packScript = RPG_Script[scriptName].get_before(team_progress_now)

    _script = {}
    for i in team_all_progress:
        _chapter=list(map(int,i.split('-')))
        _script[i]= _packScript[str(_chapter[0])]['event'][_chapter[1]]["text"]
    return _script

def get_nextevent(script_all_progress:list,now_progress:dict)->dict:
    '''script_all_progress 完整的劇情紀錄 ['1-0', '2-0', '3-2', '3-1', '4-0', '5-0', '6-0']\n 
    \nprogress_now 正在更新的進度
    '''
    if script_all_progress.index(now_progress) >= len(script_all_progress)-1:
        return now_progress
    next_progress = script_all_progress[script_all_progress.index(now_progress)+1]
    return  next_progress
    