from machine import Pin, PWM
import utime

class Motor0:
    def __init__(self, pwm_pin, dir_pin):
        self.dir = Pin(dir_pin, Pin.OUT)
        self.pwm = PWM(Pin(pwm_pin))
        self.pwm.freq(10000)
        self.pwm.duty_u16(0)
        
    def set(self, duty):
        duty *= -1;
        if((duty >= 0.0) and (duty <= 1.0)):
            self.dir.on()
            self.pwm.duty_u16(int(duty * 65535))
        elif((duty < 0.0) and (duty >= -1.0)):
            self.dir.off()
            self.pwm.duty_u16(int(-duty * 65535))
        else:
            print("ERROR: duty out of range")
            
            
class Motor1:
    def __init__(self, pwm_pin, dir_pin):
        self.dir = Pin(dir_pin, Pin.OUT)
        self.pwm = PWM(Pin(pwm_pin))
        self.pwm.freq(10000)
        self.pwm.duty_u16(0)
        
    def set(self, duty):
        if((duty >= 0.0) and (duty <= 1.0)):
            self.dir.on()
            self.pwm.duty_u16(int(duty * 65535))
        elif((duty < 0.0) and (duty >= -1.0)):
            self.dir.off()
            self.pwm.duty_u16(int(-duty * 65535))
        else:
            print("ERROR: duty out of range")
            
            
def delay(time):
    time *= 1000
    utime.sleep_ms(int(time))
            
def drive(speed, time):
    utime.sleep_ms(50)
    mot0 = Motor0(2, 14)
    mot1 = Motor0(3, 15)
    mot0.set(speed)
    mot1.set(speed)
    utime.sleep_ms(time*1000)
    mot0.set(0)
    mot1.set(0)
    utime.sleep_ms(50)
    
def turnleft():
    utime.sleep_ms(50)
    mot0 = Motor(2, 14)
    mot1 = Motor(3, 15)
    mot0.set(0.4)
    mot1.set(0.4)
    utime.sleep_ms(520)
    mot0.set(0)
    mot1.set(0)
    utime.sleep_ms(50)

def turnright():
    utime.sleep_ms(50)
    mot0 = Motor(2, 14)
    mot1 = Motor(3, 15)
    mot0.set(-0.4)
    mot1.set(-0.4)
    utime.sleep_ms(520)
    mot0.set(0)
    mot1.set(0)
    utime.sleep_ms(50)

if __name__ == "__main__":
    delay(2)
    drive(0.4, 6)
    
    