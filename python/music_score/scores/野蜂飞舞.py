music_table = \
(
    ("3++", "2++", "2++", "1++", "2++", "1++", "1++", "7+"),
    ("1++", "7+", "6+#", "6+#", "5+#", "5+#", "4+#", "4+#"),
    ("3+", "2+#", "2+#", "1+", "2+", "1+", "1+#", "7"),
    ("1+", "7", "6#", "6#", "5#", "5#", "4#", "4#"),

    ("3", "2#", "2#", "1", "2", "1", "1#", "7-"),
    ("3", "2#", "2#", "1#", "2", "1", "1#", "7-"),
    ("3", "2#", "2#", "1#", "2", "1", "1#", "7-"),
    ("3", "2#", "2#", "1#", "2", "1", "1#", "7-"),
)


import sys
sys.path.append('C:\\work\\automatic_gita\\python\\music_score')

import music_translate
music_parse = music_translate.music_trans([music_table])
music_parse.set_beat(1.3)
music_parse.music_to_play_table()

music_parse.servos_home()
music_parse.play_music()
music_parse.servos_home()
