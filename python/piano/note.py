SERVO_ID_BASE = 3
NOT_IMPLEMET = 100
FREE_ANGLE = 181

servo_table = \
{
"1--": 1, "2--": 2,"3--": 3,"4--": 4,"5--": 5,"6--": 6,"7--": 7,
"1-": 8, "2-": 9,"3-": 10,"4-": 11,"5-": 12,"6-": 13,"7-": 14,
"0": 100, "1": 15, "2": 16,"3": 17,"4": 18,"5": 19,"6": 20,"7": 21,
"1+": 22, "2+": 23,"3+": 24,"4+": 25,"5+": 26,"6+": 27,"7+": 28,
"1++": 29, "2++": 30,"3++": 31,"4++": 32,"5++": 33,"6++": 34,"7++": NOT_IMPLEMET, 
"1+++": NOT_IMPLEMET,

"1--#": 1, "2--#": 2,"4--#": 4,"5--#": 5,"6--#": 6,
"1-#": 32 + SERVO_ID_BASE, "2-#": 33 + SERVO_ID_BASE,"4-#": 34 + SERVO_ID_BASE,"5-#": 35 + SERVO_ID_BASE,"6-#": 36 + SERVO_ID_BASE,
"1#": 37 + SERVO_ID_BASE, "2#": 38 + SERVO_ID_BASE,"4#": 39 + SERVO_ID_BASE,"5#": 40 + SERVO_ID_BASE,"6#": 41 + SERVO_ID_BASE,
"1+#": 42 + SERVO_ID_BASE, "2+#": 43 + SERVO_ID_BASE,"4+#": 44 + SERVO_ID_BASE,"5+#": 45 + SERVO_ID_BASE,"6+#": 46 + SERVO_ID_BASE,
"1++#": 29, "2++#": 30,"4++#": 32,"5++#": 33,"6++#": 34,

}

D_ANGLE_COMMON = 50
D_ANGLE_COMMON_BLACK = 30
D_ANGLE_OFFSET_BLACK = 0
servos_angle = \
{
100:[100, 100], 
0: [90, D_ANGLE_COMMON - 20], 1: [100, D_ANGLE_COMMON - 20], 2: [95, D_ANGLE_COMMON - 20], 3: [95, D_ANGLE_COMMON - 20], 4: [95, D_ANGLE_COMMON - 20], 5: [90, D_ANGLE_COMMON], 6: [92, D_ANGLE_COMMON], 7: [90, D_ANGLE_COMMON],
8: [85, D_ANGLE_COMMON], 9: [95, D_ANGLE_COMMON], 10: [90, D_ANGLE_COMMON], 11: [100, D_ANGLE_COMMON], 12: [102, D_ANGLE_COMMON], 13: [98, D_ANGLE_COMMON], 14: [95, D_ANGLE_COMMON], 15: [100, D_ANGLE_COMMON + 7], 

16: [103, D_ANGLE_COMMON], 17: [100, D_ANGLE_COMMON], 18: [86, D_ANGLE_COMMON], 19: [97, D_ANGLE_COMMON], 20: [88, D_ANGLE_COMMON], 21: [85, D_ANGLE_COMMON], 22: [100, D_ANGLE_COMMON], 23: [92, D_ANGLE_COMMON],
24: [82, D_ANGLE_COMMON], 25: [90, D_ANGLE_COMMON], 26: [100, D_ANGLE_COMMON], 27: [100, D_ANGLE_COMMON], 28: [105, D_ANGLE_COMMON], 29: [95, D_ANGLE_COMMON], 30: [100, D_ANGLE_COMMON], 31: [100, D_ANGLE_COMMON],

32: [105 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],33: [105 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],34: [110 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],35: [110 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],36: [110 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],
37: [110 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],38: [110 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],39: [105 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],40: [110 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],41: [105 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],
42: [110 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],43: [105 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],44: [105 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK - 10],45: [105 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],46: [105 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],
}

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
#####################################################################

servo_table_G = \
{
"1--": 1, "2--": 2,"3--": 3,"4--": 4,"5--": 5,"6--": 6,"7--": 7,
"1-": 8, "2-": 9,"3-": 10,"4-": 11,"5-": 12,"6-": 13,"7-": 14,
"0": 100, "1": 33, "2": 16,"3": 17,"4": 18,"5": 19,"6": 20,"7": 21,
"1+": 22, "2+": 23,"3+": 24,"4+": 25,"5+": 26,"6+": 27,"7+": 28,
"1++": 29, "2++": 30,"3++": 31,"4++": 32,"5++": 33,"6++": 34,#"7++": 35,
# "1+++": 36, "2+++": 37,"3+++": 38,"4+++": 39,"5+++": 40,"6+++": 41,"7+++": 42,

"1#": 32 + SERVO_ID_BASE, "2#": 33 + SERVO_ID_BASE,"4#": 34 + SERVO_ID_BASE,"5#": 35 + SERVO_ID_BASE,"6#": 36 + SERVO_ID_BASE,
"1+#": 37 + SERVO_ID_BASE, "2+#": 38 + SERVO_ID_BASE,"4+#": 39 + SERVO_ID_BASE,"5+#": 40 + SERVO_ID_BASE,"6+#": 41 + SERVO_ID_BASE,
}

servo_table_Eb = \
{
"1--": NOT_IMPLEMET, "2--": NOT_IMPLEMET,"3--": 3,"4--": 4,"5--": 5,"6--": 6,"7--": 7,
"1-": 8, "2-": 9,"3-": 10,"4-": 11,"5-": 12,"6-": 13,"7-": 14,
"0": 100, "1": 15, "2": 16,"3": 17,"4": 18,"5": 19,"6": 20,"7": 21,
"1+": 22, "2+": 23,"3+": 24,"4+": 25,"5+": 26,"6+": 27,"7+": 28,
"1++": 29, "2++": 30,"3++": 31,"4++": 32,"5++": 33,"6++": 34,#"7++": 35,
# "1+++": 36, "2+++": 37,"3+++": 38,"4+++": 39,"5+++": 40,"6+++": 41,"7+++": 42,

"1#": 32 + SERVO_ID_BASE, "2#": 33 + SERVO_ID_BASE,"4#": 34 + SERVO_ID_BASE,"5#": 35 + SERVO_ID_BASE,"6#": 36 + SERVO_ID_BASE,
"1+#": 37 + SERVO_ID_BASE, "2+#": 38 + SERVO_ID_BASE,"4+#": 39 + SERVO_ID_BASE,"5+#": 40 + SERVO_ID_BASE,"6+#": 41 + SERVO_ID_BASE,
}
