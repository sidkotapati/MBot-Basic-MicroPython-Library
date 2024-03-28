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
        TARGET = 400*speed
        KP = 0.0009
        KD = 0.00005
        KI = 0.00001
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
        self.delay(0.02)
        
        for _ in range(int(time*(1/SAMPLETIME))):
            e0_error = TARGET - self.enc0.encoderCount
            e1_error = TARGET - self.enc1.encoderCount
            print("e0 {} e1 {}".format(self.enc0.encoderCount, self.enc1.encoderCount))
            print("err0 {} err1 {}".format(e0_error, e1_error))
            m0_speed += (e0_error * KP) + (e0_prev_error * KD) + (e0_sum_error * KI)
            m1_speed += (e1_error * KP) + (e1_prev_error * KD) + (e1_sum_error * KI)

            print("m0 {} m1 {}".format(m0_speed, m1_speed))
            
            if (m0_speed > 1 or m0_speed < -1):
                print("m0 speed out of bounds")
                self.mot0.set(0)
                self.mot1.set(0)
                break
            if (m1_speed > 1 or m1_speed < -1):
                print("m1 speed out of bounds")
                self.mot0.set(0)
                self.mot1.set(0)
                break
            
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
        self.delay(0.02)
        
    def turnleft(self):
        #need to implement using control to make
        #sure you get the right number of encoder clicks
        self.enc1.reset()
        while((self.enc1.encoderCount) < 1300):
            self.mot0.set(-0.1)
            self.mot1.set(0.3)
            self.delay(0.01)
        
        self.mot1.set(0)
        self.mot0.set(0)
        self.delay(0.01)
        
    def turnright(self):
        #need to implement using control to make
        #sure you get the right number of encoder clicks
        self.enc0.reset()
        while((self.enc0.encoderCount) < 1300):
            self.mot1.set(-0.1)
            self.mot0.set(0.3)
            self.delay(0.01)
            
        self.mot1.set(0)
        self.mot0.set(0)
        self.delay(0.01)
        
        
if __name__ == "__main__":
    r = Robot()
    r.delay(3)
    r.drive(0.6, 10)
    #for i in range(10):
        #r.turnright()
        #r.turnleft()
