from botcore import *
from time import sleep

while True:
    for i in range(1, 8):
        leds.user_num(i, True)
        sleep(.1)
        leds.user_num(i, False)
    for i in range(6, -1, -1):
        leds.user_num(i, True)
        sleep(.1)
        leds.user_num(i, False)
