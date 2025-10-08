import serial
from pub import publisher  # your MQTT publisher wrapper

serial_port = '/dev/ttyACM0'
baud_rate = 9600

arduino = serial.Serial(serial_port, baud_rate, timeout=2)

def parse_line(line: str):
    """
    Expected formats:
    - DHT,<temp>,<humidity>
    - SMOKE,<value>
    """
    parts = line.strip().split(',')
    if not parts:
        return None

    if parts[0] == "DHT" and len(parts) == 3:
        try:
            temp = float(parts[1])
            hum = float(parts[2])
            return ("DHT", temp, hum)
        except ValueError:
            return None

    elif parts[0] == "SMOKE" and len(parts) == 2:
        try:
            smoke = int(parts[1])
            return ("SMOKE", smoke)
        except ValueError:
            return None

    return None


def isFire():
    while True:
        line = arduino.readline().decode(errors='ignore').strip()
        if not line:
            continue

        parsed = parse_line(line)
        if not parsed:
            print("Unrecognized:", line)
            continue

        if parsed[0] == "DHT":
            _, temp, hum = parsed
            print(f"Temperature: {temp}°C, Humidity: {hum}%")
            publisher.publish("temperatureIn", temp)
            publisher.publish("humidity", hum)

        elif parsed[0] == "SMOKE":
            _, smoke = parsed
            print(f"Smoke Level: {smoke}")
            publisher.publish("airquality", smoke)
            if smoke >= 70:
                print("Fire alert!")


if __name__ == "__main__":
    main()
