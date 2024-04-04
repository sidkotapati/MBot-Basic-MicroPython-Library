# mbot_robot file
from machine import Pin, PWM
import utime
from mbot_motor import Motor0, Motor1
from mbot_encoder import Encoder0, Encoder1

class Robot:
    def __init__(self):
        self.mot0 = Motor0(2, 14)
        self.mot1 = Motor1(3, 15)
        self.enc0 = Encoder0(6, 7)
        self.enc1 = Encoder1(8, 9)
        
    def delay(self, time):
        time = time * 1000
        utime.sleep_ms(int(time))
            
    def drive(self, speed, time):
        SAMPLETIME = 0.1
        TARGET = 200*speed
        KP = 0.002
        KD = 0.0001
        KI = 0.00005
        e0_prev_error = 0
        e1_prev_error = 0
        
        e0_sum_error = 0
        e1_sum_error = 0
        
        m0_speed = 0
        m1_speed = 0
        
        self.enc0.reset()
        self.enc1.reset()
        self.mot0.set(m0_speed)
        self.mot1.set(m1_speed)
        print("m0 {} m1 {}".format(m0_speed, m1_speed))
        utime.sleep_ms(500)
        print("e0 {} e1 {}".format(self.enc0.encoderCount, self.enc1.encoderCount))
        
        for _ in range(int(time*(1/SAMPLETIME))):
            e0_error = TARGET - self.enc0.encoderCount
            e1_error = TARGET - self.enc1.encoderCount
            print("err0 {} err1 {}".format(e0_error, e1_error))
            m0_speed += (e0_error * KP) + (e0_prev_error * KD) + (e0_sum_error * KI)
            m1_speed += (e1_error * KP) + (e1_prev_error * KD) + (e1_sum_error * KI)

            print("m0 {} m1 {}".format(m0_speed, m1_speed))
            
            m0_speed = max(min(1, m0_speed), -1)
            m1_speed = max(min(1, m1_speed), -1)
            
            print("m0 {} m1 {}".format(m0_speed, m1_speed))
            print("e0 {} e1 {}".format(self.enc0.encoderCount, self.enc1.encoderCount))

            self.mot0.set(m0_speed)
            self.mot1.set(m1_speed)
            
            self.enc0.reset()
            self.enc1.reset()
            
            e0_prev_error = e0_error
            e1_prev_error = e1_error
            
            e0_sum_error += e0_error
            e1_sum_error += e1_error
            
            self.delay(SAMPLETIME)
            

        self.mot0.set(0)
        self.mot1.set(0)
        print(TARGET)
        utime.sleep_ms(20)
        
    def turnleft(self):
        utime.sleep_ms(50)
        self.mot0.set(0.4)
        self.mot1.set(0.4)
        utime.sleep_ms(520)
        self.mot0.set(0)
        self.mot1.set(0)
        utime.sleep_ms(50)

    def turnright(self):
        utime.sleep_ms(50)
        self.mot0.set(-0.4)
        self.mot1.set(-0.4)
        utime.sleep_ms(520)
        self.mot0.set(0)
        self.mot1.set(0)
        utime.sleep_ms(50)
        
if __name__ == "__main__":
    r = Robot()
    r.delay(3)
    r.drive(0.6, 10)
