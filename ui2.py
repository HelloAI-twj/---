import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import qtawesome
import webbrowser
from calender import calendar
from video_player import m_window
from detecting import det

class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960,700)
        self.setWindowTitle('智能交通检测')
        self.setWindowIcon(qtawesome.icon('fa.car', color='black'))
        self.main_widget = QWidget()  # 创建窗口主部件
        self.main_layout = QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格

        self.right_widget = QWidget() # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QGridLayout()
        #设置背景图片
        palette=QPalette()
        pix=QPixmap("F:/car.jpg")
        palette.setBrush(QPalette.Background,QBrush(pix))
        self.right_widget.setPalette(palette)
        self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget,0,2,12,10) # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget) # 设置窗口主部件
        self.left_close = QPushButton("")  # 关闭按钮
        self.left_visit = QPushButton("")  # 空白按钮
        self.left_mini = QPushButton("")  # 最小化按钮

        self.left_label_1 = QPushButton("智能工具")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QPushButton("本地检测")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QPushButton(qtawesome.icon('fa.eye', color='white'), "智能检测")
        self.left_button_1.setObjectName('left_button')
        self.left_button_1.clicked.connect(self.view)
        self.left_button_2 = QPushButton(qtawesome.icon('fa.map-marker', color='white'), "百度地图")
        self.left_button_2.setObjectName('left_button')
        self.left_button_2.clicked.connect(self.baidumap)
        self.left_button_3 = QPushButton(qtawesome.icon('fa.calendar', color='white'), "交通日历")
        self.left_button_3.setObjectName('left_button')
        self.left_button_3.clicked.connect(self.trancal)
        self.left_button_4 = QPushButton(qtawesome.icon('fa.home', color='white'), "本地视频")
        self.left_button_4.setObjectName('left_button')
        self.left_button_4.clicked.connect(self.videoplay)
        self.left_button_7 = QPushButton(qtawesome.icon('fa.comment', color='white'), "反馈建议")
        self.left_button_7.setObjectName('left_button')
        self.left_button_7.clicked.connect(self.feedback)
        self.left_button_8 = QPushButton(qtawesome.icon('fa.star', color='white'), "关注我们")
        self.left_button_8.setObjectName('left_button')
        self.left_button_8.clicked.connect(self.feedback)
        self.left_button_9 = QPushButton(qtawesome.icon('fa.question', color='white'), "遇到问题")
        self.left_button_9.setObjectName('left_button')
        self.left_button_9.clicked.connect(self.feedback)
        self.left_xxx = QPushButton(" ")
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)
        self.right_bar_widget = QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout = QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QLabel(' '*60+'欢迎使用智能车辆检测系统')

        self.search_icon.setFont(qtawesome.font('fa', 16))

        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                border:none;
                font-size:1000px;
                font-style:normal
                font-weight:bold;
                color:#BDC8E2;
                font:bold normal 1000px "Helvetica Neue";
            }
        ''')
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
    #点击百度地图打开网址
    def baidumap(self):
        try:
            webbrowser.get('chrome').open_new_tab('https://map.baidu.com')
        except Exception as e:
            webbrowser.open_new_tab('https://map.baidu.com')
    def trancal(self):
        self.cal=calendar()
        self.cal.show()
    def feedback(self):
        try:
            webbrowser.get('chrome').open_new_tab('https://github.com')
        except Exception as e:
            webbrowser.open_new_tab('https://github.com')
    def videoplay(self):
        self.video=m_window()
        self.video.show()
    def view(self):
        self.wri=det()
        self.wri.show()
def main():
    app = QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()