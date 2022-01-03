# -0.05 +0.02

music_table_right = \
(
    ("1A:1A:1A:1A:1A:1A:1A:1A:1A:1A=1/16",),
    ("3:3:3:3:3:3:3:3:3:3=1/16",),
    ("2:2:2:2:2:2:2:2:2:2=1/16",),
    ("3:3:3:3:3:3:3:3:3:3=1/16",),

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
sys.path.append('../')

import music_translate2 as music_translate
music_parse = music_translate.music_trans([music_table_right], beat = 150)
music_parse.music_to_play_table()
music_parse.play_music()
