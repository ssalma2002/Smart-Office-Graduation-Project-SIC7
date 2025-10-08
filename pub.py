from paho.mqtt.client import Client

publisher = Client(id="publisher")
publisher.connect("broker.emqx.io", 1883)
