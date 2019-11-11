# -*- coding: utf-8 -*-




from PyQt5 import QtCore, QtGui, QtWidgets
from Stall_Info import Ui_StallInfo
from Current_Stall import Ui_CurrentStall
from Stall_on_Date import Ui_StallonDate
from Operating_Hour import Ui_OperatingHour
from Check_Queue import Ui_CheckQueue

import Stall_Info
import pickle
from Database import Stall
from Database import item

from datetime import date
import calendar

d = date.today()
year = d.year
month = d.month
day = d.day

dayy = (calendar.weekday(year,month,day)+2)%7

data_file = open("stall_info.out", mode="rb")
db = pickle.load(data_file)
data_file.close()


index = 0



class Ui_MainWindow(object):

    #Function to open Stall_Info Menu
    #Done by Andrew Wiraatmaja
    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.window = Stall_Info.QtWidgets.QMainWindow()
        self.ui = Ui_StallInfo()
        self.ui.setupUi(self.window)
        self.window.show()
    
    #Function to open Current_Stall Menu
    #Done by Andrew Wiraatmaja
    def openWindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CurrentStall()
        self.ui.setupUi(self.window)
        self.window.show()
    
    #Function to open Stall_on_Date Menu
    #Done by Andrew Wiraatmaja
    def openWindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_StallonDate()
        self.ui.setupUi(self.window)
        self.window.show()
    
    #Function to open Operating_Hour Menu
    #Done by Andrew Wiraatmaja
    def openWindow4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OperatingHour()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 801, 651))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("bgr_menu.jpeg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")

        self.stall_info = QtWidgets.QPushButton(self.centralwidget)
        self.stall_info.setGeometry(QtCore.QRect(180, 250, 411, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.stall_info.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stall_info.setFont(font)
        self.stall_info.setAutoFillBackground(True)
        self.stall_info.setObjectName("stall_info")
        self.stall_info.clicked.connect(self.openWindow1)

        self.current_stall = QtWidgets.QPushButton(self.centralwidget)
        self.current_stall.setGeometry(QtCore.QRect(180, 320, 411, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.current_stall.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.current_stall.setFont(font)
        self.current_stall.setAutoFillBackground(True)
        self.current_stall.setObjectName("current_stall")
        self.current_stall.clicked.connect(self.openWindow2)

        self.stall_on_date = QtWidgets.QPushButton(self.centralwidget)
        self.stall_on_date.setGeometry(QtCore.QRect(180, 390, 411, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.stall_on_date.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stall_on_date.setFont(font)
        self.stall_on_date.setAutoFillBackground(True)
        self.stall_on_date.setObjectName("stall_on_date")
        self.stall_on_date.clicked.connect(self.openWindow3)

        self.operating_hour = QtWidgets.QPushButton(self.centralwidget)
        self.operating_hour.setGeometry(QtCore.QRect(180, 460, 411, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(188, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.operating_hour.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.operating_hour.setFont(font)
        self.operating_hour.setAutoFillBackground(True)
        self.operating_hour.setObjectName("operating_hour")
        self.operating_hour.clicked.connect(self.openWindow4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
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
        self.stall_info.setText(_translate("MainWindow", "Stall Info"))
        self.current_stall.setText(_translate("MainWindow", "Current Stall Available"))
        self.stall_on_date.setText(_translate("MainWindow", "Stall on Date"))
        self.operating_hour.setText(_translate("MainWindow", "Check Operating Hour"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    FirstWindow = QtWidgets.QMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
