// /dev/ttyUSB0
#include <Arduino.h>

int _output_pin = 4;
int time_trame_high = 90;
int time_trame_low = 40;
int time_trame_space = 10;
uint16_t _output_frame;
unsigned long time_last_tick;


void setup()
  {
  pinMode(_output_pin, OUTPUT);
  time_last_tick = millis();
  }

void loop()
  {
	byte address=32+16+4+1; //64+8+2; 0110101
	byte data=1; //01

	//0x55 85 hex55 B1010101
	//									1					7 bits    			10  &  11					
	_output_frame = (1 << 9) | (address << 2) | (data & 0x03); // masque 0x03 pour n'avoir que 2 bits
	//1 0110101 01
	
	for (int _output_currentBit=9;_output_currentBit>=0;_output_currentBit--)
	{
		bool output = (_output_frame & (1 << _output_currentBit));
	
		if (output)
		{
			digitalWrite(_output_pin, HIGH);
			delay(time_trame_high);
		}
		else
		{
			digitalWrite(_output_pin, HIGH);
			delay(time_trame_low);
		}
		digitalWrite(_output_pin, LOW);
		delay(time_trame_space);
	}

	delay(1000); // find de trame
	
  }

