import time
import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
import json
from os import path
import csv
from datetime import datetime

id = 'f365727a-d36d-4f31-9d01-4ada22aa5f33'
client_telemetry_topic = id + '/telemetry'
server_command_topic = id + '/commands'
client_name = id + 'temperature_sensor_client_server' 

# Inicialización del cliente MQTT
mqtt_client = mqtt.Client(CallbackAPIVersion.VERSION1, client_name)
mqtt_client.connect('test.mosquitto.org')

temperature_file_name = 'temperature.csv'
fieldnames = ['date', 'temperature']

# Crear el archivo con cabeceras si no existe
if not path.exists(temperature_file_name):
    with open(temperature_file_name, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

# Función que procesa los mensajes recibidos
def handle_telemetry(client, userdata, message):
    try:
        payload = json.loads(message.payload.decode())
        print("Mensaje recibido:", payload)
        
        with open(temperature_file_name, mode='a', newline='') as temperature_file:
            temperature_writer = csv.DictWriter(temperature_file, fieldnames=fieldnames)
            temperature_writer.writerow({
                'date': datetime.now().astimezone().replace(microsecond=0).isoformat(), 
                'temperature': payload['temperature']
            })
            print("Datos guardados en CSV.")
    except Exception as e:
        print("Error procesando o guardando el mensaje:", e)

# Configurar callbacks y suscripción antes de iniciar el bucle
mqtt_client.on_message = handle_telemetry
mqtt_client.subscribe(client_telemetry_topic)

# Iniciar el bucle de escucha de red
mqtt_client.loop_start()

print("Servidor escuchando y esperando telemetría...")

# Mantener el script principal ejecutándose
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Deteniendo servidor...")
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    
