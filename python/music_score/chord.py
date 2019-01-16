from servo import servo_control
# from servo_angles_table import SERVO_ANGLES_TABLE

CHRODS_ANGLES_SATRT  = [45, 35, 50, 50, 50, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 35, 50, 50, 50, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45]

CHRODS_ANGLES = \
{
    "1": {"default": 45, "angle1": 35, "angle2": 60},
    "2": {"default": 35, "angle1": 25, "angle2": 45},
    "3": {"default": 50, "angle1": 40, "angle2": 65},
    "4": {"default": 50, "angle1": 40, "angle2": 65},
    "5": {"default": 50, "angle1": 40, "angle2": 65},
    "6": {"default": 45, "angle1": 35, "angle2": 55},
} 

servos = servo_control()
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

        servos.set_single_angle(self.id - 1, angle)
        if run_flag:
            servos.run()
        
    def set_grade(self, grade_value, run_flag = False):
        if self.id in chord_grade_table:
            if grade_value in chord_grade_table[self.id]:
                if grade_value == 0:
                    for item in chord_grade_table[self.id][0]:
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
    1 :  {0: ((16, 50), (22, 45)), 1: (16, 65), 2: (16, 35), 3: (22, 60), 4: (22, 35)},
    2 :  {0: ((17, 50), (23, 45)), 1: (17, 65), 2: (17, 35), 3: (23, 60), 4: (23, 35)},
    3 :  {0: ((18, 50), (24, 45)), 1: (18, 65), 2: (18, 35), 3: (24, 60), 4: (24, 35)},
    4 :  {0: ((19, 32), (25, 45)), 1: (19, 52), 2: (19, 12), 3: (25, 60), 4: (25, 35)},
    5 :  {0: ((20, 38), (26, 45)), 1: (20, 53), 2: (20, 23), 3: (26, 60), 4: (26, 35)},
    6 :  {0: ((21, 50), (27, 45)), 1: (21, 65), 2: (21, 35), 3: (27, 60), 4: (27, 35)},
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


