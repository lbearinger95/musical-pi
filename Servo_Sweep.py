from myservo import Servo
from machine import Pin
import time

main_pin = 11
switch_pin = Pin(main_pin,Pin.IN,Pin.PULL_UP)

servo=Servo(16)
time.sleep_ms(1000)
servo.ServoAngle(0)
servo.ServoTime(4000)

try:
    while True: 
        if switch_pin.value() == 0:
            servo.ServoAngle(100)
            time.sleep_ms(50)
        elif switch_pin.value() == 1:
            servo.ServoAngle(0)
            time.sleep_ms(50)
except:
    servo.deinit()