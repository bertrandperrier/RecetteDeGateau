// /dev/ttyUSB0
// à mettre dans une class
#include <Arduino.h>
#include <LiquidCrystal.h>
#include "boucle_for_sans_for.h"

LiquidCrystal lcd(13, 12, 11, 10, 9, 8);
int input_pin = 3;

boucle::boucle( int debut=0, int fin=10, bool condition=true)
{
	valeur_boucle = debut;
	valeur_debut = debut;
	valeur_fin = fin;
	condition_fin=condition;
	boucle_state etat_boucle = IDLE;
}
 
boucle_state boucle::GetStateBoucle()
{
    return this->etat_boucle;
}

int boucle::GetValueBoucle()
{
    return this->valeur_boucle;
}

char* boucle::GetStateBoucleTxt()
{
	if (this->etat_boucle == 0)
		return (char*)"IDLE    ";
	if (this->etat_boucle == 1)
		return (char*)"SENDING ";
	if (this->etat_boucle == 2)
		return (char*)"FINISHED";
	return (char*)"ERROR   ";
}

void boucle::Refresh(bool condition_fin = true)
{
	this->condition_fin = condition_fin;
	
	if (this->etat_boucle == IDLE)
		this->valeur_boucle=valeur_debut;
		
	if ((this->etat_boucle == SENDING) & (this->valeur_boucle<this->valeur_fin))
		this->valeur_boucle++;

	if ((this->etat_boucle == SENDING) & (this->valeur_boucle==this->valeur_fin))
		this->etat_boucle = FINISHED;
	
	if ((this->etat_boucle == FINISHED) & (this->condition_fin))
		this->etat_boucle = IDLE;
}

bool boucle::StartBoucle()
{
	if (this->etat_boucle == IDLE)
	{
		this->etat_boucle = SENDING;
		return true;
	}
	else
	{
		return false;
	}
}


boucle boucle1(0, 20, false);
boucle boucle2(0, 20, false);
boucle boucle3(0, 20, false);
long unsigned int millis0;
long unsigned int millis1;



void setup()
{
	lcd.begin(16, 2);
	pinMode(input_pin, INPUT);
	millis0=millis();
	millis1=millis();
}

void loop()
{
	// routine
	boucle1.Refresh(boucle2.GetStateBoucle() == 1); // fin de 1 quand 2 compte
	boucle2.Refresh(boucle3.GetStateBoucle() == 1); // fin de 2 quand 3 compte
	boucle3.Refresh(boucle1.GetStateBoucle() == 1); // fin de 3 quand 1 compte
	
	
	if (millis0+10000<millis()) // toutes les 19 sec, début de 1
	{
		if(boucle1.StartBoucle())
		{
			millis0 = millis();
		}
	}
	
	if (boucle1.GetStateBoucle() == FINISHED) // quand 1 fini, début de 2
	{
		if(boucle2.StartBoucle())
		{
			millis1 = millis();
		}
	}
	
	if (boucle2.GetStateBoucle() == FINISHED) // quand input_pin, début de 3 
		boucle3.StartBoucle();
		
	lcd.setCursor(0, 0); // 1ere ligne
	lcd.print(boucle1.GetStateBoucle());
	lcd.print(":");
	lcd.print(boucle1.GetValueBoucle());
	lcd.print(" ");
	lcd.print(boucle2.GetStateBoucle());
	lcd.print(":");
	lcd.print(boucle2.GetValueBoucle());
	lcd.print(" ");
	lcd.print(boucle3.GetStateBoucle());
	lcd.print(":");
	lcd.print(boucle3.GetValueBoucle());
	lcd.print(" ");
	lcd.setCursor(0, 1); // 2eme ligne
	delay(100);
}
