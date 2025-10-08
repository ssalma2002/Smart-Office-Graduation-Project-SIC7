#from pir import pir
from servo import entranceOpen, entrance
from time import sleep, localtime
from smoke import isFire
from waterPump import pump
from buzzer import buzz_on, buzz_off
import facerecognition
from light import lightMain, lightAdmin
from button import mainDoor, adminDoors
from ultrasonic import is_person_nearby
import nfc
from pub import publisher
import threading

def openCamera():
    while True:
        if is_person_nearby():
            publisher.publish("office/cvOpen", "1")
        sleep(1)

def entranceDoor():
    while True:
        if facerecognition.recognized or localtime().tm_hour < 15 or nfc.mainNFC:
            entranceOpen()
            lightMain.on()
        sleep(1)

def adminDoor():
    while True:
        if nfc.adminNFC and localtime().tm_hour < 15:
            lightAdmin.on()
            sleep(1)

def fire():
    while True:
        if isFire():
            pump.forward()
            entrance.min()
            buzz_on()
            sleep(5)
            pump.stop()
            entrance.max()
            buzz_off()
        sleep(1)

def exitHandler():
    adminDoors.when_pressed = lambda: lightAdmin.off()
    mainDoor.when_pressed = lambda: lightMain.off(), lightAdmin.off()

def main():
    # Create threads for each task
    threads = [
        threading.Thread(target=openCamera, daemon=True),
        threading.Thread(target=entranceDoor, daemon=True),
        threading.Thread(target=adminDoor, daemon=True),
        threading.Thread(target=fire, daemon=True),
        threading.Thread(target=exitHandler, daemon=True),
        threading.Thread(target=nfc.nfcOn, daemon=True)
    ]

    # Start all threads
    for thread in threads:
        thread.start()

    # Keep the main thread running
    while True:
        sleep(1)

if __name__ == "__main__":
    main()
