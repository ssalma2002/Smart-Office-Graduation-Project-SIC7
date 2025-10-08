from gpiozero import DistanceSensor

sensor = DistanceSensor(echo=18, trigger=23)

def is_person_nearby():
    distance = sensor.distance * 100  # Convert to cm
    return distance < 50  # Threshold distance in cm

if __name__ == "__main__":
    async def main():
        from pub import publisher
        import time
        while True:
            import nfc
            await nfc.nfcOn()
            if is_person_nearby():
                print("Person detected nearby!")
                if nfc.mainNFC or nfc.adminNFC:
                    print("NFC authenticated user detected.")
                publisher.publish("office/cvOpen", "1")
            else:
                print("No one nearby.")
                publisher.publish("office/cvOpen", "0")
            time.sleep(1)
    import asyncio
    asyncio.run(main())
