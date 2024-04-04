from machine import Pin
import utime

class Encoder0:
    def __init__(self, pinA, pinB):
        self.encoderCount = 0
        self.A = Pin(pinA, Pin.IN, Pin.PULL_UP)
        self.B = Pin(pinB, Pin.IN, Pin.PULL_UP)
        self.A.irq(self.A_ISR, Pin.IRQ_RISING or Pin.IRQ_FALLING)
        self.B.irq(self.B_ISR, Pin.IRQ_RISING or Pin.IRQ_FALLING)

    def A_ISR(self, pin):
        if self.A.value():
            if self.B.value():
                self.inc()
            else:
                self.dec()
        else:
            if self.B.value():
                self.dec()
            else:
                self.inc()
    
    def B_ISR(self, pin):
        if self.B.value():
            if self.A.value():
                self.dec()
            else:
                self.inc()
        else:
            if self.A.value():
                self.inc()
            else:
                self.dec()
    
    def inc(self):
        self.encoderCount += 1
        
    def dec(self):
        self.encoderCount -= 1
        
    def reset(self):
        self.encoderCount = 0
        
        
class Encoder1:
    def __init__(self, pinA, pinB):
        self.encoderCount = 0
        self.A = Pin(pinA, Pin.IN, Pin.PULL_UP)
        self.B = Pin(pinB, Pin.IN, Pin.PULL_UP)
        self.A.irq(self.A_ISR, Pin.IRQ_RISING or Pin.IRQ_FALLING)
        self.B.irq(self.B_ISR, Pin.IRQ_RISING or Pin.IRQ_FALLING)

    def A_ISR(self, pin):
        if self.A.value():
            if self.B.value():
                self.dec()
            else:
                self.inc()
        else:
            if self.B.value():
                self.inc()
            else:
                self.dec()
    
    def B_ISR(self, pin):
        if self.B.value():
            if self.A.value():
                self.inc()
            else:
                self.dec()
        else:
            if self.A.value():
                self.dec()
            else:
                self.inc()
    
    def inc(self):
        self.encoderCount += 1
        
    def dec(self):
        self.encoderCount -= 1
        
    def reset(self):
        self.encoderCount = 0

            
if __name__ == "__main__":
    enc0 = Encoder0(6, 7)
    enc1 = Encoder1(8, 9)

    while True:
        print(f"ENC: {enc0.encoderCount} | {enc1.encoderCount}\r")
        utime.sleep_ms(100)
