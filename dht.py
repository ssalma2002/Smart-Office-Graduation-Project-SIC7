import adafruit_dht
import board

dht = adafruit_dht.DHT11(board.D17)  # or DHT22
temperature = dht.temperature
humidity = dht.humidity

print(f"Temp: {temperature}°C, Humidity: {humidity}%")
