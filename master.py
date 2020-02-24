# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'master.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from main_menu import Ui_mainMenu


class Ui_master(object):
    def setupUi(self, master):
        master.setObjectName("master")
        master.resize(486, 702)
        self.centralwidget = QtWidgets.QWidget(master)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(150, 30, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        self.enterPass_label = QtWidgets.QLabel(self.centralwidget)
        self.enterPass_label.setGeometry(QtCore.QRect(30, 260, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enterPass_label.setFont(font)
        self.enterPass_label.setObjectName("enterPass_label")
        self.pass_input = QtWidgets.QTextEdit(self.centralwidget)
        self.pass_input.setGeometry(QtCore.QRect(120, 310, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pass_input.setFont(font)
        self.pass_input.setObjectName("pass_input")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 510, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)
        master.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(master)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 26))
        self.menubar.setObjectName("menubar")
        master.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(master)
        self.statusbar.setObjectName("statusbar")
        master.setStatusBar(self.statusbar)

        self.retranslateUi(master)
        QtCore.QMetaObject.connectSlotsByName(master)

    def retranslateUi(self, master):
        _translate = QtCore.QCoreApplication.translate
        master.setWindowTitle(_translate("master", "MainWindow"))
        self.welcome_label.setText(_translate("master", "Welcome"))
        self.enterPass_label.setText(_translate("master", "Please enter the master password: "))
        self.pushButton.setText(_translate("master", "Submit"))

    def clicked(self):
        password = self.pass_input.toPlainText()
        if password == "masterpassword":
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_mainMenu()
            self.ui.setupUi(self.window)
            self.window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    master = QtWidgets.QMainWindow()
    ui = Ui_master()
    ui.setupUi(master)
    master.show()
    sys.exit(app.exec_())
