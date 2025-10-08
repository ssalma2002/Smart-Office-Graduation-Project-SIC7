from paho.mqtt.client import Client

publisher = Client()
#publisher = Client(client_id="publisher")
publisher.connect("4cb1d1ac03b54dfea0c93db78697713a.s1.eu.hivemq.cloud", 8883)
publisher.loop_start()
USERNAME = "finalProject"
PASSWORD = "finalProject123"
