from paho.mqtt.client import Client

client = Client(client_id="raspberryPi")
client.connect("localhost", 1883, 60)
client.subscribe("office/face_recognition")
client.loop_forever()

recognized = False

def on_message(message):
    global recognized
    print(f"Received message: {message.payload.decode('utf-8')}")
    if str(message.payload.decode("utf-8")) == "1":
        recognized = True
    else:
        recognized = False

client.on_message = on_message