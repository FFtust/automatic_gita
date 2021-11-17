#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import serial
import _thread
import time
import json

PORT = "COM5"

class common_link:
    # Frame header & end
    FRAME_HEADER = 0xF3
    FRAME_END = 0xF4
    FRAME_MAX_LEN = 1024
    MAX_FRAME_NUM = 64

    # FSM state
    S_HEAD = 0
    S_HEAD_CHECK = 1
    S_LEN_1 = 2
    S_LEN_2 = 3
    S_DATA = 4
    S_DATA_CHECK = 5
    S_END = 6

    def __init__(self):
        self.state = self.S_HEAD
        self.recv_buffer = bytearray()
        self.recv_len = 0
        self.head_checksum = 0
        self.len = 0
        self.frame_list = []
        self.recv_bin_sem = _thread.allocate_lock()
        self.recv_bin_sem.acquire()

    # Input a stream data, split stream to frame and save in frame_list
    def fsm(self, stream):
        for c in stream:
            receive_frame = None

            if len(self.recv_buffer) > self.FRAME_MAX_LEN:
                self.state = self.S_HEAD

            if (self.S_HEAD == self.state):
                if (self.FRAME_HEADER == c):
                    self.recv_buffer = bytearray()
                    self.recv_buffer.append(c)
                    self.state = self.S_HEAD_CHECK

            elif (self.S_HEAD_CHECK == self.state):
                self.recv_buffer.append(c)
                self.head_checksum = c
                self.state = self.S_LEN_1

            elif (self.S_LEN_1 == self.state):
                self.recv_buffer.append(c)
                self.len = c
                self.state = self.S_LEN_2

            elif (self.S_LEN_2 == self.state):
                self.recv_buffer.append(c)
                self.len += c * 0xFF
                head_checksum = (self.recv_buffer[0] + self.recv_buffer[2] + self.recv_buffer[3]) & 0xFF
                if (head_checksum == self.head_checksum):
                    self.state = self.S_DATA
                    self.recv_len = 0
                else:
                    self.state = self.S_HEAD

            elif (self.S_DATA == self.state):
                self.recv_buffer.append(c)
                self.recv_len += 1
                if (self.len == self.recv_len):
                    self.state = self.S_DATA_CHECK

            elif (self.S_DATA_CHECK == self.state):
                self.recv_buffer.append(c)
                data_checksum = 0
                for i in self.recv_buffer[4:-1]:
                    data_checksum += i
                data_checksum = data_checksum & 0xFF
                if (data_checksum == self.recv_buffer[-1]):
                    self.state = self.S_END
                else:
                    self.state = self.S_HEAD

            elif (self.S_END == self.state):
                self.recv_buffer.append(c)
                if (self.FRAME_END == c):
                    receive_frame = self.recv_buffer[:]
                self.state = self.S_HEAD

            if receive_frame:
                return receive_frame[5:-2]

    def recv(self):
        self.recv_bin_sem.acquire()
        ret_list = []
        for l in self.frame_list:
            ret_list.append(l[1:])
        self.frame_list.clear()
        return ret_list

# communication process
class communication_level():
    def __init__(self):
        self.ser = None
        self.common_link = common_link()
        self.port = PORT
        try:
            self.ser = serial.Serial(self.port, 921600, timeout = 1)
        except:
            print('com can not open')

    def __del__(self):
        self.ser.close()

    def open(self):
        self.ser = serial.Serial(self.port, 115200, timeout = 1)

    def close(self):
        if not self.ser:
            return

        self.ser.close()

    def write(self, frame):
        if not self.ser:
            return
            
        self.ser.write(frame)

    def read(self):
        start_t = time.time()
        frame = None
        while time.time() - start_t < 10:
            data = self.ser.read(1)
            frame = self.common_link.fsm(data)
            if frame:
                break
        if frame:
            serial_num = frame[0]
            json_ret = json.loads(frame[1:])

            return json_ret

communication = communication_level()
