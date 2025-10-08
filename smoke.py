import serial
from pub import publisher

# Serial Port and Speed Settings
serial_port = '/dev/ttyACM0' 
baud_rate = 9600

# Serial Port Initialization
arduino = serial.Serial(serial_port, baud_rate)

def isFire() -> bool:
    data = arduino.readline().decode().strip()
    publisher.publish("office/smoke", int(data))
    if data >= int("70"):
        return True
    return False

def main():
    isFire()

if __name__=="__main__":
    main()