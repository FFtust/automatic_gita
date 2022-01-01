import time
import math
import random
import note
import os
import sys

NOTE_SECTION_INTERVAL = 0.0
RIGHT_LEFT_INTERVAL = 0.0

SAME_NOTE_INTERVAL = 0
NOTE_CONTINUE_TIME = 0.15

CHECK_ENABLE = True

_exit_flag = False
class music_trans():
    def __init__(self, music, beat = 60, note_per = 4, move = 0):
        self.music = music

        self.beat_time = note_per * (60 / beat)
        self.origin_beat = beat
        self.play_list = []

        self.current_t = 0
        self.speed = 0

        self.servo_table = note.servo_table

        self._count = 0

        note.set_tone_moving(move)

    def set_beat(self, beat, note_per = 4):
        self.beat_time = note_per * (60 / beat)

#######################################################
    def _reset_t(self):
        self.current_t = 0

    def _rest(self, beat):
        self.current_t += self.beat_time * beat

    def _rest_with_time(self, t):
        self.current_t += t

    def _play(self, tone, speed = 0):
        if tone in self.servo_table:
            self.play_list.append([tone, 1, self.current_t, speed])

    def _stop(self, tone):
        if tone in self.servo_table:
            self.play_list.append([tone, 0, self.current_t])

######################################################################
    def cal_rest(self, l):
        for i in range(10):
            if l >= math.pow(2, i) and l < math.pow(2, i + 1):
                return math.pow(2,i)

    def music_to_play_table(self):
        last_tone = []
        rest_time = 0
        copy_index_start = None
        check_t = [[], []]
        mmm = 0

        if not isinstance(self.music, list):
            self.music = [self.music]

        for music_item in self.music:
            self._reset_t()
            self.set_beat(self.origin_beat)
            self._rest_with_time(RIGHT_LEFT_INTERVAL)
            rest_time = 0
            i = 0
            copy_index_start = None
            while i < len(music_item):
            # for i in range(len(music_item)):
                if isinstance(music_item[i], tuple):
                    for j in range(len(music_item[i])):
                        chor = music_item[i][j]

                        if "REST" in chor:
                            tmp = eval(chor)
                            rest_time = tmp["REST"]
                            continue
                        elif "NOP" in chor:
                            tmp = eval(chor)
                            self._rest(tmp["NOP"])
                            continue
                        elif "BEAT" in chor:
                            tmp = eval(chor)
                            self.set_beat(tmp["BEAT"])
                            continue
                        elif "MOVE" in chor:
                            tmp = eval(chor)
                            note.set_tone_moving(tmp["MOVE"])
                            continue
                        elif "COPY_START" in chor:
                            copy_index_start = i+1
                            continue
                        elif "COPY_STOP" in chor:
                            if copy_index_start != None:      
                                if not CHECK_ENABLE:                      
                                    i = copy_index_start
                                    i -= 1
                                copy_index_start = None
                            continue
                        elif "SPEED" in chor:
                            tmp = eval(chor)
                            self.speed = tmp["SPEED"]
                            continue
                        elif "=" in chor:
                            tmp = chor.split("=")
                            t = eval(tmp[1])


                            chors_all = tmp[0].split(":")
                            for tc in chors_all:
                                chors = tc.split(",")
                                for item in chors:
                                    self._play(item, self.speed)
                                self._rest(NOTE_CONTINUE_TIME)
                                for item in chors:
                                    self._stop(item)
                                self._rest(t - NOTE_CONTINUE_TIME)

                            continue                            

                    check_t[mmm].append([i,round(self.current_t, 1)])
                else:
                    print("error", i, music_item[i])

                i = i + 1

            mmm += 1
        if CHECK_ENABLE:
            self._check_show(check_t[0], check_t[1])
        self.play_list_sort()

    def _check_show(self, r, l):
        if len(r) != len(l):
            print("right and left section not the same, right:{}, left:()".format(len(r),len(l)))
            return

        for i in range(len(r)):
            if abs(r[i][1] - l[i][1]) > 0.001:
                print("time not sync, section:{}, notes:{}".format(i, self.music[0][i]))

    def _sort_by_time(self, play_list):
        _play_list = play_list.copy()
        ret_list = []
        while _play_list != []:
            current_index = 0
            min_t = 100000
            for i in range(len(_play_list)):
                if _play_list[i][2] < min_t:
                    min_t = _play_list[i][2]
                    current_index = i
            ret_list.append(_play_list[current_index])
            del _play_list[current_index]

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

        for i in range(1, len(temp_list1)):
            t_ret = self._check_special(temp_list1[i])
            if t_ret != []:
                for l in range(len(temp_list1[i])):
                    if l in t_ret:
                        if temp_list1[i][l][1] == 1:
                            temp_list1[i][l][2] += 0.0
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
                note.servoCtl.update()
                if _exit_flag:
                    break

            if _exit_flag:
                break
                
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
