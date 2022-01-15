import time

SERVO_ID_BASE = 0
NOT_IMPLEMET = 100
FREE_ANGLE = 181

ANG_WHITE = 30
ANG_BLACK = 30

KEY_IDLE_OFFSET = 3

ANG_OFF_BLACK = 0
ANG_OFF_WHITE = 0

TOME_MOVING = 0

servo_table = \
{
"1---": -12, "1---#": -11, "2---": -10,"2---#": -9,"3---": -8,"4---": -7, "4---#": -6,"5---": -5,"5---#": -4,"6---": -3,"6---#": -2, "7---": -1,
"1--": 0, "1--#": 1, "2--": 2,"2--#": 3,"3--": 4,"4--": 5, "4--#": 6,"5--": 7,"5--#": 8,"6--": 9,"6--#": 10, "7--": 11,
"1-": 12, "1-#": 13, "2-": 14, "2-#": 15,"3-": 16,"4-": 17, "4-#": 18,"5-": 19,"5-#": 20,"6-": 21,"6-#": 22, "7-": 23,
"1": 24, "1#": 25, "2": 26,"2#": 27,"3": 28,"4": 29, "4#": 30,"5": 31,"5#": 32,"6": 33,"6#": 34, "7": 35,
"1+": 36, "1+#": 37, "2+": 38,"2+#": 39,"3+": 40,"4+": 41, "4+#": 42,"5+": 43,"5+#": 44,"6+": 45,"6+#": 46, "7+": 47,
"1++": 48, "1++#": 49, "2++": 50,"2++#": 51,"3++": 52,"4++": 53, "4++#": 54,"5++": 55,"5++#": 56,"6++": 57,"6++#": 58, "7++": 59,
"1+++":60, "1+++#":61, "2+++":62, "2+++#":63, "3+++":100
}

midi_table = \
{
    24:"1---", 25:"1---#", 26:"2---",27:"2---#",28:"3---",29:"4---",30:"4---#",31:"5---",32:"5---#",33:"6---",34:"6---#",35:"7---",
    36:"1--", 37:"1--#", 38:"2--",39:"2--#",40:"3--",41:"4--",42:"4--#",43:"5--",44:"5--#",45:"6--",46:"6--#",47:"7--",
    48:"1-", 49:"1-#", 50:"2-",51:"2-#",52:"3-",53:"4-",54:"4-#",55:"5-",56:"5-#",57:"6-",58:"6-#",59:"7-",
    60:"1", 61:"1#", 62:"2",63:"2#",64:"3",65:"4",66:"4#",67:"5",68:"5#",69:"6",70:"6#",71:"7",
    72:"1+", 73:"1+#", 74:"2+",75:"2+#",76:"3+",77:"4+",78:"4+#",79:"5+",80:"5+#",81:"6+",82:"6+#",83:"7+",
    84:"1++", 85:"1++#", 86:"2++",87:"2++#",88:"3++",89:"4++",90:"4++#",91:"5++",92:"5++#",93:"6++",94:"6++#",95:"7++",
    96:"1+++", 97:"1+++#", 98:"2+++",99:"2+++#",100:"3+++",101:"4+++",102:"4+++#",103:"5+++","104":"5+++#",105:"6+++",

    "1---": 24, "1---#": 25, "2---": 26,"2---#": 27,"3---": 28,"4---": 29, "4---#": 30,"5---": 31,"5---#": 32,"6---": 33,"6---#": 34, "7---": 35,
    "1--": 36, "1--#": 37, "2--": 38,"2--#": 39,"3--": 40,"4--": 41, "4--#": 42,"5--": 43,"5--#": 44,"6--": 45,"6--#": 46, "7--": 47,
    "1-": 48, "1-#": 49, "2-": 50, "2-#": 51,"3-": 52,"4-": 53, "4-#": 54,"5-": 55,"5-#": 56,"6-": 57,"6-#": 58, "7-": 59,
    "1": 60, "1#": 61, "2": 62,"2#": 63,"3": 64,"4": 65, "4#": 66,"5": 67,"5#": 68,"6": 69,"6#": 70, "7": 71,
    "1+": 72, "1+#": 73, "2+": 74,"2+#": 75,"3+": 76,"4+": 77, "4+#": 78,"5+": 79,"5+#": 80,"6+": 81,"6+#": 82, "7+": 83,
    "1++": 84, "1++#": 85, "2++": 86,"2++#": 87,"3++": 88,"4++": 89, "4++#": 90,"5++": 91,"5++#": 92,"6++": 93,"6++#": 94, "7++": 95,
    "1+++":96, "1+++#":97, "2+++":98, "2+++#":99, "3+++":100
}

note_status = {}

import piano.configContent as configContent
servos_angle = configContent.servos_angle

def get_angle(servo_id, sta):
    down_ang = 30
    sign = -1
    is_white = True
    is_two_key = False

    for key in servo_table:
        if servo_id == servo_table[key]:
            if "#" in key:
                down_ang = ANG_BLACK * int(sign)
                is_white = False
            else:
                down_ang = ANG_WHITE * sign
                is_white = True

    if sta == 0:
        if servo_id in servos_angle:
            if is_white and (not is_two_key):
                angle = servos_angle[servo_id][0] - KEY_IDLE_OFFSET
            else:
                angle = servos_angle[servo_id][0]
        else:
            angle = 100
    else:
        if servo_id in servos_angle:
            if is_white and (not is_two_key):
                angle = servos_angle[servo_id][0] - down_ang - KEY_IDLE_OFFSET
            else:
                angle = servos_angle[servo_id][0] - down_ang
        else:
            angle = 100

    return int(angle)    

def get_servo(servo_id):
    if servo_id > 63:
        servo_id = 100
    elif servo_id < 0:
        servo_id = 100
    return servo_id

def set_tone_moving(move):
    global TOME_MOVING
    TOME_MOVING = move

def cal_note(note):
    global TOME_MOVING
    return midi_table[midi_table[note] + TOME_MOVING]

def cal_midi(midi):
    global TOME_MOVING

    return midi + TOME_MOVING

def get_note_by_servo(idx):
    for key in servo_table:
        if servo_table[key] == idx:
            return key

    return None

#########################################################
import sys 
from driver.raspberrypi.servo import servoCtl

def play_note(notes, update = False):
    global TOME_MOVING, note_status

    for item in notes:
        note = cal_note(item[0])
        speed = item[1]
        if note in servo_table:
            servoCtl.set_angle(get_servo(servo_table[note]) - SERVO_ID_BASE, get_angle(servo_table[note] - SERVO_ID_BASE, 1) - speed * 0.5, 0)
        note_status.update({note:True})

    if update:
        servoCtl.update()


def stop_note(note, update = False):
    global TOME_MOVING, note_status

    for item in note:
        item = cal_note(item)
        if item in servo_table:
            servoCtl.set_angle(get_servo(servo_table[item]) - SERVO_ID_BASE, get_angle(servo_table[item] - SERVO_ID_BASE, 0), 0)
        note_status.update({item:False})

    if update:
        servoCtl.update()

def is_note_playing(note):
    global note_status
    item = cal_note(note)
    if item in note_status:
        return note_status[item]
    else:
        return False
def play_midi(midi, speed = 0):
    global TOME_MOVING
    # print("aaa", midi)
    for item in midi:
        if item[0] in midi_table:
            play_note([[midi_table[cal_midi(item[0])], speed]])
    servoCtl.update()


def stop_midi(midi):
    global TOME_MOVING
    for item in midi:
        if item in midi_table:
            stop_note([midi_table[cal_midi(item)]])
    servoCtl.update()


def play_servo(servo_id, speed = 0):
    if not isinstance(servo_id, (list, tuple)):
            servo_id = [servo_id]

    for item in servo_id:
        servoCtl.set_angle(get_servo(item), get_angle(item, 1), speed)
    servo_id.servoCtl.update()

def stop_servo(servo_id):
    if not isinstance(servo_id, (list, tuple)):
            servo_id = [servo_id]

    for item in servo_id:
        servoCtl.set_angle(get_servo(item), get_angle(item, 0))
    servo_id.servoCtl.update()

def servos_home():
    ss = time.time()
    time.sleep(0.3)
    for key in servos_angle:
        servoCtl.set_angle(get_servo(key), get_angle(key, 0))
        servoCtl.update()
        time.sleep(0.02)
    time.sleep(0.3)
    while time.time() - ss < 2:
        time.sleep(0.001)

def free_all():
    for key in servos_angle:
        servoCtl.set_angle(get_servo(key), FREE_ANGLE)  
        time.sleep(0.02)
        servoCtl.update()


def servos_test():
    for m in range(5):
        for i in range(64):
            servoCtl.set_angle(i, 70)
            servoCtl.update()
            time.sleep(0.02)
        time.sleep(1)
        for i in range(64):
            servoCtl.set_angle(i, 100)
            servoCtl.update()
            time.sleep(0.02)
        time.sleep(1)
