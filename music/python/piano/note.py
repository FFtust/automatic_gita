import time

SERVO_ID_BASE = 0
NOT_IMPLEMET = 100
FREE_ANGLE = 181

ANG_WHITE = 30
ANG_BLACK = 30

KEY_IDLE_OFFSET = 13

ANG_OFF_BLACK = 0
ANG_OFF_WHITE = 0

servo_table = \
{
"1--": 0, "1--#": 1, "2--": 2,"2--#": 3,"3--": 4,"4--": 5, "4--#": 6,"5--": 7,"5--#": 8,"6--": 9,"6--#": 10, "7--": 11,
"1-": 12, "1-#": 13, "2-": 14, "2-#": 15,"3-": 16,"4-": 17, "4-#": 18,"5-": 19,"5-#": 20,"6-": 21,"6-#": 22, "7-": 23,
"1": 24, "1#": 25, "2": 260,"2#": 27,"3": 261,"4": 29, "4#": 30,"5": 31,"5#": 32,"6": 33,"6#": 34, "7": 35,
"1+": 36, "1+#": 37, "2+": 38,"2+#": 39,"3+": 40,"4+": 41, "4+#": 42,"5+": 43,"5+#": 440,"6+": 45,"6+#": 441, "7+": 47,
"1++": 48, "1++#": 630, "2++": 50,"2++#": 631,"3++": 520,"4++": 521, "4++#": 540,"5++": 550,"5++#": 541,"6++": 551,"6++#": 58, "7++": 59,
"1+++":60,
}

midi_table = \
{
  36:"1--", 37:"1--#", 38:"2--",39:"2--#",40:"3--",41:"4--",42:"4--#",43:"5--",44:"5--#",45:"6--",46:"6--#",47:"7--",
  48:"1-", 49:"1-#", 50:"2-",51:"2-#",52:"3-",53:"4-",54:"4-#",55:"5-",56:"5-#",57:"6-",58:"6-#",59:"7-",
  60:"1", 61:"1#", 62:"2",63:"2#",64:"3",65:"4",66:"4#",67:"5",68:"5#",69:"6",70:"6#",71:"7",
  72:"1+", 73:"1+#", 74:"2+",75:"2+#",76:"3+",77:"4+",78:"4+#",79:"5+",80:"5+#",81:"6+",82:"6+#",83:"7+",
  84:"1++", 85:"1++#", 86:"2++",87:"2++#",88:"3++",89:"4++",90:"4++#",91:"5++",92:"5++#",93:"6++",94:"6++#",95:"7++",
  96:"1+++"
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
    if servo_id > 100:
        is_two_key = True

        if servo_id % 2 == 0:
            sign = 1.5
        else:
            sign = -1.5

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
    if servo_id > 100:
        servo_id = servo_id // 10
    return servo_id


def get_note_by_servo(idx):
    for key in servo_table:
        if servo_table[key] == idx:
            return key

    return None

#########################################################
import servo
servoCtl = servo.servo_control()
def play_note(note):
    if not isinstance(note, (list, tuple)):
            note = [note]

    for item in note:
        servoCtl.set_single_angle(get_servo(servo_table[item]) - SERVO_ID_BASE, get_angle(servo_table[item] - SERVO_ID_BASE, 1))
    servoCtl.run()


def stop_note(note):
    if not isinstance(note, (list, tuple)):
            note = [note]

    for item in note:
        servoCtl.set_single_angle(get_servo(servo_table[item]) - SERVO_ID_BASE, get_angle(servo_table[item] - SERVO_ID_BASE, 0))
    servoCtl.run()

def play_midi(midi):
    if midi in midi_table:
        play_note(midi_table[midi])


def stop_midi(midi):
    if midi in midi_table:
        stop_note(midi_table[midi])


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

