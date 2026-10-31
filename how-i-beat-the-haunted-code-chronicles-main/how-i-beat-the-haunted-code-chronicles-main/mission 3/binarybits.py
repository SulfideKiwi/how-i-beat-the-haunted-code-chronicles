from botcore import *
from time import sleep

answer = True or True

leds.user_num(1, not answer)
leds.user_num(2, not answer)
leds.user_num(3, not answer)
leds.user_num(4, answer)

#works for 4 idk about other numbers, goodluck
