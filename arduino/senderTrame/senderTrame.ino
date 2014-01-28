// /dev/ttyACM0
const int pinData = 8;
const int speedDial = 1;
bool trame[] = {0,0,0,0,0,0,0,0};

void setup()
  {
  pinMode(pinData, OUTPUT);
  }

void loop()
  {
  for (int val_bin=0;val_bin<=bit(15);val_bin++)  // de 0 à 11111111
    {
    for (int num_bit=0;num_bit<=15;num_bit++) // de 0 à 15 bit
      {
      trame[num_bit] = HIGH && (val_bin & bit(num_bit)); // bit -> 2pn  //7-
      }
    digitalWrite(pinData, HIGH); // bit depart
    delay(8*speedDial);
    digitalWrite(pinData, LOW); // bit depart
    for (int i=0;i<=7;i++)
      {
      digitalWrite(pinData,trame[i]);
      delay(10*speedDial);
      }
    digitalWrite(pinData, LOW); // mise à zéro de la pin data
    delay(20*speedDial);
    delay(200); // durée affichage
    }
  delay(1000); // attente avant remise à zero
  }
    
