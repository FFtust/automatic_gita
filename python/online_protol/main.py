import motor
import time
from chord import *
# import console_panel 
# from file_manager import *

# while True:
#     # servo.set_angle(0, 90)
#     # servo.set_angle(1, 90)
#     chord1.pizz()
#     time.sleep(1)
#     # servo.set_angle(0, 0)
#     # servo.set_angle(1, 0)
#     chord1.pizz()
#     time.sleep(1)


# while True:
#     # servo.set_angle(0, 90)
#     # servo.set_angle(1, 90)
#     servo.set_all_angle(90)
#     time.sleep(1)
#     # servo.set_angle(0, 0)
#     # servo.set_angle(1, 0)
#     servo.set_all_angle(0)
#     time.sleep(1)
# import sys
# import PyQt5
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5 import QtCore
# from PyQt5.QtCore import *

# def loadServoData():
#     servoDict = readServoDatas()
#     for key in range(18):
#         console_panel.window.qleServoControl[key].setText(str(servoDict[key]))

# def updateServoData():
#     a = console_panel.window.qleServoControl
#     chord1.ANGLES = [a[0].text(), a[1].text(), a[2].text()]
#     chord2.ANGLES = [a[3].text(), a[4].text(), a[5].text()]
#     chord3.ANGLES = [a[6].text(), a[7].text(), a[8].text()]
#     chord4.ANGLES = [a[9].text(), a[10].text(), a[11].text()]
#     chord5.ANGLES = [a[12].text(), a[13].text(), a[14].text()]
#     chord6.ANGLES = [a[15].text(), a[16].text(), a[17].text()]

# class chord():
#     def __init__(self, id, angles):
#         self.id = id
#         self.ANGLES = angles #[110, 85, 90]
#         self.angle_index = 0

#     def reset(self):
#         updateServoData()
#         servo.set_angle(self.id, self.ANGLES[0])
#         self.angle_index = 0
#         time.sleep(0.2)

#     def pizz(self):
#         updateServoData()
#         self.angle_index = (self.angle_index + 1) % 2
#         if type(self.ANGLES[self.angle_index]) == int:
#             angle = self.ANGLES[self.angle_index]
#         else:
#             angle = int(self.ANGLES[self.angle_index], 10)

#         if self.angle_index % 2 == 0:
#             servo.set_angle(self.id, angle + 50)
#         else:
#             servo.set_angle(self.id, angle - 50)

#         time.sleep(0.05)
#         servo.set_angle(self.id, angle)

# class note():
#     def __init__(self):
#         self.note_dict = {
#         'l_3': [6, 0],
#         'l_4': [6, 1],
#         'l_5': [6, 3],
#         'l_6': [5, 0],
#         'l_7': [5, 2],
#         '1': [5, 3],
#         '2': [4, 0],
#         '3': [4, 2],
#         '4': [4, 3],
#         '5': [3, 0],
#         '6': [3, 3],
#         '7': [2, 0], 
#         'h_1': [2, 1],
#         'h_2': [2, 3],
#         'h_3': [1, 0],
#         'h_4': [1, 1],
#         'h_5': [1, 3]
#         }

#         self.servo_dict = {1: chord1,
#         2: chord2,
#         3: chord3,
#         4: chord4,
#         5: chord5,
#         6: chord6,

#         }

#     def play(self, note):
#         if note in self.note_dict:
#             if self.note_dict[note][1] == 0:
#                 self.servo_dict[self.note_dict[note][0]].pizz()


        

# def key_space_cb():
#     chord1.reset()
#     chord2.reset()
#     chord3.reset()
#     chord4.reset() 
#     chord5.reset()
#     chord6.reset()

# def key_1_cb():
#     chord1.pizz()
#     # note.play('1')

# def key_2_cb():
#     chord2.pizz()
#     # note.play('2')

# def key_3_cb():
#     chord3.pizz()
#     # note.play('3')

# def key_4_cb():
#     chord4.pizz()
#     # note.play('4')

# def key_5_cb():
#     chord5.pizz()
#     # note.play('5')

# def key_6_cb():
#     chord6.pizz()
#     # note.play('6')

# def key_7_cb():
#     chord6.pizz()
#     # note.play('7')

# debugMotorId = 0
# def setDebugMotor(id):
#     global debugMotorId
#     debugMotorId = id
#     print("set debug motor id", debugMotorId)

# console_panel.window.registerMotorDebugCb(setDebugMotor)

# def key_A_cb():
#     global debugMotorId
#     motor.set_pwm(debugMotorId, 100)

# def key_S_cb():
#     global debugMotorId
#     motor.set_pwm(debugMotorId, -100)

# def key_D_cb():
#     global debugMotorId
#     motor.set_pwm(debugMotorId, 0)

# def key_Z_cb():
#     global debugMotorId
#     motor.set_pwm(debugMotorId, -100)
#     time.sleep(0.28)
#     motor.set_pwm(debugMotorId, 0)
#     motor.set_pwm(debugMotorId, 0)

# def key_X_cb():
#     global debugMotorId
#     motor.set_pwm(debugMotorId, 100)
#     time.sleep(0.18)
#     motor.set_pwm(debugMotorId, 0)
#     motor.set_pwm(debugMotorId, 0)
#     time.sleep(0.1)

# GAIN = 1

# def rest(t = 1):
#     time.sleep(t * GAIN)

# def motorUp(id):
#     motor.set_pwm(id, 100)
#     time.sleep(0.23)
#     motor.set_pwm(id, 0)
#     motor.set_pwm(id, 0)
#     time.sleep(0.02)


# def motorDown(id):
#     motor.set_pwm(id, -100)
#     time.sleep(0.25)
#     motor.set_pwm(id, 0)
#     motor.set_pwm(id, 0)
#     # time.sleep(0.1)

# def happybirthday():
#     chord3.pizz()
#     rest(0.5)
#     chord3.pizz()
#     rest(0.25)

#     motorDown(2)
#     chord3.pizz()
#     rest(0.75)

#     motorUp(2)
#     chord3.pizz()
#     rest(0.75)
    
#     motorDown(1)
#     chord2.pizz()
#     rest(0.5)

#     motorUp(1)
#     chord2.pizz()
#     rest()
# # *****************************
#     chord3.pizz()
#     rest(0.5)
#     chord3.pizz()
#     rest(0.25)

#     motorDown(2)
#     chord3.pizz()
#     rest(0.75)

#     motorUp(2)
#     chord3.pizz()
#     rest(0.75)
    
#     motorDown(3)
#     chord2.pizz()
#     motorDown(1)
#     rest(0.45)

#     motorUp(3)
#     chord2.pizz()
#     rest()

# def testSong():
#     time.sleep(4)
#     import threading
#     th = threading.Thread(target = happybirthday, args = ())
#     th.start()


# if __name__ == '__main__':
#     loadServoData()
#     a = console_panel.window.qleServoControl

#     chord1 = chord(0, [a[0], a[1], a[2]])
#     chord2 = chord(1, [a[3], a[4], a[5]])
#     chord3 = chord(2, [a[6], a[7], a[8]])
#     chord4 = chord(3, [a[9], a[10], a[11]])
#     chord5 = chord(4, [a[12], a[13], a[14]])
#     chord6 = chord(5, [a[15], a[16], a[17]])
#     note = note()

#     console_panel.window.registerKeyboardEvent([Qt.Key_Escape, key_space_cb])
#     console_panel.window.registerKeyboardEvent([Qt.Key_A, key_A_cb])
#     console_panel.window.registerKeyboardEvent([Qt.Key_S, key_S_cb])
#     console_panel.window.registerKeyboardEvent([Qt.Key_D, key_D_cb])
#     console_panel.window.registerKeyboardEvent([Qt.Key_1, key_1_cb])
#     console_panel.window.registerKeyboardEvent([Qt.Key_2, key_2_cb])
#     console_panel.window.registerKeyboardEvent([Qt.Key_3, key_3_cb])
#     console_panel.window.registerKeyboardEvent([Qt.Key_4, key_4_cb])
#     console_panel.window.registerKeyboardEvent([Qt.Key_5, key_5_cb])
#     console_panel.window.registerKeyboardEvent([Qt.Key_6, key_6_cb])
#     console_panel.window.registerKeyboardEvent([Qt.Key_7, key_7_cb])
#     console_panel.window.registerKeyboardEvent([Qt.Key_Z, key_Z_cb])
#     console_panel.window.registerKeyboardEvent([Qt.Key_X, key_X_cb])  
#     testSong()
#     console_panel.window.controlStart()







