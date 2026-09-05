import serial
import paho.mqtt.client as mqtt

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

BROKER = "localhost"
TOPIC = "home/commands/led"

def on_message(client, userdata, msg):
    cmd = msg.payload.decode()
    print("Received command:", cmd)

    if cmd == "1":
        ser.write(b'1')
    elif cmd == "0":
        ser.write(b'0')

client = mqtt.Client()
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)

client.on_message = on_message
client.loop_forever()
