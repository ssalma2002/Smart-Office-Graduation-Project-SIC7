from gpiozero import OutputDevice
from time import sleep

waterPump = OutputDevice()


def main():
    while True:
        waterPump.on()
        sleep(1)
        waterPump.off()

if __name__ == "__main__":
    main()