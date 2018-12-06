from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QListWidgetItem
import logging

class MapWidget(QWebEngineView):
  markersChanged = pyqtSignal()

  def __init__(self):
    super().__init__()
    self.setUrl(QUrl("about:blank"))
    self.channel = QWebChannel(self.page())
    self.page().setWebChannel(self.channel)
    self.channel.registerObject("jshelper", self)
    self.load(QUrl.fromLocalFile(QDir.current().filePath("./map/qgmap.html")))
    QMetaObject.connectSlotsByName(self)
    self.markers = []
    logging.info("MapWidget: Initialized MapWidget")

  def setup(self, listWidget):
    self.listWidget = listWidget

  @pyqtSlot(float, float)
  def markerAdded(self, lat, lng):
    self.markers.append((lat, lng))
    item = QListWidgetItem("(%s, %s)"%(lat, lng))
    item.setFlags(item.flags()& (~Qt.ItemIsSelectable))
    self.listWidget.addItem(item)
    logging.info("MapWidget: Marker (%s, %s) Added"%(lat, lng))
    logging.info("MapWidget: Markers: "+str(self.markers))
    self.markersChanged.emit()

  @pyqtSlot(float, float)
  def markerRemoved(self, lat, lng):
    self.markers.remove((lat, lng))
    self.listWidget.takeItem(len(self.markers))
    logging.info("MapWidget: Marker (%s, %s) Removed"%(lat, lng))
    logging.info("MapWidget: Markers: "+str(self.markers))
    self.markersChanged.emit()

  @pyqtSlot()
  def clearAllMarkers(self):
    self.markers.clear()
    self.listWidget.clear()
    logging.info("MapWidget: Markers cleared")
    self.markersChanged.emit()