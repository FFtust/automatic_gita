import time

SERVO_ID_BASE = 0
NOT_IMPLEMET = 100
FREE_ANGLE = 181

ANG_DOWN = 30
KEY_IDLE_OFFSET = 0


servo_table = \
{

"5": 60, "3": 61,"1": 62,"4": 64,
}

import configContent
servos_angle = configContent.servos_angle

def get_angle(servo_id, sta):
    down_ang = -ANG_DOWN

    if sta == 0:
        if servo_id in servos_angle:
            angle = servos_angle[servo_id][0] - KEY_IDLE_OFFSET
        else:
            angle = 100
    else:
        if servo_id in servos_angle:
            angle = servos_angle[servo_id][0] - down_ang - KEY_IDLE_OFFSET
        else:
            angle = 100

    return int(angle)    

def get_servo(servo_id):
    return servo_id

def set_tone_moving(move):
    global TOME_MOVING
    TOME_MOVING = move

def get_note_by_servo(idx):
    for key in servo_table:
        if servo_table[key] == idx:
            return key

    return None

#########################################################
import sys 
sys.path.append("../../../../")
from driver.raspberrypi.servo import servoCtl
# servoCtl = servo.servo_control()
def play_note(note, speed = 0):
    if not isinstance(note, (list, tuple)):
            note = [note]

    for item in note:
        if item in servo_table:
            servoCtl.set_angle(get_servo(servo_table[item]), get_angle(servo_table[item], 1), speed)
    servoCtl.update()


def stop_note(note):
    global TOME_MOVING

    if not isinstance(note, (list, tuple)):
            note = [note]

    for item in note:
        if item in servo_table:
            servoCtl.set_angle(get_servo(servo_table[item]) - SERVO_ID_BASE, get_angle(servo_table[item] - SERVO_ID_BASE, 0), 0)
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
    time.sleep(0.3)
    for key in servos_angle:
        servoCtl.set_angle(get_servo(key), get_angle(key, 0))
        servoCtl.update()
        time.sleep(0.02)
    time.sleep(0.3)
    # free_all()

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
