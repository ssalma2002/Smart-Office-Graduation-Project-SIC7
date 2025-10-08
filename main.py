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
from nfc import mainNFC, adminNFC

async def openCamera():
    if is_person_nearby():
        ...
        await sleep(0)
    else:
        await sleep(0)

async def entrance():
    if recognized and localtime().tm_hour < 15 and mainNFC:
        entranceOpen()
        lightMain.on()
        await sleep(0)

async def admin():
    if adminNFC and localtime().tm_hour < 15:
        adminOpen()
        lightAdmin.on()
        await sleep(0)

async def fire():
    if isFire():
        waterPump.on()
        entrance.min()
        admin.min()
        buzz_on()
        await sleep(0)
    else:
        waterPump.off()
        entrance.max()
        admin.max()
        buzz_off()
        await sleep(0)

async def motion():
    if pir.motion_detected and localtime().tm_hour >= 15:
        entrance.max()
        admin.max()
        buzz_on()
        await sleep(0)

async def closeLights():
    if mainDoor.is_pressed:
        lightMain.off()
        lightAdmin.off()
        await sleep(0)
    if adminDoor.is_pressed:
        lightAdmin.off()
        await sleep(0)

async def main():
    while True:
        await entrance()
        await admin()
        await fire()
        await motion()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
