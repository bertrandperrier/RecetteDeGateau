int datapin = 2; 
int clockpin = 3;
int latchpin = 4;
int ledPin = 2;

void setup()
{
  pinMode(ledPin, OUTPUT);
}


void loop()
{

// 74HC595
  byte data = 0;
  int desiredPin = 1;
  bool desiredState = true;
  // bitWt(data,desiredPin,desiredState);
  bitWrite(data,desiredPin,desiredState);
  shiftOut(datapin, clockpin, MSBFIRST, data);
  digitalWrite(latchpin, HIGH);
  digitalWrite(latchpin, LOW);
  delay(1000);
}

void bitWt(byte data, int pin, bool state)
{
  float toAdd2 = pow( float(2), float(pin));
  int toAdd = int(toAdd2);
  if (state)
    {
      data += toAdd;
    }
    else
    {
      data -= toAdd;
    }
}
