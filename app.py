from flask import Flask, render_template,request,url_for,redirect,flash,session,Blueprint
from login.loginsystem import app_route as loginsystem
from script_player.scriptsystem import app_route as scriptsystem
from admin.adminsystem import app_route as adminsystem

app = Flask(__name__)
app.config['SECRET_KEY']= 'ddd'

app.register_blueprint(loginsystem)
app.register_blueprint(scriptsystem,url_prefix='')
app.register_blueprint(adminsystem)


@app.route('/')
def index():
    return render_template('home.html')




if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port="8080")
    
    