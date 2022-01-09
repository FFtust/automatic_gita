import keyboard
import time
from piano.note import servo_table, get_note_by_servo
import piano.note as note

currentMidi = 36

def saveConfig():
	with open("configContent.py", "w") as f:
		f.write("servos_angle = \\\n" + str(note.servos_angle))

def play():
	global currentMidi
	note.stop_midi(currentMidi)

def servo_play(servo_id):
    note.servoCtl.run_single_servo(servo_id, note.get_angle(servo_id, 1))

def servo_stop(servo_id):
    note.servoCtl.run_single_servo(servo_id, note.get_angle(servo_id, 0))

note.servos_home()

print("config init done")

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
			note.servos_angle[note.servo_table[note.midi_table[currentMidi]]][0] +=-3
			play()
		elif e.name == "right":
			note.servos_angle[note.servo_table[note.midi_table[currentMidi]]][0] += 3
			play()
		if e.name in key_table:
			currentMidi = key_table[e.name] + key_level * 12 + 36
			print("current midi", currentMidi)
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
			print(midi_num, "down")
			note.play_midi(midi_num)


keyboard.hook(keyEventCb)
keyboard.wait('Esc')