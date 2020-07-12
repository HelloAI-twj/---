import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class tool(QMainWindow):
    def __init__(self):
        super(tool,self).__init__()
        self.initui()
    def initui(self):
        self.setWindowTitle('工具栏')
        self.resize(300,200)
        tb1=self.addToolBar('File')
        new=QAction('new',self)
        tb1.addAction(new)
        open=QAction('open',self)
        tb1.addAction(open)
        save=QAction('save',self)
        tb1.addAction(save)
        tb1.actionTriggered.connect(self.press)
    def press(self,a):
        print('按下的按钮是',a.text())
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=tool()
    main.show()
    sys.exit(app.exec_())