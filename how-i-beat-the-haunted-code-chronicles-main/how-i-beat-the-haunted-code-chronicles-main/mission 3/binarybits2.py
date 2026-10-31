from botcore import *
from time import sleep

a = 0b11101010
b = 0b01100001

answer = a | b

for i in range(8):
    leds.user_num(i, bool(answer & (1 << i)))
