SERVO_ID_BASE = 0
NOT_IMPLEMET = 100
FREE_ANGLE = 181

ANG_COM = 50
ANG_BLACK = 40
ANG_OFF_BLACK = 0

servo_table = \
{
"1--": 0, "1--#": 1, "2--": 2,"2--#": 3,"3--": 4,"4--": 5, "4--#": 6,"5--": 7,"5--#": 8,"6--": 9,"6--#": 10, "7--": 11,
"1-": 12, "1-#": 13, "2-": 14, "2-#": 15,"3-": 16,"4-": 17, "4-#": 18,"5-": 19,"5-#": 20,"6-": 21,"6-#": 22, "7-": 23,
"1": 24, "1#": 25, "2": 26,"2#": 27,"3": 28,"4": 29, "4#": 30,"5": 31,"5#": 32,"6": 33,"6#": 34, "7": 35,
"1+": 36, "1+#": 37, "2+": 38,"2+#": 39,"3+": 40,"4+": 41, "4+#": 42,"5+": 43,"5+#": 44,"6+": 45,"6+#": 46, "7+": 47,
"1++": 48, "1++#": 630, "2++": 50,"2++#": 631,"3++": 520,"4++": 521, "4++#": 540,"5++": 55,"5++#": 541,"6++": 57,"6++#": 58, "7++": 59,
"1+++":60,
}

servos_angle = \
{
0: [90, ANG_BLACK], 1: [90, ANG_BLACK], 2: [90, 35], 3: [90, 35], 4: [90, 35], 5: [90, 35], 6: [90, ANG_BLACK], 7: [90, 35], 8: [90, ANG_BLACK], 9: [80, 30], 10: [90, ANG_BLACK], 11: [90, 35], 
12: [90, ANG_COM], 13: [90, ANG_BLACK], 14: [80, ANG_COM], 15: [90, ANG_BLACK], 16: [85, ANG_COM], 17: [90, ANG_COM], 18: [90, ANG_BLACK], 19: [90, ANG_COM], 20: [90, ANG_BLACK], 21: [85, ANG_COM], 22: [90, ANG_BLACK], 23: [90, ANG_COM],
24: [90,  ANG_COM], 25: [90, ANG_BLACK], 26: [90, ANG_COM], 27: [90, ANG_BLACK], 28: [90, ANG_COM], 29: [90, ANG_COM], 30: [90, ANG_BLACK], 31: [90, ANG_COM], 32: [90, ANG_BLACK], 33: [90, ANG_COM], 34: [90, ANG_BLACK], 35: [90, ANG_COM], 
36: [90, ANG_COM], 37: [90, ANG_BLACK], 38: [90, ANG_COM], 39: [90, ANG_BLACK], 40: [90, ANG_COM], 41: [90, ANG_COM], 42: [90, ANG_BLACK], 43: [90, ANG_COM], 44: [90, 40], 45: [90, ANG_COM], 46: [90, ANG_BLACK -15], 47: [90, ANG_COM], 
48: [90, ANG_COM], 49: [90, ANG_BLACK], 50: [90, ANG_COM], 51: [90, ANG_BLACK], 520: [90, ANG_COM], 521: [90, -ANG_COM], 53: [90, ANG_COM], 540: [90, ANG_BLACK], 541: [90, -ANG_BLACK], 55: [90, ANG_COM], 56: [90, ANG_BLACK], 57: [90, ANG_COM], 58: [90, ANG_BLACK], 59: [90, ANG_COM], 
60: [90, ANG_COM], 630: [90, ANG_BLACK], 631: [90, -ANG_BLACK], 62: [90, ANG_COM], 63: [90, ANG_BLACK], 64: [90, ANG_COM], 
100: [90, 90]
}
# import configContent
# servos_angle = configContent.servos_angle

def get_angle(servo_id, sta):
    if sta == 0:
        if servo_id in servos_angle:
            angle = servos_angle[servo_id][0]
        else:
            angle = 100
    else:
        if servo_id in servos_angle:
            angle = servos_angle[servo_id][0] - servos_angle[servo_id][1]
        else:
            angle = 100
    return angle

def get_servo(servo_id):
    if servo_id > 100:
        servo_id = servo_id // 10
    return servo_id


def get_note_by_servo(idx):
    for key in servo_table:
        if servo_table[key] == idx:
            return key

    return None