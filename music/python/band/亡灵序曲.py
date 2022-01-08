import sys,time
try:
    import thread as _thread
except:
    import _thread


sys.path.append("../")
sys.path.append("../../../")

import piano.music_translate2
import piano.example.亡灵序曲 as scores1
music_parse = piano.music_translate2.music_trans([scores1.music_table], beat=80)
music_parse.music_to_play_table()
# music_parse.play_music()

_thread.start_new_thread(music_parse.play_music, ())


import drumKit.music_translate
import drumKit.example.亡灵序曲D as scores2
music_parse2 = drumKit.music_translate.music_trans([scores2.music_table1, scores2.music_table2], beat=80)
music_parse2.music_to_play_table()
music_parse2.play_music()

_thread.start_new_thread(music_parse2.play_music, ())