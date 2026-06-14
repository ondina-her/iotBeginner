import time
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed
import paho.mqtt.client as mqtt
# 1. Importa la versión de la API
from paho.mqtt.enums import CallbackAPIVersion

CounterFitConnection.init('127.0.0.1', 5050)

light_sensor = GroveLightSensor(0)
led = GroveLed(5)

id = 'f365727a-d36d-4f31-9d01-4ada22aa5f33'
client_name = id + 'nightlight_client'

# 2. Modifica esta línea agregando CallbackAPIVersion.VERSION1 o VERSION2
mqtt_client = mqtt.Client(CallbackAPIVersion.VERSION1, client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

print("MQTT connected!")

while True:
    light = light_sensor.light
    print('Light level:', light)

    if light < 300:
        led.on()
    else:
        led.off()
    
    time.sleep(1)
