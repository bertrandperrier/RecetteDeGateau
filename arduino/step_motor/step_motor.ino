/* Contrôle Moteur pas à pas
   Un tour dans un sens puis un tour dans l’autre sens
*/

#include <Stepper.h>

// définit le nombre de pas pour un tour complet
const int nbr_pas = 50; 
                                 
// initialise la librairie sur les broches 8, 9, 10 et 11
Stepper mon_moteur(nbr_pas, 8, 9, 10, 11);           
  int i=1;
void setup()
{
  // définit la vitesse de rotation à 60 tr/min
  mon_moteur.setSpeed(5); //180
  pinMode(2, INPUT);
}

void loop()
{
  
  if (!digitalRead(2))
    {
    mon_moteur.setSpeed(i);
    }
    else
    {
    mon_moteur.setSpeed(180);
    }
  mon_moteur.step(nbr_pas/10);
  i=i+1;
  if (i==180)
    {
     i=1;
    }
  // delay(200);
 
  // tour dans l’autre direction
  // mon_moteur.setSpeed(180);
  // mon_moteur.step(-nbr_pas/10);
  // delay(500);
}
