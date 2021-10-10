music_table = \
(
    ("0", "0"),
    ("3+", "2+", "6+", "2+", "3+", "2+", "6", "2+"),
    ("3+", "2+", "6+", "2+", "3+", "2+", "6", "2+"),
    ("3+", "2+", "6+", "2+", "3+", "2+", "6", "2+"),
    ("3+", "2+", "6+", "2+", "3+", "2+", "6", "2+"),
    #4
    ("3+", "2+", "6+", "2+", "3+", "2+", "6", "2+"),
    ("3+", "2+", "6+", "2+", "3+", "2+", "6", "2+"),
    ("3+", "2+", "6+", "2+", "3+", "2+", "6", "2+"),
    ("NOP",),
    ("{'3+':[0&3/4]},{'6+':[0.08&3/4]},{'1++#':[0.16&3/4]},{'3++':[0.24&3/4]}", "-", "-", "-"),
    #9
    ("{'BEAT':96}",),
    ("3+", "-", "-", "-","-", "6","1+", "3+", "2+,7,5", "-","-", "-", "{'7+':[0&1/16]},{'2+':[0.05&1/16]},{'5+':[0.1&1/16]}", "-", "-", "-"),
    ("2+,7", "-", "-", "7+", "6+", "-", "-", "5+#", "6+,3+", "-", "-", "-","3++", "-", "-", "-"),
    ("6+,3+", "-", "-", "-", "3++,6+", "-", "-", "-", "2++", "-", "2++", "3++,2++", "7+", "-", "5+", "-"),
    ("6+", "-", "-", "-", "-", "-", "0", "3+"),
    #13
    ("3+,1+,6", "-", "-", "-", "-", "6", "1+", "3+", "2+,7,5", "-", "-", "-","5+,2+,7", "-", "-", "-"),
    ("2+,7", "-", "5+#,7", "-", "6+", "-", "7+", "-", "3+", "1++", "2+", "7+","1+", "6+", "7+", "4+#"),
    ("6+", "3++", "2++", "3++", "6+", "3++", "2++", "3++","6+", "3++", "2++", "3++","6+", "3++", "2++", "3++"),
    ("6+", "3++", "1++", "3++", "6+", "3++", "1++", "3++","6+", "3++", "1++", "3++","6+", "3++", "1++", "3++"),
    #17
    ("1++", "3+", "7+", "3+", "1++", "3+", "2++", "3+", "7+", "7", "6+", "7","5+", "-", "3+", "5+"),
    ("6+", "1+", "5+", "1+", "6+", "1+", "1++", "1+", "5+", "1+", "4+", "1+","3+", "-", "3+", "5+"),
    ("4+", "6", "3+", "6", "2+", "6", "4+", "6","3+", "3", "2+", "3","1+", "3", "3+", "3"),
    ("2+", "4", "1+", "4", "7", "4", "6", "4","5#,4", "-", "6,4", "-","7,3", "-", "-", "-"),
    # 21
    ("1+", "3", "7", "3", "1+", "3", "2+", "3", "7", "3", "6", "3","5", "-", "3", "5"),
    ("6", "1", "5", "1", "6", "1", "1+", "1", "5", "1", "4", "1","5", "-", "3", "5"),
    ("4", "-", "4+", "3+", "2+", "1+", "7", "-","3+", "2+", "3+", "4+","3+", "2+", "1+", "7"),
    ("6", "-", "3+", "-", "5#", "-", "3+", "-","6", "-", "-", "-","-", "-", "-", "-"),
    
    # 25
    ("{'6':[0&1/16]},{'1+':[0.08&1/16]},{'3+':[0.16&1/16]}", "-", "-", "-", "-", "6", "1+", "3+", "2+,7,5", "-", "-", "-","5+,2+,7", "-", "-", "-"),
    ("2+,7", "-", "-", "7+", "6+", "-", "-", "5+#", "6+,3+", "-", "-", "-","3++", "-", "t_ret-", "-"),
    ("6+,4+", "-", "-", "-", "3++,6+", "-", "-", "-","2++", "-", "2++", "3++,2++","7+", "-", "5+", "-"),
    ("6+", "-", "-", "-", "-", "-", "0", "3+"),

    # 29
    ("{'6':[0&1/16]},{'1+':[0.08&1/16]},{'3+':[0.16&1/16]}", "-", "-", "-", "-", "6", "1+", "3+", "2+,7,5", "-", "-", "-","5+,2+,7", "-", "-", "-"),
    ("2+,7", "-", "5+,7", "-", "6+", "-", "7+", "-", "1++", "3+", "7+", "2+","6+", "1+", "5+", "7"),
    ("6+", "3++", "2++", "3++", "6+", "3++", "2++", "3++","6+", "3++", "2++", "3++","6+", "3++", "2++", "3++"),
    ("6+", "3++", "1++#", "3++", "6+", "3++", "1++", "3++","6+", "3++", "1++", "3++","6+", "3++", "1++", "3++"),

    ("0", "0"),

)


music_table_left = \
(
    ("0", "0"),
    ("4-", "1", "4", "5", "6", "-", "0", "-"),
    ("5-", "2", "5", "6", "7", "-", "0", "-"),
    ("6-", "3", "6", "7", "1+", "-", "0", "-"),
    ("0", "0", "0", "0", "0", "0", "0", "0"),
    #4
    ("4-", "1", "4", "5", "6", "-", "0", "-"),
    ("5-", "2", "5", "6", "7", "-", "0", "-"),
    ("6-", "3", "6", "7", "1+", "-", "0", "-"),
    ("NOP",),
    ("{'6-':[0&3/4]},{'3':[0.03&3/4]},{'6':[0.06&3/4]}", "-", "-", "-"),
    #9
    ("{'BEAT':96}",),
    ("0", "1", "-", "0", "5-", "2", "5", "-"),
    ("3-", "7-", "3", "5#", "6-", "3", "6", "3"),
    ("4-", "1", "4", "1", "5-", "2", "5", "2"),
    ("6-", "3", "6", "7", "1+", "3", "6", "-"),
    #13
    ("4-", "1", "-", "0", "5-", "2", "5", "-"),
    ("3-", "7-", "3", "-", "6-", "3", "6", "-"),
    ("4-", "1", "4", "-", "5-", "2", "5", "-"),
    ("6-", "3", "6", "7", "1+#", "-", "0", "-"),
    #17
    ("6--", "3-", "6-", "7-", "1", "-", "3", "-", "3-", "-", "7-", "-", "5,3", "-", "-", "-"),
    ("4--", "1-", "4-", "5-", "6-", "-", "1", "-", "1-", "-", "5-", "-", "3,1", "-", "-", "-"),
    ("2-,2--", "-", "6-", "-", "4", "3", "2", "1", "6--,6---", "-", "3--", "-", "3-", "2-", "1-", "7--"),
    ("7--,7---", "4-", "2,7-", "4-", "2,2-", "1,1-", "7,7--", "3-,3--"),
    #21
    ("6--", "3-", "6-", "7-", "1", "7-", "6-", "3-", "3--", "-", "7--", "-", "5-", "-", "7--", "-"),
    ("4--", "1-", "4-", "5-", "6-", "5-", "4-", "1-", "1--", "-", "5--", "-", "3-", "-", "5--", "-"),
    ("2--", "6--", "2-", "3-", "4-", "3-", "2-", "6--", "6---", "3--", "6--", "7--", "1-", "2-", "3-", "-"),
    ("2-,2--", "-", "-", "-", "7--,7---", "-", "-", "6--,6---","6--,6---", "-", "3-", "-", "6-", "-", "-", "-"),
    #25
    ("4-,4--", "4-", "4,1", "4-", "5-,5--", "5-", "5,2", "5-"),
    ("3-,3--", "3-", "7-,5#", "3-", "6-,6--", "3-", "3,1", "3-"),
    ("4-,4--", "4-", "4,1", "4-", "5-,5--", "5-", "5,2", "5-"),
    ("6-,6--", "3", "6", "7", "1+,6", "3", "6", "-"),
    #29
    ("4-,4--", "4-", "4,1", "4-", "5-,5--", "5-", "5,2", "5-"),
    ("3-,3--", "3-", "7-,5-#", "3-", "6-,6--", "3-", "3,1", "3-"),
    ("4--", "1-", "6-,4-", "-", "5--", "2-", "7-,5-", "-"),
    ("6--", "3-", "6-", "7-", "1#", "-", "-", "6-"),


    ("0", "0"),

)

import sys,time
sys.path.append('C:\\work\\automatic_gita\\music\\python\\piano')

import music_translate
music_parse = music_translate.music_trans([music_table,music_table_left], beat = 82)
music_parse.music_to_play_table()
music_parse.play_music()

# music_parse.servos.run_single_servo(32, 70)
# time.sleep(1)
# music_parse.servos.run_single_servo(32, 100)
