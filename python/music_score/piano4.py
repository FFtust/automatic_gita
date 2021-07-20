
import time
import servo
servos = servo.servo_control()
import _thread
lock = _thread.allocate_lock()
###########################
# servo 
servo_table = {\
"1--": 1, "2--": 2,"3--": 3,"4--": 4,"5--": 5,"6--": 6,"7--": 7,
"1-": 8, "2-": 9,"3-": 10,"4-": 11,"5-": 12,"6-": 13,"7-": 14,
"1": 15, "2": 16,"3": 17,"4": 18,"5": 19,"6": 20,"7": 21,
"1+": 22, "2+": 23,"3+": 24,"4+": 25,"5+": 26,"6+": 27,"7+": 28,
"1++": 29, "2++": 30,"3++": 31,"4++": 32,"5++": 33,"6++": 34,"7++": 35,
"1+++": 36, "2+++": 37,"3+++": 38,"4+++": 39,"5+++": 40,"6+++": 41,"7+++": 42,
}

###########################

music_table = \
(
    ("5++,1++,7+", "-", "-", "-"),
    ("2+,1+,4", "-", "-", "-"),

    ("2++,7+,5+", "-", "-", "-"),
    ("2+,7,3", "-", "-", "-"),

    (("6+", "7+"), ("1++", "3++"), ("1++", "7+"), ("6+", "7+")),
    ("2+,1+,4", "-", "-", "-"),

    ("1++",  "-", "-", "-"),
    ("0", "-", "-", "-"),

##############################################
    (("3+", "2+"), ("3+", "6+"), ("3+", "2+"), ("3+", "7+")),
    ("1,4-", "-", "2,5-", "-"),

    (("3+", "2+"), ("3+", "1++"), "7+", "5+"),
    ("3,6-", "-", "-", "-"),

    (("3+", "2+"), ("3+", "6+"), ("3+", "2+"), ("3+", "7+")),
    ("1,4-", "-", "2,5-", "-"),

    ("5+", "1+", "7", "5"),
    (("6-", "3"), ("6", "3"), "0", "-"),
##############################################
    (("3+", "2+"), ("3+", "6+"), ("3+", "2+"), ("3+", "7+")),
    ("1,4-", "-", "2,5-", "-"),


    (("3+", "2+"), ("3+", "1++"), "7+", "5+"),
    ("3,6-", "-", "0", "-"),

    (("2+", "3+"), "6", ("2+", "3+"), ("6", "5")),
    (("2-", "6-"), "2", ("3", "7-"), "3"),

    ("6", "-", "-", "-"),
    (("6--", "3-"), ("6-", "7-"), "1", "-"),
##############################################
    (("6", "1+"), ("1+", "2+"), ("2+", "3+"), ("3+", "6+")),
    (("6-", "1"), "4", "-", "1"),

    ("5+", "3+", "2+", "-"),
    ("3-", "7-", "3", "-", "-", "-", "2", "-"),

    (("6", "1+"), ("1+", "2+"), ("2+", "3+"), "3+"),
    ("6-", "1", "4", "-", "-", "-", "1", "-"),

    (("6", "5"), "-", "3+", "5"),
    ("3-", "7-", "3", "-", "-", "-", "-", "-"),
)

play_list = []
ref_time = 0
def play(tone, t = 0):
    global ref_time, play_list

    if tone == "0":
        return 
    # servos.set_single_angle(servo_table[tone] - 8, 30)
    play_list.append([servo_table[tone] - 8, 30, time.time() - ref_time])

def stop(tone, t = 0):
    global ref_time, play_list

    if tone == "0":
        return 

    # servos.set_single_angle(servo_table[tone] - 8, 65)
    play_list.append([servo_table[tone] - 8, 65,  time.time() - ref_time])


BEAT_T = 0.32
def rest(beat, t = BEAT_T):
    last_t = time.time()
    while time.time() - last_t < beat * t:
        pass

def rest_t(t = 0.1):
    last_t = time.time()
    while time.time() - last_t < t / 10:
        pass

def parse_music(music, ope):
    global ref_time
    ref_time = time.time()
    last_t = time.time()

    last_tone = []
    
    for i in range(len(music) // 2):
        for j in range(4):
            if ope == "left":
                chor = music[2 * i + 1][j]
            else:
                chor = music[2 * i][j]

            if chor != '-':
                for item in last_tone:
                    stop(item)
                    servos.run()
                rest_t(0.05)
                last_tone = []

            else:
                rest(1 / 8)
                continue

            if isinstance(chor, str):
                if ',' in chor:
                    chors = chor.split(",")
                    for item in chors:
                        play(item)
                        last_tone.append(item)
                        servos.run()
                        rest_t(0.05)
                elif chor != "-":
                    play(chor)
                    last_tone.append(chor)
                    servos.run()
                               
            elif isinstance(chor, tuple):
                for k in range(len(chor)):
                    if k >= 1:
                        stop(last_tone.pop())
                    play(chor[k])
                    last_tone.append(chor[k])
                    servos.run()
                    rest(1 / 8)

            while time.time() - last_t < BEAT_T / 4:
                rest_t(0.01)
            last_t = time.time()

def init():
    time.sleep(1)
    for i in range(32):
        servos.run_single_servo(i, 90)
    servos.run()

def play_list_sort(play_data):
    hh = play_data.copy()
    ret_list = []
    while hh != []:
        current_index = 0
        min_t = 100000
        for i in range(len(hh)):
            if hh[i][2] < min_t:
                min_t = hh[i][2]
                current_index = i    
                print(len(hh), min_t)    
        ret_list.append(hh[current_index])
        print(hh[current_index], len(hh))
        del hh[current_index]
    return ret_list


init()
parse_music(music_table, "right")
print(play_list)
parse_music(music_table, "left")
print(play_list)

play_list = play_list_sort(play_list)

print("aaaaaaaaaa", play_list)
start_time = time.time()
for i in range(len(play_list)):
    while time.time() - start_time < play_list[i][2] * 10:
        pass
    servos.set_single_angle(play_list[i][0], play_list[i][1])
    servos.run()
