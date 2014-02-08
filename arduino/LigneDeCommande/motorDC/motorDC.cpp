// /dev/ttyACM0
#include <Arduino.h>
const int motorPin = 9;


void setup()
{
  // Set up the motor pin to be an output:

  pinMode(motorPin, OUTPUT);

}


void loop()
{
  int speed;
  int delayTime = 100; // milliseconds between each speed step
  
  // accelerate the motor

  for(speed = 0; speed <= 255; speed++)
  {
    analogWrite(motorPin,speed);	// set the new speed
    delay(delayTime);           	// delay between speed steps
  }
  
  // decelerate the moto
  for(speed = 255; speed >= 0; speed--)
  {
    analogWrite(motorPin,speed);	// set the new speed
    delay(delayTime);           	// delay between speed steps
  }
}
