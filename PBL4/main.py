import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QFileDialog
from imutils.video import VideoStream
import cv2
import MainForm
from MainForm import Ui_MainWindow
import ctypes
import DB_BLL
import SV
import os
import shutil
import AI
import FirebaseAPI

class MainWindow:
    chedo = 0
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.ShowData_Date()
        self.uic.btn_Delete.clicked.connect(self.DeleteSV)
        self.uic.btn_Show.clicked.connect(self.ShowData)
        self.uic.btn_Add.clicked.connect(self.Addform)
        self.uic.btn_Save.clicked.connect(self.AddorUpdate)
        self.uic.TV_student.clicked.connect(self.Binding)
        self.uic.btn_Search.clicked.connect(self.ShowData)
        self.uic.btn_attend.clicked.connect(self.ChangeAttendSV)
        self.uic.btn_addimage.clicked.connect(self.ChooseImage)
        self.uic.OpenCamera.clicked.connect(self.OpenCamera)
        self.uic.btnShow.clicked.connect(self.ShowData_Date)

    def ShowData_Date(self):
        day = self.uic.dateEdit.date().toString('yyyy-MM-dd')
        List_day = FirebaseAPI.GetData()
        DB_BLL.ResetDB()
        if day in List_day:
            List_SV = FirebaseAPI.GetDataForDay(day)
            for i in List_SV:
                DB_BLL.ChangeAttendSV(i,1)
        else:
            DB_BLL.ResetDB()
        self.ShowData()
    def OpenCamera(self):
        AI.run_camera()
    def show(self):
        self.main_win.show()
    def ShowData(self):
        text = self.uic.tv_search.toPlainText()
        if(text == ''):
            data = DB_BLL.GetData()
        else:
            data = DB_BLL.SearchSVs(self.uic.tv_search.toPlainText())
        self.uic.LoadDataTable(data)
        self.uic.TV_student.selectRow(1)
    def DeleteSV(self):
        item = self.uic.TV_student.selectedItems()
        if(ctypes.windll.user32.MessageBoxW(0, "Bạn có xác định xóa sinh viên "+item[1].text(), "Cảnh báo", 1) == 1):
            check = DB_BLL.DelSV(item[0].text())
            if(check == 0): ctypes.windll.user32.MessageBoxW(0, " Xóa không thành công ", "Thông báo", 0)
            else : ctypes.windll.user32.MessageBoxW(0, " Xóa thành công ", "Thông báo", 0)
            self.ShowData()
            self.uic.tv_mssv.setText("")
            self.uic.tv_tensv.setText("")
    def Addform(self):
        data = DB_BLL.GetData()
        mssv_new = int(data[len(data)-1][0])+1
        self.uic.tv_mssv.setText(str(mssv_new))
        self.uic.tv_tensv.setText("")
        self.uic.btn_Save.setText("Thêm")
        self.uic.tv_url.setText("")
        path = os.getcwd()
        path = os.path.join(path,'Hinhmau.png')
        self.uic.LoadImage(path)
        self.chedo = 1
    def AddorUpdate(self):
        if(self.chedo == 1):
            self.AddSV()
        else:
            self.UpdateSV()
        self.chedo = 0
    def AddSV(self):
        sv = SV()
        sv.Masv = self.uic.tv_mssv.toPlainText()
        sv.Namesv = self.uic.tv_tensv.toPlainText()
        sv.URLhinhanh = self.SaveImage(self.uic.tv_url.toPlainText(), str(sv.Masv)).replace('\\', '/')
        if (ctypes.windll.user32.MessageBoxW(0, " Bạn có xác định thêm thông tin sinh viên " + sv.Namesv, "Cảnh báo", 1) == 1):
             if(DB_BLL.AddSV(sv)==0): ctypes.windll.user32.MessageBoxW(0, " Thêm không thành công ", "Thông báo", 0)
             else: ctypes.windll.user32.MessageBoxW(0, " Thêm thành công ", "Thông báo", 0)
        self.ShowData()
    def UpdateSV(self):
        masv = self.uic.tv_mssv.toPlainText()
        tensv = self.uic.tv_tensv.toPlainText()
        urlsv = self.SaveImage(self.uic.tv_url.toPlainText(),str(masv))
        if (ctypes.windll.user32.MessageBoxW(0, " Bạn có xác định sửa thông tin sinh viên " + tensv, "Cảnh báo", 1) == 1):
            if(DB_BLL.UpdateSV(masv,tensv,urlsv)==0):  ctypes.windll.user32.MessageBoxW(0, " Sửa không thành công ", "Thông báo", 0)
            else:  ctypes.windll.user32.MessageBoxW(0, " Sửa thành công ", "Thông báo", 0)
            self.uic.tv_mssv.setText("")
            self.uic.tv_tensv.setText("")
        self.ShowData()
    def Binding(self):
        self.chedo = 0
        masv = self.uic.TV_student.selectedItems()[0].text()
        sv = DB_BLL.SearchSVByMSSV(masv)
        self.uic.tv_mssv.setText(str(sv.Masv))
        self.uic.tv_tensv.setText(str(sv.Namesv))
        self.uic.tv_url.setText(str(sv.URLhinhanh))
        if(sv.Diemdanh == True):
            self.uic.btn_attend.setText("Bỏ điểm danh")
        else:
           self.uic.btn_attend.setText("Điểm danh")
        self.uic.btn_Save.setText("Lưu thay đổi")
        self.uic.LoadImage(str(sv.URLhinhanh))
    def ChangeAttendSV(self):
        item = self.uic.TV_student.selectedItems()
        day = self.uic.dateEdit.date().toString('yyyy-MM-dd')
        if(item[2].text() == '1'):
            check = False
            FirebaseAPI.RemoveData(item[0].text(),day)
        else:
            check = True
            FirebaseAPI.SendDataWithDay(item[0].text(),day)
        DB_BLL.ChangeAttendSV(item[0].text(),check)
        self.ShowData()
    def ChooseImage(self):
        filename = QFileDialog.getOpenFileName()
        self.uic.LoadImage(str(filename[0]))
        self.uic.tv_url.setText(str(filename[0]))
    def SaveImage(self,URL,name_image):
        path = os.getcwd()
        if (os.path.exists(path) == False): os.mkdir(path)
        path = os.path.join(path, 'ImageData', '%s.jpg'%(str(name_image)))
        path = path.replace('\\','/')
        if (os.path.exists(URL) == True):
            if(path != URL):
                shutil.copy(str(URL),str(path))
        else:
            return ""
        return path
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
