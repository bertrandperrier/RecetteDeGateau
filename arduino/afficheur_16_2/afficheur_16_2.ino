#include <LiquidCrystal.h>
#include <stdio.h>

LiquidCrystal lcd(7, 6, 5, 4, 3, 2);

char buf;
int i=0;
bool buf_ok;


void setup()
  {
   lcd.begin(16, 2);
   lcd.print("HaumDuino");
   affiche("24hdc",11, 0);
  }

void loop()
  {
/*
  affiche(" #",i, 1);
  affiche("# ",14-i, 1);

  i=i+1;
  if (i==7)
    {
     i=0;
    }
    */
  char temp[20];
  sprintf(temp, "%d\",millis()/1000);
  

  //affiche(temp, 1,1);

  delay(100);
  }

void affiche(char *txt, int colonne, int ligne)
  {
  lcd.setCursor(colonne, ligne);
  lcd.print(txt);
  }
