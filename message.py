import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class message(QWidget):
    def __init__(self):
        super(message,self).__init__()
        self.initui()
    def initui(self):
        self.setWindowTitle('案例')
        self.resize(300,400)
        self.button1=QPushButton(self)
        self.button1.setText('弹出对话框')
        self.button1.move(50,50)
        self.button1.clicked.connect(self.showdialog)

        layout=QVBoxLayout()
        self.button2=QPushButton()
        self.button2.setText('显示关于对话框')
        layout.addWidget(self.button2)
        self.button2.clicked.connect(self.showdialog2)
        self.setLayout(layout)

        self.button3= QPushButton()
        self.button3.setText('显示消息对话框')
        layout.addWidget(self.button3)
        self.button3.clicked.connect(self.showdialog2)
    def showdialog(self):
        dialog= QDialog()
        button=QPushButton('确定',dialog)
        button.clicked.connect(dialog.close)
        button.move(50,50)
        dialog.setWindowTitle('对话框')
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()
    def showdialog2(self):
        text=self.sender().text()
        if text=='显示关于对话框':
            QMessageBox.about(self,'关于','这是一个关于对话框')
        elif text=='显示消息对话框':
            QMessageBox.information(self,'消息','请问是否退出',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=message()
    main.show()
    sys.exit(app.exec_())