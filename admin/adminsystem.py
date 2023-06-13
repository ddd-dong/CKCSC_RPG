from flask import Blueprint, render_template,redirect,url_for,request,jsonify
from admin.progressController import progress_tracker 
from admin.schedule import requestcheck
from login.user import isLogin
from __init__ import script_wholeprogress,teamNumber
import json

app_route = Blueprint('adminsystem',__name__,static_folder='static', static_url_path='/static')


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

@app_route.route("/api/Receive_and_update",methods = ["POST"])
def Receive_and_update():

    _input_message = requestcheck(request.get_json())
    
    return jsonify(_input_message['message'])
    
@app_route.route('/api/update_progress',methods=["POST"])
def update_realtime_progress():
    return jsonify(progress_tracker.get_all_team_all_progress())