from machine import Pin,PWM

class Servo(object):
    def __init__(self, pin: int=15, hz: int=50):
        self._servo = PWM(Pin(pin))
        self._servo.freq(hz)
    
    #duty = 1638 = 0.5ms = 65535/2/(T)(1/50)/2*1000
    def ServoDuty(self, duty): 
        if duty <= 3276:              
            duty = 3276
        if duty >= 6553:
            duty = 6553
        self._servo.duty_u16(duty)
        
    def ServoAngle(self, pos): 
        if pos <= 0:
            pos = 0
        if pos >= 180:
            pos = 180
        pos_buffer = (pos/180) * 6552
        self._servo.duty_u16(int(pos_buffer) + 1638)

    def ServoTime(self, us):
        if us <= 1000:
            us = 1000
        if us >= 4000:
            us = 4000
        pos_buffer= (us / 1000) * 3276
        self._servo.duty_u16(int(pos_buffer))
        
    def deinit(self):
        self._servo.deinit()
