import serial
import sys

# Serial Port and Speed Settings
serial_port = '/dev/ttyACM0'  # 아두이노와 연결된 포트
baud_rate = 9600

# Serial Port Initialization
arduino = serial.Serial(serial_port, baud_rate)
while True:
	data = arduino.readline().decode().strip()
	print(data)
