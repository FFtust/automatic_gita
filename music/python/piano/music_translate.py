import time
import math
import random
import note

class music_trans():
    def __init__(self, music, beat = 60):
        self.music = music

        self.beat_time = 4 * (60 / beat)
        self.origin_beat = beat
        self.play_list = []

        self.current_t = 0

        self.servo_table = note.servo_table

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

                            last_tone = []
                            ##########################
                            for m in range(len(chors)):
                                chors[m] = chors[m].replace("&", ",")

                                if '{' in chors[m]:
                                    temp = eval(chors[m])
                                    for key in temp:
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
                                    self._play(chors[m])
                                    last_tone.append(chors[m])

                        self._rest(1 / len(music_item[i]))
                        # self._rest(1 / 16)
                    self._rest_with_time(0.03)
            for nn in last_tone:
                self._stop(nn)

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
        while i < len(ret_list):
            temp_list2 = [ret_list[i]]
            if i == len(ret_list) - 1:
                temp_list1.append(temp_list2)
                break

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

        # print("aa",  temp_list1)
        # 两个连续的相同音符需要单独处理，否则将不会抬起，只有一个声音
        for i in range(1, len(temp_list1)):
            t_ret = self._check_special(temp_list1[i])
            if t_ret != []:
                for l in range(len(temp_list1[i])):
                    if l in t_ret:
                        if temp_list1[i][l][1] == 1:
                            temp_list1[i][l][2] += 0.07
                        else:
                            temp_list1[i][l][2] -= 0.07
                    else:
                        temp_list1[i][l][2] -= 0.0

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
                    ret.append(i)
                    ret.append(j)
        return ret
######################################################################
    def play_music(self, play_list = None):
        note.servos_home()
        self.create_noise()
        self.last_play = []
        if play_list == None:
            play_list = self.play_list
        start_time = time.time()
        for i in range(len(play_list)):
            while time.time() - start_time < play_list[i][0][2]:
                pass

            # for item in self.last_play:
            #     if (not (item in play_list[i])) and (not (item in play_list[i + 1])) and (not (item in play_list[i + 2])):
            #         note.servoCtl.run_single_servo(self.servo_table[item[0]] - note.SERVO_ID_BASE, note.FREE_ANGLE)

            note_play = []
            note_stop = []
            for item in play_list[i]:
                print(item, self.servo_table[item[0]] - note.SERVO_ID_BASE, note.get_angle(self.servo_table[item[0]] - note.SERVO_ID_BASE, item[1]))
                if item[1]:
                    note_play.append(item[0])
                else:
                    note_stop.append(item[0])
            note.stop_note(note_stop)
            note.play_note(note_play)

            self.last_play = play_list[i].copy()

        note.servos_home()

    def create_noise(self):
        for i in range(len(self.play_list)):
            self._count += 0.2
            for j in range(len(self.play_list[i])):
                self.play_list[i][j][2] += abs(math.sin(self._count)) * 0.03