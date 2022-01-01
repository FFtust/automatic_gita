music_table1 = \
(
    ("0:0=1/2",),
    # 1
    ("0:0:0=1/4", "4+:5+=1/8"),
    ("6+:3++:2++=1/4", "1++:2++=1/8"),
    ("2++:7+:7+:2++=1/8", "1++=3/8", "3+=1/8"),
    ("4+=1/4", "4+:3++:3++:2++:2++:1++=1/8"),

    # 5
    ("1++=3/4", "0:5-=1/8"),
    ("5,3,1=1/4", "5,3,1:0:4,2,7-:0:4,2,7-:1=1/8"),
    ("3,1,6-=3/4", "0:1=1/8"),
    ("1+,6,4=1/4", "1+,6,4:0:7,5,3:0:7,5,3-:1=1/8"),

)

music_table2 = \
(
    ("0:0=1/2",),

    # 1
    ("0=1",),
    ("4-:1=1/8", "4=1/4", "4,5-:2=1/8", "5=1/4"),
    ("3--,7--=1/8", "5-#=1/4", "6--:3-=1/8", "1=1/4"),
    ("2--:2-=1/8", "4-:4-,5--:5-=1/4"),

    # 5
    ("1--:1-:3-:5-=1/8", "1=1/2"),
    ("1-:5-=1/8", "1=1/4", "7--:5-=1/8", "7-=1/4"),
    ("6--:3-=1/8", "1=1/4", "5--:3-=1/8", "1=1/4"),
    ("4--:1-=1/8", "4-=1/4", "3--:1-=1/8", "3-=1/4"),
)

import sys,time
sys.path.append('../')
import music_translate2 as music_translate
music_parse = music_translate.music_trans([music_table1, music_table2], beat=72)
music_parse.music_to_play_table()
music_parse.play_music()