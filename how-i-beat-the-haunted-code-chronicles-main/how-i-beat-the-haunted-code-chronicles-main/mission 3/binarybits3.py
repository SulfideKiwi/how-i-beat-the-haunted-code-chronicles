from botcore import *
from time import sleep

a = 0x98
b = 0xC6

answer = a | b

for i in range(8):
    leds.user_num(i, bool(answer & (1 << i)))
