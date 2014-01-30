// /dev/ttyUSB0
#include <Arduino.h>
#include <LiquidCrystal.h>
#include "../trame.h"


byte valueReceive=0;
LiquidCrystal lcd(13, 12, 11, 10, 9, 8);

unsigned long time_last_display;

void setup()
  {
  lcd.begin(16, 2);
  pinMode(pinData, INPUT);
  lcd.setCursor(0, 0);
  //lcd.print("BitOrderMSBFIRST");
  lcd.print("trame:");
  }

void loop()
  {
  // bit_debut trame[0]
  int bits_no_carte = 0; // trame[1-7]
  int bits_donnees = 0; // trame[8-9]
  
  // reception de la tram
  if (digitalRead(pinData))
    {
    delay(10*speedDial);
    
    // reception de la trame
    for (int num_bit=1;num_bit<=9;num_bit++)
      {
      trame[num_bit]=digitalRead(pinData);
      delay(10*speedDial);
      }
    
    // enregistrement du temps à l'affichage
    time_last_display = millis();
    }
  else
    {
	// par de trame recu depuis 500 ms
	if (time_last_display+1000 < millis())
	  {
	  lcd.setCursor(6, 0);
	  lcd.print("no  signal");
	  }
	else
	  {
	  // affichage de la trame
	  lcd.setCursor(6, 0);
	  for (int num_bit=0;num_bit<=9;num_bit++)
		{
		lcd.print(trame[num_bit]);
		}
  
	  // trame to bits_no_carte
	  for (int num_bit=1;num_bit<=7;num_bit++)
		{
		if (HIGH && trame[num_bit] && bit(num_bit))
		  {
		  bits_no_carte += bit(7-num_bit);
		  }
		}
    
	  // trame to bits_donnees
	  for (int num_bit=8;num_bit<=9;num_bit++)
		{
		if (HIGH && trame[num_bit] && bit(num_bit))
		  {
		  bits_donnees += bit(num_bit-8);
		  }
		}

	  lcd.setCursor(0, 1);
	  lcd.print("c:");
	  lcd.print(bits_no_carte, 10);
	  lcd.setCursor(12, 1);
	  lcd.print("d:");
	  lcd.print(bits_donnees, 10);
  
	  //0123456789012345
	  //trame:1234567890
	  //c:1234567   d:89
	  }
	}
  }
