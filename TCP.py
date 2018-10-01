from PyQt5.QtCore import *
import threading
import time
import socket

class TCPThread(threading.Thread):
	msgGiven = pyqtSignal(float)


	def run(self):
		x = 1
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("128.46.96.229", 5050))
		while True:
			print(x, ' 46543')
			sent = s.sendall('46543'.encode())
			if sent == 0:
				logging.warning("socket connection broken")
			# time.sleep(5)
			x = x+1
			data = s.recv(1024)
			print(data)
		# print("{} started!".format(self.getName()))
		# time.sleep(1)
		# print("{} finished!".format(self.getName()))
