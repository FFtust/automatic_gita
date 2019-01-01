import time
import common_link

def set_angle_by_port(port, slot, angle):
    protocol_frame = bytearray()
    protocol_frame.append(0xff)
    protocol_frame.append(0x55)
    protocol_frame.append(0x06)
    protocol_frame.append(0x00)
    protocol_frame.append(0x02)
    protocol_frame.append(0x0b)

    protocol_frame.append(port)
    protocol_frame.append(slot)
    protocol_frame.append(angle)
    common_link.communication.write(protocol_frame)


def set_all_angle(angle):
	for i in range(6):
		set_angle_by_port(6 + i // 2, i % 2 + 1, angle)

def set_angle(id, angle):
	set_angle_by_port(6 + id // 2, id % 2 + 1, angle)