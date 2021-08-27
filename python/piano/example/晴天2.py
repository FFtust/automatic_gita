music_table = \
(
 	("0", "-", "-", "-"),
    ("0", "-", "1", "-", "5", "-", "1", "-", "0", "-", "5-", "-", "5", "-", "1", "-"),
    ("0", "-", "5-", "-", "5", "-", "1", "-", "5-", "-", "5", "-", "5-", "-", "2", "-"),
    ("0", "-", "1", "-", "5", "-", "1", "-", "0", "-", "5-", "-", "5", "-", "1", "-"),
    ("0", "-", "5-", "-", "5", "-", "1", "-", "5-", "-", "1", "-", "2", "-", "5-", "-"),

    ("0", "-", "1", "-", "5", "-", "1", "-", "0", "-", "5-", "-", "5", "-", "1", "-"),
    ("0", "-", "5-", "-", "5", "-", "1", "-", "5-", "-", "5", "-", "5-", "-", "2", "-"),
    ("0", "-", "1", "-", "5", "-", "1", "-", "0", "-", "5-", "-", "5", "-", "1", "-"),
    ("0", "-", "5-", "-", "5", "-", "1", "-", "5-", "-", "1", "-", "2", "-", "5-", "-"),

    ("0", "-", "5", "-", "5", "-", "1", "-", "1", "-", "-", "-", "2", "-", "3", "-"),
    ("-", "-", "5", "-", "5", "-", "1", "-", "1", "-", "2", "3", "2", "-", "1", "-"),
    ("0", "-", "5", "-", "5", "-", "1", "-", "1", "-", "-", "-", "2", "-", "3", "-"),
    ("-", "-", "3", "-", "-", "-", "-", "3", "4", "3", "2", "4", "3", "-", "1", "-"),

    ("0", "-", "3,6-", "-", "3,6-", "-", "3,6-", "-", "4,6-", "-", "3", "-", "2,6-", "-", "1", "2"),
    ("3,5-", "-", "3,5-", "-", "3,5-", "-", "3,5-", "-", "2", "3", "2,5-", "-", "1,5-", "-", "-", "-"),
    ("6-", "-", "7-", "-", "1", "-", "3", "-", "4,6-", "-", "3", "-", "2", "-", "1", "2"),
    ("3,5-", "-", "3,5-", "-", "3,5-", "-", "3,5-", "-", "2", "3", "2,5-", "-", "1,5-", "-", "-", "-"),
)

music_table_left = \
(
 	("0", "-", "-", "-"),
	("6--", "-", "-", "-", "-", "-", "-", "-", "4--", "-", "-", "-", "-", "-", "-", "-"),
	("1-", "-", "-", "-", "-", "-", "-", "-", "1-", "-", "-", "-", "7--", "-", "-", "-"),
	("6--", "-", "-", "-", "-", "-", "-", "-", "4--", "-", "-", "-", "-", "-", "-", "-"),
	("1-", "-", "-", "-", "-", "-", "-", "-", "1-", "-", "-", "-", "7--", "-", "-", "-"),

	("6---", "-", "3--", "-", "1-", "-", "4--", "-", "4---", "-", "1--", "-", "6--", "-", "1--", "-"),
	("1--", "-", "5--", "-", "3-", "-", "5--", "-", "1--", "-", "5--", "-", "7--,7---", "-", "-", "-"),
	("6---", "-", "3--", "-", "1-", "-", "4--", "-", "4---", "-", "1--", "-", "6--", "-", "1--", "-"),
	("1--", "-", "5--", "-", "3-", "-", "5--", "-", "1--", "-", "5--", "-", "7--,7---", "-", "5--", "-"),

	("6---", "-", "3--", "-", "1-", "-", "4--", "-", "4---", "-", "1--", "-", "1-", "-", "6--", "-"),
	("1--", "-", "5--", "-", "3-", "-", "5--", "-", "3-", "-", "5--", "-", "7--,7---", "-", "5--", "-"),
	("6---", "-", "3--", "-", "1-", "-", "4--", "-", "4---", "-", "1--", "-", "1-", "-", "6--", "-"),
	("1--", "-", "5--", "-", "3-", "-", "5--", "-", "3-", "-", "5--", "-", "7--,7---", "-", "5--", "-"),

	("6---", "-", "3--", "-", "1-", "-", "4--", "-", "4---", "-", "1--", "-", "1-", "-", "6--", "-"),
	("1--", "-", "5--", "-", "3-", "-", "5--", "-", "3-", "-", "5--", "-", "7--,7---", "-", "5--", "-"),
	("6---", "-", "3--", "-", "1-", "-", "4--", "-", "4---", "-", "1--", "-", "1-", "-", "6--", "-"),
	("1--", "-", "5--", "-", "3-", "-", "5--", "-", "3-", "-", "5--", "-", "7--,7---", "-", "5--", "-"),

)


import sys
sys.path.append('C:\\work\\automatic_gita\\python\\piano')

import music_translate
music_parse = music_translate.music_trans([music_table, music_table_left], toneG="G")
music_parse.set_beat(68`)
music_parse.servos_home()
music_parse.music_to_play_table()
music_parse.play_music()
music_parse.servos_home()

