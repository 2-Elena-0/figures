import sys
from random import randint
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.do_paint = False
        self.button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter(self)
            painter.begin(self)
            painter.setPen(QtGui.QPen(QtGui.QColor(randint(0, 256), randint(0, 256), randint(0, 256)), 5))
            coords = [randint(70, 440), randint(0, 290)]
            size = randint(2, 200)
            if int(coords[0]) + size > 450:
                size = 450 - int(coords[0])
            if int(coords[1]) + size > 301:
                size = 301 - int(coords[1])
            painter.drawEllipse(coords[0], coords[1], size, size)
            painter.end()

    def paint(self):
        self.do_paint = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
