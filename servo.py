from gpiozero import Servo
from time import sleep

entrance = Servo(20)

def entranceOpen():
    entrance.min()
    sleep(2)
    entrance.max()

def main():
    while True:
        entranceOpen()
        sleep(2)

if __name__ == "__main__":
    main()