from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from qgmap # Retrived from https://github.com/eyllanesc/qMap
from mainwindow import Ui_MainWindow
<<<<<<< HEAD
from qgmap.common import QGoogleMap

qgmap.use("PyQt5")
=======
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtWebEngine import QWebEngineSettings
from PyQt5.QtWebKitWidgets import QWebPage, QWebView
>>>>>>> baea7c106f17dbf2309fe8ac75d774aeee7a2081


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()


if __name__ == '__main__':

    app = QApplication([])
    window = MainWindow()
    app.exec_()
