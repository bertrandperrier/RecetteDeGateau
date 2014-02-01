// /dev/ttyUSB0
#include <Arduino.h>
#include <LiquidCrystal.h>
float time_each_tick=2.5; // en ms - 2,5 ms
void tick2500ms();
int _output_pin = 4;
byte valueReceive=0;
LiquidCrystal lcd(13, 12, 11, 10, 9, 8);
uint16_t _output_frame;
uint16_t _input_frame;
int _input_current_bit;
unsigned long time_last_tick;
void setup()
  {
  lcd.begin(16, 2);
  pinMode(_output_pin, OUTPUT);
  time_last_tick = millis();
  }

void loop()
  {
	byte address=0x55;
	byte data=0x02;

										//85 hex55 B1010101
	//									1					1010101 00			10  &  11					
	_output_frame = (1 << 9) | (address << 2) | (data & 0x03); // masque 0x03 pour n'avoir que 2 bits
																					 //1 1010101 10
																					 


  lcd.setCursor(0, 0);
  lcd.print("I            ");
  lcd.setCursor(0, 1);
	lcd.print("O            ");
  lcd.setCursor(1, 1);
	_input_frame = 0x0000;
	//lcd.print(_output_frame, 2); // 2eme ligne
	
  for (int _output_currentBit=9;_output_currentBit>=0;_output_currentBit--)
		{
		/* ne fonctionne pas car il y a des delays plus bas
		if (time_last_tick+time_each_tick < millis())
			{
			tick2500ms();
			time_last_tick = millis();
			}
		*/

		bool output = (_output_frame & (1 << _output_currentBit));
		// digitalWrite(_output_pin, HIGH);
		lcd.print(output); // 2eme ligne

		if (output)
			{delay(900);
			_input_current_bit=_output_currentBit;
			_input_frame |= (1 << _input_current_bit);
			}
		else
			{delay(400);}
		
		
		}
  lcd.setCursor(1, 0); // 1ere ligne
  lcd.print(_input_frame,2);
	delay(1000); // find de trame
	
  }

void tick2500ms()
	{
	digitalWrite(_output_pin, HIGH);
	delay(100);
	digitalWrite(_output_pin, LOW);
	}
