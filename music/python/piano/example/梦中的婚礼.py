music_table = \
(
    ("{'6-':1/8}", "-", "{'1':1/8}", "-",  "{'3':1/8}", "-", "{'1':1/8}", "-",  "{'3':1/8}", "-", "{'1':1/8}", "-", "{'3':1/8}", "-", "{'1':1/8}", "6+"),

    ("6+,{'6-':1/8}", "7+", "7+,{'1':1/8}", "1++", "1++,{'3':1/8}", "7+", "7+,{'1':1/8}", "6+", "6+,{'3':1/8}", "3+", "3+,{'1':1/8}", "1+", "1+,{'3':1/8}", "6", "6,{'1':1/8}", "5+"),
    
    ("5+,{'6-':1/8}", "4+", "4+,{'2':1/8}", "3+", "4+,{'4':1/8}", "5+", "{'4+':3/8},{'2':1/8}", "-", "{'4':1/8}", "-", "{'2':1/8}", "-"),

    ("{'2-':1/8}", "4+", "4+,{'5-':1/8}", "5+", "5+,{'7-':1/8}", "6+", "6+,{'5-':1/8}", "7+", "7+,{'7-':1/8}", "5+", "5+,{'5-':1/8}", "2+", "2+,{'7-':1/8}", "4+"),

    ("{'5-':1/8},4+", "3+", "3+,{'1':1/8}", "2+", "2+,{'3':1/8}", "4+", "{'3+':3/8},{'1':3/8}", "-", "-", "-", "-"),

# ##############################################
    ("{'3+':1/8},{'3-':1/8}", "-", "6,{'6-':1/8}", "1+", "3+,{'1':1/8}", "2+", "{'3+':1/8},{'3-':1/8}", "-", "6,{'6-':1/8}", "1+", "3+,{'1':1/8}", "2+", "{'3+':1/8},{'3-':1/8}", "-", "6,{'6-':1/8}", "1+", "4+,{'1':1/8}", "3+", "{'4+':1/8},{'2-':1/8}", "-", "6,{'6-':1/8}", "1+", "4+,{'2':1/8}", "3+"),

    ("{'4+':1/8},{'6-':1/8}", "-", "4+", "3+", "5+", "4+", "{'5+':1/8},{'5-':1/8}", "-", "5+", "6+", "5+", "6+", "{'3+':3/8},{'1-':1/8}", "-", "{'5-':1/8}", "-", "{'1':1/8}", "-"),

    ("{'3+':1/8},{'3-':1/8}", "-", "6,{'6-':1/8}", "1+", "3+,{'1':1/8}", "2+", "{'3-':1/8},{'3+':1/8}", "-", "6,{'6-':1/8}", "1+", "3+,{'1':1/8}", "2+", "{'3-':1/8},{'3+':1/8}", "-", "6,{'6-':1/8}", "1+", "4+,{'1':1/8}", "3+", "{'2-':1/8},{'4+':1/8}", "-", "6,{'6-':1/8}", "1+", "4+,{'2':1/8}", "3+"),

    ("{'4-':1/8},{'4+':1/8}", "-", "4+,{'6-':1/8}", "3+", "5+,{'1':1/8}", "4+", "{'5-':1/8},{'5+':1/8}", "-", "5+,{'7-':1/8}", "6+", "5+,{'2':1/8}", "6+", "{'3+':3/8},{'1-':1/8}", "-", "{'5-':1/8}", "-", "{'1':1/8}", "-"),

# ##############################################
    ("{'1++':3/16},{'6-':1/8}", "-", "{'1':1/8}", "3+", "3+,{'3':1/8}", "4+", "{'4+':3/16},{'6-':1/8}", "-", "{'2':1/8}", "2+", "2+,{'4':1/8}", "7+", "{'7+':3/16},{'5-':1/8}", "-", "{'7-':1/8}", "2+", "2+,{'2':1/8}", "3+", "{'3+':1/8},{'5-':1/8}", "-", "{'1':1/8},1+", "1+", "6+,{'3':1/8}", "5+"),
    
    ("{'6+':3/16},{'3-':1/8}", "-", "{'6-':1/8}", "1+", "1+,{'1':1/8}", "2+", "{'2+':3/16},{'4-':1/8}", "-", "{'7-':1/8}", "7", "3+,{'2':1/8}", "2+", "{'3+':3/8},{'3-':1/8}", "-", "{'4-':1/8}", "-", "{'5-':1/8}", "-"),
# ##############################################
    ("{'1++':3/16},{'3-':1/8}", "-", "{'6-':1/8}", "1++", "1++,{'1':1/8}", "2++", "{'2++':3/16},{'2-':1/8}", "-", "{'6-':1/8}", "1++", "7+,{'1':1/8}", "6+", "{'5+':3/16},{'2-':1/8}", "-", "{'5-':1/8}", "5+", "6+,{'7-':1/8}", "5+", "{'3+':3/16},{'3-':1/8}", "-", "{'6-':1/8}", "-", "{'1':1/8}", "-"),
   
    ("{'1++':1/8},{'3-':1/8}", "-", "1++,{'6-':1/8}", "1++", "1++,{'1':1/8}", "2++", "{'2++':3/16},{'2-':1/8}", "-", "{'6-':1/8}", "1++", "7+,{'1':1/8}", "6+", "{'5+':3/8},{'2-':1/8}", "-", "{'5-':1/8}", "5+", "6+,{'7-':1/8}", "5+", "{'6+':3/16},{'3-':1/8}", "-", "{'6-':1/8}", "-", "{'1':1/8}", "-"),

)


import sys
sys.path.append('../')

import music_translate2 as music_translate
music_parse = music_translate.music_trans([music_table], beat = 68)
music_parse.music_to_play_table()
music_parse.play_music()
