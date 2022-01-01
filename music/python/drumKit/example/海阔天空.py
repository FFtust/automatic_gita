
music_table1 = \
(
	("0:0=1/4",),
	("1:1+=1/8",),
    ("4:4:4:1:1,2:1:1:1=1/8",),
    ("1:1:1:1:1,2:1:1:1=1/8",),

    ("3:3:3:3:3,2:3:3:3=1/8","3:3:3:3:4,2:3:3:3=1/8",),

)

music_table2 = \
(
	("0:0=1/4",),
    ("1=1/4","0=3/4", "1=1/4", "0=1/2", "1=1/8", "0=1/8"),
    ("1=1/4","0=3/4", "1=1/4", "0=1/2", "1=1/8", "0=1/8"),

)

import sys,time
sys.path.append('../')

import music_translate2 as music_translate
music_parse = music_translate.music_trans([music_table1, music_table2], beat=110)
music_parse.music_to_play_table()
music_parse.play_music()