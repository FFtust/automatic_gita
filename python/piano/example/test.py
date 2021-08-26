music_table = \
(
    # ("1-", "2-", "3-", "4-", "5-", "6-", "7-", "1", "2", "3", "4", "5", "6", "7", "1+", "2+"),
    # ("3+", "4+", "5+", "6+", "7+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),

    ("1", "1#", "2#", "4#", "5#", "6#"),
    ("1+#", "1+#", "2+#", "4+#", "5+#", "6+#"),

)


# music_table = \
# (
#     # ("1-", "2-", "3-", "4-", "5-", "6-", "7-", "1", "2", "3", "4", "5", "6", "7", "1+", "2+"),
#     # ("3+", "4+", "5+", "6+", "7+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),

#     ("1-", "1-", "2-", "2-", "3-", "3-", "4-", "4-", "5-", "5-", "6-", "6-", "7-", "7-", "1", "1"),
#     ("2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7", "1+", "1+", "2+", "2+"),
#     ("3+", "3+", "4+", "4+", "5+", "5+", "6+", "6+", "7+", "7+", "7+", "7+", "7+", "7+", "7+", "7+"),

# )

import sys,time
sys.path.append('C:\\work\\automatic_gita\\python\\music_score')

import music_translate
music_parse = music_translate.music_trans([music_table])
music_parse.servos_home()
music_parse.set_beat(10)
music_parse.music_to_play_table()
music_parse.play_music()
music_parse.servos_home()

# music_parse.servos.run_single_servo(32, 70)
# time.sleep(1)
# music_parse.servos.run_single_servo(32, 100)
