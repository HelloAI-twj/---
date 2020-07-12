import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class calendar(QWidget):
    def __init__(self):
        super(calendar,self).__init__()

        self.initui()
    def initui(self):
        self.cal=QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1988,1,1))
        self.cal.setMaximumDate(QDate(2088,1,1))
        self.cal.setGridVisible(True)
        self.cal.move(20,20)
        self.cal.clicked.connect(self.showdata)
        self.lable=QLabel(self)
        data=self.cal.selectedDate()
        self.lable.setText(data.toString('yyyy-MM-dd dddd'))
        self.lable.move(20,300)
        self.setWindowTitle('日历')
        self.resize(400,350)
    def showdata(self):
        data = self.cal.selectedDate()
        self.lable.setText(data.toString('yyyy-MM-dd dddd'))
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=calendar()
    main.show()
    sys.exit(app.exec_())
