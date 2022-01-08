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
"0": [90, 50], "1": [90, 40], "2": [90, 50],"3": [90, 50],"4": [90, 50],"5": [90, 50],"6": [90, 50],"7": [90, 50],
"8": [90, 50], "9": [90, 50],"10": [90, 50],"11": [90, 50],"12": [90, 50],"13": [90, 50],"14": [90, 40],
"15": [90, 40], "16": [90, 40],"17": [90, 40],"18": [90, 40],"19": [90, 40],"20": [90, 50],"21": [90, 50],
"22": [90, 50], "23": [90, 50],"24": [90, 40],"25": [90, 40],"26": [90, 50],"27": [90, 50],"28": [90, 50],
"29": [90, 50], "30": [90, 50],"31": [90, 50],"32": [90, 50],"33": [90, 50],"34": [90, 50],"35": [90, 50],
}
class music_trans():
    def __init__(self, music, beat_time = 3.2):
        self.servo_idx_base = 2

        self.music = music
        self.beat_time = beat_time
        self.play_list = []

        self.current_t = 0
        self.offset = 0

        self.tone_status = {}

        for key in servo_table:
            self.tone_status.update({key:0})
    def music_to_play_table(self, ope = "right"):
        if ope == "left":
            self.current_t = 0.1
        last_tone = []
        for i in range(len(self.music) // 2):
            if ope == "left":
                check_idx = 2 * i + 1
            else:
                check_idx = 2 * i
                        
            if isinstance(self.music[check_idx], tuple):
                for j in range(len(self.music[check_idx])):
                    offset_t = 0

                    chor = self.music[check_idx][j]

                    if chor != '-':
                        self.current_t -= 0.1
                        if last_tone != []:
                            for item in last_tone:
                                self._stop(item)
                        self.current_t += 0.1

                        last_tone = []

                    if isinstance(chor, str):
                        if "-" == chor:
                            self._rest(1 / 4)
                        elif ',' in chor:
                            chors = chor.split(",")
                            offset_t = 0
                            for item in chors:
                                self._play(item)
                                last_tone.append(item)
                                offset_t += 0
                                self.current_t += 0
                            self.current_t -= offset_t

                            self._rest(1 / 4)
                        elif chor != "-":
                            self._play(chor)
                            last_tone.append(chor)
                            self._rest(1 / 4)
                    elif isinstance(chor, tuple):
                        for k in range(len(chor)):
                            if chor[k] != "-":
                                if k >= 1:
                                    if last_tone != []:
                                        self._stop(last_tone.pop())
                                self._play(chor[k])
                                last_tone.append(chor[k])
                            else:
                                pass                            
                            self._rest(1 / (len(chor * 4)))

            elif isinstance(music[check_idx], dict):
                info = self.music[check_idx]["origin"]
                for item in info:
                    self.current_t + item[1]
                    self._play(item[0])
                    self.current_t + item[2]
                    self._stop(item)
        self.play_list_sort()

    def play_list_sort(self):
        hh = self.play_list.copy()
        ret_list = []
        while hh != []:
            current_index = 0
            min_t = 100000
            for i in range(len(hh)):
                if hh[i][2] < min_t:
                    min_t = hh[i][2]
                    current_index = i
            ret_list.append(hh[current_index])
            del hh[current_index]

        last_angles = []
        for i in range(len(ret_list)):
            last_angles = [(i, ret_list[i][0])]
            k = i
            for j in range(k + 1, len(ret_list)):
                if ret_list[j][2] - ret_list[k][2] < 0.02:
                    i += 1

                    for jjj in last_angles:
                        if ret_list[j][0] == jjj[1]:
                            ret_list[j][2] += 0
                            ret_list[jjj[0]][2] -= 0.06
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
    def music_to_play_table2(self, ope = "right"):
        last_tone = []
        for i in range(len(self.music)):
            check_idx = i
            if isinstance(self.music[check_idx], tuple):
                for j in range(len(self.music[check_idx])):
                    offset_t = 0

                    chor = self.music[check_idx][j]

                    if chor != '-':
                        self.current_t -= 0.05
                        if last_tone != []:
                            for item in last_tone:
                                chors = chor.split(",")
                                if item in chors:
                                    self._stop(item, 80)
                                else:
                                    self._stop(item)
                        self.current_t += 0.05
                        offset_t = 0
                        last_tone = []

                    if isinstance(chor, str):
                        if "-" != chor:
                            chors = chor.split(",")
                            for item in chors:
                                self._play(item)
                                last_tone.append(item)
                        self.current_t -= offset_t
                        offset_t = 0
                        self._rest(1 / 16)

            elif isinstance(music[check_idx], dict):
                info = self.music[check_idx]["origin"]
                for item in info:
                    self.current_t + item[1]
                    self._play(item[0])
                    self.current_t + item[2]
                    self._stop(item)
        self.play_list_sort()
######################################################################
    def music_to_play_table3(self, ope = "right"):
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
music_parse = music_trans(music_table)
music_parse.music_to_play_table3("right")
# music_parse.music_to_play_table("left")

def play_music(play_list):
    print(play_list)
    start_time = time.time()
    for i in range(len(play_list)):
        while time.time() - start_time < play_list[i][2]:
            pass
        servos.set_single_angle(play_list[i][0], play_list[i][1])

        k = i
        for j in range(k + 1, len(play_list)):
            if play_list[j][2] - play_list[i][2] < 0.02:
                servos.set_single_angle(play_list[j][0], play_list[j][1])
                print(111)
                i += 1
            else:
                break
        servos.run()
        print(222)


servos = servo.servo_control()

def init():
    time.sleep(2)
    for i in range(32):
        servos.run_single_servo(i, 90)
    servos.run()
init()

play_music(music_parse.play_list)
