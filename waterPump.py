from gpiozero import Motor
from time import sleep

# Define H-bridge control pins
pump = Motor(forward=17, backward=18)
if __name__ == "__main__":
    print("Pump ON")
    pump.forward()   # Turns pump ON in one direction
    sleep(5)

    print("Pump OFF")
    pump.stop()      # Stops pump

