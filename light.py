from gpiozero import LED
from time import sleep

#lightMain = OutputDevice()
#lightAdmin = OutputDevice()
lightMain = LED()
lightAdmin = LED()

def main():
    while True:
        lightMain.on()
        sleep(1)
        lightMain.off()
        sleep(1)
        lightAdmin.on()
        sleep(1)
        lightAdmin.off()
        sleep(1)

if __name__ == "__main__":
    main()
