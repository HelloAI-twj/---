import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
class window(QWidget):
    def __init__(self):
        super(window,self).__init__()
        self.initui()
    def initui(self):
        layout=QVBoxLayout()
        self.button1=QPushButton('打开文件',self)
        self.button1.clicked.connect(self.openfile)
        layout.addWidget(self.button1)
        self.lable=QLabel()
        layout.addWidget(self.lable)
        self.button2=QPushButton('打开文本文件',self)
        self.button2.clicked.connect(self.opentext)
        layout.addWidget(self.button2)
        self.contents=QTextEdit()
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle('智能交通')
    def openfile(self):
       frame,_=QFileDialog.getOpenFileNames(self,'打开文件','.')
       self.lable.setPixmap(QPixmap(frame))
    def opentext(self):
        dialog=QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec_():
            filenames=dialog.selectedFiles()
            print(filenames)
            #open(filenames[0],'r')
            with open(filenames[0],'r') as f:
                data=f.read()
                self.contents.setText(data)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=window()
    main.show()
    sys.exit(app.exec_())
