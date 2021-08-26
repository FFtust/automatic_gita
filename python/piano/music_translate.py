import time
import servo
import math

SERVO_ID_BASE = 3
NOT_IMPLEMET = 100
servo_table = \
{
"1--": 1, "2--": 2,"3--": 3,"4--": 4,"5--": 5,"6--": 6,"7--": 7,
"1-": 8, "2-": 9,"3-": 10,"4-": 11,"5-": 12,"6-": 13,"7-": 14,
"0": 100, "1": 15, "2": 16,"3": 17,"4": 18,"5": 19,"6": 20,"7": 21,
"1+": 22, "2+": 23,"3+": 24,"4+": 25,"5+": 26,"6+": 27,"7+": 28,
"1++": 29, "2++": 30,"3++": 31,"4++": 32,"5++": 33,"6++": 34,"7++": NOT_IMPLEMET, 
"1+++": NOT_IMPLEMET,

"1#": 32 + SERVO_ID_BASE, "2#": 33 + SERVO_ID_BASE,"4#": 34 + SERVO_ID_BASE,"5#": 35 + SERVO_ID_BASE,"6#": 36 + SERVO_ID_BASE,
"1+#": 37 + SERVO_ID_BASE, "2+#": 38 + SERVO_ID_BASE,"4+#": 39 + SERVO_ID_BASE,"5+#": 40 + SERVO_ID_BASE,"6+#": 41 + SERVO_ID_BASE,
}

servos_angle = \
{
100:[100, 100], 
0: [90, 50], 1: [100, 50], 2: [95, 50], 3: [95, 50], 4: [95, 50], 5: [90, 50], 6: [92, 50], 7: [90, 50],
8: [85, 50], 9: [95, 50], 10: [90, 50], 11: [94, 50], 12: [102, 50], 13: [95, 50], 14: [100, 50], 15: [100, 50], 

16: [103, 50], 17: [100, 50], 18: [86, 50], 19: [97, 50], 20: [88, 50], 21: [85, 50], 22: [100, 50], 23: [92, 50],
24: [82, 50], 25: [90, 50], 26: [100, 50], 27: [100, 50], 28: [105, 50], 29: [95, 50], 30: [100, 50], 31: [100, 50],

32: [115, 35],33: [115, 35],34: [115, 35],35: [115, 35],36: [115, 35],
37: [115, 35],38: [115, 35],39: [115, 35],40: [115, 35],41: [115, 35],
42: [115, 35],43: [115, 35],44: [115, 35],45: [115, 35],46: [115, 35],
}


class music_trans():
    def __init__(self, music, beat = 60, toneG = "C"):
        self.toneG = toneG
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
        print(servo_id, sta)
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
        print(angle)
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
                    print(len(music_item[i],))
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

                        self._rest(1 / 16)
        self.play_list_sort()

    def play_list_sort(self):
        _paly_list = self.play_list.copy()
        ret_list = []
        # 按时间排序
        while _paly_list != []:
            current_index = 0
            min_t = 100000
            for i in range(len(_paly_list)):
                if _paly_list[i][2] < min_t:
                    min_t = _paly_list[i][2]
                    current_index = i
            ret_list.append(_paly_list[current_index].copy())
            del _paly_list[current_index]

        # 将同一时间操作的音符放在一个list中
        temp_list1 = []
        temp_list2 = []
        i = 0
        while i < len(ret_list) - 1:
            temp_list2 = [ret_list[i].copy()]
            k = i
            for j in range(i + 1, len(ret_list)):
                if math.fabs(ret_list[j][2] - ret_list[k][2]) < 0.02:
                    temp_list2.append(ret_list[j].copy())
                    i += 1
                else:
                    i += 1
                    break
            temp_list1.append(temp_list2.copy())

        # 两个连续的相同音符需要单独处理，否则将不会抬起，只有一个声音
        ret_list = []
        for i in range(1, len(temp_list1)):
            if self._check_special(temp_list1[i]):
                inser_down = []
                inser_up = []
                for item2 in temp_list1[i]:
                    if item2[1]:
                        item2[2] += 0
                        inser_down.append(item2.copy())
                    else:
                        item2[2] -= 0.07
                        inser_up.append(item2.copy())

                ret_list.append(inser_up.copy())
                ret_list.append(inser_down.copy())
            else:
                ret_list.append(temp_list1[i].copy())

        self.play_list = ret_list

    def _check_special(self, item):
        for i in range(len(item)):
            for j in range(i + 1, len(item)):
                if item[i][0] == item[j][0]:
                    return True
        return False
######################################################################
    def servos_home(self, angle = 100):
        time.sleep(1)
        for key in self.servos_angle:
            time.sleep(0.02)
            self.servos.run_single_servo(int(key), self.servos_angle[key][0])            

    def servos_play(self, angle = 100):
        time.sleep(1)
        for key in self.servos_angle:
            time.sleep(0.02)
            self.servos.run_single_servo(int(key), self.servos_angle[key][0] - self.servos_angle[key][1])    

    def play_music(self, play_list = None):
        if play_list == None:
            play_list = self.play_list
        start_time = time.time()
        for i in range(len(play_list)):
            while time.time() - start_time < play_list[i][0][2]:
                pass
            for item in play_list[i]:
                print(item, self.servo_table[item[0]] - SERVO_ID_BASE, self.get_angle(self.servo_table[item[0]] - SERVO_ID_BASE, item[1]))
                self.servos.set_single_angle(self.servo_table[item[0]] - SERVO_ID_BASE, self.get_angle(self.servo_table[item[0]] - SERVO_ID_BASE, item[1]))
            self.servos.run()



# music_parse = music_trans([()])
# music_parse.music_to_play_table()

# music_parse.servos_home()
# time.sleep(5)
# music_parse.servos_play()
# time.sleep(5)
# music_parse.servos_home()
