// Include the required Wire library for I2C
#include <Wire.h>

int LED = 11;

int x = 0;

void setup() {

// Define the LED pin as Output

pinMode (LED, OUTPUT);

// Start the I2C Bus as Slave on address 9

Wire.begin(9);

// Attach a function to trigger when something is received.

Wire.onReceive(receiveEvent);

//bit rate for data transfer over Serial communication

Serial.begin(9600);

}

void receiveEvent(int bytes) {

x = Wire.read(); // read one character from the I2C

}

void loop() {

//potentiometer value from sensor

int ledPWM = map(x, 0, 255, 0, 1023);

analogWrite(LED, ledPWM);

Serial.print("X is: ");

Serial.println(x);

Serial.print("PWM is: ");

Serial.println(ledPWM);

delay(1000);

}