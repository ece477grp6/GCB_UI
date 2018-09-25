from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from mainwindow import *
from urllib import request
import http.client as httplib

if __name__ == '__main__':

	# conn = httplib.HTTPConnection("128.46.96.229:90")
	# conn.request("GET", "/123")
	# r1 = conn.getresponse()
	# data1 = r1.read()
	# print(data1)
	
	# response = request.urlopen('http://128.46.96.229:90')
	# html = response.read()
	# print(html)
	app = QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()
