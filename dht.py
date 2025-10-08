import adafruit_dht
import board

dhtDevice = adafruit_dht.DHT11(board.D4)

try:
    temperature = dhtDevice.temperature
    humidity = dhtDevice.humidity
    print(f"Temp={temperature}°C  Humidity={humidity}%")
except RuntimeError as e:
    print(e)
