from mainwindowGUI import *
from map.MapWidget import *
from CompassWidget import *
import logging


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.setAcceptDrops(True)

		self.map = MapWidget()
		self.map.setup(self.listWidget)
		self.verticalLayout_map.insertWidget(0,self.map)
		self.verticalLayout_map.setStretch(0, 5)
		self.verticalLayout_map.setStretch(1, 3)

		self.compass = CompassWidget()
		self.verticalLayout_compass.insertWidget(0,self.compass)
		self.pushButton_belt_on = 1

		self.pushButton_clearMarkers.pressed.connect(self.clearMarkers)
		self.pushButton_loadFile.pressed.connect(self.openFileNameDialog)
		self.pushButton_saveToFile.pressed.connect(self.saveFileDialog)
		self.pushButton_belt.pressed.connect(self.toogleConveyorBelt)
		logging.info("MainWindow: Initialized MainWindow")

	def toogleConveyorBelt(self):
		if self.pushButton_belt_on:
			self.pushButton_belt.setText("Conveyor Belt On")
			logging.info("MainWindow: Conveyor Belt is Off")
		else:
			self.pushButton_belt.setText("Conveyor Belt Off")
			logging.info("MainWindow: Conveyor Belt is On")
		self.pushButton_belt_on = 1 - self.pushButton_belt_on

	def clearMarkers(self):
		self.map.page().runJavaScript("clearMarkers()");
		
	def saveFileDialog(self):
		fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)")
		if fileName:
			open(fileName, 'w').writelines("\n".join(["%s, %s"%(lat,lng) for lat,lng in self.map.markers]))
			logging.info("MainWindow: Coords saved to %s"%(fileName))

	def openFileNameDialog(self):    
		fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Text Files (*.txt)")
		if fileName:
			self.clearMarkers()
			lines = [line.split(',') for line in open(fileName)]
			lines = [(line[0].strip(), line[1].strip()) for line in lines]
			for lat, lng in lines:
				self.map.page().runJavaScript("addMarkerLatlng(%s, %s)" %(lat,lng));
			logging.info("MainWindow: Coords loaded from %s"%(fileName))


		
