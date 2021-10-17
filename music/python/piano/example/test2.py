# -0.05 +0.02

music_table = \
(
    ("0", "-", "-", "-"),
    ("3", "-", "-", "-"),
    ("3++,7+", "1++", "6+", "-", "3++,7+", "1++", "6+", "-", "6+,3+", "4+", "2+", "-", "6+,3+", "4+", "2+", "-"),
    ("7+,4+#", "5+#", "3+", "-", "7+,3+", "-", "3+,7", "1+", "6", "-", "3+,7", "1+", "6", "-", "-", "-"),

)

music_table_left = \
(
    ("0", "-", "-", "-"),
    ("6-,6--", "-", "-", "-"),
    ("6-", "-", "4-", "-"),
    ("3-", "-", "6--", "-")
)

import sys
sys.path.append('C:\\work\\automatic_gita\\python\\piano')

import music_translate
music_parse = music_translate.music_trans([music_table, music_table_left], beat = 96)
music_parse.music_to_play_table()
music_parse.play_music()
