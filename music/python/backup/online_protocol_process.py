# -*- coding: utf-8 -*-  
from struct import pack, unpack

COMMON_PROTOCOL_HEAD = 0xF3
COMMON_PROTOCOL_END = 0xF4

ONLINE_CMD_ID = 0x04

def create_frame(exec_str, serial_num = 0):
    protocol_frame = bytearray()
    protocol_frame.append(COMMON_PROTOCOL_HEAD)
    
    # strlen + cmd + serial num
    datalen = len(exec_str) + 1 + 1 
    data_len_byte = datalen.to_bytes(2, "little")

    head_check = (data_len_byte[0] + data_len_byte[1] + COMMON_PROTOCOL_HEAD) & 0xFF

    protocol_frame.append(head_check)
    protocol_frame += data_len_byte
    #print("head", protocol_frame)

    data_sum = 0
    protocol_frame.append(ONLINE_CMD_ID)
    data_sum =+ ONLINE_CMD_ID
    protocol_frame.append(serial_num)
    data_sum += serial_num

    strbytes = bytes(exec_str, "utf8")
    #print("strbytes", strbytes)
    
    protocol_frame += strbytes
    for i in range(len(strbytes)):
        data_sum += strbytes[i]
    
    data_sum = data_sum & 0xFF
    protocol_frame.append(data_sum)   
    protocol_frame.append(COMMON_PROTOCOL_END)  
    
    print("whole frame", protocol_frame)
    
    return protocol_frame

def print_frame(frame):
    out_str = ""
    for i in range(len(frame)):
        temp = ('%2x' %frame[i])
        temp = temp.replace(" ", "0")
        out_str += temp
        out_str += " "

    print(out_str)

def parse_frame(cmd_bytes):
    data_region = cmd_bytes[5: -2]
    #print("data region", data_region)
    cmnd_str = str(data_region, "utf8")
    #print("cmnd_str", cmnd_str)
 

def test():
    import serial
    import common_link
    import json
    common = common_link.common_link()

    ser = serial.Serial("COM8", 115200, timeout = 0.5)
    #ser.write(create_frame("button.is_pressed()"))
    ser.write(create_frame("led.show_all(244,50,0)"))

    data = ser.read(32)
    #print("data is:", data)

    common.fsm(data)
    frame = common.recv()
    #print("frame is:", frame)
    temp = json.loads(frame[0])
    #print("json", temp)
    ser.close()
    return eval(temp['ret'])
