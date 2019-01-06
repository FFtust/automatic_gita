import time
import common_link

def send_servo_cmd(info):
    protocol_frame = bytearray()
    protocol_frame.append(0xff)
    protocol_frame.append(0x55)
    protocol_frame.append(len(info) * 2)

    for i in range(len(info)):
        info[i][0] &= 0xff 
        if info[i][1] > 180:
            info[i][1] = 180
        if info[i][1] < 0:
            info[i][1] = 0

        protocol_frame.append(info[i][0])
        protocol_frame.append(info[i][1])

    common_link.communication.write(protocol_frame)


def set_all_angle(angle):
    info = []
    for i in range(16):
        info.append([i, angle])
    send_servo_cmd(info)


def set_angle(id, angle):
    send_servo_cmd(([id, angle], ))

def set_muti_angles(info):
    send_servo_cmd(info)