from botcore import *
from time import sleep

leds.user_num(0, True)
leds.user_num(4, True)
leds.user_num(7, True)

motors.enable(True)
motors.run(LEFT, 40)
motors.run(RIGHT, 40)
sleep(1.5)

motors.run(LEFT, -20)
motors.run(RIGHT, -20)
sleep(2.0)

motors.run(LEFT, 30)
motors.run(RIGHT, -30)
sleep(2.5)

motors.enable(False)
