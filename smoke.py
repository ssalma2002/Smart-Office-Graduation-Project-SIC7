import serial

# Serial Port and Speed Settings
serial_port = '/dev/ttyACM0'  # 아두이노와 연결된 포트
baud_rate = 9600

# Serial Port Initialization
arduino = serial.Serial(serial_port, baud_rate)

def isFire() -> bool:
    data = arduino.readline().decode().strip()
    if data == "1":
        return True
    return False

def main():
    isFire()

if __name__=="__main__":
    main()