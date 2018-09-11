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
		self.widget = MapWidget()
		self.verticalLayout_2.insertWidget(0,self.widget)
		self.verticalLayout_2.setStretch(0, 5)
		self.verticalLayout_2.setStretch(1, 3)


		
