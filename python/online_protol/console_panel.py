import time

import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QLineEdit
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor

saveServoButtonCb = None
def setSaveServoButtonCb(cb):
    global saveServoButtonCb
    saveServoButtonCb = cb

class ConsolePanelControl():
    def __init__(self):
        self.control_enable = False

    def enable(self):
        self.control_enable = True

    def disable(self):
        self.control_enable = False

    def is_enabled(self):
        return self.control_enable


ConsolePanel = ConsolePanelControl()

class Window(QWidget):
    def __init__(self):
        self.keyboardEventList = []

        super().__init__()
        self.initUI()
        ConsolePanel.disable()

    def createServoControlTxt(self):
        self.qleServoControl = [None] * 18
        for i in range(18):
            self.qleServoControl[i] = QLineEdit(self)
            self.qleServoControl[i].move(150 + 120 * (i % 3), 50 + 80 * (i // 3))
            self.qleServoControl[i].resize(100, 40)
            self.qleServoControl[i].setText('90')

    def initUI(self):
        global saveServoButtonCb
        self.setGeometry(300, 300, 1000, 800)
        # self.setFixedWidth(300)
        # self.setFixedHeight(200)
        self.setWindowTitle('电吉他控制台')

        self.btn = QPushButton('ButtonEnable', self)
        # self.btn.resize(self.btn.sizeHint())
        self.btn.resize(50, 50)        
        self.btn.move(50, 50)  
        self.btn.setStyleSheet("background-color: black")
        self.buttonColor = 'black' 
        self.btn.clicked.connect(self.enableButtonCb)

        self.btnSaveServo = QPushButton('ButtonServoData', self)
        # self.btn.resize(self.btn.sizeHint())
        self.btnSaveServo.resize(50, 50)        
        self.btnSaveServo.move(50, 150)  
        self.btnSaveServo.clicked.connect(self.saveServoButtonCb)
        
        self.qleMotorDebug = QLineEdit(self)
        self.qleMotorDebug.move(50, 250)
        self.qleMotorDebug.resize(100, 40)
        self.qleMotorDebug.setText('0')

        self.btnMotorDebug = QPushButton('ButtonMotorDebug', self)
        # self.btn.resize(self.btn.sizeHint())
        self.btnMotorDebug.resize(50, 50)        
        self.btnMotorDebug.move(50, 300)  
        self.btnMotorDebug.clicked.connect(self.motorDebugCb)


        self.createServoControlTxt()
        self.show()
    
    def registerMotorDebugCb(self, func):
        self.motorDebugFunc = func

    def motorDebugCb(self):
        self.motorDebugFunc(int(self.qleMotorDebug.text(), 10))

    def enableButtonCb(self):
        if self.buttonColor == 'black':
            self.btn.setStyleSheet("background-color: green")
            self.buttonColor = 'green' 
            ConsolePanel.enable()
        else:
            self.btn.setStyleSheet("background-color: black")
            self.buttonColor = 'black'  
            ConsolePanel.disable()   

    def saveServoButtonCb(self):
        global saveServoButtonCb
        saveServoButtonCb()        
    
    def registerKeyboardEvent(self, item):
        self.keyboardEventList.append(item)

    def keyPressEvent(self, event):
        if not ConsolePanel.is_enabled():
            return 
        print(self.keyboardEventList)
        for item in self.keyboardEventList:
            if event.key() == item[0]:
                if item[1]:
                    item[1]()

        print("按下：" + str(event.key()))

    def controlStart(self):
        sys.exit(app.exec_())

app = QApplication(sys.argv)
window = Window()





