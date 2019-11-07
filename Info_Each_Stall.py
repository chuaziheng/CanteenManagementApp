# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Andrew Wiraatmaja\Documents\Project\Info_Each_Stall.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pickle
from Database import Stall
from Database import item

data_file = open("stall_info.out", mode="rb")
db = pickle.load(data_file)
data_file.close()

class Ui_InfoEachStall1(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(489, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stall_name = QtWidgets.QLabel(self.centralwidget)
        self.stall_name.setGeometry(QtCore.QRect(70, 30, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stall_name.setFont(font)
        self.stall_name.setAlignment(QtCore.Qt.AlignCenter)
        self.stall_name.setObjectName("stall_name")
        self.stall_name.setText(db[0].st_name)

        self.desc_stall = QtWidgets.QLabel(self.centralwidget)
        self.desc_stall.setGeometry(QtCore.QRect(70, 110, 351, 61))
        self.desc_stall.setAlignment(QtCore.Qt.AlignCenter)
        self.desc_stall.setObjectName("desc_stall")
        self.desc_stall.setText(db[0].desc)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 200, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 340, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 270, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 420, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 31))
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
        self.pushButton.setText(_translate("MainWindow", "Menu"))
        self.pushButton_2.setText(_translate("MainWindow", "Check Queue"))
        self.pushButton_3.setText(_translate("MainWindow", "Operating Hour"))
        self.pushButton_4.setText(_translate("MainWindow", "Menu on Date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_InfoEachStall1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
