from mainwindow import *
import os

if __name__ == '__main__':
	if os.path.exists("GCB.log"):
		os.remove("GCB.log")
	logging.basicConfig(filename='GCB.log',level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
	app = QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()

