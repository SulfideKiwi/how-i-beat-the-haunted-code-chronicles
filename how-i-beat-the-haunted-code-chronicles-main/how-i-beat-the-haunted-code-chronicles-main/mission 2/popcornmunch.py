from botcore import *
from time import 

def munch(left, right, tm):
    motors.run(LEFT, left)
    motors.run(RIGHT, right)
    sleep(tm)

motors.enable(True)

munch(55, 50, 6)
munch(55, 30, 3)
munch(50, 65, 3)
munch(50, 50, 4)
