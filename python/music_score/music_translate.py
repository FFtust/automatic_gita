import time
import servo
import math

servo_table = \
{
"1--": 1, "2--": 2,"3--": 3,"4--": 4,"5--": 5,"6--": 6,"7--": 7,
"1-": 8, "2-": 9,"3-": 10,"4-": 11,"5-": 12,"6-": 13,"7-": 14,
"0": 100, "1": 15, "2": 16,"3": 17,"4": 18,"5": 19,"6": 20,"7": 21,
"1+": 22, "2+": 23,"3+": 24,"4+": 25,"5+": 26,"6+": 27,"7+": 28,
"1++": 29, "2++": 30,"3++": 31,"4++": 32,"5++": 33,"6++": 34,"7++": 35,
"1+++": 36, "2+++": 37,"3+++": 38,"4+++": 39,"5+++": 40,"6+++": 41,"7+++": 42,
}

servos_angle = \
{
"0": [100, 70], "1": [100, 70], "2": [100, 50],"3": [100, 50],"4": [100, 50],"5": [100, 50],"6": [100, 50],"7": [100, 50],
"8": [100, 50], "9": [100, 50],"10": [100, 50],"11": [100, 50],"12": [100, 50],"13": [100, 50],"14": [100, 50],
"15": [100, 50], "16": [100, 50],"17": [100, 50],"18": [100, 50],"19": [100, 50],"20": [100, 50],"21": [100, 50],
"22": [100, 50], "23": [100, 50],"24": [100, 50],"25": [100, 50],"26": [100, 50],"27": [100, 50],"28": [100, 50],
"29": [100, 50], "30": [100, 50],"31": [100, 50],"32": [100, 50],"33": [100, 50],"34": [100, 50],"35": [100, 50],
}
# servos_angle = {}
# for i in range(0, 36):
#     servos_angle.update({str(i):[90, 50]})

class music_trans():
    def __init__(self, music, beat_time = 5, toneG = "C"):
        self.servo_idx_base = 3
        self.toneG = toneG
        self.music = music

        self.beat_time = beat_time
        self.play_list = []

        self.current_t = 0

        self.servos = servo.servo_control()

    def set_beat(self, beat):
        self.beat_time = beat

#######################################################
    def _reset_t(self):
        self.current_t = 0

    def _rest(self, beat):
        self.current_t += self.beat_time * beat

    def _play(self, tone):
        if tone in servo_table:
            self.play_list.append([tone, 1, self.current_t])

    def _stop(self, tone):
        if tone in servo_table:
            self.play_list.append([tone, 0, self.current_t])

    def get_angle(slef, play_item):
        if play_item[1] == 0:
            if str(play_item[0]) in servos_angle:
                angle = servos_angle[str(play_item[0])][0]
            else:
                angle = 90
        else:
            if str(play_item[0]) in servos_angle:
                angle = servos_angle[str(play_item[0])][1]
            else:
                angle = 50

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
            ret_list.append(_paly_list[current_index])
            del _paly_list[current_index]

        # 两个连续的相同音符需要单独处理，否则将不会抬起，只有一个声音
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

                ret_list.append(inser_up)
                ret_list.append(inser_down)
            else:
                ret_list.append(temp_list1[i])

        self.play_list = ret_list

    def _check_special(self, item):
        for i in range(len(item)):
            for j in range(i + 1, len(item)):
                if item[i][0] == item[j][0]:
                    return True
        return False
######################################################################
    def servos_home(self):
        time.sleep(1)
        for i in range(32):
            self.servos.run_single_servo(i, 100)


    def play_music(self, play_list = None):
        if self.toneG == "G":
            offset = 4
        elif self.toneG == "C":
            offset = 0

        if play_list == None:
            play_list = self.play_list
        start_time = time.time()
        for i in range(len(play_list)):
            while time.time() - start_time < play_list[i][0][2]:
                pass
            for item in play_list[i]:
                print(item, servo_table[item[0]] - self.servo_idx_base + offset, self.get_angle(item))
                self.servos.set_single_angle(servo_table[item[0]] - self.servo_idx_base + offset, self.get_angle(item))
            self.servos.run()

# from scores.亡靈序曲 import music_table
# from scores.梦中的婚礼 import music_table
# from scores.晴天 import music_table
# from scores.test import music_table
# from scores.天空之城 import music_table

# music_parse = music_trans(music_table)
# music_parse.music_to_play_table()

