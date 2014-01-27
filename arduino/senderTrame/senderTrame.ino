// /dev/ttyACM0
const int pinStart = 9;
const int pinData = 8;

const int speedDial = 10;

bool bit0;
bool bit1;
bool bit2;
bool bit3;

void setup()
  {
  pinMode(pinStart, OUTPUT);
  pinMode(pinData, OUTPUT);    
  }

void loop()
  {
  for (int i=0;i<=15;i++) // de 0 à 15
    {
    switch(i)
      {
      case 0:  bit0 = 0; bit1 = 0; bit2 = 0; bit3 = 0; break;
      case 1:  bit0 = 0; bit1 = 0; bit2 = 0; bit3 = 1; break;
      case 2:  bit0 = 0; bit1 = 0; bit2 = 1; bit3 = 0; break;
      case 3:  bit0 = 0; bit1 = 0; bit2 = 1; bit3 = 1; break;
      case 4:  bit0 = 0; bit1 = 1; bit2 = 0; bit3 = 0; break;
      case 5:  bit0 = 0; bit1 = 1; bit2 = 0; bit3 = 1; break;
      case 6:  bit0 = 0; bit1 = 1; bit2 = 1; bit3 = 0; break;
      case 7:  bit0 = 0; bit1 = 1; bit2 = 1; bit3 = 1; break;
      case 8:  bit0 = 1; bit1 = 0; bit2 = 0; bit3 = 0; break;
      case 9:  bit0 = 1; bit1 = 0; bit2 = 0; bit3 = 1; break;
      case 10: bit0 = 1; bit1 = 0; bit2 = 1; bit3 = 0; break;
      case 11: bit0 = 1; bit1 = 0; bit2 = 1; bit3 = 1; break;
      case 12: bit0 = 1; bit1 = 1; bit2 = 0; bit3 = 0; break;
      case 13: bit0 = 1; bit1 = 1; bit2 = 0; bit3 = 1; break;
      case 14: bit0 = 1; bit1 = 1; bit2 = 1; bit3 = 0; break;
      case 15: bit0 = 1; bit1 = 1; bit2 = 1; bit3 = 1; break;
      }
    digitalWrite(pinStart, HIGH); // bit depart
    delay(8*speedDial);
    digitalWrite(pinStart, LOW); // bit depart
    digitalWrite(pinData, bit0);
    delay(10*speedDial);
    digitalWrite(pinData, bit1);
    delay(10*speedDial);
    digitalWrite(pinData, bit2);
    delay(10*speedDial);
    digitalWrite(pinData, bit3);
    delay(10*speedDial);
    digitalWrite(pinData, LOW);
    delay(20*speedDial);
    }
  delay(1000);
}
    
