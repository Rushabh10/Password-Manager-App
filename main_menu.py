# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from add_acc import Ui_MainWindow
from change_pass import Ui_changePass
from remove_acc import Ui_removeAcc
from view_passwords import Ui_viewPass


class Ui_mainMenu(object):
    def setupUi(self, mainMenu):
        mainMenu.setObjectName("mainMenu")
        mainMenu.resize(486, 702)
        self.centralwidget = QtWidgets.QWidget(mainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.passManager = QtWidgets.QLabel(self.centralwidget)
        self.passManager.setGeometry(QtCore.QRect(30, 30, 421, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.passManager.setFont(font)
        self.passManager.setObjectName("passManager")
        self.addAcc_button = QtWidgets.QPushButton(self.centralwidget)
        self.addAcc_button.setGeometry(QtCore.QRect(150, 180, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addAcc_button.setFont(font)
        self.addAcc_button.setObjectName("addAcc_button")
        self.addAcc_button.clicked.connect(self.openAdd)
        self.changePass_button = QtWidgets.QPushButton(self.centralwidget)
        self.changePass_button.setGeometry(QtCore.QRect(130, 270, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.changePass_button.setFont(font)
        self.changePass_button.setObjectName("changePass_button")
        self.changePass_button.clicked.connect(self.openChange)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 370, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openRemove)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 480, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openShow)
        mainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 26))
        self.menubar.setObjectName("menubar")
        mainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainMenu)
        self.statusbar.setObjectName("statusbar")
        mainMenu.setStatusBar(self.statusbar)

        self.retranslateUi(mainMenu)
        QtCore.QMetaObject.connectSlotsByName(mainMenu)

    def retranslateUi(self, mainMenu):
        _translate = QtCore.QCoreApplication.translate
        mainMenu.setWindowTitle(_translate("mainMenu", "MainWindow"))
        self.passManager.setText(_translate("mainMenu", "Password Manager"))
        self.addAcc_button.setText(_translate("mainMenu", "Add Account"))
        self.changePass_button.setText(_translate("mainMenu", "Change Password"))
        self.pushButton.setText(_translate("mainMenu", "Remove Account"))
        self.pushButton_2.setText(_translate("mainMenu", "View Password"))

    def openAdd(self):
    	self.window = QtWidgets.QMainWindow()
    	self.ui = Ui_MainWindow()
    	self.ui.setupUi(self.window)
    	self.window.show()

    def openChange(self):
    	self.window = QtWidgets.QMainWindow()
    	self.ui = Ui_changePass()
    	self.ui.setupUi(self.window)
    	self.window.show()

    def openRemove(self):
    	self.window = QtWidgets.QMainWindow()
    	self.ui = Ui_removeAcc()
    	self.ui.setupUi(self.window)
    	self.window.show()

    def openShow(self):
    	self.window = QtWidgets.QMainWindow()
    	self.ui = Ui_viewPass()
    	self.ui.setupUi(self.window)
    	self.window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainMenu = QtWidgets.QMainWindow()
    ui = Ui_mainMenu()
    ui.setupUi(mainMenu)
    mainMenu.show()
    sys.exit(app.exec_())
