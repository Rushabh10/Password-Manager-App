# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_acc.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint

def encrypt(password, key):
    encrypted = ""
    for i in range(len(password)):
        encrypted += chr(ord(password[i]) - key)

    return encrypted


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 702)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addAccount = QtWidgets.QLabel(self.centralwidget)
        self.addAccount.setGeometry(QtCore.QRect(100, 40, 281, 81))
        
        #Setting the title to Add Account
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.addAccount.setFont(font)
        self.addAccount.setObjectName("addAccount")
        self.account_label = QtWidgets.QLabel(self.centralwidget)
        self.account_label.setGeometry(QtCore.QRect(60, 250, 91, 31))
        
        #Setting labels for the account and password
        font = QtGui.QFont()
        font.setPointSize(14)
        self.account_label.setFont(font)
        self.account_label.setObjectName("account_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 300, 111, 21))
        
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("pass_label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 440, 151, 71))
       
        #Setting the submit button and input textboxes 
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)
        self.acc_input = QtWidgets.QTextEdit(self.centralwidget)
        self.acc_input.setGeometry(QtCore.QRect(170, 250, 104, 31))
        self.acc_input.setObjectName("acc_input")
        self.pass_input = QtWidgets.QTextEdit(self.centralwidget)
        self.pass_input.setGeometry(QtCore.QRect(170, 300, 104, 31))
        self.pass_input.setObjectName("pass_input")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 26))
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
        self.addAccount.setText(_translate("MainWindow", "Add Account"))
        self.account_label.setText(_translate("MainWindow", "Account:"))
        self.label.setText(_translate("MainWindow", "Password: "))
        self.pushButton.setText(_translate("MainWindow", "Add Account"))

    def clicked(self):
        file = open("pass.txt", "r")
        account_str = file.read()
        account_data = eval(account_str)
        file.close()
        file_1 = open("keys.txt", "r")
        keys_str = file_1.read()
        keys_data = eval(keys_str)
        file_1.close()
        account = self.acc_input.toPlainText()
        password = self.pass_input.toPlainText()
        key = randint(2, 15)
        encrypted = encrypt(password, key)
        account_data[account] = encrypted
        keys_data[account] = key
        file = open("pass.txt", "w")
        file.write(str(account_data))
        file.close()
        file_1 = open("keys.txt", "w")
        file_1.write(str(keys_data))
        file_1.close()
        print("Added Password")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
