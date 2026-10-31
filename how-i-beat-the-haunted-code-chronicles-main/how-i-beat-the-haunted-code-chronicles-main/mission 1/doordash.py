from botcore import *
from time import sleep

motors.enable(True)
motors.run(LEFT, 100)
motors.run(RIGHT, 100)
sleep(4)

motors.enable(False)
