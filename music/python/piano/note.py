import time

SERVO_ID_BASE = 0
NOT_IMPLEMET = 100
FREE_ANGLE = 181

ANG_WHITE = 35
ANG_BLACK = 30

KEY_IDLE_OFFSET = 10

ANG_OFF_BLACK = 0
ANG_OFF_WHITE = 0

TOME_MOVING = 0

servo_table = \
{
"1---": -12, "1---#": -11, "2---": -10,"2---#": -9,"3---": -8,"4---": -7, "4---#": -6,"5---": -5,"5---#": -4,"6---": -3,"6---#": -2, "7---": -1,
"1--": 0, "1--#": 100, "2--": 2,"2--#": 101,"3--": 4,"4--": 5, "4--#": 6,"5--": 7,"5--#": 8,"6--": 9,"6--#": 10, "7--": 11,
"1-": 12, "1-#": 13, "2-": 14, "2-#": 15,"3-": 16,"4-": 17, "4-#": 18,"5-": 1900,"5-#": 20,"6-": 1901,"6-#": 22, "7-": 23,
"1": 24, "1#": 25, "2": 2600,"2#": 27,"3": 2601,"4": 29, "4#": 30,"5": 31,"5#": 32,"6": 33,"6#": 34, "7": 35,
"1+": 36, "1+#": 37, "2+": 38,"2+#": 39,"3+": 40,"4+": 41, "4+#": 42,"5+": 43,"5+#": 4400,"6+": 45,"6+#": 4401, "7+": 47,
"1++": 48, "1++#": 4900, "2++": 50,"2++#": 4901,"3++": 5200,"4++": 5201, "4++#": 5400,"5++": 5500,"5++#": 5401,"6++": 5501,"6++#": 58, "7++": 59,
"1+++":60
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
    "1+++":96,
}

# 舵机信息在configContent里配置
import configContent
servos_angle = configContent.servos_angle

def get_angle(servo_id, sta):
    down_ang = 30
    sign = 1
    is_white = True
    is_two_key = False

    # 处理一个舵机控制两个琴键的情况
    if servo_id >= 100:
        is_two_key = True

        if servo_id % 2 == 0:
            sign = 1.4
        else:
            sign = -1.4

    # 判断黑白键
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
    if servo_id >= 100:
        servo_id = servo_id // 100
    return servo_id

def set_tone_moving(move):
    global TOME_MOVING
    TOME_MOVING = move

def cal_note(note, move = 0):
    return midi_table[midi_table[note] + move]

def cal_midi(midi, move = 0):
    return midi + move

def get_note_by_servo(idx):
    for key in servo_table:
        if servo_table[key] == idx:
            return key

    return None

#########################################################
import servo
servoCtl = servo.servo_control()
def play_note(note):
    global TOME_MOVING

    if not isinstance(note, (list, tuple)):
            note = [note]

    for item in note:
        item = cal_note(item, TOME_MOVING)
        if item in servo_table:
            servoCtl.set_single_angle(get_servo(servo_table[item]) - SERVO_ID_BASE, get_angle(servo_table[item] - SERVO_ID_BASE, 1))
    servoCtl.run()


def stop_note(note):
    global TOME_MOVING123qwerty234565523

    if not isinstance(note, (list, tuple)):
            note = [note]

    for item in note:
        item = cal_note(item, TOME_MOVING)
        if item in servo_table:
            servoCtl.set_single_angle(get_servo(servo_table[item]) - SERVO_ID_BASE, get_angle(servo_table[item] - SERVO_ID_BASE, 0))
    servoCtl.run()

def play_midi(midi):
    global TOME_MOVING

    if midi in midi_table:
        play_note(midi_table[cal_midi(midi,TOME_MOVING)])


def stop_midi(midi):
    global TOME_MOVING

    if midi in midi_table:
        stop_note(midi_table[cal_midi(midi, TOME_MOVING)])


def play_servo(servo_id):
    if not isinstance(servo_id, (list, tuple)):
            servo_id = [servo_id]

    for item in servo_id:
        servoCtl.set_single_angle(get_servo(item), get_angle(item, 1))
    servo_id.servoCtl.run()

def stop_servo(servo_id):
    if not isinstance(servo_id, (list, tuple)):
            servo_id = [servo_id]

    for item in servo_id:
        servoCtl.set_single_angle(get_servo(item), get_angle(item, 0))
    servo_id.servoCtl.run()

def servos_home():
    time.sleep(0.3)
    for key in servos_angle:
        servoCtl.run_single_servo(get_servo(key), get_angle(key, 0))
        time.sleep(0.1)
    time.sleep(0.3)
    free_all()

def free_all():
    for key in servos_angle:
        servoCtl.run_single_servo(get_servo(key), FREE_ANGLE)  
        time.sleep(0.01)

