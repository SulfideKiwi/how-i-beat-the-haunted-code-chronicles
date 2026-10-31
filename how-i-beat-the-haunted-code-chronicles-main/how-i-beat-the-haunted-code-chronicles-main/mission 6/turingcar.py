from botcore import *
from time import sleep

code = [2, 0, 2, 4]  
m = [1, 9, 1, 2]    
b = [1, 9, 5, 4]      

def encrypt(x, m, b):
    return m * x + b 

for i in range(len(code)):
    y = encrypt(code[i], m[i], b[i])
    leds.ls(y)
    sleep(3)
