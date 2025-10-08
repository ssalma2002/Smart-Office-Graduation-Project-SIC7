from gpiozero import DistanceSensor

sensor = DistanceSensor(echo=18, trigger=23)

def is_person_nearby():
    distance = sensor.distance * 100  # Convert to cm
    return distance < 50  # Threshold distance in cm

if __name__ == "__main__":
    import time
    while True:
        if is_person_nearby():
            print("Person detected nearby!")
        else:
            print("No one nearby.")
        time.sleep(1)
