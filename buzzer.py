from gpiozero import Buzzer

buzzer = Buzzer()

def buzz_on():
    buzzer.on()

def buzz_off():
    buzzer.off()

if __name__ == "__main__":
    buzz_on()
    print("Buzzer is ON")
    import time
    time.sleep(2)
    buzz_off()
    print("Buzzer is OFF")