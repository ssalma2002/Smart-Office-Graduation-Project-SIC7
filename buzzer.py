from gpiozero import Buzzer
import time

buzzer = Buzzer(22)

def buzz_on():
    period = 1.0 / 2000
    buzzer.frequency = 2000
    buzzer.value = 0.5 
    buzzer.off()

def buzz_off():
    buzzer.off()

if __name__ == "__main__":
    while True:
        x = int(input())
        if time.localtime().tm_hour < x:
            continue
        buzz_on()
        print("Buzzer is ON")
        time.sleep(2)
        buzz_off()
        print("Buzzer is OFF")
