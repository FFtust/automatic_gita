music_table = \
(
    ("3++,6+,1+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("1++,5+,2+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("6+#,4+,1+", "-", "-", "-", "-", "-", "-", "-", "2+,6+#,3+", "-", "-", "-", "-", "-", "-", "-"),
    ("-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),

    ("0", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("0", "-", "3+", "-", "3+", "-", "3+", "-", "3+", "-", "2+", "-", "3+", "-", "6+", "-"),
    ("3+", "-", "2+", "2+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("0", "-", "2+", "-", "2+", "-", "2+", "-", "2+", "-", "1+", "-", "2+", "-", "5+", "-"),

    ("2+", "-", "1+", "-", "7", "-", "1+", "-", "-", "-", "-", "-", "-", "-", "6", "7"),
    ("1+", "-", "1+", "-", "1+", "-", "1+", "-", "1+", "-", "-", "-", "-", "-", "6", "7"),
    ("1+", "-", "1+", "-", "1+", "-", "1+", "-", "7", "-", "1+", "-", "-", "-", "6", "7"),
    ("1+", "-", "1+", "-", "1+", "-", "1+", "-", "1+", "-", "5+", "-", "-", "-", "1+", "-"),

    ("0", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("0", "-", "3+", "-", "3+", "-", "3+", "-", "3+", "-", "2+", "-", "3+", "-", "6+", "-"),
    ("3+", "-", "2+", "2+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("0", "-", "2+", "-", "2+", "-", "2+", "-", "2+", "-", "1+", "-", "2+", "-", "5+", "-"),
)


music_table_left = \
(
    ("1+,4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("7,3", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("6,2", "-", "-", "-", "-", "-", "-", "-", "4,4#,1", "-", "-", "-", "-", "-", "-", "-"),
    ("-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "0"),

    ("3,7-,4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("5,2,6-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),

    ("-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("4,1,5-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("3,7-,4-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("2,6-3-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),

    ("1,5-,2-", "-", "-", "-", "-", "-", "-", "-", "2,6-,3-", "-", "-", "-", "-", "-", "-", "-"),
    ("3,7-,6-,4--", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("5--", "-", "4-", "-", "5-", "-", "2", "-", "-", "-", "-", "-", "-", "-", "-", "-"),
    ("2,6-3-,1--", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),

    ("0",),
)

import sys,time
sys.path.append('../')

import music_translate
music_parse = music_translate.music_trans([music_table_left, music_table], beat = 80)
music_parse.music_to_play_table()
music_parse.play_music()
