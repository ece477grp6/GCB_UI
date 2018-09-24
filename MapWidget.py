from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal, QUrl, QDir, QMetaObject

class MapWidget(QWebEngineView):
    def __init__(self):

        super().__init__()
        self.setUrl(QUrl("about:blank"))
        self.channel = QWebChannel(self.page())
        self.page().setWebChannel(self.channel)
        self.channel.registerObject("qtWidget", self)
        self.load(QUrl.fromLocalFile(QDir.current().filePath("qgmap.html")))
        

    markerAdded = pyqtSignal(float, float)
    markerRemoved = pyqtSignal(float, float)
