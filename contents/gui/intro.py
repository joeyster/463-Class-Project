# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'intro.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from warehouse import Ui_MainWindow

class Ui_IntroWindow(object):
    def setupUi(self, IntroWindow):
        IntroWindow.setObjectName("IntroWindow")
        IntroWindow.resize(566, 273)
        IntroWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(IntroWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 50, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 150, 91, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")

        # connect the start button to the startButton function
        self.pushButton.clicked.connect(self.startButton)

        IntroWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(IntroWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 21))
        self.menubar.setObjectName("menubar")
        IntroWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(IntroWindow)
        self.statusbar.setObjectName("statusbar")
        IntroWindow.setStatusBar(self.statusbar)

        self.retranslateUi(IntroWindow)
        QtCore.QMetaObject.connectSlotsByName(IntroWindow)

    def retranslateUi(self, IntroWindow):
        _translate = QtCore.QCoreApplication.translate
        IntroWindow.setWindowTitle(_translate("IntroWindow", "MainWindow"))
        self.label.setText(_translate("IntroWindow", "The Kitchen"))
        self.pushButton.setText(_translate("IntroWindow", "Start"))

    # shows the warehouse gui if the start button is pushed
    def startButton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        IntroWindow.hide()
        self.window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IntroWindow = QtWidgets.QMainWindow()
    ui = Ui_IntroWindow()
    ui.setupUi(IntroWindow)
    IntroWindow.show()
    sys.exit(app.exec_())
