import time
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed
import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
import json

CounterFitConnection.init('127.0.0.1', 5050)

light_sensor = GroveLightSensor(0)
led = GroveLed(5)

id = 'f365727a-d36d-4f31-9d01-4ada22aa5f33'

client_telemetry_topic = id + '/telemetry'
client_name = id + 'nightlight_client'

# CORRECCIÓN: Agrega CallbackAPIVersion.VERSION1 aquí
mqtt_client = mqtt.Client(CallbackAPIVersion.VERSION1, client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

print("MQTT connected!")

while True:
    light = light_sensor.light
    telemetry = json.dumps({'light' : light})

    print("Sending telemetry ", telemetry)

    mqtt_client.publish(client_telemetry_topic, telemetry)

    time.sleep(5)
