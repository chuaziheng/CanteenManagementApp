# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\chuaz\Downloads\NTU\CZ1003 Intro To Comp Thinking\Mini project\check queue.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 171)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-60, -10, 481, 351))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("widget background translucent.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 301, 51))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.people = QtWidgets.QTextEdit(Dialog)
        self.people.setGeometry(QtCore.QRect(310, 40, 61, 41))
        self.people.setObjectName("people")
        self.calculateButton = QtWidgets.QPushButton(Dialog)
        self.calculateButton.setGeometry(QtCore.QRect(170, 110, 112, 34))
        self.calculateButton.setObjectName("calculateButton")
        self.calculateButton.clicked.connect(self.check_queue_int)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def check_queue_int (self):
        num_of_people = self.people.toPlainText()
        while True:
            try:
                num_of_people = int(num_of_people)
                break
            except ValueError:
                print ("Not a valid integer, please try again")
        num = self.people.toPlainText()
        tim = float(float(num)*2)
        self.label_2.setText(str(float(tim)))
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Enter the number of people queuing:"))
        self.calculateButton.setText(_translate("Dialog", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
