from flask import Blueprint, render_template,redirect,url_for,request
from login.user import isLogin,loginState,logoutAct
app_route = Blueprint('loginsystem',__name__)



@app_route.route('/users')
def userPage(): 
    _LoginUser_infomation = isLogin()
    if _LoginUser_infomation:
        return render_template('userPage.html',userN = _LoginUser_infomation)
    return redirect(url_for('loginsystem.login'))

@app_route.route('/login',methods=['GET','POST'])
def login():
    if request.method!='POST':
        if isLogin():
            return redirect(url_for('loginsystem.userPage'))
        return render_template('login.html')
    
    _loginErro = loginState(request.form)
    if _loginErro:
        return render_template('login.html',login_m=_loginErro)
    return redirect(url_for('loginsystem.userPage'))


@app_route.route('/logout')
def logout():
    logoutAct()
    return redirect(url_for('index'))