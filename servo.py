from gpiozero import Servo
from time import sleep
#import os
entrance = Servo(20)

def entranceOpen():
    entrance.min()
    sleep(2)
    entrance.max()

