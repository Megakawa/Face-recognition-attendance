# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Doan.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 611)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Show = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Show.setGeometry(QtCore.QRect(430, 80, 161, 41))
        self.btn_Show.setObjectName("btn_Show")
        self.btn_Add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Add.setGeometry(QtCore.QRect(430, 130, 161, 41))
        self.btn_Add.setObjectName("btn_Add")
        self.btn_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Delete.setGeometry(QtCore.QRect(430, 180, 161, 41))
        self.btn_Delete.setObjectName("btn_Delete")
        self.tv_search = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.tv_search.setGeometry(QtCore.QRect(10, 10, 391, 31))
        self.tv_search.setObjectName("tv_search")
        self.btn_Search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Search.setGeometry(QtCore.QRect(430, 10, 161, 31))
        self.btn_Search.setObjectName("btn_Search")
        self.TV_student = QtWidgets.QTableWidget(self.centralwidget)
        self.TV_student.setGeometry(QtCore.QRect(10, 50, 391, 511))
        self.TV_student.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.TV_student.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TV_student.setObjectName("TV_student")
        self.TV_student.setColumnCount(3)
        self.TV_student.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TV_student.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TV_student.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TV_student.setHorizontalHeaderItem(2, item)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(610, 10, 421, 561))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 300, 121, 31))
        self.label_3.setObjectName("label_3")
        self.tv_tensv = QtWidgets.QTextEdit(self.groupBox)
        self.tv_tensv.setGeometry(QtCore.QRect(140, 380, 201, 31))
        self.tv_tensv.setObjectName("tv_tensv")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 380, 121, 31))
        self.label_4.setObjectName("label_4")
        self.tv_mssv = QtWidgets.QTextEdit(self.groupBox)
        self.tv_mssv.setEnabled(False)
        self.tv_mssv.setGeometry(QtCore.QRect(140, 300, 201, 31))
        self.tv_mssv.setObjectName("tv_mssv")
        self.btn_Save = QtWidgets.QPushButton(self.groupBox)
        self.btn_Save.setGeometry(QtCore.QRect(160, 510, 121, 31))
        self.btn_Save.setObjectName("btn_Save")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(140, 20, 201, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lb_avatar = QtWidgets.QLabel(self.groupBox_2)
        self.lb_avatar.setGeometry(QtCore.QRect(10, 30, 181, 201))
        self.lb_avatar.setAutoFillBackground(True)
        self.lb_avatar.setText("")
        self.lb_avatar.setScaledContents(True)
        self.lb_avatar.setObjectName("lb_avatar")
        self.btn_addimage = QtWidgets.QPushButton(self.groupBox)
        self.btn_addimage.setGeometry(QtCore.QRect(160, 270, 161, 21))
        self.btn_addimage.setObjectName("btn_addimage")
        self.tv_url = QtWidgets.QTextEdit(self.groupBox)
        self.tv_url.setEnabled(False)
        self.tv_url.setGeometry(QtCore.QRect(140, 340, 201, 31))
        self.tv_url.setObjectName("tv_url")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 340, 121, 31))
        self.label_5.setObjectName("label_5")
        self.btn_attend = QtWidgets.QPushButton(self.centralwidget)
        self.btn_attend.setGeometry(QtCore.QRect(430, 230, 161, 41))
        self.btn_attend.setObjectName("btn_attend")
        self.OpenCamera = QtWidgets.QPushButton(self.centralwidget)
        self.OpenCamera.setGeometry(QtCore.QRect(430, 280, 161, 41))
        self.OpenCamera.setObjectName("OpenCamera")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 340, 121, 16))
        self.label.setObjectName("label")
        self.btnShow = QtWidgets.QPushButton(self.centralwidget)
        self.btnShow.setGeometry(QtCore.QRect(430, 390, 161, 41))
        self.btnShow.setObjectName("btnShow")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(430, 360, 161, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1058, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_Show.setText(_translate("MainWindow", "Xuất"))
        self.btn_Add.setText(_translate("MainWindow", "Thêm"))
        self.btn_Delete.setText(_translate("MainWindow", "Xóa"))
        self.btn_Search.setText(_translate("MainWindow", "Tìm kiếm "))
        item = self.TV_student.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Mã số sinh viên"))
        item = self.TV_student.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tên sinh viên"))
        item = self.TV_student.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Điểm danh "))
        self.groupBox.setTitle(_translate("MainWindow", "Thông tin sinh viên "))
        self.label_3.setText(_translate("MainWindow", "Mã số sinh viên"))
        self.label_4.setText(_translate("MainWindow", "Họ và tên"))
        self.btn_Save.setText(_translate("MainWindow", "Lưu thay đổi"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Hình ảnh sinh viên"))
        self.btn_addimage.setText(_translate("MainWindow", "Đổi ảnh"))
        self.label_5.setText(_translate("MainWindow", "URL Hình ảnh"))
        self.btn_attend.setText(_translate("MainWindow", "Điểm danh"))
        self.OpenCamera.setText(_translate("MainWindow", "Mở điểm danh"))
        self.label.setText(_translate("MainWindow", "Hiển thị theo ngày"))
        self.btnShow.setText(_translate("MainWindow", "Hiển thị"))
    def LoadDataTable(self, data):
        row = 0
        self.TV_student.setRowCount(len(data))
        for sv in data:
            self.TV_student.setItem(row, 0, QtWidgets.QTableWidgetItem(sv[0]))
            self.TV_student.setItem(row, 1, QtWidgets.QTableWidgetItem(sv[1]))
            self.TV_student.setItem(row, 2, QtWidgets.QTableWidgetItem(str(sv[2])))
            row = row + 1

    def LoadImage(self, URL):
        px = QtGui.QPixmap(str(URL))
        self.lb_avatar.setPixmap(px)