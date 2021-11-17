 # C： 135 
 # Dm： 2#46
 # Em：357 
 # F： 461 
 # G：572 
 # B：7#2#4

music_table = \
(
  ("5,7,5", "-", "5,7,5", "-", "3,5,7", "-", "3,5,7", "-"),
)


import sys
sys.path.append('C:\\work\\automatic_gita\\python\\piano')

import music_translate
music_parse = music_translate.music_trans([music_table], beat = 60)
music_parse.music_to_play_table()

# music_parse.play_music()

