import time
import math
import random
import note

NOTE_SECTION_INTERVAL = 0.03
RIGHT_LEFT_INTERVAL = 0.03

SAME_NOTE_INTERVAL = 0.07

class music_item_c():
    def __init__(self, music_data, music_parse):
        self.music_data = music_data
        self.section_chors_id = 0
        self.section_parse_id = 0
        self.current_t = 0

        self.music_parse = music_parse

    def _reset_t(self):
        self.current_t = 0

    def _rest(self, beat):
        self.current_t += self.music_parse.beat_time * beat

    def _rest_with_time(self, t):
        self.current_t += t
        

class music_trans():
    def __init__(self, music, beat = 60, note_per = 4, move = 0):
        self.music = music

        self.beat_time = note_per * (60 / beat)
        self.origin_beat = beat
        self.play_list = []

        self.current_t = 0

        self.servo_table = note.servo_table

        self._count = 0

        self.section_parse_id = 0
        self.copy_index_start = 0

        note.set_tone_moving(move)

    def set_beat(self, beat, note_per = 4):
        self.beat_time = note_per * (60 / beat)

    def _play(self, tone, music_item):
        if tone in self.servo_table:
            self.play_list.append([note.cal_note(tone), 1, music_item.current_t])

    def _stop(self, tone, music_item):
        if tone in self.servo_table:
            self.play_list.append([note.cal_note(tone), 0, music_item.current_t])

#######################################################
    def cal_rest(self, l):
        for i in range(10):
            if l >= math.pow(2, i) and l < math.pow(2, i + 1):
                return math.pow(2,i)


#######################################################

    def _parse_cmd(self, chor, music_item):
        ret = False
        if "REST" in chor:
            tmp = eval(chor)
            rest_time = tmp["REST"]
            ret = True
        elif "NOP" in chor:
            tmp = eval(chor)
            music_item._rest(tmp["NOP"])
            ret = True
        elif "BEAT" in chor:
            tmp = eval(chor)
            self.set_beat(tmp["BEAT"])
            ret = True
        elif "MOVE" in chor:
            tmp = eval(chor)
            note.set_tone_moving(tmp["MOVE"])
            ret = True
        elif "COPY_START" in chor:
            self.copy_index_start = self.section_parse_id + 1
            ret = True
        elif "COPY_STOP" in chor:
            if self.copy_index_start != None:                            
                self.section_parse_id = self.copy_index_start
                self.section_parse_id -= 1
                self.copy_index_start = None
            ret = True

        return ret

######################################################################
    def cal_rest(self, l):
        for i in range(10):
            if l >= math.pow(2, i) and l < math.pow(2, i + 1):
                return math.pow(2,i)

    def music_to_play_table(self):
        check_t = []

        for i in range(len(self.music)):
            self.music[i] = music_item_c(self.music[i],self)

        if len(self.music) > 1:
            for i in range(1, len(self.music)):
                if len(self.music[i].music_data) != len(self.music[0].music_data):
                    raise "music len error"

        self.set_beat(self.origin_beat)

        self.section_parse_id = 0
        copy_index_start = None
        check_t = []
        while self.section_parse_id < len(self.music[0].music_data):
            for music_item in self.music:
                for j in range(len(music_item.music_data[self.section_parse_id])):
                    # 解析1/16节拍
                    chor = music_item.music_data[self.section_parse_id][j]

                    if self._parse_cmd(chor, music_item) == True:
                        continue
                    elif "=" in chor:
                        tmp = chor.split("=")
                        t = eval(tmp[1])

                        chors_all = tmp[0].split(":")
                        for tc in chors_all:
                            chors = tc.split(",")
                            for item in chors:
                                self._play(item, music_item)
                            music_item._rest(t)
                            for item in chors:
                                self._stop(item, music_item)
                        continue                            

                music_item._rest_with_time(NOTE_SECTION_INTERVAL)


            self.section_parse_id += 1

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
                if math.fabs(ret_list[j][2] - ret_list[k][2]) < 0.0001:
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
                    if l in t_ret:
                        if temp_list1[i][l][1] == 1:
                            temp_list1[i][l][2] += 0.02
                        else:
                            temp_list1[i][l][2] -= SAME_NOTE_INTERVAL
                    else:
                        temp_list1[i][l][2] += 0.0

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
        # self.create_noise()
        self.last_play = []
        if play_list == None:
            play_list = self.play_list
        start_time = time.time()
        for i in range(len(play_list)):
            while time.time() - start_time < play_list[i][0][2]:
                pass

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


