from botcore import *
from time import sleep

def go(left, right, duration):
    motors.enable(True)
    motors.run(LEFT, left)
    motors.run(RIGHT, right)
    sleep(duration)
    motors.enable(False)

def unhex_pumpkin(pumpkin_hex):
    mat_light = ls.read(2)
    magic = mat_light & pumpkin_hex
    leds.user(magic)

go(63, 60, 3)
unhex_pumpkin(0x84)
go(60, 70, 1)
go(65, 60, 2)
go(60, 60, 3)
go(40, 60, 1)
go(60, 60, 1)

unhex_pumpkin(0x2C)
go(60, 65, 2)
go(60, 60, 4)

unhex_pumpkin(0x48)
