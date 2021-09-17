import time
import servo
import math
import random
from note import *

class music_trans():
    def __init__(self, music, beat = 60):
        self.music = music

        self.beat_time = 4 * (60 / beat)
        self.origin_beat = beat
        self.play_list = []

        self.current_t = 0

        self.servos_angle = servos_angle
        self.servo_table = servo_table

        self.servos = servo.servo_control()

        self._count = 0

    def set_beat(self, beat):
        self.beat_time = 4 * (60 / beat)

#######################################################
    def _reset_t(self):
        self.current_t = 0

    def _rest(self, beat):
        self.current_t += self.beat_time * beat

    def _rest_with_time(self, t):
        self.current_t += t

    def _play(self, tone):
        if tone in self.servo_table:
            self.play_list.append([tone, 1, self.current_t])

    def _stop(self, tone):
        if tone in self.servo_table:
            self.play_list.append([tone, 0, self.current_t])

    def get_angle(self, servo_id, sta):
        angle = 100
        if sta == 0:
            if servo_id in self.servos_angle:
                angle = self.servos_angle[servo_id][0]
        else:
            if servo_id in self.servos_angle:
                angle = self.servos_angle[servo_id][0] - self.servos_angle[servo_id][1]
        return angle
######################################################################
    def music_to_play_table(self):
        last_tone = []

        if not isinstance(self.music, list):
            self.music = [self.music]

        for music_item in self.music:
            self._reset_t()
            self.set_beat(self.origin_beat)

            for i in range(len(music_item)):
                if isinstance(music_item[i], tuple):
                    for j in range(len(music_item[i])):
                        # 解析1/16节拍
                        chor = music_item[i][j]

                        if chor == "NOP":
                            self._rest(1 / 24)
                            continue
                        elif "BEAT" in chor:
                            tmp = eval(chor)
                            self.set_beat(tmp["BEAT"])
                            continue
                        # - 代表这个节拍无变化
                        if chor != '-':
                            # 多个音符以 逗号间隔
                            chors = chor.split(",")
                            # 抬起需要停止的音符
                            for item in last_tone:
                                self._stop(item)
                            last_tone_tmp = last_tone.copy()
                            last_tone = []
                            ##########################
                            for m in range(len(chors)):
                                chors[m] = chors[m].replace("&", ",")

                                if '{' in chors[m]:
                                    temp = eval(chors[m])
                                    for key in temp:
                                        if key in last_tone_tmp:
                                            self._rest_with_time(0.0)
                                            last_tone_tmp = []
                                        if isinstance(temp[key], list):
                                            self._rest_with_time(temp[key][0])
                                            self._play(key)
                                            self._rest(temp[key][1])
                                            self._rest_with_time(-temp[key][0])
                                            self._stop(key)
                                            self._rest(-temp[key][1])
                                        else: 
                                            self._play(key)
                                            self._rest(temp[key])
                                            self._stop(key)
                                            self._rest(-temp[key])
                                else:
                                    if chors[m] in last_tone_tmp:
                                        self._rest_with_time(0.0)
                                        last_tone_tmp = []
                                    self._play(chors[m])
                                    last_tone.append(chors[m])

                        self._rest(1 / len(music_item[i]))
                        # self._rest(1 / 16)

                    # self._rest_with_time(0.02)

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
                if math.fabs(ret_list[j][2] - ret_list[k][2]) < 0.001:
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
            t_ret = self._check_special(temp_list1[i])
            if t_ret != []:
                for l in range(len(temp_list1[i])):
                    if not (l in t_ret):
                        temp_list1[i][l][2] += 0.00
                    else:
                        temp_list1[i][l][2] -= 0.06

                for j in range(i + 1, len(temp_list1)):
                    for m in range(len(temp_list1[j])):
                        temp_list1[j][m][2] += 0.0
            else:
                for k in range(len(temp_list1[i])):
                    if temp_list1[i][k][1] == 1:
                        temp_list1[i][k][2] -= 0

        temp = []
        for item in temp_list1:
            for item2 in item:
                temp.append(item2)

        self.play_list = self._sort_by_time(temp)

    def _check_special(self, item):
        ret = []
        for i in range(len(item)):
            for j in range(i + 1, len(item)):
                if item[i][0] == item[j][0]:
                    if item[i][1] == 0:
                        ret.append(i)
                    else:
                        ret.append(j)
        return ret
######################################################################
    def servos_home(self):
        time.sleep(1)
        for key in self.servos_angle:
            time.sleep(0.02)
            self.servos.run_single_servo(int(key), self.servos_angle[key][0])    
        self.free_all()

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


    def servos_play(self, angle = 100):
        time.sleep(1)
        for key in self.servos_angle:
            time.sleep(0.02)
            self.servos.run_single_servo(int(key), self.servos_angle[key][0] - self.servos_angle[key][1])    

    def play_music(self, play_list = None):
        self.home()
        self.create_noise()
        self.last_play = []
        if play_list == None:
            play_list = self.play_list
        start_time = time.time()
        for i in range(len(play_list)):
            while time.time() - start_time < play_list[i][0][2]:
                pass

            # for item in self.last_play:
            #     self.servos.run_single_servo(self.servo_table[item[0]] - SERVO_ID_BASE, FREE_ANGLE)

            for item in play_list[i]:
                print(item, self.servo_table[item[0]] - SERVO_ID_BASE, self.get_angle(self.servo_table[item[0]] - SERVO_ID_BASE, item[1]))
                self.servos.set_single_angle(self.servo_table[item[0]] - SERVO_ID_BASE, self.get_angle(self.servo_table[item[0]] - SERVO_ID_BASE, item[1]))

            self.last_play = play_list[i].copy()

            self.servos.run()

        self.home()

    def create_noise(self):
        for i in range(len(self.play_list)):
            self._count += 0.2
            for j in range(len(self.play_list[i])):
                self.play_list[i][j][2] += abs(math.sin(self._count)) * 0.01