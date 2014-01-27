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
  lcd.print(" num bit : 0123");
  }

void loop()
  {
  if (digitalRead(pinStart))
    {
    lcd.setCursor(0, 1);
    lcd.print("etat bit : ----");
    lcd.setCursor(11, 1);
    delay(10*speedDial);
    lcd.print(digitalRead(pinData));
    delay(10*speedDial);
    lcd.setCursor(12, 1);
    lcd.print(digitalRead(pinData));
    delay(10*speedDial);
    lcd.setCursor(13, 1);
    lcd.print(digitalRead(pinData));
    delay(10*speedDial);
    lcd.setCursor(14, 1);
    lcd.print(digitalRead(pinData));
    }
  }

void receiveTrame()
  {

  }
