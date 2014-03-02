// /dev/ttyUSB0
#include <Arduino.h>
#include <Wire.h>

#define LED_PIN 1
byte x = 0;

void setup()
{
  Wire.begin(); // Start I2C Bus as Master
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

}
void loop()
{
  
  Wire.beginTransmission(9); // transmit to device #9
  Wire.send(x);              // sends x 
  Wire.endTransmission();    // stop transmitting
  x++;
  if (x > 5)
  {
    x=0;
    digitalWrite(LED_PIN, HIGH);
  }
  if (x == 1) digitalWrite(LED_PIN, LOW);
  delay(450);
}

