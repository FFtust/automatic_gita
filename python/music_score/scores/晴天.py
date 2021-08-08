music_table = \
(
    ("6,1+,3+,{'6-':1/8}", "-", "-", "-", "6,1+,3+,{'6-':1/8}", "-", "-", "-"),
    ("4,6,1+,{'4-':1/8}", "-", "-", "-","4,6,1+,{'4-':1/8}",  "-", "-", "-"),
    ("1-,3-,5-,{'1--':1/8}",  "-", "-", "-","1-,3-,5-,{'1--':1/8}",  "-", "-", "-"),
    ("5,7,2,{'5-':1/8}",  "-", "-", "-","5,7,2,{'5-':1/8}",  "-", "-", "-"),
)


import sys
sys.path.append('C:\\work\\automatic_gita\\python\\music_score')

import music_translate
music_parse = music_translate.music_trans([music_table])
music_parse.set_beat(4)
music_parse.music_to_play_table()
music_parse.servos_home()
music_parse.play_music()

