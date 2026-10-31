from botcore import *
from time import sleep

motors.enable(True)

while True:
    x, y, z = accel.read()
    if x < 0:
        motors.run(LEFT, 20)
        motors.run(RIGHT, 30)
    elif x > 0:
        motors.run(LEFT, 30)
        motors.run(RIGHT, 20)
    else:    
        motors.run(LEFT, 30)
        motors.run(RIGHT, 30)
