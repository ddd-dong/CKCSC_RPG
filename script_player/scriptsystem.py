from flask import Blueprint, render_template,redirect,url_for,request
from login.user import isLogin
from script_player.scriptController import RPG_Script
from script_player.showscript_player import show_old_script,get_nextevent
from admin.progressController import progress_tracker 
import json
app_route = Blueprint('scriptsystem',__name__,static_folder='static', static_url_path='/static')

'''__測試用__'''
# player_progress = {'ㄎㄎ長線':2, '兇靈線':8, '大學長線':6, '巫師線':5, '李日凱線':0}
# player_all_progress = {
# '兇靈線':[{"event":1,"choise":0}, {"event":2,"choise":0}, {"event":3,"choise":0}, {"event":4,"choise":0}, {"event":5,"choise":0}, {"event":6,"choise":0}, {"event":7,"choise":1}, {"event":8,"choise":0}]
# }

''''''

@app_route.route('/dashboard')
def dashboard():
    return render_template("The_progress_of_each_group.html")

@app_route.route('/rpg')
def rpg_main():
    _LoginUser_infomation = isLogin()
    if not _LoginUser_infomation:
        return redirect(url_for('loginsystem.login'))
    return render_template('choose_script.html',userN = _LoginUser_infomation)

@app_route.route('/rpg/show/<scriptName>')
def rpg_showscript(scriptName:str):
    _LoginUser_infomation = isLogin()
    if not _LoginUser_infomation:
        return redirect(url_for('loginsystem.login'))
    if _LoginUser_infomation["privileges"]=="admin":
        return redirect(url_for('scriptsystem.rpg_main'))
    if not _LoginUser_infomation['privileges'].isdigit():
        print(_LoginUser_infomation)
        return "你4誰"
    _teamN = int(_LoginUser_infomation['privileges'])
    # print(progress_tracker.get_all_progress(1))
    # print(_teamN,progress_tracker.get_all_progress(_teamN))
    _old_script=show_old_script(progress_tracker.get_all_progress(_teamN)[scriptName],scriptName,progress_tracker.get_progress(_teamN)[scriptName]['event'])
    # print(progress_tracker.get_all_progress(_teamN)[scriptName])
    return render_template("show_script.html",scriptName=scriptName,old_script=json.dumps(_old_script),
                           scriptAllprogress = json.dumps(progress_tracker.get_all_progress(_teamN)[scriptName]))

@app_route.route("/api/script",methods = ["POST"])
def returnScript():
    _LoginUser_infomation = isLogin()
    if not _LoginUser_infomation['privileges'].isdigit():
        print(_LoginUser_infomation)
        return {"text":f"ERRO:{_LoginUser_infomation} is not intable",
        "chapter":"0-0"
        }
    
    _teamN = int(_LoginUser_infomation['privileges'])
    # print(request.args)
    scriptName = request.args['scriptName']
    # print(request.args['updateChapter'].split('-'))
    updateChapter =  {'event':int(request.args['updateChapter'].split('-')[0]),'choise':int(request.args['updateChapter'].split('-')[1])}
    updateChapter = get_nextevent(progress_tracker.get_all_progress(_teamN)[scriptName],updateChapter)
    # print(updateChapter,f"{updateChapter['event']}-{updateChapter['choise']}")
    # print(RPG_Script[scriptName].get_act(updateChapter['event']).get_event(updateChapter['choise']))
    return {"text":RPG_Script[scriptName].get_act(updateChapter['event']).get_event(updateChapter['choise']).text,
            "chapter": f"{updateChapter['event']}-{updateChapter['choise']}"}





