import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from cardetect import car_detect
class det(QMainWindow):
    def __init__(self):
        super(det,self).__init__()
        self.initui()
    def initui(self):
        self.main_widget=QWidget()
        self.main_layout = QGridLayout()
        self.main_widget.setLayout(self.main_layout)
        self.setWindowTitle('采集')
        self.resize(400, 350)
        self.setCentralWidget(self.main_widget)


        self.top_widget=QWidget()
        self.top_layout=QGridLayout()
        self.top_widget.setLayout(self.top_layout)
        self.button1=QPushButton('预测视频地址(使用英文模式)：')
        self.edit1=QLineEdit()
        self.edit1.editingFinished.connect(self.over1)
        self.top_layout.addWidget(self.button1,0,0,1,2)
        self.top_layout.addWidget(self.edit1,0,3,1,5)
        self.button2=QPushButton('保存视频地址(使用英文模式):')
        self.edit2=QLineEdit()
        self.edit2.editingFinished.connect(self.over2)
        self.button3 = QPushButton('确定')
        self.button3.clicked.connect(self.transport)
        self.button4=QPushButton('取消')
        self.top_layout.addWidget(self.button2, 1, 0, 1, 2)
        self.top_layout.addWidget(self.edit2, 1, 3, 1, 5)
        self.button5=QPushButton('视频分辨率(使用英文模式):')
        self.edit5 = QLineEdit()
        self.edit5.editingFinished.connect(self.over3)
        self.top_layout.addWidget(self.button5, 2, 0, 1, 2)
        self.top_layout.addWidget(self.edit5, 2, 3, 1, 5)
        self.top_layout.addWidget(self.button3,3,0,1,3)
        self.top_layout.addWidget(self.button4,3,5,1,3)

        self.main_layout.addWidget(self.top_widget,0,0,3,8)

    def over1(self):
        self.predict = self.edit1.text()
        print(type(self.predict))
    def over2(self):
        self.save=self.edit2.text()
        print(type(self.save))
    def over3(self):
        self.reso=self.edit5.text()
        print(type(self.reso))
    def transport(self):
        print('开始预测')
        data = car_detect(self.predict, self.save, tuple(self.reso))
        data.detection()


if __name__=='__main__':
    app=QApplication(sys.argv)
    main=det()

    main.show()

    sys.exit(app.exec_())

