// /dev/ttyUSB0
#include <LiquidCrystal.h>
const int pinData = 4;
const int pinStart = 2;
const int speedDial = 1;
bool bit0=false;
bool bit1=false;
bool bit2=false;
bool bit3=false;
bool bit4=false;
bool bit5=false;
bool bit6=false;
bool bit7=false;

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
    lcd.print("st bit :");

    
    delay(10*speedDial);
    bit0=digitalRead(pinData);
    delay(10*speedDial);
    bit1=digitalRead(pinData);
    delay(10*speedDial);
    bit2=digitalRead(pinData);
    delay(10*speedDial);
    bit3=digitalRead(pinData);
    delay(10*speedDial);
    bit4=digitalRead(pinData);
    delay(10*speedDial);
    bit5=digitalRead(pinData);
    delay(10*speedDial);
    bit6=digitalRead(pinData);
    delay(10*speedDial);
    bit7=digitalRead(pinData);
    
    
    lcd.print(bit0);
    lcd.print(bit1);
    lcd.print(bit2);
    lcd.print(bit3);
    lcd.print(bit4);
    lcd.print(bit5);
    lcd.print(bit6);
    lcd.print(bit7);

    }
  }

void receiveTrame()
  {

  }
