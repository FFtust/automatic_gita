music_table = \
(
    ("3+", "2+", "2+", "1+", "1+", "4+", "3+", "2+"),
    ("3+", "2+", "2+", "1+", "1+", "1+", "2+", "2+"),
    ("3+", "2+", "2+", "1+", "1+", "4+", "3+", "2+"),
    ("3+", "2+", "2+", "1+", "1+", "1+", "2+", "2+"),
    ("3+", "2+", "2+", "1+", "2+", "1+", "1+", "7"),
    ("1+", "1+", "2+", "2+", "3+", "4+", "3+", "-"),
)


import sys
sys.path.append('C:\\work\\automatic_gita\\python\\music_score')

import music_translate
music_parse = music_translate.music_trans([music_table])
music_parse.set_beat(3)
music_parse.music_to_play_table()

music_parse.servos_home()
music_parse.play_music()
music_parse.servos_home()
