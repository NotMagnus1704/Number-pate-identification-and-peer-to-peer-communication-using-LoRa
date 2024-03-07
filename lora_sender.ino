#include <SPI.h>
#include <LoRa.h>

void setup() {
  Serial.begin(9600);  // Start the serial communication
  while (!Serial);

  Serial.println("LoRa Sender");

  // Initialize LoRa
  if (!LoRa.begin(433E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}

void loop() {
  if (Serial.available()) {
    // Read incoming data
    String input = Serial.readString();

    // Send data over LoRa
    LoRa.beginPacket();
    LoRa.print(input);
    LoRa.endPacket();

    Serial.print("Sent: ");
    Serial.println(input);
  }
}
