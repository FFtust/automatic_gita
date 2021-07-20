
import time
import servo
servos = servo.servo_control()

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
## chord
DO_ = 1
RE_ = 2
MI_ = 3
FA_ = 4
SO_ = 5
LA_ = 6
XI_ = 7


music_table = \
(
    ("3+", "-", "-", "-"), 
    ("1", "3", "5", "-"),

    ("2+", "-", "-", "-"), 
    ("5-", "7-", "2", "-"),

    ("1+", "-", "-", "-"), 
    ("6-", "1", "3", "-"),

    ("7", "-", "-", "-"), 
    ("3-", "5-", "7-", "-"),

    ("6", "-", "-", "-"), 
    ("4-", "6-", "1", "-"),
######
    ("5", "-", "-", "-"), 
    ("1-", "3-", "5-", "-"),

    ("6", "-", "-", "-"), 
    ("4-", "6-", "1", "-"),

    ("7", "-", "-", "-"), 
    ("5-", "7-", "2", "-"),

    ("3+", "-", "3+", "1+"), 
    ("1", "3", "5", "-"),

    ("2+", "-", "-", "7"), 
    ("5-", "7-", "2", "-"),    
#######
    ("1+", "-", "1+", "6"), 
    ("6-", "1", "3", "-"),

    ("7", "-", "-", "5"), 
    ("3-", "5-", "7-", "-"),

    ("6", "-", "6", "4"), 
    ("4-", "6-", "1", "-"),

    ("5", "-", "-", "3"), 
    ("1-", "3-", "5-", "-"),

    ("6", "-", "6", "1+"), 
    ("4-", "6-", "1", "-"),

#####
    ("7", "-", "1+", "2+"), 
    ("5-", "7-", "2", "-"),

    ("3+", "2+", "3+", "4+"), 
    ("1-", "5-", "3", "-"),

    ("5+", "2+", "5+", "4+"), 
    ("5-", "2-", "7-", "-"),

    ("3+", "6+", "5+", "4+"), 
    ("6-", "3-", "1", "-"),

    ("5+", "4+", "3+", "2+"), 
    ("3-", "7-", "5-", "-"),
)

music_table2 = \
(
    ("3", "3"), 
    ("6", "-", "5", "6",  "-", "6", "-", "-", "-",  "6", "-", "-", "-",  "0", "-", "3", "3"),

    ("2+", "-", "-", "-"), 
    ("5-", "7-", "2", "-"),

    ("1+", "-", "-", "-"), 
    ("6-", "1", "3", "-"),

    ("7", "-", "-", "-"), 
    ("3-", "5-", "7-", "-"),

    ("6", "-", "-", "-"), 
    ("4-", "6-", "1", "-"),
######
    ("5", "-", "-", "-"), 
    ("1-", "3-", "5-", "-"),

    ("6", "-", "-", "-"), 
    ("4-", "6-", "1", "-"),

    ("7", "-", "-", "-"), 
    ("5-", "7-", "2", "-"),

    ("3+", "-", "3+", "1+"), 
    ("1", "3", "5", "-"),

    ("2+", "-", "-", "7"), 
    ("5-", "7-", "2", "-"),    
#######
    ("1+", "-", "1+", "6"), 
    ("6-", "1", "3", "-"),

    ("7", "-", "-", "5"), 
    ("3-", "5-", "7-", "-"),

    ("6", "-", "6", "4"), 
    ("4-", "6-", "1", "-"),

    ("5", "-", "-", "3"), 
    ("1-", "3-", "5-", "-"),

    ("6", "-", "6", "1+"), 
    ("4-", "6-", "1", "-"),

#####
    ("7", "-", "1+", "2+"), 
    ("5-", "7-", "2", "-"),

    ("3+", "2+", "3+", "4+"), 
    ("1-", "5-", "3", "-"),

    ("5+", "2+", "5+", "4+"), 
    ("5-", "2-", "7-", "-"),

    ("3+", "6+", "5+", "4+"), 
    ("6-", "3-", "1", "-"),

    ("5+", "4+", "3+", "2+"), 
    ("3-", "7-", "5-", "-"),
)

def play(tone):
    # servos.run_single_servo(servo_table[tone] - 8, 50)
    servos.set_single_angle(servo_table[tone] - 8, 30)
    print("{} play".format(tone))
    # time.sleep(0.01)


def stop(tone):
    # servos.run_single_servo(servo_table[tone] - 8, 90)
    servos.set_single_angle(servo_table[tone] - 8, 75)

    print("{} stop".format(tone))

    # time.sleep(0.01)


def parse_music(music):
    last_tone_1 = music[0][0]
    last_tone_2 = music[1][0]

    for i in range(len(music) // 2):
        for j in range(4):
            if music[2 * i][j] != '-':
                if last_tone_1 != music[2 * i][j]:
                    stop(last_tone_1)
                play(music[2 * i][j])
                last_tone_1 = music[2 * i][j]

            if music[2 * i + 1][j] != '-':
                if last_tone_2 != music[2 * i + 1][j]:
                    stop(last_tone_2)
                play(music[2 * i + 1][j])
                last_tone_2 = music[2 * i + 1][j]
            servos.run()

            time.sleep(0.4)


def test():
    for i in range(7):
        play(str(i + 1) + "-")
        time.sleep(0.5)

def init():
    # for i in range(32):
    #     servos.run_single_servo(i, 45)
    #     time.sleep(0.1)

    time.sleep(1)
    for i in range(32):
        servos.run_single_servo(i, 90)
        time.sleep(0.1)
    time.sleep(2)

while True:
    init()
    parse_music(music_table)    

    init()