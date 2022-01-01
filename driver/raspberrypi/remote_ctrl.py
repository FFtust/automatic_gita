import socket
import time
import thread
from servo import servoCtl

HOST = ''
PORT = 5050
ADDR = (HOST,PORT)


class remote_ctl():
    def __init__(self):
        self.start_listening()

    def start_listening(self):
        self.my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.my_socket.bind(ADDR)
        self.my_socket.listen(20)

        while True:
            res = self.my_socket.accept()
            print("accept:", res)
            # (socet, (remote ip, port))

            new_connection(res, self.process)


    def process(self, data):
        try:
            exec(data)
        except:
            print("exec error", data)


class new_connection():
    def __init__(self, skt, process = None):
        self.socket = skt[0]
        self.remote_ip = skt[1][0]
        self.port = skt[1][1]

        self.process = process

        thread.start_new_thread(self.work, ())

    def register_process(self, process):
        self.process = process

    def work(self):
        while True:
            ret_data = self.socket.makefile().readline()
            print("client read data:", ret_data)
            # EOF check
            if ret_data == "":
                print("socket close or other error happend")
                self.socket.close()
                break
            if self.process:
                self.process(ret_data)

remote_ctl()