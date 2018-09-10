from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from mainwindow import Ui_MainWindow
import sys
sys.path.insert(0, "./qMap/")
import qgmap # Retrived from https://github.com/eyllanesc/qMap
from qgmap.common import QGoogleMap

qgmap.use("PyQt5")


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()


if __name__ == '__main__':

    app = QApplication([])
    window = MainWindow()
    app.exec_()
