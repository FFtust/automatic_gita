import keyboard
import time
from note import servo_table, get_note_by_servo
import servo

servoCtl = servo.servo_control()

configTable = None
currentServo = 0

def saveConfig():
	with open("configContent.py", "w") as f:
		f.write("servos_angle = \\\n" + str(configTable))

def readConfig():
	global configTable
	with open("configContent.py", "r") as f:
		time.sleep(0.1)
		configTable = eval(f.read()[16:])

def play():
	global currentServo
	if currentServo in configTable:
		print(currentServo, get_note_by_servo(currentServo), configTable[currentServo])
		servoCtl.run_single_servo(currentServo, configTable[currentServo][0])
	else:
		print("not find", currentServo)
readConfig()

for key in configTable:
	servoCtl.run_single_servo(key, configTable[key][0])

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
		saveConfig()

keyboard.hook(keyEventCb)
keyboard.wait('Ctrl')
saveConfig()