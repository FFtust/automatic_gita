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
"0": [80, 40], "1": [80, 40], "2": [80, 40],"3": [80, 40],"4": [80, 40],"5": [80, 40],"6": [80, 40],"7": [80, 40],
"8": [80, 40], "9": [80, 40],"10": [80, 40],"11": [80, 40],"12": [80, 40],"13": [80, 40],"14": [80, 40],
"15": [80, 40], "16": [80, 40],"17": [80, 40],"18": [80, 40],"19": [80, 40],"20": [80, 40],"21": [80, 40],
"22": [80, 40], "23": [80, 40],"24": [80, 40],"25": [80, 40],"26": [80, 40],"27": [80, 40],"28": [80, 40],
"29": [80, 40], "30": [80, 40],"31": [80, 40],"32": [80, 40],"33": [80, 40],"34": [80, 40],"35": [80, 40],
}
class music_trans():
    def __init__(self, music, beat_time = 4):
        self.servo_idx_base = 3

        self.music = music
        self.beat_time = beat_time
        self.play_list = []

        self.current_t = 0
        self.offset = 0

        self.tone_status = {}

        for key in servo_table:
            self.tone_status.update({key:0})

    def play_list_sort(self):
        hh = self.play_list.copy()
        ret_list = []
        # 按时间排序
        while hh != []:
            current_index = 0
            min_t = 100000
            for i in range(len(hh)):
                if hh[i][2] < min_t:
                    min_t = hh[i][2]
                    current_index = i
            ret_list.append(hh[current_index])
            del hh[current_index]

        # 两个连续的相同音符需要单独处理，否则将不会抬起，只有一个声音
        last_angles = []
        for i in range(len(ret_list)):
            last_angles = [(i, ret_list[i][0])]
            k = i
            for j in range(k + 1, len(ret_list)):
                if ret_list[j][2] - ret_list[k][2] < 0.02:
                    i += 1

                    for jjj in last_angles: 
                        if ret_list[j][0] == jjj[1]:
                            ret_list[j][2] += self.beat_time * (1/150)#0.04
                            ret_list[jjj[0]][2] -= self.beat_time * (1/150)#0.04
                            break

                    last_angles.append((j, ret_list[j][0]))
                    print((j, ret_list[j][0]))
                else:
                    break

        self.play_list = ret_list
#######################################################
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
        for i in range(len(self.music)):
            check_idx = i
            if isinstance(self.music[check_idx], tuple):
                for j in range(len(self.music[check_idx])):
                    offset_t = 0

                    chor = self.music[check_idx][j]

                    if chor != '-':
                        chors = chor.split(",")
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

import time
import servo

from scores.亡靈序曲 import music_table
# from scores.梦中的婚礼 import music_table
# from scores.晴天 import music_table
music_parse = music_trans(music_table)
music_parse.music_to_play_table()

def play_music(play_list):
    start_time = time.time()
    for i in range(len(play_list)):
        while time.time() - start_time < play_list[i][2]:
            pass
        servos.set_single_angle(play_list[i][0], play_list[i][1])

        k = i
        for j in range(k + 1, len(play_list)):
            if play_list[j][2] - play_list[i][2] < 0.02:
                servos.set_single_angle(play_list[j][0], play_list[j][1])
                i += 1
            else:
                break
        servos.run()

servos = servo.servo_control()

def init():
    time.sleep(2)
    for i in range(32):
        servos.run_single_servo(i, 90)
init()
play_music(music_parse.play_list)
