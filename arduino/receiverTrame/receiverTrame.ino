// /dev/ttyUSB0
#include <LiquidCrystal.h>
const int pinData = 4;
const int speedDial = 1;
bool trame[] = {0,0,0,0,0,0,0,0};
byte valueReceive=0;
LiquidCrystal lcd(13, 12, 11, 10, 9, 8);

void setup()
  {
  lcd.begin(16, 2);
  pinMode(pinData, INPUT);
  lcd.setCursor(0, 0);
  //lcd.print("BitOrderMSBFIRST");
  lcd.print("binaire:");
  lcd.setCursor(0, 1);
  //lcd.print("st bit :");
  lcd.print("decimal:");
  }

void loop()
  {
  if (digitalRead(pinData))
    {
    lcd.setCursor(8, 1);
    delay(12*speedDial);
    
    for (int num_bit=0;num_bit<=7;num_bit++)
      {
      trame[num_bit]=digitalRead(pinData);
      delay(10*speedDial);
      }
      
    lcd.setCursor(8, 0);
    for (int num_bit=0;num_bit<=7;num_bit++)
      {
      lcd.print(trame[7-num_bit]);
      delay(10*speedDial);
      }

    }
    
  for (int num_bit=0;num_bit<=7;num_bit++)
    {
    if (HIGH && trame[num_bit] && bit(num_bit))
      {
      valueReceive += bit(num_bit);
      }
    }
    lcd.setCursor(8, 1);
    lcd.print(valueReceive, 10);
    valueReceive = 0;
  }
