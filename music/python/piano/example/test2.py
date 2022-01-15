# -0.05 +0.02

music_table_key_test = \
(
    ("0", "-", "-", "-"),
    ("1--", "1--#", "2--", "2--#","3--", "4--", "4--#","5--", "5--#","6--", "6--#","7--"),
    ("1-", "1-#", "2-", "2-#","3-", "4-", "4-#","5-", "5-#","6-", "6-#","7-"),
    ("1", "1#", "2", "2#","3", "4", "4#","5", "5#","6", "6#","7"),
    ("1+", "1+#", "2+", "2+#","3+", "4+", "4+#","5+", "5+#","6+", "6+#","7+"),
    ("1++", "1++#", "2++", "2++#","3++", "4++", "4++#","5++", "5++#","6++", "6++#","7++"),
)

music_table_speed_test = \
(
    ("0", "-", "-", "-"),
    ("1-", "-", "5--", "-"),
    ("6--", "-", "3--", "-"),
    ("4----", "-", "5--", "-"),
    ("4----", "-", "5--", "-"),

)


import sys, time
sys.path.append('../../')
sys.path.append('../../../../')



def sleep(t):
    import piano.note as note

    s = time.time()
    while time.time() - s < t:
        note.servoCtl.update()
        time.sleep(0.0001)

def speed_test():
    import piano.note as note
    note.servos_home()
    for i in range(10):
        note.play_note([("1", 0)], 1)
        sleep(0.07)
        note.stop_note("1", 1)
        sleep(0.07)

speed_test()
# if __name__ == "__main__":
#     import piano.music_translate2 as music_translate

#     music_parse = music_translate.music_trans([music_table_key_test], beat = 80)
#     music_parse.music_to_play_table()
#     music_parse.play_music()