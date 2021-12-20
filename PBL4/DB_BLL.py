import DB
import SV
def GetData():
   query = "SELECT * FROM sinhvien;"
   data = DB.ExecuteQuery(query)
   return data
def DelSV(masv):
   query = "DELETE FROM sinhvien WHERE MSSV = '%s'"%(str(masv))
   data = DB.ExecuteNonQuery(query)
   return data
def AddSV(masv,tensv,urlsv):
   query = "insert into sinhvien values ('%s','%s',%s,'%s')"%(masv,tensv,False,urlsv)
   data = DB.ExecuteNonQuery(query)
   return data
def UpdateSV(masv,tensv,urlsv):
   query = "UPDATE doan.sinhvien SET TenSV ='%s' , imageURL = '%s' WHERE MSSV = '%s'"%(tensv,urlsv,masv)
   data = DB.ExecuteNonQuery(query)
   return data
def SearchSVs(text):
   query = " SELECT * FROM doan.sinhvien WHERE MSSV LIKE '%"+str(text)+"%'OR TenSV LIKE'%"+str(text)+"%'"
   data = DB.ExecuteQuery(query)
   return data
def CheckAttend(text):
   query = " SELECT * FROM doan.sinhvien WHERE MSSV LIKE '%"+str(text)+"%' AND DiemDanh = 1"
   data = DB.ExecuteQuery(query)
   return data
def ChangeAttendSV(masv,check):
   query = "UPDATE doan.sinhvien SET Diemdanh = %s WHERE MSSV = '%s'" % (check,masv)
   DB.ExecuteNonQuery(query)
def SearchSVByMSSV(masv):
   query = " SELECT * FROM doan.sinhvien WHERE MSSV = '%s' LIMIT 1" %(masv)
   data = DB.ExecuteQuery(query)
   sv = SV.ChangeToSV(data[0])
   return sv
def ResetDB():
   query = "UPDATE doan.sinhvien SET Diemdanh = 0"
   DB.ExecuteNonQuery(query)
def ChangeData(data):
   if(data != ""):
      list_sv = []
      for row in data:
         sv = SV.ChangeToSV(row)
         list_sv.append(sv)
      return list_sv
   return -1


