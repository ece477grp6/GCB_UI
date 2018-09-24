from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MapWidget import *
from mainwindowGUI import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.setAcceptDrops(True)
		self.map = MapWidget()
		self.verticalLayout_2.insertWidget(0,self.map)
		self.verticalLayout_2.setStretch(0, 5)
		self.verticalLayout_2.setStretch(1, 3)
		self.map.markerAdded.connect(self.onAddMarker)
		self.map.markerRemoved.connect(self.onRmMarker)
		QMetaObject.connectSlotsByName(self.map)


	# def _callback(self, result):
	# 	print(result)
	@pyqtSlot(float, float)
	def onAddMarker(lat, lng):
		print("Marker Added: ", lat, lng);
	
	@pyqtSlot(float, float)
	def onRmMarker(lat, lng):
		print("Marker Removed: ", lat, lng);

	# 	self.map.page().runJavaScript("GetMarkers()", self._callback)


		
