# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remove_acc.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_removeAcc(object):
    def setupUi(self, removeAcc):
        removeAcc.setObjectName("removeAcc")
        removeAcc.resize(486, 702)
        self.centralwidget = QtWidgets.QWidget(removeAcc)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.acc_label = QtWidgets.QLabel(self.centralwidget)
        self.acc_label.setGeometry(QtCore.QRect(70, 220, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.acc_label.setFont(font)
        self.acc_label.setObjectName("acc_label")
        self.acc_input = QtWidgets.QTextEdit(self.centralwidget)
        self.acc_input.setGeometry(QtCore.QRect(170, 230, 104, 31))
        self.acc_input.setObjectName("acc_input")
        self.removeAcc_button = QtWidgets.QPushButton(self.centralwidget)
        self.removeAcc_button.setGeometry(QtCore.QRect(140, 450, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.removeAcc_button.setFont(font)
        self.removeAcc_button.setObjectName("removeAcc_button")
        self.removeAcc_button.clicked.connect(self.clicked)
        removeAcc.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(removeAcc)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 26))
        self.menubar.setObjectName("menubar")
        removeAcc.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(removeAcc)
        self.statusbar.setObjectName("statusbar")
        removeAcc.setStatusBar(self.statusbar)

        self.retranslateUi(removeAcc)
        QtCore.QMetaObject.connectSlotsByName(removeAcc)

    def retranslateUi(self, removeAcc):
        _translate = QtCore.QCoreApplication.translate
        removeAcc.setWindowTitle(_translate("removeAcc", "MainWindow"))
        self.label.setText(_translate("removeAcc", "Remove Account"))
        self.acc_label.setText(_translate("removeAcc", "Account: "))
        self.removeAcc_button.setText(_translate("removeAcc", "Remove Account"))

    def clicked(self):
        file = open("pass.txt", "r")
        account_str = file.read()
        account_data = eval(account_str)
        file.close()
        account = self.acc_input.toPlainText()
        del account_data[account]
        file = open("pass.txt", "w")
        file.write(str(account_data))
        print("Removed Account")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    removeAcc = QtWidgets.QMainWindow()
    ui = Ui_removeAcc()
    ui.setupUi(removeAcc)
    removeAcc.show()
    sys.exit(app.exec_())
