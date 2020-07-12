import sys
from PyQt5.Qt import QUrl
import qtawesome
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from screenshoot import Screenshot
class m_window(QMainWindow):
    def __init__(self):
        super(m_window, self).__init__()
        self.initui()
    def initui(self):
        self.main_widget = QWidget()  # 创建窗口主部件
        self.main_layout = QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setFixedSize(960,700)
        self.setWindowTitle('视频播放')

        self.down_widget = QWidget()  # 创建左侧部件,建立一个窗口
        self.down_widget.setObjectName('down_widget')
        self.down_layout=QGridLayout()  # 创建左侧部件的网格布局层
        self.down_widget.setLayout(self.down_layout)  # 设置左侧部件布局为网格

        #layout=QVBoxLayout()
        self.main_layout.addWidget(self.down_widget, 3, 0,1 ,13)
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件


        self.button1=QPushButton('打开视频文件')
        self.button1.setIcon(qtawesome.icon('fa.folder', color='black'))
        self.button1.clicked.connect(self.openVideoFile)
        self.button2=QPushButton('播放')
        self.button2.setIcon(qtawesome.icon('fa.play-circle', color='black'))
        self.button2.clicked.connect(self.play)
        self.button3=QPushButton('暂停')
        self.button3.setIcon(qtawesome.icon('fa.pause-circle', color='black'))
        self.button3.clicked.connect(self.pause)
        self.button4=QPushButton('截屏')
        self.button4.setIcon(qtawesome.icon('fa.camera', color='black'))
        self.button4.clicked.connect(self.srcshoot)
        self.down_layout.addWidget(self.button1,3,1,1,2)
        self.down_layout.addWidget(self.button2, 3,4, 1, 2)
        self.down_layout.addWidget(self.button3, 3, 7, 1, 2)
        self.down_layout.addWidget(self.button4, 3, 10, 1, 2)

        self.slider=QSlider(Qt.Horizontal,self)#设置滑动条
        self.down_layout.addWidget(self.slider,2,0,1,10)
        self.player = QMediaPlayer()
        self.screen=QVideoWidget()
        self.down_layout.addWidget(self.screen,0,0,2,13)
        self.player.setVideoOutput(self.screen)
        self.player.positionChanged.connect(self.changeSlide)

    def openVideoFile(self):
        self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))
        self.player.play()

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()
    def changeSlide(self,position):
        self.vidoeLength = self.player.duration()+0.1
        self.slider.setValue(round((position/self.vidoeLength)*100))
    def srcshoot(self):
        self.act=Screenshot()
        self.act.show()
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=m_window()
    main.show()
    sys.exit(app.exec_())