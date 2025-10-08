import board
import busio
from adafruit_pn532.i2c import PN532_I2C
from time import sleep
# Initialize PN532
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)
pn532.SAM_configuration()

print("Waiting for NFC card...")

# Dictionary of known users
users = {
    '96 80 CA 01': {'name': 'Admin', 'role': 'admin', 'id': 1001},
    '13 3C 56 34': {'name': 'Employee1', 'role': 'employee', 'id': 2001},
}

mainNFC = False
adminNFC = False

while True:
    uid = pn532.read_passive_target(timeout=0.5)
    if uid is None:
        continue

    uid_str = ' '.join([f'{i:02X}' for i in uid])
    print(f"Card detected with UID: {uid_str}")

    if uid_str in users:
        user = users[uid_str]
        if user['role'] == 'admin':
            print(f"Welcome Admin: {user['name']}")
            adminNFC = True
            mainNFC = True
        else:
            print(f"Welcome Employee: {user['name']}")
            mainNFC = True
    else:
        print("Access Denied")
    
    sleep(1)

