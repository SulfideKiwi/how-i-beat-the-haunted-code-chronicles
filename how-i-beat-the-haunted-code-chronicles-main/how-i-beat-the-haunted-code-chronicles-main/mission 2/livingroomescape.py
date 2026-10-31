from botcore import *
from time import sleep

while True:
    light_reading = prox.detect()
    print(light_reading)

    if light_reading == (False, False):
        leds.ls_num(2, True)
        leds.user_num(3, False)
        motors.enable(True)
        motors.run(LEFT, 100)
        motors.run(RIGHT, 100)
        
    elif light_reading == (True, True):
        leds.ls_num(2, False)
        leds.user_num(3, True)
        motors.enable(False)
            
