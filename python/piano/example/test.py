# music_table1 = \
# (
#     ("0", "0"),
# 	("1--", "1--#", "2--", "2--#","3--", "4--", "4--#","5--", "5--#","6--", "6--#","7--"),
# 	("1-", "1-#", "2-", "2-#","3-", "4-", "4-#","5-", "5-#","6-", "6-#","7-"),
# 	("1", "1#", "2", "2#","3", "4", "4#","5", "5#","6", "6#","7"),
# 	("1+", "1+#", "2+", "2+#","3+", "4+", "4+#","5+", "5+#","6+", "6+#","7+"),
# 	("1++", "1++#", "2++", "2++#","3++", "4++", "4++#","5++", "5++#","6++", "6++#","7++"),
#     ("1+++", "1+++"),
# )

# music_table2 = \
# (
#     ("0", "0"),
# 	("1--", "1--#", "2--", "2--#","3--", "4--", "4--#","5--", "5--#","6--", "6--#","7--"),
# 	("1-", "1-#", "2-", "2-#","3-", "4-", "4-#","5-", "5-#","6-", "6-#","7-"),
# 	("1", "1#", "2", "2#","3", "4", "4#","5", "5#","6", "6#","7"),
# 	("1+", "1+#", "2+", "2+#","3+", "4+", "4+#","5+", "5+#","6+", "6+#","7+"),
# 	("1++", "1++#", "2++", "2++#","3++", "4++", "4++#","5++", "5++#","6++", "6++#","7++"),
#     ("1+++", "1+++"),
# )

music_table1 = \
(
    ("0", "0"),
	("1,2,3", "1", "1", "1,2,3","1", "1", "1", "1"),
	# ("2", "1", "2", "1"),
	# ("1", "1", "1", "1"),

)

# music_table = \
# (
#     # ("1-", "2-", "3-", "4-", "5-", "6-", "7-", "1", "2", "3", "4", "5", "6", "7", "1+", "2+"),
#     # ("3+", "4+", "5+", "6+", "7+", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"),

#     ("1-", "1-", "2-", "2-", "3-", "3-", "4-", "4-", "5-", "5-", "6-", "6-", "7-", "7-", "1", "1"),
#     ("2", "2", "3", "3", "4", "4", "5", "5", "6", "6", "7", "7", "1+", "1+", "2+", "2+"),
#     ("3+", "3+", "4+", "4+", "5+", "5+", "6+", "6+", "7+", "7+", "7+", "7+", "7+", "7+", "7+", "7+"),

# )

import sys,time
sys.path.append('C:\\work\\automatic_gita\\python\\piano')

# import 一千个伤心的理由
# import 那个夏天
# import 亡靈序曲
# import 克罗地亚狂想曲
# import 卡农
# import 晴天
# import 梦中的婚礼
# import 野蜂飞舞.py

# music_table1 = \
# (
#     ("0", "0"),
# 	("6#", "6#", "6#", "6#", "6#", "6#", "6#", "6#"),
# 	("1", "1", "1", "1", "1", "1", "1", "1"),
# )

import music_translate
music_parse = music_translate.music_trans([music_table1], beat=30)
music_parse.music_to_play_table()
# music_parse.home()
music_parse.play_music()
# while 1:
# 	music_parse.servos.run_single_servo(0, 90)
# 	time.sleep(1)
# 	music_parse.servos.run_single_servo(0, 30)
# 	time.sleep(1)

# music_parse.servos.run_single_servo(32, 70)
# time.sleep(1)
# music_parse.servos.run_single_servo(32, 100)
