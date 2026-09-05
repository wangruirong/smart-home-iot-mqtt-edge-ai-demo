📘 Smart Home IoT + MQTT + Edge AI Demo
A full-stack IoT → AI → IoT control loop using Arduino UNO, Raspberry Pi, MQTT, and Jetson Nano.

⭐ Overview
This project demonstrates a complete smart home system that connects embedded sensors, an IoT gateway, an MQTT messaging layer, and an Edge AI agent running on Jetson Nano.
The system collects environmental data, performs real-time AI-driven decisions, and controls physical devices accordingly.

It is designed as a full FDE-style demo showcasing:

IoT sensing

MQTT messaging

Edge AI decision-making

Workflow automation

Real-time device control

End-to-end system integration

🏛 System Architecture
Code
Arduino UNO → Raspberry Pi → MQTT Broker → Jetson Nano → MQTT → Raspberry Pi → Arduino UNO
Component Roles
Layer	Device	Role	Responsibilities
AI Layer	Jetson Nano	Edge AI Brain	MQTT subscribe/publish, decision logic
IoT Gateway Layer	Raspberry Pi	Home Hub	MQTT broker, device management, serial communication
Device Layer	Arduino UNO	Sensors & Actuators	Temperature/humidity sensing, LED/fan/relay control
Client Layer	PC / Phone	Visualization	Terminal logs, future Web UI


🔌 Data Flow
1. Upstream: Environment → AI Decision
Arduino UNO collects temperature & humidity using DHT11

Sends data to Raspberry Pi via USB serial

Raspberry Pi publishes data to MQTT topics

Jetson Nano subscribes to sensor topics

Jetson Nano agent evaluates data and makes decisions

2. Downstream: AI Decision → Device Action
Jetson Nano publishes control commands (ON/OFF)

Raspberry Pi receives commands and forwards via serial

Arduino UNO executes actions (LED ON/OFF)

📡 Completed Modules (70% Done)
3.1 Arduino UNO (DHT11 + LED)
Successfully reads temperature & humidity

Receives LED control commands

Stable 2-second sampling cycle

Code Snippet

cpp
if (Serial.available()) {
    char cmd = Serial.read();
    if (cmd == '1') digitalWrite(LED_BUILTIN, HIGH);
    if (cmd == '0') digitalWrite(LED_BUILTIN, LOW);
}
3.2 Raspberry Pi (MQTT Publisher)
Publishes sensor data:

Code
Published: {'temperature': 26, 'humidity': 40, 'device': 'raspberrypi-d1', 'timestamp': ...}
3.3 Raspberry Pi (MQTT Control)
Receives Jetson Nano control commands:

Code
Received command: 0
Received command: 1
3.4 Jetson Nano (AI Agent)
Subscribes to sensor data and makes decisions:

Code
Received: temp=25, hum=52
Decision: Temperature normal → Turn LED OFF

Received: temp=27, hum=77
Decision: Temperature high → Turn LED ON
3.5 MQTT Broker (Raspberry Pi)
Supports multi-device communication:

Code
{"temperature": 26, "humidity": 49, ...}
🖼 System Screenshots (from your demo)
Raspberry Pi Publishing Data
Code
Published: {'temperature': 26, 'humidity': 40, ...}
Raspberry Pi Receiving Control Commands
Code
Received command: 0
Received command: 1
Jetson Nano AI Agent Decisions
Code
Received: temp=27, hum=77
Decision: Temperature high → Turn LED ON
Jetson Nano agent.py
python
if temp > 26:
    client.publish(TOPIC_PUB, "1")
else:
    client.publish(TOPIC_PUB, "0")
📊 Current Progress Summary
Module	Status
Arduino Sensor Reading	✔ Completed
Arduino LED Control	✔ Completed
Raspberry Pi Serial Read	✔ Completed
Raspberry Pi MQTT Publish	✔ Completed
Raspberry Pi MQTT Control	✔ Completed
Jetson Nano MQTT Subscribe	✔ Completed
Jetson Nano AI Decision	✔ Completed
End-to-End IoT → AI → IoT Loop	✔ Completed


🚀 Next Steps (Planned)
Add door sensor (reed switch)

Add Web UI (Streamlit)

Add workflow engine (n8n)

Add LLM-based agent (Ollama)

Add more actuators (fan / relay)

📌 Purpose
This demo is designed for:

FDE interviews

AI Solution Architect interviews

IoT + AI integration showcase

Portfolio / LinkedIn Featured

YouTube technical demo video
