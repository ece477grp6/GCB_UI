from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QListWidgetItem

class MapWidget(QWebEngineView):

  markerAddedSignal = pyqtSignal()

  def __init__(self):
    super().__init__()
    self.setUrl(QUrl("about:blank"))
    self.channel = QWebChannel(self.page())
    self.page().setWebChannel(self.channel)
    self.channel.registerObject("jshelper", self)
    self.load(QUrl.fromLocalFile(QDir.current().filePath("./map/qgmap.html")))
    QMetaObject.connectSlotsByName(self)
    self.markers = []

  def setup(self, listWidget):
    self.listWidget = listWidget

  @pyqtSlot(float, float)
  def markerAdded(self, lat, lng):
    self.markers.append((lat, lng))
    print("Marker Added: ", lat, lng)
    print("Markers:", self.markers)
    item = QListWidgetItem("(%s, %s)"%(lat, lng))
    item.setFlags(item.flags()& (~Qt.ItemIsSelectable))
    self.listWidget.addItem(item)

  @pyqtSlot(float, float)
  def markerRemoved(self, lat, lng):
    self.markers.remove((lat, lng))
    print("Marker Removed: ", lat, lng)
    print("Markers:", self.markers)
    self.listWidget.takeItem(len(self.markers))

  @pyqtSlot()
  def clearAllMarkers(self):
    self.markers.clear()
    self.listWidget.clear()