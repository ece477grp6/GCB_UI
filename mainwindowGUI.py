# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_all = QtWidgets.QHBoxLayout()
        self.horizontalLayout_all.setObjectName("horizontalLayout_all")
        self.verticalLayout_map = QtWidgets.QVBoxLayout()
        self.verticalLayout_map.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_map.setSpacing(10)
        self.verticalLayout_map.setObjectName("verticalLayout_map")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_fixRoute = QtWidgets.QWidget()
        self.tab_fixRoute.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.tab_fixRoute.setObjectName("tab_fixRoute")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_fixRoute)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_tabFixRoute = QtWidgets.QVBoxLayout()
        self.verticalLayout_tabFixRoute.setObjectName("verticalLayout_tabFixRoute")
        self.horizontalLayout_button = QtWidgets.QHBoxLayout()
        self.horizontalLayout_button.setSpacing(20)
        self.horizontalLayout_button.setObjectName("horizontalLayout_button")
        self.pushButton_loadFile = QtWidgets.QPushButton(self.tab_fixRoute)
        self.pushButton_loadFile.setObjectName("pushButton_loadFile")
        self.horizontalLayout_button.addWidget(self.pushButton_loadFile)
        self.pushButton_saveToFile = QtWidgets.QPushButton(self.tab_fixRoute)
        self.pushButton_saveToFile.setObjectName("pushButton_saveToFile")
        self.horizontalLayout_button.addWidget(self.pushButton_saveToFile)
        self.pushButton_clearMarkers = QtWidgets.QPushButton(self.tab_fixRoute)
        self.pushButton_clearMarkers.setObjectName("pushButton_clearMarkers")
        self.horizontalLayout_button.addWidget(self.pushButton_clearMarkers)
        self.verticalLayout_tabFixRoute.addLayout(self.horizontalLayout_button)
        self.listWidget = QtWidgets.QListWidget(self.tab_fixRoute)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_tabFixRoute.addWidget(self.listWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_tabFixRoute)
        self.tabWidget.addTab(self.tab_fixRoute, "")
        self.tab_manual = QtWidgets.QWidget()
        self.tab_manual.setObjectName("tab_manual")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_manual)
        self.horizontalLayout_5.setContentsMargins(30, 50, 30, 50)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setSpacing(80)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_straight = QtWidgets.QPushButton(self.tab_manual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_straight.sizePolicy().hasHeightForWidth())
        self.pushButton_straight.setSizePolicy(sizePolicy)
        self.pushButton_straight.setAutoFillBackground(False)
        self.pushButton_straight.setCheckable(False)
        self.pushButton_straight.setObjectName("pushButton_straight")
        self.verticalLayout_4.addWidget(self.pushButton_straight)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_left = QtWidgets.QPushButton(self.tab_manual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_left.sizePolicy().hasHeightForWidth())
        self.pushButton_left.setSizePolicy(sizePolicy)
        self.pushButton_left.setCheckable(False)
        self.pushButton_left.setObjectName("pushButton_left")
        self.horizontalLayout_7.addWidget(self.pushButton_left)
        self.pushButton_right = QtWidgets.QPushButton(self.tab_manual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_right.sizePolicy().hasHeightForWidth())
        self.pushButton_right.setSizePolicy(sizePolicy)
        self.pushButton_right.setCheckable(False)
        self.pushButton_right.setObjectName("pushButton_right")
        self.horizontalLayout_7.addWidget(self.pushButton_right)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_speedl = QtWidgets.QLabel(self.tab_manual)
        self.label_speedl.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speedl.setObjectName("label_speedl")
        self.verticalLayout_6.addWidget(self.label_speedl)
        self.horizontalSlider = QtWidgets.QSlider(self.tab_manual)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider.setMaximum(6)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_6.addWidget(self.horizontalSlider)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.pushButton_speedU = QtWidgets.QPushButton(self.tab_manual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_speedU.sizePolicy().hasHeightForWidth())
        self.pushButton_speedU.setSizePolicy(sizePolicy)
        self.pushButton_speedU.setCheckable(False)
        self.pushButton_speedU.setObjectName("pushButton_speedU")
        self.verticalLayout_5.addWidget(self.pushButton_speedU)
        self.pushButton_speedD = QtWidgets.QPushButton(self.tab_manual)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_speedD.sizePolicy().hasHeightForWidth())
        self.pushButton_speedD.setSizePolicy(sizePolicy)
        self.pushButton_speedD.setCheckable(False)
        self.pushButton_speedD.setObjectName("pushButton_speedD")
        self.verticalLayout_5.addWidget(self.pushButton_speedD)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 2)
        self.verticalLayout_5.setStretch(2, 2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5.setStretch(0, 7)
        self.horizontalLayout_5.setStretch(1, 2)
        self.tabWidget.addTab(self.tab_manual, "")
        self.verticalLayout_map.addWidget(self.tabWidget)
        self.horizontalLayout_all.addLayout(self.verticalLayout_map)
        self.verticalLayout_infoAll = QtWidgets.QVBoxLayout()
        self.verticalLayout_infoAll.setObjectName("verticalLayout_infoAll")
        self.graphicsView_camera = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_camera.setObjectName("graphicsView_camera")
        self.verticalLayout_infoAll.addWidget(self.graphicsView_camera)
        self.horizontalLayout_infoPart = QtWidgets.QHBoxLayout()
        self.horizontalLayout_infoPart.setSpacing(0)
        self.horizontalLayout_infoPart.setObjectName("horizontalLayout_infoPart")
        self.verticalLayout_compass = QtWidgets.QVBoxLayout()
        self.verticalLayout_compass.setSpacing(10)
        self.verticalLayout_compass.setObjectName("verticalLayout_compass")
        self.pushButton_belt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_belt.sizePolicy().hasHeightForWidth())
        self.pushButton_belt.setSizePolicy(sizePolicy)
        self.pushButton_belt.setCheckable(False)
        self.pushButton_belt.setChecked(False)
        self.pushButton_belt.setObjectName("pushButton_belt")
        self.verticalLayout_compass.addWidget(self.pushButton_belt)
        self.horizontalLayout_infoPart.addLayout(self.verticalLayout_compass)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_infoPart.addItem(spacerItem)
        self.gridLayout_info = QtWidgets.QGridLayout()
        self.gridLayout_info.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_info.setContentsMargins(-1, 10, -1, 10)
        self.gridLayout_info.setHorizontalSpacing(20)
        self.gridLayout_info.setObjectName("gridLayout_info")
        self.label_right_motor = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_right_motor.sizePolicy().hasHeightForWidth())
        self.label_right_motor.setSizePolicy(sizePolicy)
        self.label_right_motor.setObjectName("label_right_motor")
        self.gridLayout_info.addWidget(self.label_right_motor, 5, 0, 1, 1)
        self.label_heading = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_heading.sizePolicy().hasHeightForWidth())
        self.label_heading.setSizePolicy(sizePolicy)
        self.label_heading.setObjectName("label_heading")
        self.gridLayout_info.addWidget(self.label_heading, 0, 0, 1, 1)
        self.label_battery_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_battery_info.sizePolicy().hasHeightForWidth())
        self.label_battery_info.setSizePolicy(sizePolicy)
        self.label_battery_info.setObjectName("label_battery_info")
        self.gridLayout_info.addWidget(self.label_battery_info, 2, 1, 1, 1)
        self.label_right_motor_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_right_motor_info.sizePolicy().hasHeightForWidth())
        self.label_right_motor_info.setSizePolicy(sizePolicy)
        self.label_right_motor_info.setObjectName("label_right_motor_info")
        self.gridLayout_info.addWidget(self.label_right_motor_info, 5, 1, 1, 1)
        self.label_speed = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_speed.sizePolicy().hasHeightForWidth())
        self.label_speed.setSizePolicy(sizePolicy)
        self.label_speed.setObjectName("label_speed")
        self.gridLayout_info.addWidget(self.label_speed, 4, 0, 1, 1)
        self.label_coords = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_coords.sizePolicy().hasHeightForWidth())
        self.label_coords.setSizePolicy(sizePolicy)
        self.label_coords.setObjectName("label_coords")
        self.gridLayout_info.addWidget(self.label_coords, 1, 0, 1, 1)
        self.label_coords_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_coords_info.sizePolicy().hasHeightForWidth())
        self.label_coords_info.setSizePolicy(sizePolicy)
        self.label_coords_info.setTextFormat(QtCore.Qt.AutoText)
        self.label_coords_info.setWordWrap(True)
        self.label_coords_info.setObjectName("label_coords_info")
        self.gridLayout_info.addWidget(self.label_coords_info, 1, 1, 1, 1)
        self.label_speed_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_speed_info.sizePolicy().hasHeightForWidth())
        self.label_speed_info.setSizePolicy(sizePolicy)
        self.label_speed_info.setObjectName("label_speed_info")
        self.gridLayout_info.addWidget(self.label_speed_info, 4, 1, 1, 1)
        self.label_storage_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_storage_info.sizePolicy().hasHeightForWidth())
        self.label_storage_info.setSizePolicy(sizePolicy)
        self.label_storage_info.setObjectName("label_storage_info")
        self.gridLayout_info.addWidget(self.label_storage_info, 3, 1, 1, 1)
        self.label_storage = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_storage.sizePolicy().hasHeightForWidth())
        self.label_storage.setSizePolicy(sizePolicy)
        self.label_storage.setObjectName("label_storage")
        self.gridLayout_info.addWidget(self.label_storage, 3, 0, 1, 1)
        self.label_battery = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_battery.sizePolicy().hasHeightForWidth())
        self.label_battery.setSizePolicy(sizePolicy)
        self.label_battery.setObjectName("label_battery")
        self.gridLayout_info.addWidget(self.label_battery, 2, 0, 1, 1)
        self.label_left_motor = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_left_motor.sizePolicy().hasHeightForWidth())
        self.label_left_motor.setSizePolicy(sizePolicy)
        self.label_left_motor.setObjectName("label_left_motor")
        self.gridLayout_info.addWidget(self.label_left_motor, 6, 0, 1, 1)
        self.label_1left_motor_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1left_motor_info.sizePolicy().hasHeightForWidth())
        self.label_1left_motor_info.setSizePolicy(sizePolicy)
        self.label_1left_motor_info.setObjectName("label_1left_motor_info")
        self.gridLayout_info.addWidget(self.label_1left_motor_info, 6, 1, 1, 1)
        self.label_heading_info = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_heading_info.sizePolicy().hasHeightForWidth())
        self.label_heading_info.setSizePolicy(sizePolicy)
        self.label_heading_info.setObjectName("label_heading_info")
        self.gridLayout_info.addWidget(self.label_heading_info, 0, 1, 1, 1)
        self.horizontalLayout_infoPart.addLayout(self.gridLayout_info)
        self.horizontalLayout_infoPart.setStretch(1, 1)
        self.horizontalLayout_infoPart.setStretch(2, 8)
        self.verticalLayout_infoAll.addLayout(self.horizontalLayout_infoPart)
        self.verticalLayout_infoAll.setStretch(0, 5)
        self.verticalLayout_infoAll.setStretch(1, 3)
        self.horizontalLayout_all.addLayout(self.verticalLayout_infoAll)
        self.horizontalLayout_all.setStretch(0, 5)
        self.horizontalLayout_all.setStretch(1, 4)
        self.horizontalLayout.addLayout(self.horizontalLayout_all)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUser_Manual = QtWidgets.QAction(MainWindow)
        self.actionUser_Manual.setObjectName("actionUser_Manual")
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.actionView_Logging = QtWidgets.QAction(MainWindow)
        self.actionView_Logging.setObjectName("actionView_Logging")
        self.menuHelp.addAction(self.actionUser_Manual)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Us)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Garbage Collecting Boat"))
        self.pushButton_loadFile.setText(_translate("MainWindow", "Load From File"))
        self.pushButton_saveToFile.setText(_translate("MainWindow", "Save To File"))
        self.pushButton_clearMarkers.setText(_translate("MainWindow", "Clear All Markers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_fixRoute), _translate("MainWindow", "Fix-Route Mode"))
        self.pushButton_straight.setText(_translate("MainWindow", "Straight"))
        self.pushButton_left.setText(_translate("MainWindow", "Left"))
        self.pushButton_right.setText(_translate("MainWindow", "Right"))
        self.label_speedl.setText(_translate("MainWindow", "Speed Level"))
        self.pushButton_speedU.setText(_translate("MainWindow", "Speed Up"))
        self.pushButton_speedD.setText(_translate("MainWindow", "Speed Down"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_manual), _translate("MainWindow", "Manual Mode"))
        self.pushButton_belt.setText(_translate("MainWindow", "Conveyor Belt Off"))
        self.label_right_motor.setText(_translate("MainWindow", "Right Motor Load"))
        self.label_heading.setText(_translate("MainWindow", "Heading"))
        self.label_battery_info.setText(_translate("MainWindow", "N/A"))
        self.label_right_motor_info.setText(_translate("MainWindow", "N/A"))
        self.label_speed.setText(_translate("MainWindow", "Speed"))
        self.label_coords.setText(_translate("MainWindow", "Coords"))
        self.label_coords_info.setText(_translate("MainWindow", "N/A"))
        self.label_speed_info.setText(_translate("MainWindow", "N/A"))
        self.label_storage_info.setText(_translate("MainWindow", "N/A"))
        self.label_storage.setText(_translate("MainWindow", "Storage Room"))
        self.label_battery.setText(_translate("MainWindow", "Battery Level"))
        self.label_left_motor.setText(_translate("MainWindow", "Left Motor Load"))
        self.label_1left_motor_info.setText(_translate("MainWindow", "N/A"))
        self.label_heading_info.setText(_translate("MainWindow", "N/A"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionUser_Manual.setText(_translate("MainWindow", "User Manual"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))
        self.actionView_Logging.setText(_translate("MainWindow", "View Logging"))

