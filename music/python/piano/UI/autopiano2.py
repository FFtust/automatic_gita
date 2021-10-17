# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autopiano.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

WHITE_KEY_SIZE = [30, 60]
BLACK_KEY_SIZE = [20, 60]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButtonKey = [None] * 60
        for i in range(6):
            for j in range(12):
                idx = i * 12 + j
                self.pushButtonKey[idx] = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(0, 190, 31, 61))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton.setFont(font)
                self.pushButton.setObjectName("pushButton" + str(idx))
                self.pushButton_4.setStyleSheet("background-color: rgb(8, 8, 8);\n"
        "color: rgb(255, 255, 255);")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 150, 21, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(8, 8, 8);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 150, 21, 51))
        self.pushButton_5.setStyleSheet("background-color: rgb(8, 8, 8);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(90, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(120, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(180, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(140, 150, 21, 51))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(110, 150, 21, 51))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(170, 150, 21, 51))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(210, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(360, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(260, 150, 21, 51))
        self.pushButton_15.setStyleSheet("background-color: rgb(8, 8, 8);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(230, 150, 21, 51))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(330, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(390, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(320, 150, 21, 51))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(350, 150, 21, 51))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(240, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(270, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(300, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(380, 150, 21, 51))
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(420, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(570, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(470, 150, 21, 51))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(440, 150, 21, 51))
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setGeometry(QtCore.QRect(540, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(600, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_31.setGeometry(QtCore.QRect(530, 150, 21, 51))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32.setGeometry(QtCore.QRect(560, 150, 21, 51))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_33.setGeometry(QtCore.QRect(450, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_34.setGeometry(QtCore.QRect(480, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_35.setGeometry(QtCore.QRect(510, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_36.setGeometry(QtCore.QRect(590, 150, 21, 51))
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_37.setGeometry(QtCore.QRect(630, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_38.setGeometry(QtCore.QRect(780, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_39.setGeometry(QtCore.QRect(680, 150, 21, 51))
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_40.setGeometry(QtCore.QRect(650, 150, 21, 51))
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_41.setGeometry(QtCore.QRect(750, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_42.setGeometry(QtCore.QRect(810, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_43.setGeometry(QtCore.QRect(740, 150, 21, 51))
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_44.setGeometry(QtCore.QRect(770, 150, 21, 51))
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_45 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_45.setGeometry(QtCore.QRect(660, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_46.setGeometry(QtCore.QRect(690, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_46.setFont(font)
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_47 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_47.setGeometry(QtCore.QRect(720, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_47.setFont(font)
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_48.setGeometry(QtCore.QRect(800, 150, 21, 51))
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_49.setGeometry(QtCore.QRect(1050, 150, 21, 51))
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_50 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_50.setGeometry(QtCore.QRect(990, 150, 21, 51))
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_51 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_51.setGeometry(QtCore.QRect(930, 150, 21, 51))
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_52 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_52.setGeometry(QtCore.QRect(1060, 190, 31, 61))
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_53 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_53.setGeometry(QtCore.QRect(900, 150, 21, 51))
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_54 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_54.setGeometry(QtCore.QRect(1020, 150, 21, 51))
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_55 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_55.setGeometry(QtCore.QRect(1030, 190, 31, 61))
        self.pushButton_55.setObjectName("pushButton_55")
        self.pushButton_56 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_56.setGeometry(QtCore.QRect(880, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_56.setFont(font)
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_57 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_57.setGeometry(QtCore.QRect(910, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_57.setFont(font)
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_58 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_58.setGeometry(QtCore.QRect(970, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_58.setFont(font)
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_59 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_59.setGeometry(QtCore.QRect(1000, 190, 31, 61))
        self.pushButton_59.setObjectName("pushButton_59")
        self.pushButton_60 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_60.setGeometry(QtCore.QRect(940, 190, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_60.setFont(font)
        self.pushButton_60.setObjectName("pushButton_60")
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 22))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "1#"))
        self.pushButton_5.setText(_translate("MainWindow", "2#"))
        self.pushButton_6.setText(_translate("MainWindow", "4"))
        self.pushButton_7.setText(_translate("MainWindow", "5"))
        self.pushButton_8.setText(_translate("MainWindow", "6"))
        self.pushButton_9.setText(_translate("MainWindow", "7"))
        self.pushButton_10.setText(_translate("MainWindow", "5#"))
        self.pushButton_11.setText(_translate("MainWindow", "4#"))
        self.pushButton_12.setText(_translate("MainWindow", "6#"))
        self.pushButton_13.setText(_translate("MainWindow", "1"))
        self.pushButton_14.setText(_translate("MainWindow", "6"))
        self.pushButton_15.setText(_translate("MainWindow", "2#"))
        self.pushButton_16.setText(_translate("MainWindow", "1#"))
        self.pushButton_17.setText(_translate("MainWindow", "5"))
        self.pushButton_18.setText(_translate("MainWindow", "7"))
        self.pushButton_19.setText(_translate("MainWindow", "4#"))
        self.pushButton_20.setText(_translate("MainWindow", "5#"))
        self.pushButton_21.setText(_translate("MainWindow", "2"))
        self.pushButton_22.setText(_translate("MainWindow", "3"))
        self.pushButton_23.setText(_translate("MainWindow", "4"))
        self.pushButton_24.setText(_translate("MainWindow", "6#"))
        self.pushButton_25.setText(_translate("MainWindow", "1"))
        self.pushButton_26.setText(_translate("MainWindow", "6"))
        self.pushButton_27.setText(_translate("MainWindow", "2#"))
        self.pushButton_28.setText(_translate("MainWindow", "1#"))
        self.pushButton_29.setText(_translate("MainWindow", "5"))
        self.pushButton_30.setText(_translate("MainWindow", "7"))
        self.pushButton_31.setText(_translate("MainWindow", "4#"))
        self.pushButton_32.setText(_translate("MainWindow", "5#"))
        self.pushButton_33.setText(_translate("MainWindow", "2"))
        self.pushButton_34.setText(_translate("MainWindow", "3"))
        self.pushButton_35.setText(_translate("MainWindow", "4"))
        self.pushButton_36.setText(_translate("MainWindow", "6#"))
        self.pushButton_37.setText(_translate("MainWindow", "1"))
        self.pushButton_38.setText(_translate("MainWindow", "6"))
        self.pushButton_39.setText(_translate("MainWindow", "2#"))
        self.pushButton_40.setText(_translate("MainWindow", "1#"))
        self.pushButton_41.setText(_translate("MainWindow", "5"))
        self.pushButton_42.setText(_translate("MainWindow", "7"))
        self.pushButton_43.setText(_translate("MainWindow", "4#"))
        self.pushButton_44.setText(_translate("MainWindow", "5#"))
        self.pushButton_45.setText(_translate("MainWindow", "2"))
        self.pushButton_46.setText(_translate("MainWindow", "3"))
        self.pushButton_47.setText(_translate("MainWindow", "4"))
        self.pushButton_48.setText(_translate("MainWindow", "6#"))
        self.pushButton_49.setText(_translate("MainWindow", "6#"))
        self.pushButton_50.setText(_translate("MainWindow", "4#"))
        self.pushButton_51.setText(_translate("MainWindow", "2#"))
        self.pushButton_52.setText(_translate("MainWindow", "7"))
        self.pushButton_53.setText(_translate("MainWindow", "1#"))
        self.pushButton_54.setText(_translate("MainWindow", "5#"))
        self.pushButton_55.setText(_translate("MainWindow", "6"))
        self.pushButton_56.setText(_translate("MainWindow", "1"))
        self.pushButton_57.setText(_translate("MainWindow", "2"))
        self.pushButton_58.setText(_translate("MainWindow", "4"))
        self.pushButton_59.setText(_translate("MainWindow", "5"))
        self.pushButton_60.setText(_translate("MainWindow", "3"))
