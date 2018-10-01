from mainwindow import *
import os
import socket
from TCP import *

if __name__ == '__main__':
	# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# s.connect(("128.46.96.229", 5050))
	# sent = s.sendall('4654653'.encode())
	# if sent == 0:
	# 	raise RuntimeError("socket connection broken")
	# data = s.recv(1024)
	# print(data)
	if os.path.exists("GCB.log"):
		os.remove("GCB.log")
	logging.basicConfig(filename='GCB.log',level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
	tcp = TCPThread()
	tcp.start()
	app = QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()

