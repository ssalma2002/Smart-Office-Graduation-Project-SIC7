from paho.mqtt.client import Client

publisher = Client(client_id="publisher")
publisher.connect("10.178.13.231", 1883)
publisher.loop_start()
