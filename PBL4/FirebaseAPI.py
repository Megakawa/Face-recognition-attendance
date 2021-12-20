from firebase import firebase  
from datetime import datetime
import pyrebase
import DB_BLL
def SendData(lb):
    sv = DB_BLL.SearchSVs(lb)
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d")
    current_time2 = now.strftime("%H:%M:%S")
    firebas = firebase.FirebaseApplication("https://diary-eb1a5-default-rtdb.asia-southeast1.firebasedatabase.app/",None)
    data = {
        'author':sv[0][1],
        'content':sv[0][0],
        'timestamp':current_time2
    }
    result = firebas.post("Attendance/"+current_time,data)
def RemoveData(lb,day_remove):
    sv = DB_BLL.SearchSVs(lb)
    now = datetime.now()
    firebaseconfig={'apiKey':'AIzaSyBnD-EflwrkXcBIifqQFqFQb3W46tTwlvA',
    'authDomain':'diary-eb1a5.firebaseapp.com',
    "databaseURL":'https://diary-eb1a5-default-rtdb.asia-southeast1.firebasedatabase.app',  
    "storageBucket":'diary-eb1a5.appspot.com'}
    fb=pyrebase.initialize_app(firebaseconfig)
    db=fb.database()
    days=db.child('Attendance/'+day_remove).get()
    for day in days.each():
        if (lb==day.val()["content"]):
            db.child('Attendance').child(day_remove).child(day.key()).remove()

def GetData():
    firebaseconfig={'apiKey':'AIzaSyBnD-EflwrkXcBIifqQFqFQb3W46tTwlvA',
    'authDomain':'diary-eb1a5.firebaseapp.com',
    "databaseURL":'https://diary-eb1a5-default-rtdb.asia-southeast1.firebasedatabase.app',  
    "storageBucket":'diary-eb1a5.appspot.com'}
    fb=pyrebase.initialize_app(firebaseconfig)
    db=fb.database()
    List_day=[]
    days=db.child('Attendance').get()
    for day in days.each():
        List_day.append(day.key())
    return List_day
def GetDataForDay(day):
    firebaseconfig={'apiKey':'AIzaSyBnD-EflwrkXcBIifqQFqFQb3W46tTwlvA',
    'authDomain':'diary-eb1a5.firebaseapp.com',
    "databaseURL":'https://diary-eb1a5-default-rtdb.asia-southeast1.firebasedatabase.app',  
    "storageBucket":'diary-eb1a5.appspot.com'}
    fb=pyrebase.initialize_app(firebaseconfig)
    db=fb.database()
    List_SV=[]
    days=db.child('Attendance/'+day).get()
    for sv in days.each():
        List_SV.append(sv.val()["content"])
    return List_SV
def SendDataWithDay(lb,day):
    sv = DB_BLL.SearchSVs(lb)
    now = datetime.now()
    current_time2 = now.strftime("%H:%M:%S")
    firebas = firebase.FirebaseApplication("https://diary-eb1a5-default-rtdb.asia-southeast1.firebasedatabase.app/",None)
    data = {
        'author':sv[0][1],
        'content':sv[0][0],
        'timestamp':current_time2
    }
    result = firebas.post("Attendance/"+day,data)

