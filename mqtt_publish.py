import serial
import json
import time
import paho.mqtt.client as mqtt

# Serial port for Arduino
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)

# MQTT settings
BROKER = "localhost"   # ← Replace with your Pi's IP
TOPIC = "home/sensors/dht11"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    line = ser.readline().decode('utf-8').strip()
    if line.startswith("Sample OK"):
        # Example: "Sample OK: 25 *C, 56 %"
        parts = line.replace("Sample OK: ", "").replace(" *C", "").replace(" %", "")
        temp, hum = parts.split(", ")

        payload = {
            "temperature": int(temp),
            "humidity": int(hum),
            "device": "raspberrypi-01",
            "timestamp": time.time()
        }

        client.publish(TOPIC, json.dumps(payload))
        print("Published:", payload)

    time.sleep(0.1)
