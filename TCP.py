from PyQt5.QtCore import *
import select
import socket
import time
import math

class TCPThread(QThread):
    msgGiven = pyqtSignal()

    def __init__(self, parent = None):
        QThread.__init__(self)
        self.rspeed = 0
        self.lspeed = 0
        self.speedl = 0
        self.belt = 1
        self.inr=0.00001

    def run(self):
        x = 1
        re_connect = True
        # msg = "11222"
        while True:
            msg = str(self.lspeed)+","+str(self.rspeed)+","+str(self.belt)
            # rcv_data = "4026.872,N,08652.031,E,022.4,23,-72"
            # print(rcv_data)
            # self.process_data(rcv_data)
            # time.sleep(1)
            try:
                if re_connect:
                    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # self.s.connect(("128.46.96.229", 5050))
                    self.s.connect(("192.168.0.100", 333))
                    self.s.setblocking(0)
                    re_connect = False
                sent = self.s.sendall(msg.encode())
                if sent == 0:
                    logging.warning("socket connection broken")
                    re_connect = True
                print("msg to the boat:", msg)
                ready = select.select([self.s], [], [], 5)
                if ready[0]:
                    rcv_data = self.s.recv(1024)
                    self.process_data(rcv_data.decode("utf-8"))
                    print("Data received from the boat:", rcv_data)
                    time.sleep(1)
                else:
                    re_connect = True
            except:
                print("error")
                time.sleep(1)
    
    def process_data(self, rcv_data):
        data = rcv_data.split(",")
        print(data)
        self.gps_x = int(float(data[0])/100)+(float(data[0])%100)/60
        if data[1] is "S": self.gps_x = -self.gps_x
        self.gps_y = int(float(data[2])/100)+(float(data[2])%100)/60
        if data[3] is "E": self.gps_y = -self.gps_y
        self.angle = math.atan(int(data[5])/int(data[6]))/math.pi*180
        print("angle = ",self.angle)
        # for testing
        self.inr+=0.00001
        self.gps_x = self.gps_x + self.inr
        self.gps_y = self.gps_y + self.inr

        print("GPS coords = ", self.gps_x, self.gps_y)
        self.msgGiven.emit()
