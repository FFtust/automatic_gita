music_table = \
(
 	("0", "0", "0", "0", "0", "0"),

 	("0", "0", "0", "0", "0", "0"),
 	("0", "0", "0", "0", "0", "0"),
 	# 3
 	("6-,3-,1-,6--", "-", "6-,3-,1-,6--", "-", "6-,6--", "7-,7--", "1,6-,4-,1-", "-", "1,6-,4-,1-", "-", "1,1-", "2,2-", "7-,5-,3-,7--", "-", "7-,5-,3-,7--", "-", "6-,6--", "5-,5--", "5-,5--", "6-, 6--", "-", "-", "3-,3--", "5-,5--"),
 	("6-,4-,1-,6--", "-", "6-,4-,1-,6--", "-", "6-,6--", "7-,7--", "1,5-,4-,1-", "-", "1,5-,4-,1-", "-", "1,1-", "2,2-", "7-,5-,2-,7--", "-", "7-,5-,2-,7--", "-", "6-,6--", "5-,5--", "6-,6--", "-", "-", "-", "3-,3--", "5-,5--"),
 	# 5
 	("6-,3-,1-,6--", "-", "6-,3-,1-,6--", "-", "6-,6--", "1,1-", "2,6-,4-,2-", "-", "2,6-,4-,2-", "-", "2,2-", "3,3-", "4,2,6-,4-", "-", "4,2,6-,4-", "-", "3,3-", "2,2-", "3,1,6-,3-", "6-, 6--", "-", "-", "6-,6--", "7-,7--"),
 	("1,6-,4-,1-", "-", "1,6-,4-,1-", "-", "2,2-", "-", "3,1,6-,3-", "6-,6--", "-", "-", "6-,6--", "1,1-", "7-,5-#,3-,7--", "-", "7-,5-#,3-,7--", "-", "1,1-", "6-,6--", "7-,5-#,3-,7--", "-", "0", "-", "3,3-", "5,5-"),
 	# 7
)

music_table_left = \
(
 	("0", "0", "0", "0", "0", "0"),

    ("6--,6---", "0", "6--,6---", "6--,6---", "0", "6--,6---", "6--,6---", "0", "6--,6---", "6--,6---", "0", "6--,6---","6--,6---", "0", "6--,6---", "6--,6---", "0", "6--,6---","6--,6---", "0", "6--,6---", "6--,6---", "0", "6--,6---"),
    ("6--,6---", "0", "6--,6---", "6--, 6---", "0", "6--,6---", "6--,6---", "0", "6--,6---", "6--,6---", "0", "6--,6---","6--,6---", "0", "6--,6---", "6--,6---", "0", "6--,6---","6--,6---", "0", "6--,6---", "6--,6---", "0", "6--,6---"),

    # 3
 	("6--,6---", "-", "-", "6--,6---", "-", "-", "4-,4--", "-", "-", "4-,4--", "-", "-", "3-,3--", "-", "-", "3-,3--", "-", "-", "6--,6---", "-", "-", "6--,6---", "-", "-"),
 	("6--,6---", "-", "-", "6--,6---", "-", "-", "4-,4--", "-", "-", "4-,4--", "-", "-", "3-,3--", "-", "-", "3-,3--", "-", "-", "6--,6---", "-", "-", "6--,6---", "-", "-"),

)
import sys
sys.path.append('C:\\work\\automatic_gita\\music\\python\\piano')

import music_translate
music_parse = music_translate.music_trans([music_table, music_table_left], beat = 82)
music_parse.music_to_play_table()
music_parse.play_music()

