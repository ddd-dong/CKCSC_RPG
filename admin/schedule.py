from admin.progressController import progress_tracker 

def getteamsprogress(teamNumber:int=3)->dict:
    '''
    所有隊伍的目前進度，結構:{隊伍:str,進度:dict}
    '''
    _ALLprogress = {}
    for i in range(teamNumber):
        _ALLprogress[str(i)]=progress_tracker.get_progress(i)
    return _ALLprogress

def getAllteam_Allprogress(teamNumber:int=3)->dict:
    '''
    所有隊伍目前的所有進度，結構:{隊伍:str,全進度:dict}
    '''
    _ALLprogress = {}
    for i in range(teamNumber):
        _ALLprogress[str(i)]=progress_tracker.get_all_progress(i)
    return _ALLprogress

# print(getAllteamprogress(),getAllteam_Allprogress())