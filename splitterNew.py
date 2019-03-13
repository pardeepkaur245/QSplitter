# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splitter.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame, 
    QSplitter, QStyleFactory, QApplication ,QPushButton, QTextEdit,QLabel)
from PyQt5.QtCore import Qt
import sys
textfrlabel = 'vcxvxc'
text1 = 'vcvc'
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
       
        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        #add button in left frame
        btn = QPushButton('button', topleft)
        btn.setFixedSize(50, 20)
        btn.move(50,50)
        
        
        
 
        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)
        #add text Edit in right frame
        
        self.text2=QTextEdit('textedit2 ',topright)
        self.text2.setFixedSize(100,100)
       
        
      
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)
        self.text1=QTextEdit(' ',bottom)
        self.text1.setFixedSize(100,100)
        btn.clicked.connect(self.aaaa)

       
        def aaaa(self):
            print('1')
            textfrlabel=self.text2.text()
            print('2')
            self.text1.setText(textfrlabel)


        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
