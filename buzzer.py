from gpiozero import PWMOutputDevice
import time

buzzer = PWMOutputDevice(17)

def buzz_on():
    period = 1.0 / 200
    buzzer.frequency = 200
    buzzer.value = 0.5  # 50% duty cycle (medium volume)

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
