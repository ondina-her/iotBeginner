import json
import time

import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion


id = 'f365727a-d36d-4f31-9d01-4ada22aa5f33'

client_telemetry_topic = id + '/telemetry'
client_name = id + '_nightlight_server'

mqtt_client = mqtt.Client(CallbackAPIVersion.VERSION1, client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(2)