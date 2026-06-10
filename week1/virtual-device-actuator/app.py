import time
from counterfit_shims_grove.grove_led import GroveLed
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor

CounterFitConnection.init('127.0.0.1', 5050)
light_sensor = GroveLightSensor(0)
led = GroveLed(5)


while True:
    light_value = light_sensor.light
    print(f"Light value: {light_value}")
    if light_value < 300:
        led.on()
    else:
        led.off()
    time.sleep(1)