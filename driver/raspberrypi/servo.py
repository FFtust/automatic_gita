import time
try:
    import thread as _thread
except:
    import _thread

REMOTE_CTL = False

if not REMOTE_CTL:
    import Adafruit_PCA9685

FREE_ANGLE=181
SERVO_NUM = 80
# ADRESS_TABLE = [0x40,0x41,0x42,0x44,0x00,0x00,0x00,0x00]
ADRESS_TABLE = [0x42,0x44,0x41,0x40,0x47,0x00,0x00,0x00]

SPEED_CTL_ANGLE_INTERVAL = 2
SPEED_CTL_T_INTERVAL = 500

class servo_c():
    def __init__(self, num = SERVO_NUM, address = ADRESS_TABLE):
        self.servo_num = SERVO_NUM
        self.driver_address = address

        self.current_angles = [255] * self.servo_num 
        self.angles_to = [90] * self.servo_num 
        self.servo_speeds = [0] * self.servo_num 
        self.servo_speeds_t_record = [[0, 0]] * self.servo_num 


        self.pwm = [None] * (self.servo_num // 16)

        for i in range(len(self.pwm)):
            self.pwm[i] = Adafruit_PCA9685.PCA9685(self.driver_address[i], busnum=1)
            self.pwm[i].set_pwm_freq(50)
            
    def start_update_task(self):
        _thread.start_new_thread(self.update_task, ())

    def _run_to(self, idx, angle):
        driver_id = idx // 16
        servo_id = idx % 16
        print(driver_id, servo_id, angle)

        date = 4096 * ((angle * 11) + 500) / 20000
        self.pwm[driver_id].set_pwm(servo_id, 0, int(date))

        self.current_angles[idx] = angle

####################################################
    def free(self, idx):
        driver_id = idx // 16
        servo_id = idx % 16
        self.pwm[driver_id].set_pwm(servo_id, 0, 0)

    def set_angle(self, idx, angle, speed = 0, update = False):
        if idx >=  self.servo_num:
            print("invalid servo id")
            return
        
        self.angles_to[idx] = angle
        self.servo_speeds[idx] = speed

        if update:
            self.update()
    def _cal_delta_angle(self, to, current, speed):
        diff = to - current
        if speed == 0 or abs(diff) > 10:
            return diff, abs(diff) * 1500
        else:
            return (SPEED_CTL_ANGLE_INTERVAL if diff > 0 else (-SPEED_CTL_ANGLE_INTERVAL)), SPEED_CTL_ANGLE_INTERVAL * 1500 + speed * 500


    def update(self):
        for i in range(self.servo_num):
            if self.angles_to[i] == FREE_ANGLE:
                self.free(i)
                continue

            if abs(self.angles_to[i] - self.current_angles[i]) > SPEED_CTL_ANGLE_INTERVAL:
                if time.time() * 1000000 - self.servo_speeds_t_record[i][0] >= self.servo_speeds_t_record[i][1]:
                    delta, run_t = self._cal_delta_angle(self.angles_to[i], self.current_angles[i], self.servo_speeds[i])
                    self._run_to(i, self.current_angles[i] + delta)
                    self.servo_speeds_t_record[i][0] = time.time() * 1000000
                    self.servo_speeds_t_record[i][1] = run_t
            else:
                self.servo_speeds_t_record[i][1] = 0

    def update_task(self):
        while 1:
            self.update()
            
####################################################
    def test(self):

        while 1:
            self.set_angle(0, 60, 0)
            time.sleep(1)
            self.set_angle(0, 110, 10)
            time.sleep(1)
            self.set_angle(0, 60, 0)
            time.sleep(1)
            self.set_angle(0, 110, 0)
            time.sleep(1)


from socket import *

HOST = '192.168.1.103' # or 'localhost'
PORT = 5050
ADDR = (HOST,PORT)
 
class servo_rmt_c():
    def __init__(self, num = SERVO_NUM, address = ADRESS_TABLE):
        self.tcpCliSock = socket(AF_INET,SOCK_STREAM)
        self.tcpCliSock.connect(ADDR)

    def _run_to(self, idx, angle):
        ctlStr = "servoCtl.set_angle({}, {}, {}, {})\n".format(idx, angle, speed, True)
        self.tcpCliSock.send(bytes(ctlStr, "utf8"))

####################################################
    def set_angle(self, idx, angle, speed = 0, update = False):
        ctlStr = "servoCtl.set_angle({}, {}, {}, {})\n".format(idx, angle, speed, update)
        self.tcpCliSock.send(bytes(ctlStr, "utf8"))

    def update(self):
        ctlStr = "servoCtl.update()\n"
        self.tcpCliSock.send(bytes(ctlStr, "utf8"))

if REMOTE_CTL:
    servoCtl = servo_rmt_c()
else:
    servoCtl = servo_c()