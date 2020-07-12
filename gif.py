import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class video(QWidget):
    def __init__(self):
        super().__init__()
        self.label=QLabel('',self)
        self.setFixedSize(1080,720)
        self.setWindowFlag(Qt.Dialog | Qt.CustomizeWindowHint)
        self.movie=QMovie('H:/video-1.avi')
        self.lable.setMovie(self.movie)
        self.movie.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = video()
    main.show()
    sys.exit(app.exec_())
