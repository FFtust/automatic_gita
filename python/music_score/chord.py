from servo import servo_control
# from servo_angles_table import SERVO_ANGLES_TABLE

CHRODS_ANGLES_SATRT  = [45, 35, 50, 50, 50, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45]

CHRODS_ANGLES = \
{
    "1": {"default": 45, "angle1": 35, "angle2": 60},
    "2": {"default": 35, "angle1": 25, "angle2": 45},
    "3": {"default": 50, "angle1": 40, "angle2": 65},
    "4": {"default": 50, "angle1": 40, "angle2": 65},
    "5": {"default": 50, "angle1": 40, "angle2": 65},
    "6": {"default": 45, "angle1": 35, "angle2": 55},
} 

servos = servo_control(CHRODS_ANGLES_SATRT)
servos.start_control()

class single_chrod():
    def __init__(self, id, info):
        self.id = id
        self.ANGLES = info # info is a list of 3 items
        self.angle_index = 0

    def reset(self):
        servo.set_angle(self.id, self.ANGLES[0])
        self.angle_index = 0
        time.sleep(0.2)

    def pizz(self, run_flag = False):
        self.angle_index = (self.angle_index + 1) % 2
        if type(self.ANGLES[self.angle_index]) == int:
            angle = self.ANGLES[self.angle_index + 1]
        else:
            angle = int(self.ANGLES[self.angle_index + 1], 10)

        # if self.angle_index % 2 == 0:
        #     servo.set_angle(self.id, angle + 50)
        # else:
        #     servo.set_angle(self.id, angle - 50)

        # time.sleep(0.05)
        print("angle is", angle)
        servos.set_single_angle(self.id - 1, angle)
        if run_flag:
            servos.run()
        
    def set_grade(self, grade_value, run_flag = False):
        if self.id in chord_grade_table:
            if grade_value in chord_grade_table[self.id]:
                if grade_value == 0:
                    for item in chord_grade_table[self.id][0]:
                        print("item", item)
                        servos.set_single_angle(item[0], item[1])
                else:
                    servos.set_single_angle(chord_grade_table[self.id][grade_value][0], chord_grade_table[self.id][grade_value][1])


        if run_flag:
            servos.run()


chord1 = single_chrod(1, [CHRODS_ANGLES['1']["default"], CHRODS_ANGLES['1']["angle1"], CHRODS_ANGLES['1']["angle2"]])
chord2 = single_chrod(2, [CHRODS_ANGLES["2"]["default"], CHRODS_ANGLES["2"]["angle1"], CHRODS_ANGLES["2"]["angle2"]])
chord3 = single_chrod(3, [CHRODS_ANGLES["3"]["default"], CHRODS_ANGLES["3"]["angle1"], CHRODS_ANGLES["3"]["angle2"]])
chord4 = single_chrod(4, [CHRODS_ANGLES["4"]["default"], CHRODS_ANGLES["4"]["angle1"], CHRODS_ANGLES["4"]["angle2"]])
chord5 = single_chrod(5, [CHRODS_ANGLES["5"]["default"], CHRODS_ANGLES["5"]["angle1"], CHRODS_ANGLES["5"]["angle2"]])
chord6 = single_chrod(6, [CHRODS_ANGLES["6"]["default"], CHRODS_ANGLES["6"]["angle1"], CHRODS_ANGLES["6"]["angle2"]])
chords = [chord1, chord2, chord3, chord4, chord5, chord6]


# press
chord_grade_table = \
{
    #chord:[(grade, (servo_id, angle, servo_id, angle, ...), ...]
    1 :  {0: ((6, 40), (12, 45)), 1: (6, 60), 2: (6, 30), 3: (12, 60), 4: (12, 35)},
    2 :  {0: ((7, 50), (13, 45)), 1: (7, 65), 2: (7, 35), 3: (13, 60), 4: (13, 35)},
    3 :  {0: ((8, 55), ), 1: (8, 70), 2: (8, 35), 3: (14, 45), 4: (14, 35)},
    4 :  {0: ((9, 45), ), 1: (9, 60), 2: (9, 35), 3: (15, 45), 4: (15, 35)},
    5 :  {0: ((10, 45), ), 1: (10, 60), 2: (10, 35), 3: (16, 45), 4: (16, 35)},
    6 :  {0: ((11, 45), ), 1: (11, 60), 2: (11, 35), 3: (17, 45), 4: (17, 35)},
}

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
        pass


C  = chord_def("C", "chrod C", info_chord_C)
Dm = chord_def("Dm", "chrod Dm", info_chord_Dm)
Em = chord_def("Em", "chrod Em", info_chord_Em)
F  = chord_def("F", "chrod F", info_chord_F)
G  = chord_def("G", "chrod G", info_chord_G)
Am = chord_def("Am", "chrod Am", info_chord_Am)
G7 = chord_def("G7", "chrod G7", info_chord_G7)


