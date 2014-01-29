// /dev/ttyACM0
#include "/home/bertrand/github/RecetteDeGateau/arduino/libraries/SenderReceiverTrame.h"

void setup()
  {
  pinMode(pinData, OUTPUT);
  }

void loop()
  {

  /* demo trame 8 bit de 0 à 11111111
  for (int val_bin=0;val_bin<=bit(15);val_bin++)  // de 0 à 11111111
    {
    for (int num_bit=0;num_bit<=15;num_bit++) // de 0 à 15 bit
      {
      trame[num_bit] = HIGH && (val_bin & bit(num_bit)); // bit -> 2pn  //7-
      }
  */
  trame[0] = true; // bit start
  // no carte
  trame[1] = false;
  trame[2] = false;
  trame[3] = false;
  trame[4] = true;
  trame[5] = false;
  trame[6] = true;
  trame[7] = true;

  // bits de donnees
  //trame[8] = true;
  //trame[9] = true;
  
  for (int bits_donnees=0;bits_donnees<=3;bits_donnees++)  // de 00 à 11(3)
    {
    trame[8] = HIGH && (bits_donnees & bit(0));
    trame[9] = HIGH && (bits_donnees & bit(1));
    
    digitalWrite(pinData, HIGH); // bit depart
    delay(8*speedDial);
    digitalWrite(pinData, LOW); // bit depart
    for (int i=1;i<=9;i++)
      {
      digitalWrite(pinData,trame[i]);
      delay(10*speedDial);
      }
    digitalWrite(pinData, LOW); // mise à zéro de la pin data
    delay(700); // durée affichage
    }
  delay(100); // attente avant remise à zero
  }
    
