# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_pass.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_changePass(object):
    def setupUi(self, changePass):
        changePass.setObjectName("changePass")
        changePass.resize(486, 702)
        self.centralwidget = QtWidgets.QWidget(changePass)
        self.centralwidget.setObjectName("centralwidget")
        self.changePassword = QtWidgets.QLabel(self.centralwidget)
        self.changePassword.setGeometry(QtCore.QRect(50, 50, 391, 61))
        
        #Setting the title to Change Password
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.changePassword.setFont(font)
        self.changePassword.setObjectName("changePassword")
        self.acc_label = QtWidgets.QLabel(self.centralwidget)
        self.acc_label.setGeometry(QtCore.QRect(90, 280, 101, 21))
        
        #Setting labels for account and passowrd
        font = QtGui.QFont()
        font.setPointSize(14)
        self.acc_label.setFont(font)
        self.acc_label.setObjectName("acc_label")
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(80, 330, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        
        #Setting textboxes for account and password input
        self.acc_input = QtWidgets.QTextEdit(self.centralwidget)
        self.acc_input.setGeometry(QtCore.QRect(190, 280, 104, 31))
        self.acc_input.setObjectName("acc_input")
        self.pass_input = QtWidgets.QTextEdit(self.centralwidget)
        self.pass_input.setGeometry(QtCore.QRect(190, 330, 104, 31))
        self.pass_input.setObjectName("pass_input")
        
        #Setting the submit button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 480, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)
        
        changePass.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(changePass)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 26))
        self.menubar.setObjectName("menubar")
        changePass.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(changePass)
        self.statusbar.setObjectName("statusbar")
        changePass.setStatusBar(self.statusbar)

        self.retranslateUi(changePass)
        QtCore.QMetaObject.connectSlotsByName(changePass)

    def retranslateUi(self, changePass):
        _translate = QtCore.QCoreApplication.translate
        changePass.setWindowTitle(_translate("changePass", "MainWindow"))
        self.changePassword.setText(_translate("changePass", "Change Password"))
        self.acc_label.setText(_translate("changePass", "Account: "))
        self.pass_label.setText(_translate("changePass", "Password: "))
        self.pushButton.setText(_translate("changePass", "Change Password"))

    def clicked(self):
        file = open("pass.txt", "r")
        account_str = file.read()
        account_data = eval(account_str)
        file.close()
        account = self.acc_input.toPlainText()
        password = self.pass_input.toPlainText()
        account_data[account] = password
        file = open("pass.txt", "w")
        file.write(str(account_data))
        print("Changed Password")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    changePass = QtWidgets.QMainWindow()
    ui = Ui_changePass()
    ui.setupUi(changePass)
    changePass.show()
    sys.exit(app.exec_())
