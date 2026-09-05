import json
import paho.mqtt.client as mqtt

BROKER = "192.168.18.145"   # Raspberry Pi IP
TOPIC_SUB = "home/sensors/dht11"
TOPIC_PUB = "home/commands/led"

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    temp = data["temperature"]
    hum = data["humidity"]

    print(f"Received: temp={temp}, hum={hum}")

    # Simple rule-based decision
    if temp > 26:
        print("Decision: Temperature high → Turn LED ON")
        client.publish(TOPIC_PUB, "1")
    else:
        print("Decision: Temperature normal → Turn LED OFF")
        client.publish(TOPIC_PUB, "0")

client = mqtt.Client()
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC_SUB)

client.on_message = on_message
client.loop_forever()
