from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from map.MapWidget import *
from mainwindowGUI import Ui_MainWindow
from decimal import Decimal


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.setAcceptDrops(True)
		self.map = MapWidget()
		self.map.setup(self.listWidget)
		self.verticalLayout_2.insertWidget(0,self.map)
		self.verticalLayout_2.setStretch(0, 5)
		self.verticalLayout_2.setStretch(1, 3)
		self.pushButton_clearMarkers.pressed.connect(self.clearMarkers)
		self.pushButton_loadFile.pressed.connect(self.openFileNameDialog)

	def clearMarkers(self):
		self.map.page().runJavaScript("clearMarkers()");
		

	def openFileNameDialog(self):    
		fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;txt Files (*.txt)")
		if fileName:
			self.clearMarkers()
			lines = [line.split(',') for line in open(fileName)]
			lines = [(line[0].strip(), line[1].strip()) for line in lines]
			for lat, lng in lines:
				self.map.page().runJavaScript("addMarkerLatlng(%s, %s)" %(lat,lng));


		
