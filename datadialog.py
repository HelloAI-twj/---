import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class datadialog(QDialog):
    def __init__(self,parent=None):
        super(datadialog,self).__init__(parent)
        self.setWindowTitle('datadialog')
        layout=QVBoxLayout(self)
        self.datetime=QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.datetime)
        buttons=QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal,self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
    def datetime(self):
        return self.datetime.datetime()
    @staticmethod
    def getdatetime(parent=None):
        dialog=datadialog(parent)
        result=dialog.exec()
        date=dialog.datetime()
        return (date.date(),date.time(),result==QDialog.Accepted)