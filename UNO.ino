// Chapter 7 - Communications
// I2C Master // By Cornel Amariei for Packt Publishing

// Include the required Wire library for I2C

#include <Wire.h>

int x = 0;

int sensorPin = A0;

int sensorValue = 0;

void setup() {

// Start the I2C Bus as Master

Wire.begin();

Serial.begin(9600);

}

void loop() {

sensorValue = analogRead(sensorPin);

Serial.println(sensorValue);

Wire.beginTransmission(9);

// transmit to device #9

Wire.write(sensorValue);

delay(1000);

Wire.endTransmission();

// stop transmitting

}