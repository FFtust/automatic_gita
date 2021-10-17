# -0.05 +0.02

music_table = \
(
    ("0", "-", "-", "-"),
)

music_table_left = \
(
    ("0", "-", "-", "-"),
)

import sys
sys.path.append('C:\\work\\automatic_gita\\python\\piano')

import music_translate
music_parse = music_translate.music_trans([music_table, music_table_left], beat = 60)
music_parse.music_to_play_table()
music_parse.play_music()
