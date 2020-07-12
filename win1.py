import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from py_player_demo2 import myMainWindow
from datadialog import datadialog
from calender import calendar
class win1(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1080,720)
        self.setWindowTitle('智能交通')
        self.setWindowIcon(QIcon('F:/timg.jpg'))
        #self.lineedit=QLineEdit(self)
        self.button1=QPushButton('车辆检测')
        self.button1.clicked.connect(self.click)
        self.button2= QPushButton('视频播放')
        self.button2.clicked.connect(self.click2)
        self.button3=QPushButton('日历')
        self.button3.clicked.connect(self.click3)
        self.lable=QLabel()
        gridlayout=QGridLayout()
        gridlayout.addWidget(self.lable)
        gridlayout.addWidget(self.button1)
        gridlayout.addWidget(self.button2)
        gridlayout.addWidget(self.button3)
        #gridlayout.addWidget(self.lable)
        #gridlayout.addWidget(self.lineedit)
        self.setLayout(gridlayout)
    def click(self):
        dialog=datadialog(self)
        result=dialog.exec()
        date=dialog.datetime()
        self.lineedit.setText(date.date().toString())
        dialog.destroy()
    def click2(self):
        #app = QApplication(sys.argv)
        dialog_win=QDialog()
        dialog_win.resize(600,500)
        dialog_win.setWindowTitle('视频播放')
        v_layout=QVBoxLayout(dialog_win)
        vieo_gui = myMainWindow()
        #vieo_gui.setWindowModality(Qt.ApplicationModal)
        #vieo_gui.show()
        v_layout.addWidget(vieo_gui)
        dialog_win.exec()
    def click3(self):
        dialog_win2= QDialog()
        dialog_win2.resize(400,350)
        dialog_win2.setWindowTitle('日历')
        v_layout = QVBoxLayout(dialog_win2)
        cal = calendar()
        v_layout.addWidget(cal)
        dialog_win2.exec()
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=win1()
    main.show()
    # b=myMainWindow()
    # main.button2.clicked.connect(b.show)
    sys.exit(app.exec_())