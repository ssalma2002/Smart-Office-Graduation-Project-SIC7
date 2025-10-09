from gpiozero import LED
from time import sleep
from paho.mqtt.client import Client

lightMain = LED()
lightAdmin = LED()
roomLight1 = LED()
roomLight2 = LED()
roomLight3 = LED()

def roomsON():
    def room3On(client, userdata, message):
        roomLight1.on() if str(message.payload.decode("utf-8")) == "1" else roomLight1.off()
    room1 = Client(client_id='sub1')
    room1.on_message = room3On
    room1.connect("127.0.0.1", 1883, 60)
    ret1 = room1.subscribe("office/room1")
    room1.loop_start()

    def room2On(client, userdata, message):
        roomLight2.on() if str(message.payload.decode("utf-8")) == "1" else roomLight2.off()
    room2 = Client(client_id='sub2')
    room2.on_message = room2On
    room2.connect("127.0.0.1", 1883, 60)
    ret2 = room2.subscribe("office/room2")
    room2.loop_start()

    def room1On(client, userdata, message):
        roomLight3.on() if str(message.payload.decode("utf-8")) == "1" else roomLight3.off()
    room3 = Client(client_id='sub3')
    room3.on_message = room1On
    room3.connect("127.0.0.1", 1883, 60)
    ret3 = room3.subscribe("office/room3")
    room3.loop_start()


    while True:
        sleep(1)