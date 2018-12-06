from mainwindowGUI import *
from map.MapWidget import *
from CompassWidget import *
from TCP import *
# from serialCompass import *
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
        self.compass.angle = 10
        self.verticalLayout_compass.insertWidget(0,self.compass)

        self.pushButton_clearMarkers.pressed.connect(self.clearMarkers)
        self.pushButton_loadFile.pressed.connect(self.openFileNameDialog)
        self.pushButton_saveToFile.pressed.connect(self.saveFileDialog)
        self.pushButton_belt.pressed.connect(self.toogleConveyorBelt)
        self.pushButton_right.pressed.connect(self.goRight)
        self.pushButton_left.pressed.connect(self.goLeft)
        self.pushButton_straight.pressed.connect(self.goStraight)
        self.pushButton_speedU.pressed.connect(self.goUp)
        self.pushButton_speedD.pressed.connect(self.goDown)
        self.pushButton_start.pressed.connect(self.start)
        self.pushButton_stop.pressed.connect(self.stop)
        self.tabWidget.currentChanged.connect(self.onChange)
        # self.pushButton_clearPath.pressed.connect(self)
        
        self.leftClicked = False
        self.rightClicked = False
        logging.info("MainWindow: Initialized MainWindow")

        self.tcp = TCPThread()
        self.tcp.start()
        self.tcp.msgGiven.connect(self.update_data)
        self.label_info.setText("Connecting Wi-Fi......")
        self.map.markersChanged.connect(self.update_markers)

    def update_markers(self):
        self.tcp.markers = self.map.markers

    def start(self):
        self.tcp.mode = 1
        self.tcp.curr_marker = 0
        self.map.page().runJavaScript("lock()")

    def stop(self):
        self.tcp.mode = 0
        self.map.page().runJavaScript("unlock()")

    def onChange(self):
        if self.tabWidget.currentIndex() == 1:
            self.tcp.mode = 2

    def update_data(self):
        if self.tcp.re_connect is True:
            self.label_info.setText("Reconecting Wi-Fi......")
            return
        if self.tcp.gps_x <= 0.1 and self.tcp.gps_y <= 0.1:
            self.label_info.setText("Waiting for GPS to connect......")
            return
        self.label_info.setText("")
        self.map.page().runJavaScript("setCenter(%f, %f)" %(self.tcp.gps_x, self.tcp.gps_y))
        self.map.page().runJavaScript("updateCurrentPos(%f, %f)" %(self.tcp.gps_x, self.tcp.gps_y))
        self.compass.angle = self.tcp.angle
        self.label_heading_info.setText(str(self.tcp.angle))
        self.label_coords_info.setText("%s,%s"%(self.tcp.gps_x, self.tcp.gps_y))
        self.label_battery_info.setText("%d,%d,%d" %(self.tcp.battery1/4095*4.2, self.tcp.battery2/4095*4.2, self.tcp.battery3/4095*4.2))
        if self.tcp.ct >= 2:
            self.label_storage_info.setText("full")
        else:
            self.label_storage_info.setText("not full")
        self.label_speed_info.setText(self.tcp.speed)
        self.label_1left_motor_info.setText(str(self.tcp.lspeed))
        self.label_right_motor_info.setText(str(self.tcp.rspeed))


    def setSpeed(self):
        val = self.tcp.speedl - 6
        if val < 0:
            val = 0
        self.horizontalSlider.setValue(val)
        if self.tcp.speedl == 0:
            self.tcp.rspeed = 0
            self.tcp.lspeed = 0
            return
        if self.leftClicked == True:
            if self.tcp.speedl == 7:
                self.tcp.rspeed = 8
                self.tcp.lspeed = 7
            elif self.tcp.speedl == 12:
                self.tcp.lspeed = 11
                self.tcp.rspeed = 12
            else:
                self.tcp.rspeed = self.tcp.speedl + 1
                self.tcp.lspeed = self.tcp.speedl - 1
        elif self.rightClicked == True:
            if self.tcp.speedl == 7:
                self.tcp.lspeed = 8
                self.tcp.rspeed = 7
            elif self.tcp.speedl == 12:
                self.tcp.rspeed = 11
                self.tcp.lspeed = 12
            else:
                self.tcp.lspeed = self.tcp.speedl + 1
                self.tcp.rspeed = self.tcp.speedl - 1
        else:
            self.tcp.lspeed = self.tcp.speedl
            self.tcp.rspeed = self.tcp.speedl
        print(self.tcp.lspeed, " ",self.tcp.rspeed)

    def goUp(self):
        if self.tcp.speedl == 12:
            return
        if self.tcp.speedl == 0:
            self.tcp.speedl = 7
        else:
            self.tcp.speedl = self.tcp.speedl + 1
        self.setSpeed()

    def goDown(self):
        if self.tcp.speedl == 0:
            return
        if self.tcp.speedl == 7:
            self.tcp.speedl = 0
        else:
            self.tcp.speedl = self.tcp.speedl - 1
        self.setSpeed()

    def goLeft(self):
        if self.tcp.speedl == 0 or self.tcp.rspeed > self.tcp.lspeed :
            return
        self.leftClicked = True
        self.rightClicked = False
        self.setSpeed()

    def goRight(self):
        if self.tcp.speedl == 0 or self.tcp.rspeed < self.tcp.lspeed :
            return
        self.rightClicked = True
        self.leftClicked = False
        self.setSpeed()

    def goStraight(self):
        if self.tcp.speedl == 0 or self.tcp.rspeed == self.tcp.lspeed :
            return
        self.rightClicked = False
        self.leftClicked = False
        self.setSpeed()

    def toogleConveyorBelt(self):
        if self.tcp.belt:
            self.pushButton_belt.setText("Conveyor Belt On")
            logging.info("MainWindow: Conveyor Belt is Off")
        else:
            self.pushButton_belt.setText("Conveyor Belt Off")
            logging.info("MainWindow: Conveyor Belt is On")
        self.tcp.belt = 1 - self.tcp.belt

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


        
