//www.elegoo.com
//2016.12.9

#include <SimpleDHT.h>

int pinDHT11 = 2;
SimpleDHT11 dht11;

unsigned long lastReadTime = 0;          // Last DHT11 read timestamp
const unsigned long readInterval = 2000; // Read every 2 seconds

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {

  // 1. Read DHT11 every 2 seconds (non-blocking)
  unsigned long now = millis();
  if (now - lastReadTime >= readInterval) {
    lastReadTime = now;

    Serial.println("=================================");
    Serial.println("Sample DHT11...");

    byte temperature = 0;
    byte humidity = 0;
    byte data[40] = {0};

    // Attempt to read DHT11
    if (dht11.read(pinDHT11, &temperature, &humidity, data)) {
      Serial.println("Read DHT11 failed");
    } else {
      Serial.print("Sample RAW Bits: ");
      for (int i = 0; i < 40; i++) {
        Serial.print((int)data[i]);
        if (i > 0 && ((i + 1) % 4) == 0) {
          Serial.print(' ');
        }
      }
      Serial.println("");

      Serial.print("Sample OK: ");
      Serial.print((int)temperature);
      Serial.print(" *C, ");
      Serial.print((int)humidity);
      Serial.println(" %");
    }
  }
  
  //add by larry for test 8.25 2026
  //digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  //delay(1000);                       // wait for a second
  //digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  //delay(1000);                       // wait for a second

  // 2. Handle serial commands from Raspberry Pi
  if (Serial.available()) {
    char cmd = Serial.read();
    if (cmd == '1') {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("LED ON");
    }
    if (cmd == '0') {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("LED OFF");
    }
  }
}
