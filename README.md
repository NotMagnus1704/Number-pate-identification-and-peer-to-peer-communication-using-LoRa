# Number-pate-identification-and-peer-to-peer-communication-using-LoRa
This has the necessary files to perform Peer to peer communication and extract data from a number plate using Python libraries

*******************************************************************
Make sure to upload the code to Arduino Uno and close the Arduino ide [sender script] before running the Python script
*******************************************************************

Pin Configuration:
**Same setup for both transmission and receiver**

Connect 3.3V on the Arduino to VCC on the RA-02.
Connect GND on the Arduino to GND on the RA-02.
Connect D10 on the Arduino to NSS (Chip Select) on the RA-02.
Connect D11 on the Arduino to MOSI on the RA-02.
Connect D12 on the Arduino to MISO on the RA-02.
Connect D13 on the Arduino to SCK on the RA-02.
Connect D2 on the Arduino to DIO0 on the RA-02.
Optionally, connect D6 on the Arduino to RST on the RA-02 for reset control.

Components required :
2 Arduino Uno [one for receiver, one for sender]
2 SP1278 LoRa modules [one for receiver, one for sender]
Jumper wires
Antena [for better connectivity]

Pip install these libraries:
cv2
easyocr
serial
