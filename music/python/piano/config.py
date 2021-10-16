import keyboard
import time
from note import servo_table, get_note_by_servo
import note

configTable = None
currentMidi = 0

def saveConfig():
	with open("configContent.py", "w") as f:
		f.write("servos_angle = \\\n" + str(configTable))

def readConfig():
	global configTable
	with open("configContent.py", "r") as f:
		time.sleep(0.1)
		configTable = eval(f.read()[16:])

def play():
	global currentMidi
	servo_idx = note.get_servo(note.servo_table[note.midi_table[currentMidi]])
	if servo_idx in configTable:
		print(servo_idx, get_note_by_servo(servo_idx), configTable[servo_idx])
		note.servoCtl.run_single_servo(servo_idx, configTable[servo_idx][0])
	else:
		print("not find", servo_idx)

def servo_play(servo_id):
    note.servoCtl.run_single_servo(servo_id, note.get_angle(servo_id, 1))

def servo_stop(servo_id):
    note.servoCtl.run_single_servo(servo_id, note.get_angle(servo_id, 0))


readConfig()

for key in configTable:
	note.servoCtl.run_single_servo(key, configTable[key][0])

key_level = 0
key_table = {"q":0, "w":2, "e":4, "r":5, "t":7, "y":9, "u":11, "2":1, "3":3, "5":6, "6":8, "7":10}

def keyEventCb(e):
	global currentMidi,key_level,key_table
	if e.event_type == "up":
		if e.name == "up":
			key_level += 1
			print("level", key_level)
		elif e.name == "down":
			key_level -= 1
			print("level", key_level)
		if e.name == "left":
			key_level +=-3
			print("level", key_level)
		elif e.name == "right":
			key_level += 3
			print("level", key_level)

		if e.name in key_table:
			currentMidi = key_table[e.name] + key_level * 12 + 36
			print(midi_num, "up")
		play()
		saveConfig()

def keyEventCb2(e):
	global key_level
	if e.event_type == "up":
		if e.name == "up":
			key_level += 1
			print("level", key_level)
		elif e.name == "down":
			key_level -= 1
			print("level", key_level)
		
		if e.name in key_table:
			midi_num = key_table[e.name] + key_level * 12 + 36
			note.stop_midi(midi_num)
			print(midi_num, "up")

	if e.event_type == "down":
		if e.name in key_table:
			midi_num = key_table[e.name] + key_level * 12 + 36
			note.play_midi(midi_num)
			print(midi_num, "down")


keyboard.hook(keyEventCb2)
keyboard.wait('Ctrl')
saveConfig()