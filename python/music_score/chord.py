from servo import servo_control
import time
# from servo_angles_table import SERVO_ANGLES_TABLE

class single_chrod():
    def __init__(self, id, info):
        self.id = id
        self.ANGLES = info # info is a list of 3 items
        self.angle_index = 1
        self.current_grade = 0

    def reset(self, run_flag = False):
        servos.set_single_angle(self.id - 1, self.ANGLES[0])
        self.angle_index = 0
        if run_flag:
            servos.run()

    def pizz(self, run_flag = False):
        angle = self.ANGLES[0] + self.ANGLES[self.angle_index + 1]
        servos.set_single_angle(self.id - 1, angle)

        if run_flag:
            if self.ANGLES[self.angle_index + 1] < 0:
                # servos.run_single_servo(self.id - 1, angle - 30) 
                # time.sleep(0.05)
                servos.run()
            else:
                # servos.run_single_servo(self.id - 1, angle + 30) 
                # time.sleep(0.05)
                servos.run()
        self.angle_index = (self.angle_index + 1) % 2
 
            
    def set_grade(self, grade_value, run_flag = False):
        if self.id in chord_grade_table:
            if grade_value in chord_grade_table[self.id]:
                if grade_value == 0:
                    for item in chord_grade_table[self.id][0]:
                        servos.set_single_angle(item[0], item[1])
                else:

                    # if self.current_grade > grade_value:
                    for item in chord_grade_table[self.id][0]:
                        servos.set_single_angle(item[0], item[1])
                    servo_index = chord_grade_table[self.id][0][chord_grade_table[self.id][grade_value][0]][0]
                    angle = chord_grade_table[self.id][0][chord_grade_table[self.id][grade_value][0]][1] + chord_grade_table[self.id][grade_value][1]
                    servos.set_single_angle(servo_index, angle)
                    # servos.set_single_angle(chord_grade_table[self.id][grade_value][0], chord_grade_table[self.id][grade_value][1])

            self.current_grade = grade_value



        if run_flag:
            servos.run()


CHRODS_ANGLES_SATRT  = [45] * 32

CHRODS_ANGLES = \
{
    "1": {"default": 40, "angle1": -15, "angle2": 15},
    "2": {"default": 35, "angle1": -15, "angle2": 15},
    "3": {"default": 50, "angle1": -15, "angle2": 15},
    "4": {"default": 50, "angle1": -10, "angle2": 10},
    "5": {"default": 45, "angle1": -10, "angle2": 10},
    "6": {"default": 45, "angle1": -10, "angle2": 10},
} 

chord_grade_table = \
{
    #chord:[(grade, (servo_id, angle, servo_id, angle, ...), ...]
    1 :  {0: ((16, 50), (22, 40)), 1: (0, 15), 2: (0, -15), 3: (1, 15), 4: (1, -15)},
    2 :  {0: ((17, 50), (23, 40)), 1: (0, 15), 2: (0, -15), 3: (1, 15), 4: (1, -25)},
    3 :  {0: ((18, 58), (24, 55)), 1: (0, 20), 2: (0, -20), 3: (1, 25), 4: (1, -25)},
    4 :  {0: ((19, 50), (25, 30)), 1: (0, -25), 2: (0, 25), 3: (1, -35), 4: (1, 25)},
    5 :  {0: ((20, 38), (26, 40)), 1: (0, -20), 2: (0, 20), 3: (1, -20), 4: (1, 20)},
    6 :  {0: ((21, 50), (27, 53)), 1: (0, -20), 2: (0, 20), 3: (1, -20), 4: (1, 20)},
}

CHRODS_ANGLES_SATRT[0] = CHRODS_ANGLES['1']["default"] + CHRODS_ANGLES['1']["angle1"]
CHRODS_ANGLES_SATRT[1] = CHRODS_ANGLES['2']["default"] + CHRODS_ANGLES['2']["angle1"]
CHRODS_ANGLES_SATRT[2] = CHRODS_ANGLES['3']["default"] + CHRODS_ANGLES['3']["angle1"]
CHRODS_ANGLES_SATRT[3] = CHRODS_ANGLES['4']["default"] + CHRODS_ANGLES['4']["angle1"]
CHRODS_ANGLES_SATRT[4] = CHRODS_ANGLES['5']["default"] + CHRODS_ANGLES['5']["angle1"]
CHRODS_ANGLES_SATRT[5] = CHRODS_ANGLES['6']["default"] + CHRODS_ANGLES['6']["angle1"]

for i in range(6):
    for item in chord_grade_table[i + 1][0]:
        CHRODS_ANGLES_SATRT[item[0]] = item[1]

print("start angle is", CHRODS_ANGLES_SATRT)

servos = servo_control(CHRODS_ANGLES_SATRT)
servos.start_control()

chord1 = single_chrod(1, [CHRODS_ANGLES['1']["default"], CHRODS_ANGLES['1']["angle1"], CHRODS_ANGLES['1']["angle2"]])
chord2 = single_chrod(2, [CHRODS_ANGLES["2"]["default"], CHRODS_ANGLES["2"]["angle1"], CHRODS_ANGLES["2"]["angle2"]])
chord3 = single_chrod(3, [CHRODS_ANGLES["3"]["default"], CHRODS_ANGLES["3"]["angle1"], CHRODS_ANGLES["3"]["angle2"]])
chord4 = single_chrod(4, [CHRODS_ANGLES["4"]["default"], CHRODS_ANGLES["4"]["angle1"], CHRODS_ANGLES["4"]["angle2"]])
chord5 = single_chrod(5, [CHRODS_ANGLES["5"]["default"], CHRODS_ANGLES["5"]["angle1"], CHRODS_ANGLES["5"]["angle2"]])
chord6 = single_chrod(6, [CHRODS_ANGLES["6"]["default"], CHRODS_ANGLES["6"]["angle1"], CHRODS_ANGLES["6"]["angle2"]])
chords = [None, chord1, chord2, chord3, chord4, chord5, chord6]

# (chrod_num, grade)
info_chord_C = ((2, 1), (4, 2), (5, 3))
info_chord_Dm = ((1, 1), (2, 3), (3, 2))
info_chord_Em = ((4, 2), (5, 2))
info_chord_F = ((1, 1), (2, 1), (3, 2), (4, 3), (5, 3), (6, 1))
info_chord_G = ((1, 3), (5, 2), (6, 3))
info_chord_Am = ((2, 1), (3, 2), (4, 2))
info_chord_G7 = ((1, 1), (5, 2), (6, 2))


class chord_def():
    def __init__(self, name, des, info):
        self.name = name
        self.description = des
        self.info = info

    def run(self):
        chord1.set_grade(0, False)
        chord2.set_grade(0, False)
        chord3.set_grade(0, False)
        chord4.set_grade(0, False)
        chord5.set_grade(0, False)
        chord6.set_grade(0, False)

        for i in range(len(self.info)):
            if i == len(self.info) - 1:
                chords[self.info[i][0]].set_grade(self.info[i][1], True)
            else:
                chords[self.info[i][0]].set_grade(self.info[i][1], False)


C  = chord_def("C", "chrod C", info_chord_C)
Dm = chord_def("Dm", "chrod Dm", info_chord_Dm)
Em = chord_def("Em", "chrod Em", info_chord_Em)
F  = chord_def("F", "chrod F", info_chord_F)
G  = chord_def("G", "chrod G", info_chord_G)
Am = chord_def("Am", "chrod Am", info_chord_Am)
G7 = chord_def("G7", "chrod G7", info_chord_G7)

