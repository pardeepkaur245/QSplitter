# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\765354\Desktop\QtUiFiles\test1.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QSplitter, QLineEdit, QHBoxLayout, QLayout
from PyQt5.QtCore import Qt
g="hello"
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        hbox = QHBoxLayout()
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QFrame.StyledPanel) 
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 131, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.resize(100,100)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(40, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")

        
       

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)

        splitter2=QSplitter(Qt.Vertical)
        #splitter2.addWidget(splitter1)
        splitter2.addWidget(self.frame_2)
        splitter2.addWidget(self.frame_3)
        splitter2.setSizes([100,100])
        

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(self.frame)
        splitter1.addWidget(splitter2)
        
        
        splitter1.setSizes([80,200])
        hbox.addWidget(splitter1)
        self.centralwidget.setLayout(hbox)
        MainWindow.setCentralWidget(self.centralwidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

    def printMessage(self):
        value=self.lineEdit_1.text()
        self.lineEdit.clear()            
        self.lineEdit.setText(value)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
