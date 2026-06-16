import time

from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_seeed_python_dht import DHT
CounterFitConnection.init('127.0.0.1', 5050)

dht_sensor = DHT("DHT11", 5)

while True:
    _, temp = dht_sensor.read()
    print(f'Temperature {temp}°C')

    time.sleep(10)