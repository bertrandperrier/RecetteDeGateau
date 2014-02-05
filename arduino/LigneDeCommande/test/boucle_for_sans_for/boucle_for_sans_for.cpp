// /dev/ttyUSB0
// à mettre dans une class
#include <Arduino.h>
#include <LiquidCrystal.h>
#include "boucle_for_sans_for.h"

LiquidCrystal lcd(13, 12, 11, 10, 9, 8);


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
		return "IDLE    ";
	if (this->etat_boucle == 1)
		return "SENDING ";
	if (this->etat_boucle == 2)
		return "FINISHED";
	return "ERROR   ";
}

void boucle::Refresh(bool condition_fin = true)
{
	this->condition_fin = condition_fin;
	
	if (this->etat_boucle == IDLE)
		this->valeur_boucle=valeur_debut;
		
	if (this->etat_boucle == SENDING & this->valeur_boucle<this->valeur_fin)
		this->valeur_boucle++;

	if (this->etat_boucle == SENDING & this->valeur_boucle==this->valeur_fin)
		this->etat_boucle = FINISHED;
	
	if (this->etat_boucle == FINISHED & this->condition_fin)
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


boucle boucle1(5, 45, true);
boucle boucle2(0, 10, true);
long unsigned int millis0;
long unsigned int millis1;



void setup()
{
	lcd.begin(16, 2);
	millis0=millis();
	millis1=millis();
}

void loop()
{
	// routine
	boucle1.Refresh(true);
	boucle2.Refresh(true);
	if (millis0+5000<millis()) // lancement de la boucle 1 toute les 5 sec
	{
		if(boucle1.StartBoucle())
		{
			millis0 = millis();
		}
	}
	
	if (millis1+2000<millis()) // lancement de la boucle 2 toute les 2 sec
	{
		if(boucle2.StartBoucle())
		{
			millis1 = millis();
		}
	}
	
	lcd.setCursor(0, 0); // 1ere ligne
	lcd.print(boucle1.GetStateBoucle());
	lcd.print(":");
	lcd.print(boucle1.GetStateBoucleTxt());
	lcd.print(boucle1.GetValueBoucle());
	lcd.print(" ");
	lcd.setCursor(0, 1); // 2eme ligne
	lcd.print(boucle2.GetStateBoucle());
	lcd.print(":");
	lcd.print(boucle2.GetStateBoucleTxt());
	lcd.print(boucle2.GetValueBoucle());
	lcd.print(" ");
	delay(100);
}
