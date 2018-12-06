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
        self.mode = 0
        self.markers =[]
        self.curr_marker = 0
        self.gps_x = 0
        self.gps_y = 0
        self.adc_init = []
        self.ct = 0
        self.speed = 0

    def run(self):
        x = 1
        self.re_connect = True
        # msg = "11222"
        while True:
            msg = self.format_msg()
            # rcv_data = "4026.87226,N,08652.02631,E,0.134,23,-72"
            # rcv_data = "0000.00000,N,00000.00000,E,0.000,23,-72"
            # print(rcv_data)
            # self.process_data(rcv_data)
            # time.sleep(1)
            try:
                if self.re_connect:
                    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    # self.s.connect(("128.46.96.229", 5050))
                    # self.s.connect(("192.168.0.100", 333))
                    self.s.connect(("73.103.73.130", 8686))
                    # self.s.setblocking(0)
                    self.re_connect = False
                sent = self.s.sendall(msg.encode())
                if sent == 0:
                    logging.warning("socket connection broken")
                    self.re_connect = True
                print("msg to the boat:", msg)
                # ready = select.select([self.s], [], [], 5)
                # if ready[0]:
                rcv_data = self.s.recv(1024)
                print(rcv_data)
                # if rcv_data == b'OK':
                #     print("OK")
                #     ready = select.select([self.s], [], [], 100)
                #     if ready[0]:
                #         rcv_data = self.s.recv(1024)
                self.process_data(rcv_data.decode("utf-8"))
                # self.process_data("4026.87226,N,08652.02631,E,0.134,23,-72")
                print("Data received from the boat:", rcv_data)
                time.sleep(1)
                # else:
                #     self.re_connect = True
            except Exception as e:
                print(e)
                time.sleep(1)

    def format_msg(self):
        if self.mode is 2:
            return "%02d%02d%d" % (self.lspeed, self.rspeed, self.belt)
        elif self.mode is 0:
            return "0000"+str(self.belt)
        else:
            # p12 = pow(self.gps_x-self.prev_x, 2) + pow(self.gps_y-self.prev_y, 2)
            # p13 = pow(self.markers[self.curr_marker][0]-self.prev_x, 2) + pow(self.markers[self.curr_marker][1]-self.prev_y, 2)
            # p23 = pow(self.gps_x - markers[self.curr_marker][0], 2) + pow(self.gps_y - markers[self.curr_marker][1], 2)
            # curr_angle = math.acos((p12+p13-p23)/(2*math.sqrt(p12)*math.sqrt(p13)))/math.pi*180
            # pass
            if(self.gps_x - self.prev_x > 0):
                if(self.markers[self.curr_marker][1] > self.gps_y):
                    self.lspeed = 8
                    self.rspeed = 7
                    return "0807"+str(self.belt)
                else:
                    self.lspeed = 7
                    self.rspeed = 8
                    return "0708"+str(self.belt)
            else:
                if(self.markers[self.curr_marker][1] > self.gps_y):
                    self.lspeed = 7
                    self.rspeed = 8
                    return "0708"+str(self.belt)
                else:
                    self.lspeed = 8
                    self.rspeed = 7
                    return "0807"+str(self.belt)


    
    def process_data(self, rcv_data):
        data = rcv_data.split(",")
        print(data)
        self.prev_x = self.gps_x
        self.prev_y = self.gps_y
        self.gps_x = int(float(data[0])/100)+(float(data[0])%100)/60
        if data[1] is "S": self.gps_x = -self.gps_x
        self.gps_y = int(float(data[2])/100)+(float(data[2])%100)/60
        if data[3] is "E": self.gps_y = -self.gps_y
        self.speed = data[4]
        self.angle = math.atan(int(data[5])/int(data[6]))/math.pi*180
        print("angle = ",self.angle)
        if self.adc_init == []:
            for x in range(7, 12):
                self.adc_init.append(int(data[x]))
        else:
            if self.belt == 1:
                for x in range(7, 12):
                    if abs(self.adc_init[x-7] - int(data[x])) > 1000:
                        self.ct = self.ct + 1
                if self.ct >= 2:
                    self.belt = 0
        self.battery1 = 0
        self.battery2 = 0
        self.battery3 = 0
        for x in range(12, 15):
            self.battery1 = self.battery1 + int(data[x])
        self.battery1 = self.battery1 / 3
        for x in range(15, 18):
            self.battery2 = self.battery2 + int(data[x])
        self.battery2 = self.battery2 / 3
        for x in range(18, 21):
            self.battery3 = self.battery3 + int(data[x])
        self.battery3 = self.battery3 / 3
        # ct = 0
        # for x in range(7, 11):
        #     if int(data[x]) < 1000:
        #         ct = ct + 1
        # if ct >= 2:
        #     self.belt = 0

        # for testing
        self.inr+=0.00001
        self.gps_x = self.gps_x + self.inr
        self.gps_y = self.gps_y + self.inr

        print("GPS coords = ", self.gps_x, self.gps_y)
        self.msgGiven.emit()
