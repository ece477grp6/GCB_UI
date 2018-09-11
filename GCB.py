from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from mainwindow import *



if __name__ == '__main__':

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
