import time
import console_panel 
from file_manager import *
import servo

import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore
from PyQt5.QtCore import *

def loadServoData():
    servoDict = readServoDatas()
    for key in range(18):
        console_panel.window.qleServoControl[key].setText(str(servoDict[key]))

def updateServoData():
    a = console_panel.window.qleServoControl
    chord1.ANGLES = [a[0].text(), a[1].text(), a[2].text()]
    chord2.ANGLES = [a[3].text(), a[4].text(), a[5].text()]
    chord3.ANGLES = [a[6].text(), a[7].text(), a[8].text()]
    chord4.ANGLES = [a[9].text(), a[10].text(), a[11].text()]
    chord5.ANGLES = [a[12].text(), a[13].text(), a[14].text()]
    chord6.ANGLES = [a[15].text(), a[16].text(), a[17].text()]

class chord():
    def __init__(self, id, angles):
        self.id = id
        self.ANGLES = angles #[110, 85, 90]
        self.angle_index = 0

    def reset(self):
        updateServoData()
        servo.set_angle(self.id, self.ANGLES[0])
        self.angle_index = 0
        time.sleep(0.2)

    def pizz(self):
        updateServoData()
        self.angle_index = (self.angle_index + 1) % 2
        if type(self.ANGLES[self.angle_index]) == int:
            angle = self.ANGLES[self.angle_index]
        else:
            angle = int(self.ANGLES[self.angle_index], 10)

        if self.angle_index % 2 == 0:
            servo.set_angle(self.id, angle + 50)
        else:
            servo.set_angle(self.id, angle - 50)

        time.sleep(0.05)
        servo.set_angle(self.id, angle)

def key_space_cb():
    chord1.reset()
    chord2.reset()
    chord3.reset()
    chord4.reset() 
    chord5.reset()
    chord6.reset()

def key_1_cb():
    chord1.pizz()

def key_2_cb():
    chord2.pizz()

def key_3_cb():
    chord3.pizz()

def key_4_cb():
    chord4.pizz()

def key_5_cb():
    chord5.pizz()

def key_6_cb():
    chord6.pizz()

def key_7_cb():
    chord6.pizz()

def key_A_cb():
    pass

def key_S_cb():
    pass

def key_D_cb():
    pass

def key_Z_cb():
    pass

def key_X_cb():
    pass


def main():
    loadServoData()
    a = console_panel.window.qleServoControl

    chord1 = chord(0, [a[0], a[1], a[2]])
    chord2 = chord(1, [a[3], a[4], a[5]])
    chord3 = chord(2, [a[6], a[7], a[8]])
    chord4 = chord(3, [a[9], a[10], a[11]])
    chord5 = chord(4, [a[12], a[13], a[14]])
    chord6 = chord(5, [a[15], a[16], a[17]])

    console_panel.window.registerKeyboardEvent([Qt.Key_Escape, key_space_cb])
    console_panel.window.registerKeyboardEvent([Qt.Key_A, key_A_cb])
    console_panel.window.registerKeyboardEvent([Qt.Key_S, key_S_cb])
    console_panel.window.registerKeyboardEvent([Qt.Key_D, key_D_cb])
    console_panel.window.registerKeyboardEvent([Qt.Key_1, key_1_cb])
    console_panel.window.registerKeyboardEvent([Qt.Key_2, key_2_cb])
    console_panel.window.registerKeyboardEvent([Qt.Key_3, key_3_cb])
    console_panel.window.registerKeyboardEvent([Qt.Key_4, key_4_cb])
    console_panel.window.registerKeyboardEvent([Qt.Key_5, key_5_cb])
    console_panel.window.registerKeyboardEvent([Qt.Key_6, key_6_cb])
    console_panel.window.registerKeyboardEvent([Qt.Key_7, key_7_cb])
    console_panel.window.registerKeyboardEvent([Qt.Key_Z, key_Z_cb])
    console_panel.window.registerKeyboardEvent([Qt.Key_X, key_X_cb])  
    console_panel.window.controlStart()


if __name__ == '__main__':
    main()




