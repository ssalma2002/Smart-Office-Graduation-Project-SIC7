from gpiozero import DistanceSensor

sensor = DistanceSensor(echo=18, trigger=23)

def is_person_nearby():
    distance = sensor.distance * 100  # Convert to cm
    return distance < 50  # Threshold distance in cm

if __name__ == "__main__":
    import nfc, threading, time
    from pub import publisher
    def ultra():
        while True:
            if is_person_nearby():
                print("Person detected nearby!")
                publisher.publish("office/cvOpen", "1")
            else:
                print("No person nearby.")
                publisher.publish("office/cvOpen", "0")
            time.sleep(1)
    
    threads = [
        threading.Thread(target=ultra, daemon=True),
        threading.Thread(target=nfc.nfcOn, daemon=True)
    ]
    
    # Start all threads
    for thread in threads:
        thread.start()
    
    # Keep the main thread running
    while True:
        time.sleep(1)
