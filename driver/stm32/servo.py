import time
import common_link
import threading
import _thread

SERVO_NUM = 80

class servo_control():
    def __init__(self, info = None):
        start_angles = [181] * SERVO_NUM
        if info != None:
            for i in range(len(info)):
                start_angles[i] = info[i]

        self.all_servo_angles_to = start_angles.copy()
        self.all_servo_current_angles = start_angles.copy()

    def all_servos_update(self):
        changed_servo_info = []
        for i in range(SERVO_NUM):
            if self.all_servo_angles_to[i] != self.all_servo_current_angles[i]:
                changed_servo_info.append([i, self.all_servo_angles_to[i]])
        self.__send_servo_cmd(changed_servo_info)
        self.all_servo_current_angles = self.all_servo_angles_to.copy()

    def set_all_angles(self, angle):
        if angle > 181:
            angle = 181
        if angle < 0:
            angle = 0
        self.all_servo_angles_to = [angle] * SERVO_NUM

    def set_single_angle(self, index, angle):
        if index < 0 or index >= SERVO_NUM:
            return

        if angle > 181:
            angle = 181
        if angle < 0:
            angle = 0

        self.all_servo_angles_to[index] = angle

    def run(self):
        self.all_servos_update()

    def run_all_servos(self, angle):
        info = []
        for i in range(SERVO_NUM):
            info.append([i, angle])
        self.__send_servo_cmd(info)


    def run_single_servo(self, id, angle):
        self.__send_servo_cmd(([id, angle], ))

    def run_muti_angles_directly(self, info):
        self.__send_servo_cmd(info)

    def __send_servo_cmd(self, info):
        if info == []:
            return
        protocol_frame = bytearray()
        protocol_frame.append(0xff)
        protocol_frame.append(0x55)
        protocol_frame.append(len(info) * 2)

        for i in range(len(info)):
            info[i][0] &= 0xff 
            if info[i][1] > 181:
                info[i][1] = 181
            if info[i][1] < 0:
                info[i][1] = 0

            protocol_frame.append(info[i][0])
            protocol_frame.append(info[i][1])

        # print("protocol_frame", protocol_frame)
        common_link.communication.write(protocol_frame)