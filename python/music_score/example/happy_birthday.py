import time
from chord import *


# while True:
#     chord1.set_grade(0, True)
#     time.sleep(0.2)
#     chord1.pizz(True)
#     time.sleep(2)

#     chord1.set_grade(1, True)
#     time.sleep(0.2)
#     chord1.pizz(True)
#     # servos.run_single_servo(0, 0)
#     time.sleep(1)

#     chord1.set_grade(2, True)
#     time.sleep(0.2)
#     chord1.pizz(True)
#     # servos.run_single_servo(0, 0)
#     time.sleep(1)

#     # chord2.set_grade(0)
#     # chord2.set_grade(3, True)
#     # time.sleep(0.2)
#     # chord2.pizz(True)
#     # # servos.run_single_servo(0, 0)
#     # time.sleep(1)

tick = 0.7
grade_interval = 0.1

def main():
    chord1.set_grade(0)
    chord2.set_grade(0)
    chord3.set_grade(0)
    chord4.set_grade(0)
    chord5.set_grade(0)
    chord6.set_grade(0, True)
    time.sleep(1)

    chord3.pizz(True)    # 5
    time.sleep(tick / 2)
    chord3.pizz(True)    # 5
    time.sleep(tick * 0.68- grade_interval)
    chord3.set_grade(2, True)
    time.sleep(grade_interval)

    chord3.pizz(True)    # 6
    time.sleep(tick - grade_interval)
    chord3.set_grade(0, True)
    time.sleep(grade_interval)

    chord3.pizz(True)   # 5
    time.sleep(tick - grade_interval)
    chord2.set_grade(1, True)
    time.sleep(grade_interval)

    chord2.pizz(True)   # 1_u
    time.sleep(tick - grade_interval) 
    chord2.set_grade(0, True)
    time.sleep(grade_interval)

    chord2.pizz(True)   # 7
#######################################
    chord1.set_grade(0)
    chord2.set_grade(0)
    chord3.set_grade(0)
    chord4.set_grade(0)
    chord5.set_grade(0)
    chord6.set_grade(0, True)
    time.sleep(1)

    chord3.pizz(True)    # 5
    time.sleep(tick / 2)
    chord3.pizz(True)    # 5
    time.sleep(tick * 0.68 - grade_interval)
    chord3.set_grade(2, True)
    time.sleep(grade_interval)

    chord3.pizz(True)    # 6
    time.sleep(tick - grade_interval)
    chord3.set_grade(0, True)
    time.sleep(grade_interval)

    chord3.pizz(True)   # 5
    time.sleep(tick - grade_interval)
    chord2.set_grade(3, True)
    time.sleep(grade_interval)

    chord2.pizz(True)   # 2_u
    time.sleep(tick - grade_interval) 
    chord2.set_grade(0)
    chord2.set_grade(1, True)
    time.sleep(grade_interval)

    chord2.pizz(True)   # 1_u
#######################################
    chord1.set_grade(0)
    chord2.set_grade(0)
    chord3.set_grade(0)
    chord4.set_grade(0)
    chord5.set_grade(0)
    chord6.set_grade(0, True)
    time.sleep(1)

    chord3.pizz(True)    # 5
    time.sleep(tick / 2)
    chord3.pizz(True)    # 5
    time.sleep(tick * 0.68 - grade_interval)
    chord1.set_grade(3, True)
    time.sleep(grade_interval)

    chord1.pizz(True)    # 5_
    time.sleep(tick - grade_interval)
    chord1.set_grade(0, True)
    time.sleep(grade_interval)

    chord1.pizz(True)   # 3_
    time.sleep(tick - grade_interval)
    chord2.set_grade(1, True)
    time.sleep(grade_interval)

    chord2.pizz(True)   # 1_u
    time.sleep(tick - grade_interval) 
    chord2.set_grade(0, True)
    time.sleep(grade_interval)

    chord2.pizz(True)   # 7

while True:
    main()
    time.sleep(2)