import time
from chord import *
time.sleep(1)

from note import note
from chord import *

time.sleep(2)
tick = 1
# while True:
#     # pass
#     # a = input("angle:")
#     # servos.run_single_servo(18, int(a))

#     note.play_note("6")
#     time.sleep(tick / 2)
#     note.play_note("7")
#     time.sleep(tick / 2)

#     Am.run()
#     time.sleep(tick / 2)
#     chord2.pizz(False)
#     # chord5.pizz(True)
#     time.sleep(tick / 2)
#     chord4.pizz(True)
#     time.sleep(tick / 2)
#     chord3.pizz(True)
#     time.sleep(tick / 2)
#     chord2.pizz(True)
#     time.sleep(tick / 2)
#     chord2.pizz(True)
#     time.sleep(tick / 2)
#     chord4.pizz(True)
#     time.sleep(tick / 2)
#     chord1.pizz(True)
#     time.sleep(tick / 2)

#     Em.run()
#     time.sleep(tick / 2)
#     chord2.pizz(True)
#     # chord5.pizz(True)
#     time.sleep(tick * 3)

while True:
    note.play_note("5", 1 / 8)

    note.play_note("1_u", 1 / 2)
    note.play_note("2_u", 1 / 3)    
    note.play_note("3_u", 1 / 6)

    note.play_note("5_u", 1 / 6)
    note.play_note("3_u", 1 / 6)    
    note.play_note("3_u", 1 / 2)   
    note.play_note("5", 1 / 6)   

    note.play_note("1_u", 1 / 2)
    note.play_note("2_u", 1 / 6)
    note.play_note("1_u", 1 / 6)    
    note.play_note("6", 1 / 6)  

    note.play_note("5", 5 / 6)
    note.play_note("5", 1 / 6)    
   
    note.play_note("1_u", 1 / 2)
    note.play_note("2_u", 1 / 3)    
    note.play_note("3_u", 1 / 6)

    note.play_note("6_u", 1 / 6)  
    note.play_note("3_u", 1 / 6)
    note.play_note("5_u", 1 / 3)  
    note.play_note("3_u", 1 / 6)
    note.play_note("2_u", 1 / 6)  

    note.play_note("1_u", 1 / 3)  
    note.play_note("1_u", 1 / 6)
    note.play_note("2_u", 1 / 3)  
    note.play_note("5_u", 1 / 6)
    
    note.play_note("2_u", 5 / 6)  
    note.play_note("3_u", 1 / 6)  

    note.play_note("5_u", 1 / 2)
    note.play_note("5_u", 1 / 6)  
    note.play_note("3_u", 5 / 6)
    note.play_note("5_u", 1 / 6)  

    note.play_note("6_u", 1 / 6)
    note.play_note("1_u", 1 / 6)  
    note.play_note("6_u", 1 / 6)
    note.play_note("6_u", 1 / 3)  
    note.play_note("3_u", 1 / 6)  

    note.play_note("2_u", 1 / 3)
    note.play_note("1_u", 1 / 6)  
    note.play_note("2_u", 1 / 3)
    note.play_note("3_u", 1 / 6)  

    note.play_note("3_u", 5 / 6)
    note.play_note("3_u", 1 / 6)

    note.play_note("5_u", 2 / 3)  
    note.play_note("3_u", 1 / 6)
    note.play_note("3_u", 1 / 6)  

    note.play_note("2_u", 1 / 6)
    note.play_note("1_u", 1 / 6)  
    note.play_note("6", 1 / 2)
    note.play_note("1_u", 1 / 6)

    note.play_note("2_u", 1 / 3)  
    note.play_note("1_u", 1 / 6)
    note.play_note("3_u", 1 / 3)  
    note.play_note("2_u", 1 / 6)

    note.play_note("1_u", 1)  
    time.sleep(5)



