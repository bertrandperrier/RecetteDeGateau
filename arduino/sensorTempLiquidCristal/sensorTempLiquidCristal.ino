

// include the library code:
#include <LiquidCrystal.h>

const int temperaturePin = 0;

int hour = 19;
int minute = 1;
int second = 30;

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  // set up the LCD's number of columns and rows: 
  lcd.begin(16, 2);


  pinMode(temperaturePin, OUTPUT);

}

void loop() {
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  lcd.setCursor(0, 1);
  // print the number of seconds since reset:
  lcd.print(analogRead(A0));

  
  float voltage, degreesC;
  voltage = getVoltage(temperaturePin);
  degreesC = (voltage - 0.5) * 100.0;

  
  lcd.setCursor(0,0);
  lcd.print("temp.   :");
  lcd.setCursor(10,0);
  lcd.print(degreesC,1);
  lcd.setCursor(14,0);
  int thisByte = 223; // °
  lcd.write(thisByte);
  lcd.print("C");
  
    

  lcd.setCursor(0,1);
  lcd.print(hour);
  lcd.setCursor(2,1);
  lcd.print(":");
  lcd.setCursor(3,1);
  lcd.print(minute);
  lcd.setCursor(5,1);
  lcd.print(":");
  lcd.setCursor(6,1);
  lcd.print(second);

   
  delay(1000);
  // repeat once per second (change as you wish!)
  second += 1;
  if (second == 60)
    {
    second = 0;
    minute += 1;
    }
  if (minute == 60)
    {
    minute = 0;
    hour += 1;
    }
  if (hour == 24)
    {
    hour = 0;
    }
  
}




float getVoltage(int pin)
{
 return (analogRead(pin) * 0.004882814);
}
