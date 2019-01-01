import time
import common_link

motor_num = 6

def set_pwm(id, speed):
    if speed < 0:
        speed = 256 + speed
    protocol_frame = bytearray()
    protocol_frame.append(0xff)
    protocol_frame.append(0x55)
    protocol_frame.append(0x02)
    protocol_frame.append(id)
    protocol_frame.append(speed)
    common_link.communication.write(protocol_frame)

def stop_all():
    global motor_num
    for i in range(motor_num):
        set_pwm(i, 0)