from flask import Blueprint, render_template,redirect,url_for,request
from admin.progressController import progress_tracker 
from admin.schedule import getAllteam_Allprogress
from login.user import isLogin
from __init__ import script_wholeprogress,teamNumber
import json

app_route = Blueprint('adminsystem',__name__,static_folder='static', static_url_path='/static')

'''__init__'''

# progress_tracker.join(0,'1-0',"兇靈線")
# progress_tracker.join(0,'1-0',"巫師線")
# progress_tracker.join(0,'1-0',"ㄎㄎ長線")
# progress_tracker.join(0,'1-0',"大學長線")
# progress_tracker.join(0,'1-0',"李日凱線")
# progress_tracker.join(1,'1-0',"兇靈線")
# progress_tracker.join(1,'1-0',"巫師線")
# progress_tracker.join(1,'1-0',"ㄎㄎ長線")
# progress_tracker.join(1,'1-0',"大學長線")
# progress_tracker.join(1,'1-0',"李日凱線")
# progress_tracker.join(2,'1-0',"兇靈線")
# progress_tracker.join(2,'1-0',"巫師線")
# progress_tracker.join(2,'1-0',"ㄎㄎ長線")
# progress_tracker.join(2,'1-0',"大學長線")
# progress_tracker.join(2,'1-0',"李日凱線")
'''__________'''

@app_route.route("/schedule")
def control_schedule():
    _LoginUser_infomation = isLogin()
    if not _LoginUser_infomation:
        return redirect(url_for('loginsystem.login'))
    if _LoginUser_infomation["privileges"]!="admin":
        return redirect(url_for('scriptsystem.rpg_main'))
    _ap = progress_tracker.get_all_team_all_progress()
    print(_ap)
    return render_template("control_schedule.html",allprogress = json.dumps(_ap),script_wholeprogress=json.dumps(script_wholeprogress),teamNumber=teamNumber)


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
    modified_progress=str(request.values['level'])
    if join_delete=="join":
        print(progress_tracker.join(select_team,modified_progress,plot_line))
    elif join_delete=="delete":
        progress_tracker.delete(select_team,modified_progress,plot_line)
    return redirect(url_for('adminsystem.control_schedule'))

