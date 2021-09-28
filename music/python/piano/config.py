import keyboard
import time
from note import servo_table, get_note_by_servo
import servo

servoCtl = servo.servo_control()

configTable = None
currentServo = 0

def saveConfig():
	with open("configContent,py", "w") as f:
		f.write(str(configTable))

def readConfig():
	global configTable
	with open("configContent.py", "r") as f:
		configTable = eval(f.read())

def play():
	global currentServo
	print(currentServo, get_note_by_servo(currentServo), configTable[currentServo])
	servoCtl.run_single_servo(currentServo, configTable[currentServo][0])
readConfig()

def keyEventCb(e):
	global currentServo
	if e.event_type == "up":
		if e.name == "w":
			configTable[currentServo][0] += 3 
		elif e.name == "s":
			configTable[currentServo][0] -= 3 
		elif e.name == "a":
			currentServo -= 1
		elif e.name == "d":
			currentServo += 1
		play()

keyboard.hook(keyEventCb)
keyboard.wait('Ctrl')
saveConfig()