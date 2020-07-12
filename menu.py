import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class menu(QMainWindow):
    def __init__(self):
        super(menu,self).__init__()
        self.initui()
        bar=self.menuBar()#获取菜单栏
        file=bar.addMenu('文件')
        file.addAction('新建')#子菜单
        save=QAction('保存',self)
        save.setShortcut('Ctrl+S')
        file.addAction(save)
        save.triggered.connect(self.process)
        edit=bar.addMenu('编辑')
        edit.addAction('copy')
        edit.addAction('paste')
        quit=QAction('quit',self)#在当前窗口下建立子菜单方法2，要加上self
        file.addAction(quit)
    def initui(self):
        pass
    def process(self,a):
        print(self.sender().text())
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=menu()
    main.show()
    sys.exit(app.exec_())
