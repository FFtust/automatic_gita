import keyboard
import time
from note import servo_table, get_note_by_servo
import note

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
		note.servoCtl.run_single_servo(currentServo, configTable[currentServo][0])
	else:
		print("not find", currentServo)

def servo_play(servo_id):
    note.servoCtl.run_single_servo(servo_id, note.get_angle(servo_id, 1))

def servo_stop(servo_id):
    note.servoCtl.run_single_servo(servo_id, note.get_angle(servo_id, 0))


readConfig()

for key in configTable:
	note.servoCtl.run_single_servo(key, configTable[key][0])

def keyEventCb(e):
	global currentServo
	if e.event_type == "up":
		if e.name == "up":
			configTable[currentServo][0] += 3 
		elif e.name == "down":
			configTable[currentServo][0] -= 3 
		elif e.name == "left":
			currentServo -= 1
		elif e.name == "right":
			currentServo += 1
		play()
		saveConfig()

key_level = 0
key_table = {"q":1, "w":3, "e":5, "r":6, "t":8, "y":10, "u":12, "2":2, "3":4, "5":7, "6":9, "7":11}

def keyEventCb2(e):
	global key_level
	if e.event_type == "up":
		if e.name == "up":
			key_level += 1
			print("level", key_level)
		elif e.name == "down":
			key_level -= 1
			print("level", key_level)
		elif e.name in key_table:
			idx = key_table[e.name] + key_level * 12 - 1
			servo_stop(idx)

	if e.event_type == "down":
		if e.name in key_table:
			idx = key_table[e.name] + key_level * 12 - 1
			servo_play(idx)



keyboard.hook(keyEventCb2)
keyboard.wait('Ctrl')
saveConfig()