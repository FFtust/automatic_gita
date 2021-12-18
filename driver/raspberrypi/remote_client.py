from socket import *

HOST = '127.0.0.1' # or 'localhost'
PORT = 5050
ADDR = (HOST,PORT)
 
tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)


def set_angle(idx, angle, speed = 0, update = False):
    ctlStr = "servoCtl.set_angle({}, {}, {}, {})\n".format(idx, angle, speed, update)
    tcpCliSock.send(bytes(ctlStr, "utf8"))


