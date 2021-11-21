import Adafruit_PCA9685
import time
import thread as _thread

SERVO_NUM = 16
ADRESS_TABLE = [0x40,0x41,0x42,0x44,0x00,0x00,0x00,0x00]
SPEED_CTL_ANGLE_INTERVAL = 1
SPEED_CTL_T_INTERVAL = 1

class servo_c():
    def __init__(self, num = SERVO_NUM, address = ADRESS_TABLE):
        self.servo_num = SERVO_NUM
        self.driver_address = address

        self.current_angles = [255] * self.servo_num 
        self.angles_to = [90] * self.servo_num 
        self.servo_speeds = [0] * self.servo_num 
        self.servo_speeds_t_record = [0] * self.servo_num 


        self.pwm = [None] * (self.servo_num // 16)

        for i in range(len(self.pwm)):
            self.pwm[i] = Adafruit_PCA9685.PCA9685(self.driver_address[i], busnum=1)
            self.pwm[i].set_pwm_freq(50)
            
        _thread.start_new_thread(self.update_task, ())
        time.sleep(2)

    def _run_to(self, idx, angle):
        driver_id = idx // 16
        servo_id = idx % 16
        print(driver_id, servo_id, angle)

        date = 4096 * ((angle * 11) + 500) / 20000
        self.pwm[driver_id].set_pwm(servo_id, 0, int(date))

        self.current_angles[idx] = angle

####################################################
    def set_angle(self, idx, angle, speed = 0):
        if idx >=  self.servo_num:
            print("invalid servo id")
            return
        
        self.angles_to[idx] = angle
        self.servo_speeds[idx] = speed

    def update(self):
        for i in range(self.servo_num):
            if abs(self.angles_to[i] - self.current_angles[i]) > SPEED_CTL_ANGLE_INTERVAL:
                if time.time() * 1000 - self.servo_speeds_t_record[i] > self.servo_speeds[i] * SPEED_CTL_T_INTERVAL:
                    if self.servo_speeds[i] == 0:
                        self._run_to(i, self.angles_to[i])
                    else:
                        if self.angles_to[i] >= self.current_angles[i]:
                            self._run_to(i, self.current_angles[i] + SPEED_CTL_ANGLE_INTERVAL)
                        else:
                            self._run_to(i, self.current_angles[i] - SPEED_CTL_ANGLE_INTERVAL)
                    self.servo_speeds_t_record[i] = time.time() * 1000
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