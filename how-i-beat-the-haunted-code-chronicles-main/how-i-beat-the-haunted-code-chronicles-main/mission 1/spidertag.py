from botcore import *
from time import sleep

motors.enable(True)
motors.run(LEFT, -30)
motors.run(RIGHT, -30)
sleep(2)
motors.enable(False)
sleep(0.5)

motors.enable(True)
motors.run(LEFT, 60)
motors.run(RIGHT, 80)
sleep(2)
motors.enable(False)
sleep(0.5)

motors.enable(True)
motors.run(LEFT, -100)
motors.run(RIGHT, -80)
sleep(2)
motors.enable(False)
sleep(0.5)

motors.enable(True)
motors.run(LEFT, -50)
motors.run(RIGHT, -80)
sleep(2.5)
motors.enable(False)
sleep(0.5)

motors.enable(True)
motors.run(LEFT, 80)
motors.run(RIGHT, 80)
sleep(2.5)
motors.enable(False)
sleep(0.5)

motors.enable(False)
