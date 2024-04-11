import time
from breakout_pmw3901 import BreakoutPMW3901 as FlowSensor


class PID:
    
    integral = 0
    error_old = 0
    error = 0
    
    def __init__(self, kp, ki, kd, target):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        
        self.target = target
        
    def set_target(self, target):
        self.target = target
    
    def control(self, current):
        self.error_old = self.error
        
        self.error = self.target - current
        self.integral += self.error*dt
        differential = (self.error - self.error_old) / dt
        
        output = self.kp*self.error + self.ki*self.integral + self.kd*differential
        
        return output


class flowsensor:
    
    flo = Flowsensor()
    flo.set_rotation(FlowSensor.DEGREES_0)
    
    straight = PID(0.1, 0, 0, 0)
    speed = PID(0.1, 0, 0, 0)
    
    def get_xy(self):
        # returns a vector (x, y) of the flowsensor
        return self.flo.get_motion()
    
    def print_xy(self):
        delta = self.flo.get_motion()
        print("Relative: x {}, y {}".format(delta[0], delta[1]))
    
    def straight_control(self):
        return self.straight.control(self.get_xy()[0])
    
    def set_speed(self, speed):
        self.speed.set_target(speed)
    
    def speed_control(self):
        return self.speed.control(self.get_xy()[1])


def stop(self, prev_speed):
    change = prev_speed / 5
    for _ in range(5):
        self.mot0.set(prev_speed)
        self.mot1.set(prev_speed)
        prev_speed -= change
        self.delay(0.1)
    
