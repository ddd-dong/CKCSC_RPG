from flask import Blueprint, render_template,redirect,url_for,request
from admin.progressController import progress_tracker 
from admin.schedule import getAllteam_Allprogress
from login.user import isLogin
from __init__ import script_wholeprogress
import json

app_route = Blueprint('adminsystem',__name__,static_folder='static', static_url_path='/static')

'''__測試用__'''

progress_tracker.update_team_progress(0,"join",{"event":1,"choise":0},"兇靈線")
progress_tracker.update_team_progress(0,"join",{"event":1,"choise":0},"巫師線")
progress_tracker.update_team_progress(0,"join",{"event":1,"choise":0},"ㄎㄎ長線")
progress_tracker.update_team_progress(0,"join",{"event":1,"choise":0},"大學長線")
progress_tracker.update_team_progress(0,"join",{"event":1,"choise":0},"李日凱線")

progress_tracker.update_team_progress(1,"join",{"event":1,"choise":0},"兇靈線")
progress_tracker.update_team_progress(1,"join",{"event":1,"choise":0},"巫師線")
progress_tracker.update_team_progress(1,"join",{"event":1,"choise":0},"ㄎㄎ長線")
progress_tracker.update_team_progress(1,"join",{"event":1,"choise":0},"大學長線")
progress_tracker.update_team_progress(1,"join",{"event":1,"choise":0},"李日凱線")

progress_tracker.update_team_progress(2,"join",{"event":1,"choise":0},"兇靈線")
progress_tracker.update_team_progress(2,"join",{"event":1,"choise":0},"巫師線")
progress_tracker.update_team_progress(2,"join",{"event":1,"choise":0},"ㄎㄎ長線")
progress_tracker.update_team_progress(2,"join",{"event":1,"choise":0},"大學長線")
progress_tracker.update_team_progress(2,"join",{"event":1,"choise":0},"李日凱線")
'''__________'''

@app_route.route("/schedule")
def control_schedule():
    _LoginUser_infomation = isLogin()
    if not _LoginUser_infomation:
        return redirect(url_for('loginsystem.login'))
    if _LoginUser_infomation["privileges"]!="admin":
        return redirect(url_for('scriptsystem.rpg_main'))
    _ap = getAllteam_Allprogress()
    return render_template("control_schedule.html",allprogress = json.dumps(_ap),script_wholeprogress=json.dumps(script_wholeprogress))


@app_route.route("/api/Receive_and_update",methods = ["GET","POST"])
def Receive_and_update():
    if request.method!='POST':
        return redirect(url_for('adminsystem.control_schedule'))
    if (not request.values['select_team'].isdigit()) or request.values['join_delete'] == '加入進度還是移出進度' or request.values['select_team'] == '請選擇小分隊'\
    or request.values['plot_line'] == '請選擇當前劇情線' or request.values['level']==None:
        return redirect(url_for('adminsystem.control_schedule'))
    print(request.values)
    join_delete=str(request.values['join_delete'])
    select_team=int(request.values['select_team'])
    plot_line=str(request.values['plot_line'])
    event,choise=map(int,request.values['level'].split("-"))
    modified_progress={"event":event,"choise":choise}
    if join_delete=="join":
        progress_tracker.join(select_team,modified_progress,plot_line)
    elif join_delete=="delete":
        progress_tracker.delete(select_team,modified_progress,plot_line)
    return redirect(url_for('adminsystem.control_schedule'))
    
