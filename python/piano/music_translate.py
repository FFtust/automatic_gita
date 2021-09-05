import time
import servo
import math

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
8: [85, D_ANGLE_COMMON], 9: [95, D_ANGLE_COMMON], 10: [90, D_ANGLE_COMMON], 11: [94, D_ANGLE_COMMON], 12: [102, D_ANGLE_COMMON], 13: [95, D_ANGLE_COMMON], 14: [100, D_ANGLE_COMMON], 15: [100, D_ANGLE_COMMON], 

16: [103, D_ANGLE_COMMON], 17: [100, D_ANGLE_COMMON], 18: [86, D_ANGLE_COMMON], 19: [97, D_ANGLE_COMMON], 20: [88, D_ANGLE_COMMON], 21: [85, D_ANGLE_COMMON], 22: [100, D_ANGLE_COMMON], 23: [92, D_ANGLE_COMMON],
24: [82, D_ANGLE_COMMON], 25: [90, D_ANGLE_COMMON], 26: [100, D_ANGLE_COMMON], 27: [100, D_ANGLE_COMMON], 28: [105, D_ANGLE_COMMON], 29: [95, D_ANGLE_COMMON], 30: [100, D_ANGLE_COMMON], 31: [100, D_ANGLE_COMMON],

32: [105 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],33: [105 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],34: [110 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],35: [110 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],36: [110 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],
37: [110 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],38: [110 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],39: [115 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],40: [110 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],41: [110 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],
42: [115 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],43: [115 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],44: [115 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],45: [115 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],46: [115 + D_ANGLE_OFFSET_BLACK, D_ANGLE_COMMON_BLACK],
}


class music_trans():
    def __init__(self, music, beat = 60):
        self.music = music

        self.beat_time = 4 * (60 / beat)
        self.play_list = []

        self.current_t = 0

        self.servos_angle = servos_angle
        self.servo_table = servo_table

        self.servos = servo.servo_control()

    def set_beat(self, beat):
        self.beat_time = 4 * (60 / beat)

#######################################################
    def _reset_t(self):
        self.current_t = 0

    def _rest(self, beat):
        self.current_t += self.beat_time * beat

    def _play(self, tone):
        if tone in self.servo_table:
            self.play_list.append([tone, 1, self.current_t])

    def _stop(self, tone):
        if tone in self.servo_table:
            self.play_list.append([tone, 0, self.current_t])

    def get_angle(self, servo_id, sta):
        if sta == 0:
            if servo_id in self.servos_angle:
                angle = self.servos_angle[servo_id][0]
            else:
                angle = 100
        else:
            if servo_id in self.servos_angle:
                angle = self.servos_angle[servo_id][0] - self.servos_angle[servo_id][1]
            else:
                angle = 100
        return angle
######################################################################
    def music_to_play_table(self):
        last_tone = []

        if not isinstance(self.music, list):
            self.music = [self.music]

        for music_item in self.music:
            self._reset_t()
            for i in range(len(music_item)):
                if isinstance(music_item[i], tuple):
                    for j in range(len(music_item[i])):
                        # 解析1/16节拍
                        chor = music_item[i][j]

                        # - 代表这个节拍无变化
                        if chor != '-':
                            # 多个音调以 逗号间隔
                            chors = chor.split(",")
                            # 抬起需要停止的音符
                            for item in last_tone:
                                self._stop(item)

                            last_tone = []
                            ##########################
                            for item in chors:
                                if '{' in item:
                                    temp = eval(item)
                                    for key in temp:
                                        self._play(key)
                                        self._rest(temp[key])
                                        self._stop(key)
                                        self._rest(-temp[key])
                                else:
                                    self._play(item)
                                    last_tone.append(item)

                        self._rest(1 / len(music_item[i]))
        self.play_list_sort()

    def _sort_by_time(self, play_list):
        _play_list = play_list.copy()
        ret_list = []
        # 按时间排序
        while _play_list != []:
            current_index = 0
            min_t = 100000
            for i in range(len(_play_list)):
                if _play_list[i][2] < min_t:
                    min_t = _play_list[i][2]
                    current_index = i
            ret_list.append(_play_list[current_index])
            del _play_list[current_index]

        # 将同一时间操作的音符放在一个list中
        temp_list1 = []
        temp_list2 = []
        i = 0
        while i < len(ret_list) - 1:
            temp_list2 = [ret_list[i]]
            k = i
            for j in range(i + 1, len(ret_list)):
                if math.fabs(ret_list[j][2] - ret_list[k][2]) < 0.02:
                    temp_list2.append(ret_list[j])
                    i += 1
                else:
                    i += 1
                    break
            temp_list1.append(temp_list2)
        return temp_list1

    def play_list_sort(self):
        temp_list1 = self._sort_by_time(self.play_list)

        # 两个连续的相同音符需要单独处理，否则将不会抬起，只有一个声音
        for i in range(1, len(temp_list1)):
            if self._check_special(temp_list1[i]):
                for l in range(len(temp_list1[i])):
                    if temp_list1[i][l][1]:
                        temp_list1[i][l][2] += 0
                    else:
                        temp_list1[i][l][2] -= 0.05

                # for j in range(i + 1, len(temp_list1)):
                #     for m in range(len(temp_list1[j])):
                #         temp_list1[j][m][2] += 0.05
            else:
                for k in range(len(temp_list1[i])):
                    if temp_list1[i][k][1] == 1:
                        temp_list1[i][k][2] -= 0.01
                # for l in range(len(temp_list1[i])):
                #     if temp_list1[i][l][1]:
                #         temp_list1[i][l][2] -= 0.015
                #     else:
                #         temp_list1[i][l][2] += 0.015

        temp = []
        for item in temp_list1:
            for item2 in item:
                temp.append(item2)

        self.play_list = self._sort_by_time(temp)

    def _check_special(self, item):
        for i in range(len(item)):
            for j in range(i + 1, len(item)):
                if item[i][0] == item[j][0]:
                    return True
        return False
######################################################################
    def servos_home(self):
        time.sleep(1)
        for key in self.servos_angle:
            time.sleep(0.02)
            self.servos.run_single_servo(int(key), self.servos_angle[key][0])    

    def free_all(self):
        time.sleep(1)
        for key in self.servos_angle:
            self.servos.run_single_servo(int(key), FREE_ANGLE)  

    def home(self):
        time.sleep(1)
        for i in range(len(self.play_list)):
            for item in self.play_list[i]:
                self.servos.set_single_angle(self.servo_table[item[0]] - SERVO_ID_BASE, self.get_angle(self.servo_table[item[0]] - SERVO_ID_BASE, 0))
            self.servos.run()
        time.sleep(1)
        self.free_all()


    def servos_play(self, angle = 100):
        time.sleep(1)
        for key in self.servos_angle:
            time.sleep(0.02)
            self.servos.run_single_servo(int(key), self.servos_angle[key][0] - self.servos_angle[key][1])    

    def play_music(self, play_list = None):
        self.home()
        if play_list == None:
            play_list = self.play_list
        start_time = time.time()
        last_item = []
        for i in range(len(play_list)):
            while time.time() - start_time < play_list[i][0][2]:
                pass
            for item in last_item:
                self.servos.set_single_angle(self.servo_table[item[0]] - SERVO_ID_BASE, FREE_ANGLE)

            for item in play_list[i]:
                print(item, self.servo_table[item[0]] - SERVO_ID_BASE, self.get_angle(self.servo_table[item[0]] - SERVO_ID_BASE, item[1]))
                self.servos.set_single_angle(self.servo_table[item[0]] - SERVO_ID_BASE, self.get_angle(self.servo_table[item[0]] - SERVO_ID_BASE, item[1]))
            self.servos.run()
        self.home()