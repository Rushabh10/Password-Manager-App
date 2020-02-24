# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_passwords.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
file = open("pass.txt", "r")
account_str = file.read()
account_data = eval(account_str)
file.close()

file_1 = open("keys.txt", "r")
keys_str = file_1.read()
keys_data = eval(keys_str)
file_1.close()

def decrypt(encrypted, key):
    decrypted = ""
    for i in range(len(encrypted)):
        decrypted += chr(ord(encrypted[i]) + key)

    return decrypted

class Ui_viewPass(object):
    
    def setupUi(self, viewPass):
        viewPass.setObjectName("viewPass")
        viewPass.resize(486, 702)
        self.centralwidget = QtWidgets.QWidget(viewPass)
        self.centralwidget.setObjectName("centralwidget")
        self.viewPasswords = QtWidgets.QLabel(self.centralwidget)
        self.viewPasswords.setGeometry(QtCore.QRect(70, 30, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.viewPasswords.setFont(font)
        self.viewPasswords.setObjectName("viewPasswords")
        self.allAccs = QtWidgets.QLabel(self.centralwidget)
        self.allAccs.setGeometry(QtCore.QRect(80, 140, 331, 301))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.allAccs.setText("")
        self.allAccs.setObjectName("allAccs")
        self.allAccs.setFont(font)
        account_names = list(account_data.keys())
        self.allAccs.setText("\n".join(map(str, account_names)))


        self.acc_label = QtWidgets.QLabel(self.centralwidget)
        self.acc_label.setGeometry(QtCore.QRect(40, 490, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.acc_label.setFont(font)
        self.acc_label.setObjectName("acc_label")
        self.acc_input = QtWidgets.QTextEdit(self.centralwidget)
        self.acc_input.setGeometry(QtCore.QRect(140, 490, 121, 41))
        self.acc_input.setObjectName("acc_input")
        self.showPass_button = QtWidgets.QPushButton(self.centralwidget)
        self.showPass_button.setGeometry(QtCore.QRect(280, 490, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.showPass_button.setFont(font)
        self.showPass_button.setObjectName("showPass_button")
        self.showPass_button.clicked.connect(self.clicked)
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(40, 590, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        self.passShow_label = QtWidgets.QLabel(self.centralwidget)
        self.passShow_label.setGeometry(QtCore.QRect(160, 580, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passShow_label.setFont(font)
        self.passShow_label.setObjectName("passShow_label")
        viewPass.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(viewPass)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 26))
        self.menubar.setObjectName("menubar")
        viewPass.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(viewPass)
        self.statusbar.setObjectName("statusbar")
        viewPass.setStatusBar(self.statusbar)

        self.retranslateUi(viewPass)
        QtCore.QMetaObject.connectSlotsByName(viewPass)

    def retranslateUi(self, viewPass):
        _translate = QtCore.QCoreApplication.translate
        viewPass.setWindowTitle(_translate("viewPass", "MainWindow"))
        self.viewPasswords.setText(_translate("viewPass", "View Passwords"))
        self.acc_label.setText(_translate("viewPass", "Account: "))
        self.showPass_button.setText(_translate("viewPass", "Show Password"))
        self.pass_label.setText(_translate("viewPass", "Password: "))
        self.passShow_label.setText(_translate("viewPass", "-------------"))


    def clicked(self):
        account = self.acc_input.toPlainText()
        encrypted = account_data[account]
        key = keys_data[account]
        password = decrypt(encrypted, key)
        self.passShow_label.setText(password)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewPass = QtWidgets.QMainWindow()
    ui = Ui_viewPass()
    ui.setupUi(viewPass)
    viewPass.show()
    sys.exit(app.exec_())
