// /dev/ttyUSB0
#include <Arduino.h>
#include <LiquidCrystal.h>


LiquidCrystal lcd(13, 12, 11, 10, 9, 8);

void setup()
  {
  lcd.begin(16, 2);
  }

void loop()
  {
		for (int i=0;i<=2;i++)
				{
				lcd.setCursor(0, 0);
				lcd.print("  tchou tchou ! ");
				delay(300);
				lcd.setCursor(0, 0);
				lcd.print("                ");
				delay(300);
			 }
			 
		for (int i=0;i<=12;i++)
				{
					
				lcd.setCursor(i, 0);
    lcd.print(" --.");
    lcd.setCursor(i, 1);
    lcd.print("|oo|");
    
    if (i>=3) 
						{
							 lcd.setCursor(i-2, 0);
								lcd.print("ooo");
						}

    delay(500);
    lcd.setCursor(0, 0);
    lcd.print("                ");
    lcd.setCursor(0, 1);
    lcd.print("________________");
				}
		}
