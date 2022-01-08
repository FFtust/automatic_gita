# -0.05 +0.02

music_table_right = \
(
    ("0", "-", "-", "-"),
    ("3", "-", "2", "-"),
    ("1", "-", "7-", "-"),
    ("6-", "-", "5-", "-"),
    ("6-", "-", "7-", "-"),


)

music_table_left = \
(
    ("0", "-", "-", "-"),
    ("1-", "-", "5--", "-"),
    ("6--", "-", "3--", "-"),
    ("4----", "-", "5--", "-"),
    ("4----", "-", "5--", "-"),

)

import sys
sys.path.append('C:\\work\\automatic_gita\\python\\piano')

import music_translate
music_parse = music_translate.music_trans([music_table_right, music_table_left], beat = 82)
music_parse.music_to_play_table()
music_parse.play_music()
