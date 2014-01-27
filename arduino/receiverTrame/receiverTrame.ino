// /dev/ttyUSB0
#include <LiquidCrystal.h>
const int pinData = 4;
const int pinStart = 2;
const int speedDial = 1;
bool bit0=false;
bool bit1=false;
bool bit2=false;
bool bit3=false;

LiquidCrystal lcd(13, 12, 11, 10, 9, 8);

void setup()
  {
  //attachInterrupt(0, receiveTrame, FALLING);
  lcd.begin(16, 2);
  pinMode(pinStart, INPUT);
  pinMode(pinData, INPUT);  
  lcd.setCursor(0, 0);
  lcd.print("BitOrderMSBFIRST");
  }

void loop()
  {
  if (digitalRead(pinStart))
    {
    lcd.setCursor(0, 1);
    lcd.print("state bit : ");

    
    delay(10*speedDial);
    bit0=digitalRead(pinData);
    delay(10*speedDial);
    bit1=digitalRead(pinData);
    delay(10*speedDial);
    bit2=digitalRead(pinData);
    delay(10*speedDial);
    bit3=digitalRead(pinData);
    
    lcd.print(bit0);
    lcd.print(bit1);
    lcd.print(bit2);
    lcd.print(bit3);
    }
  }

void receiveTrame()
  {

  }
