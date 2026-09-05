System Architecture — Smart Home IoT + MQTT + Edge AI Demo
This document describes the architecture of the Smart Home IoT + MQTT + Edge AI system, including device roles, data flow, communication protocols, and integration points.

🏛 1. Architecture Overview
The system is designed as a full IoT → AI → IoT closed loop:

Code
Arduino UNO → Raspberry Pi → MQTT Broker → Jetson Nano → MQTT → Raspberry Pi → Arduino UNO
It consists of four layers:

Layer	Device	Role	Responsibilities
AI Layer	Jetson Nano	Edge AI Brain	MQTT subscribe/publish, decision logic
IoT Gateway Layer	Raspberry Pi	Home Hub	MQTT broker, device management, serial communication
Device Layer	Arduino UNO	Sensors & Actuators	Temperature/humidity sensing, LED/fan/relay control
Client Layer	PC / Phone	Visualization	Terminal logs, future Web UI


🔌 2. Component Responsibilities
Arduino UNO (Device Layer)
Reads temperature & humidity via DHT11

Sends sensor data to Raspberry Pi via USB serial

Executes control commands (LED ON/OFF, relay control)

Raspberry Pi (IoT Gateway Layer)
Runs Mosquitto MQTT broker

Publishes sensor data to MQTT topics

Subscribes to control commands

Forwards commands to Arduino via serial

Jetson Nano (AI Layer)
Subscribes to sensor topics

Runs Python-based decision agent

Publishes control commands based on rules or AI logic

Future: LLM (Ollama), workflow engine (n8n), RAG

🔁 3. Data Flow
Upstream: Environment → AI Decision
Arduino UNO collects temperature & humidity

Sends data to Raspberry Pi via serial

Raspberry Pi publishes data to MQTT topic:

Code
home/sensors/dht11
Jetson Nano subscribes to the topic

Jetson Nano agent evaluates sensor values and makes decisions

Downstream: AI Decision → Device Action
Jetson Nano publishes control commands:

Code
home/commands/led
Raspberry Pi receives the command

Raspberry Pi forwards the command to Arduino via serial

Arduino executes the action (LED ON/OFF)

📡 4. Communication Protocols
Link	Protocol	Purpose
Arduino → Pi	Serial (USB)	Sensor data transmission
Pi → MQTT Broker	MQTT Publish	Sensor data distribution
Jetson → MQTT Broker	MQTT Subscribe	AI decision input
Jetson → MQTT Broker	MQTT Publish	Control commands
Pi → Arduino	Serial (USB)	Device control


🧠 5. AI Decision Logic (Current Version)
Simple rule-based logic:

python
if temp > 26:
    publish("1")  # LED ON
else:
    publish("0")  # LED OFF
Future upgrades:

LLM-based decision (Ollama)

Workflow automation (n8n)

RAG knowledge integration

Multi-sensor fusion

Multi-actuator orchestration

🖼 6. Architecture Diagram (ASCII Version)
Code
           ┌───────────────────────────────┐
           │           PC / Phone          │
           │  - Web UI (future)            │
           └───────────────▲──────────────┘
                           │ HTTP (future)
                           │
           ┌───────────────┴──────────────┐
           │        Jetson Nano            │
           │  - AI Agent (Python)          │
           │  - MQTT subscribe/publish     │
           └───────────────▲──────────────┘
                           │ MQTT
                           │
           ┌───────────────┴──────────────┐
           │        Raspberry Pi           │
           │  - Mosquitto MQTT Broker      │
           │  - IoT Gateway (Python)       │
           │  - Serial ↔ Arduino           │
           └───────────────▲──────────────┘
                           │ Serial (USB)
                           │
           ┌───────────────┴──────────────┐
           │        Arduino UNO            │
           │  - DHT11 Sensor               │
           │  - LED / Relay                │
           └───────────────────────────────┘
📌 7. Purpose of This Architecture
This architecture demonstrates:

Full-stack IoT + AI integration

Real-time sensor-driven decision-making

Edge AI deployment

MQTT-based messaging

Hardware + software orchestration

FDE-style system design and delivery

It is optimized for:

FDE interviews

AI Solution Architect interviews

IoT + AI portfolio

YouTube demo

LinkedIn Featured showcase
