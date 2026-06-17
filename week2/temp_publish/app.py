import time
from counterfit_connection import CounterFitConnection
from counterfit_shims_seeed_python_dht import DHT
import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
import json

CounterFitConnection.init('127.0.0.1', 5050)

dht_sensor = DHT("11", 5)


id = 'f365727a-d36d-4f31-9d01-4ada22aa5f33'

client_telemetry_topic = id + '/telemetry'
client_name = id + 'temperature_sensor_client'

# CORRECCIÓN: Agrega CallbackAPIVersion.VERSION1 aquí
mqtt_client = mqtt.Client(CallbackAPIVersion.VERSION1, client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

print("MQTT connected!")

while True:
    _, temp = dht_sensor.read()
    telemetry = json.dumps({"temperature": temp})
    
    print(f'Sending telemetry: {telemetry}')

    mqtt_client.publish(client_telemetry_topic, telemetry)


    time.sleep(10 * 60);