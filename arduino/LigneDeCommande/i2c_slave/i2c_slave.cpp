// /dev/ttyACM0
#include <Arduino.h>
#include <Wire.h>

#define LED_1 1
#define LED_2 2

int x;
void receiveI2C(int);

void setup() {
  Wire.begin(9);                // Start I2C Bus as a Slave (Device Number 9)
  Wire.onReceive(receiveI2C); // register event
  
  pinMode(LED_1, OUTPUT);
  pinMode(LED_2, OUTPUT);
  
  digitalWrite(LED_1, LOW);
  digitalWrite(LED_2, LOW);
  
  x = 0;
}

void loop() {
  //If value received is 0 blink LED 1
  if (x == 0) {
    digitalWrite(LED_1, HIGH);
    delay(200);
    digitalWrite(LED_1, LOW);
    delay(200);
  }
  //If value received is 1 blink LED 2
  if (x == 1) {
    digitalWrite(LED_2, HIGH);
    delay(200);
    digitalWrite(LED_2, LOW);
    delay(200);
  }
}

void receiveI2C(int a) {
  x = Wire.receive();    // receive byte as an integer
}
