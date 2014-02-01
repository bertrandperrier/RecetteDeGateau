// /dev/ttyUSB0
#include <Arduino.h>
#include <LiquidCrystal.h>

int _input_pin = 3;
int time_trame_high = 90;
int time_trame_low = 40;
LiquidCrystal lcd(13, 12, 11, 10, 9, 8);
uint16_t _input_frame;
int _input_current_bit;
unsigned long time_last_tick;

void setup()
	{
	lcd.begin(16, 2);
	pinMode(_input_pin, INPUT);
	lcd.setCursor(0, 0);
	lcd.print("T");
	}

void loop()
{

	lcd.setCursor(1, 0);

	_input_frame = 0x0000;
	
	for (_input_current_bit=9;_input_current_bit>=0;_input_current_bit--)
	{
		while (!digitalRead(_input_pin)) {}
		
		delay(time_trame_low+5);
		if (digitalRead(_input_pin)) // toujours à 1 => long -> niveau 1
		{
			_input_frame |= (1 << _input_current_bit);
			// _input_frame += (uint16_t)pow(2, _input_current_bit);
		}
		while (digitalRead(_input_pin)) {}
	}
	lcd.setCursor(1, 0); // 1ere ligne
	lcd.print(_input_frame,2);
	delay(200); // find de trame

}
