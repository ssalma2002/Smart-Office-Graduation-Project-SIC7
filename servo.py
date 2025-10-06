from gpiozero import Servo
from time import sleep

entrance = Servo()
master = Servo()

def entranceOpen():
    entrance.max()
    sleep(2)
    entrance.min()


def adminOpen():
    master.max()
    sleep(2)
    master.min()

def main():
    while True:
        entranceOpen()
        sleep(2)
        adminOpen()
        sleep(2)

if __name__ == "__main__":
    main()