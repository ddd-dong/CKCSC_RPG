from flask import session
from bson import ObjectId
from __init__ import db


collection = db["token_rpg"]

class User(): 
    def __init__(self,_data:dict):
        self.token = _data["token"]
        self.privileges=_data["privileges"]
        self.data=_data
    
def isLogin()->dict:
    if session:
        return collection.find_one({"_id":ObjectId(session['user_id'])})
    return None

def loginState(_Rform)->str:
        if _Rform["token"] == "":
            return "Token欄位為空"
        _user = collection.find_one({"token":_Rform['token']})
        if not _user:
            return "帳號不存在"
        userN = User(_user)
        session['user_id']=str(userN.data["_id"])
        return None
            
def logoutAct()->None:
    session.clear()