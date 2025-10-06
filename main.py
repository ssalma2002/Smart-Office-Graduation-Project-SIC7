from pir import pir
from servo import entranceOpen, adminOpen
from time import sleep
from smoke import isFire
from waterpump import waterPump
from buzzer import buzz_on, buzz_off

async def entrance():
    if ...:
        entranceOpen()
        ...
        await sleep(0)

async def admin():
    if ...:
        adminOpen()
        ...
        await sleep(0)

async def fire():
    if isFire():
        waterPump.on()
        buzz_on()
        await sleep(0)
    else:
        waterPump.off()
        buzz_off()
        await sleep(0)

async def motion():
    if pir.motion_detected and ...:
        ...  # Add your logic here
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
