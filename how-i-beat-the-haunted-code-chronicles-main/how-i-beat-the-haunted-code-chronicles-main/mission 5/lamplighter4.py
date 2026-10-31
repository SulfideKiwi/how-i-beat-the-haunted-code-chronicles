from botcore import *
from time import sleep, time

while True:
    tau_sec = int(time())
    lamp = (3 * tau_sec) % 5

    for i in range(5):
        leds.ls_num(i, False)
    leds.ls_num(lamp, True)
    sleep(0.05)
