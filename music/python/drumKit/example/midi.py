key_servo_table = \
{
    36:"1--",37:"1--#",38:"2--",39:"2--#",40:'3--',41:"4--",42:"4--#",43:"5--",44:"5--#",45:"6--",46:"6--#",47:"7--",
    48:"1-",49:"1-#",50:"2-",51:"2-#",52:'3-',53:"4-",54:"4-#",55:"5-",56:"5-#",57:"6-",58:"6-#",59:"7-",
    60:"1",61:"1#",62:"2",63:"2#",64:'3',65:"4",66:"4#",67:"5",68:"5#",69:"6",70:"6#",71:"7",
    72:"1+",73:"1+#",74:"2+",75:"2+#",76:'3+',77:"4+",78:"4+#",79:"5+",80:"5+#",81:"6+",82:"6+#",83:"7+",
    84:"1++",85:"1++#",86:"2++",87:"2++#",88:'3++',89:"4++",90:"4++#",91:"5++",92:"5++#",93:"6++",94:"6++#",95:"7++",
}
import sys
sys.path.append('C:\\work\\automatic_gita\\python\\piano')

import time
import servo
import math
import random
from note import *

import sys
sys.path.append('C:\\work\\automatic_gita\\python\\piano')

import music_translate
music_parse = music_translate.music_trans([], beat = 68)

music_parse.servos_home()


file = open("script2.txt") 
while 1:
    line = file.readline()
    if not line:
        break
    tmp = line.split(' ')
    # print(tmp)
    if tmp[0] == "sleep":
        val = eval(tmp[1][:-1])
        if val < 70:
            val = 70
        time.sleep(val / 1000)
    elif tmp[0] == "noteon":
        val = eval(tmp[2])
        if val in key_servo_table:
            note = key_servo_table[val]
            print(servo_table[note] - SERVO_ID_BASE, get_angle(servo_table[note] - SERVO_ID_BASE, 1))
            music_parse.servos.run_single_servo(servo_table[note] - SERVO_ID_BASE, get_angle(servo_table[note] - SERVO_ID_BASE, 1))

    elif tmp[0] == "noteoff":
        val = eval(tmp[2][:-1])
        if val in key_servo_table:
            note = key_servo_table[val]
            music_parse.servos.run_single_servo(servo_table[note] - SERVO_ID_BASE, get_angle(servo_table[note] - SERVO_ID_BASE, 0))


      
file.close()