// /dev/ttyACM0
const int pinStart = 9;
const int pinData = 8;

const int speedDial = 1;

bool trame[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};

void setup()
  {
  pinMode(pinStart, OUTPUT);
  pinMode(pinData, OUTPUT);    
  }

void loop()
  {
for (int val_bin=0;val_bin<=bit(15);val_bin++)  // de 0 à bit(15)
  {
  for (int num_bit=0;num_bit<=15;num_bit++) // de 0 à 15 bit
    {
    trame[7-num_bit] = HIGH && (val_bin & bit(num_bit)); // bit -> 2pn  
    }
  digitalWrite(pinStart, HIGH); // bit depart
  delay(8*speedDial);
  digitalWrite(pinStart, LOW); // bit depart
  for (int i=0;i<=7;i++)
    {
    digitalWrite(pinData,trame[i]);
    delay(10*speedDial);
    }
  digitalWrite(pinData, LOW);
  delay(20*speedDial);
  delay(200);
  }
  delay(1000);
}
    
