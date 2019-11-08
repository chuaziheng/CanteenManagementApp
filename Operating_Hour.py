# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Andrew Wiraatmaja\Documents\Mini Project CZ1003\Operating_Hour.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Check_Queue import Ui_CheckQueue

import pickle
from Database import Stall
from Database import item
from datetime import date
import calendar
import datetime

t = datetime.datetime.now()
hour = t.hour
minute = t.minute

d = date.today()
year = d.year
month = d.month
day = d.day

dayy = (calendar.weekday(year,month,day)+2)%7

data_file = open("stall_info.out", mode="rb")
db = pickle.load(data_file)
data_file.close()

list_stall = []
list_pic = ["McDonald.png","italian.png","pizzahut.png"]
index = 0

for i in range(3):
    list_stall.append(db[i].st_name)

class Ui_OperatingHour(object):

    def displayStall(self):
        self.ch_stall.hide()
        self.comboBox.hide()
        self.proceed.hide()
        self.stall_name.show()
        text = str(self.comboBox.currentText())
        self.stall_name.setText(text)
        for i in range(3) :
            if db[i].st_name == text :
                index = i
        self.desc.setText(db[index].desc)
        self.desc.show()
        self.open_time.setText(db[index].opening_time[dayy])
        self.open_time.show()
        self.close_time.setText(db[index].closing_time[dayy])
        self.close_time.show()
        self.label_2.show()
        self.label_3.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(578, 383)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 571, 371))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.ch_stall = QtWidgets.QLabel(self.centralwidget)
        self.ch_stall.setGeometry(QtCore.QRect(130, 80, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(20)
        self.ch_stall.setFont(font)
        self.ch_stall.setAutoFillBackground(True)
        self.ch_stall.setAlignment(QtCore.Qt.AlignCenter)
        self.ch_stall.setObjectName("ch_stall")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 160, 311, 61))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        for i in range(3):
            self.comboBox.addItem(QtGui.QIcon(list_pic[i]),list_stall[i])

        self.proceed = QtWidgets.QPushButton(self.centralwidget)
        self.proceed.setGeometry(QtCore.QRect(370, 250, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.proceed.setFont(font)
        self.proceed.setObjectName("proceed")
        self.proceed.clicked.connect(self.displayStall)
        
        self.stall_name = QtWidgets.QLabel(self.centralwidget)
        self.stall_name.setGeometry(QtCore.QRect(140, 20, 311, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.stall_name.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(20)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.stall_name.setFont(font)
        self.stall_name.setAlignment(QtCore.Qt.AlignCenter)
        self.stall_name.setObjectName("stall_name")
        self.stall_name.hide()

        self.desc = QtWidgets.QLabel(self.centralwidget)
        self.desc.setGeometry(QtCore.QRect(10, 100, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.desc.setFont(font)
        self.desc.setAlignment(QtCore.Qt.AlignCenter)
        self.desc.setObjectName("desc")
        self.desc.hide()

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(70, 10, 141, 81))
        self.logo.setObjectName("logo")
        self.logo.hide()

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 170, 221, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 220, 231, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2.hide()
        self.label_3.hide()

        self.open_time = QtWidgets.QLabel(self.centralwidget)
        self.open_time.setGeometry(QtCore.QRect(350, 170, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.open_time.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(16)
        self.open_time.setFont(font)
        self.open_time.setObjectName("open_time")
        self.open_time.hide()

        self.close_time = QtWidgets.QLabel(self.centralwidget)
        self.close_time.setGeometry(QtCore.QRect(350, 220, 171, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.close_time.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(16)
        self.close_time.setFont(font)
        self.close_time.setObjectName("close_time")
        self.close_time.hide()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 31))
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
        self.ch_stall.setText(_translate("MainWindow", "Choose Stall"))
        self.stall_name.setText(_translate("MainWindow", "TextLabel"))
        self.desc.setText(_translate("MainWindow", "TextLabel"))
        self.logo.setText(_translate("MainWindow", "Logo"))
        self.label_2.setText(_translate("MainWindow", "Opening Hours :"))
        self.label_3.setText(_translate("MainWindow", "Closing Hours :"))
        self.open_time.setText(_translate("MainWindow", "Open"))
        self.close_time.setText(_translate("MainWindow", "Close"))
        self.proceed.setText(_translate("MainWindow", "Proceed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_OperatingHour()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
