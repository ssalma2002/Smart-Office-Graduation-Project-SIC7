from pir import pir
from servo import *
from time import sleep, localtime
from smoke import isFire
from waterPump import waterPump
from buzzer import buzz_on, buzz_off
from facerecognition import recognized
from light import lightMain, lightAdmin
from button import mainDoor, adminDoor
from ultrasonic import is_person_nearby
from nfc import mainNFC, adminNFC, nfcOn
from pub import publisher
import threading

def openCamera():
    while True:
        if is_person_nearby():
            publisher.publish("office/cvOpen", "1")
        sleep(1)

def entranceDoor():
    while True:
        if recognized and localtime().tm_hour < 15 and mainNFC:
            entranceOpen()
            lightMain.on()
        sleep(1)

def adminDoor():
    while True:
        if adminNFC and localtime().tm_hour < 15:
            adminOpen()
            lightAdmin.on()
        sleep(1)

def fire():
    while True:
        if isFire():
            waterPump.on()
            entrance.min()
            admin.min()
            buzz_on()
        else:
            waterPump.off()
            entrance.max()
            admin.max()
            buzz_off()
        sleep(1)

def motion():
    while True:
        if pir.motion_detected and localtime().tm_hour >= 15:
            entrance.max()
            admin.max()
            buzz_on()
        sleep(1)

def closeLights():
    while True:
        if mainDoor.is_pressed:
            lightMain.off()
            lightAdmin.off()
        if adminDoor.is_pressed:
            lightAdmin.off()
        sleep(1)

def main():
    # Create threads for each task
    threads = [
        threading.Thread(target=nfcOn, daemon=True),
        threading.Thread(target=openCamera, daemon=True),
        threading.Thread(target=entranceDoor, daemon=True),
        threading.Thread(target=adminDoor, daemon=True),
        threading.Thread(target=fire, daemon=True),
        threading.Thread(target=motion, daemon=True),
        threading.Thread(target=closeLights, daemon=True)
    ]
    
    # Start all threads
    for thread in threads:
        thread.start()
    
    # Keep the main thread running
    while True:
        sleep(1)

if __name__ == "__main__":
    main()