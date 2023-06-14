from flask import Flask, render_template,request,url_for,redirect,flash,session,Blueprint
from login.loginsystem import app_route as loginsystem,isLogin
from script_player.scriptsystem import app_route as scriptsystem
from admin.adminsystem import app_route as adminsystem

app = Flask(__name__)
app.config['SECRET_KEY']= 'ddd'

app.register_blueprint(loginsystem)
app.register_blueprint(scriptsystem,url_prefix='')
app.register_blueprint(adminsystem)


@app.route('/')
def index():
    _LoginUser_infomation = isLogin()
    if not _LoginUser_infomation:
        return redirect(url_for('loginsystem.login'))
    if _LoginUser_infomation['privileges'] == 'admin':
        return render_template('userPage.html',userN = _LoginUser_infomation)
    return redirect(url_for('scriptsystem.rpg_main'))




if __name__=="__main__":
    app.run(debug=True,port="8080") #,host="0.0.0.0"
    
    