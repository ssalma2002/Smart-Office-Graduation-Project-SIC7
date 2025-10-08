from paho.mqtt.client import Client

def on_message(client, userdata, message):
    global recognized
    if str(message.payload.decode("utf-8")) == "1":
        recognized = True
    else:
        recognized = False


client = Client(client_id="raspberryPi")
client.connect("localhost", 1883)
client.on_message = on_message
client.subscribe("office/face_recognition")
client.loop_forever()

recognized = False

