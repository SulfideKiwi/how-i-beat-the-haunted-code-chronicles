from botcore import *
from time import sleep
motors.enable(True)
motors.run(LEFT, 30)
motors.run(RIGHT, 30)

while True:
    val = ls.read(2)
    print(val)
    sleep(.2)
