import time
import servo

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
"0": [80, 45], "1": [80, 45], "2": [80, 45],"3": [80, 45],"4": [80, 45],"5": [80, 45],"6": [80, 45],"7": [80, 45],
"8": [80, 45], "9": [80, 45],"10": [80, 45],"11": [80, 45],"12": [80, 45],"13": [80, 45],"14": [80, 45],
"15": [80, 45], "16": [80, 45],"17": [80, 45],"18": [80, 45],"19": [80, 45],"20": [80, 45],"21": [80, 45],
"22": [80, 45], "23": [80, 45],"24": [80, 45],"25": [80, 45],"26": [80, 45],"27": [80, 45],"28": [80, 45],
"29": [80, 45], "30": [80, 45],"31": [80, 45],"32": [80, 45],"33": [80, 45],"34": [80, 45],"35": [80, 45],
}
servos_angle = {}
for i in range(0, 36):
    servos_angle.update({str(i):[90, 50]})

class music_trans():
    def __init__(self, music, beat_time = 5):
        self.servo_idx_base = 3

        self.music = music

        self.beat_time = beat_time
        self.play_list = []

        self.current_t = 0

        self.tone_status = {}

        for key in servo_table:
            self.tone_status.update({key:0})

        self.servos = servo.servo_control()

    def set_beat(self, beat):
        self.beat_time = beat

#######################################################
    def _reset_t(self):
        self.current_t = 0

    def _rest(self, beat):
        self.current_t += self.beat_time * beat

    def _sleep(self, t_s):
        self.current_t += t_s

    def _play(self, tone, angle = None):
        self.tone_status[tone] = 1

        if angle == None:
            if str(servo_table[tone] - self.servo_idx_base) in servos_angle:
                angle = servos_angle[str(servo_table[tone] - self.servo_idx_base)][1]
            else:
                angle = 30
        if tone in servo_table:
            self.play_list.append([servo_table[tone] - self.servo_idx_base, angle, self.current_t])

    def _stop(self, tone, angle = None):
        self.tone_status[tone] = 0

        if angle == None:
            if str(servo_table[tone] - self.servo_idx_base) in servos_angle:
                angle = servos_angle[str(servo_table[tone] - self.servo_idx_base)][0]
            else:
                angle = 90

        if tone in servo_table:
            self.play_list.append([servo_table[tone] - self.servo_idx_base, angle, self.current_t])

######################################################################
    def music_to_play_table(self):
        last_tone = []

        if not isinstance(self.music, list):
            self.music = [self.music]

        for music_item in self.music:
            self._reset_t()
            for i in range(len(music_item)):
                check_idx = i
                if isinstance(music_item[check_idx], tuple):
                    for j in range(len(music_item[check_idx])):
                        # 解析1/16节拍
                        chor = music_item[check_idx][j]

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
        last_tones = []
        for i in range(len(ret_list)):
            last_tones = [(i, ret_list[i][0])]
            for j in range(i + 1, len(ret_list)):
                if ret_list[j][2] - ret_list[i][2] < 0.02:
                    if ret_list[j][0] == last_tones[0][1]:
                        ret_list[j][2] += 0.05
                        ret_list[last_tones[0][0]][2] -= 0.05
                else:
                    break

        self.play_list = ret_list

######################################################################
    def servos_home(self):
        time.sleep(1)
        for i in range(32):
            self.servos.run_single_servo(i, 90)

    def play_music(self, play_list = None):
        if play_list == None:
            play_list = self.play_list

        start_time = time.time()
        for i in range(len(play_list)):
            while time.time() - start_time < play_list[i][2]:
                pass
            self.servos.set_single_angle(play_list[i][0], play_list[i][1])

            k = i
            for j in range(k + 1, len(play_list)):
                if play_list[j][2] - play_list[i][2] < 0.02:
                    self.servos.set_single_angle(play_list[j][0], play_list[j][1])
                    i += 1
                else:
                    break
            self.servos.run()

# from scores.亡靈序曲 import music_table
# from scores.梦中的婚礼 import music_table
# from scores.晴天 import music_table
# from scores.test import music_table
# from scores.天空之城 import music_table

# music_parse = music_trans(music_table)
# music_parse.music_to_play_table()

