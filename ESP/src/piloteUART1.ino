//piloteUART1:
//Historique: 
// 2018-09-08, Yves Roy, creation

//INCLUSIONS
#include "main.h"
#include "piloteUART1.h"

//Definitions privees
//pas de definitions privees

//Declarations de fonctions privees:
//pas de fonctions privees

//Definitions de variables privees:
//pas de variables privees

//Definitions de fonctions privees:
//pas de fonctions privees

//Definitions de variables publiques:
// pas de variables publiques

//Definitions de fonctions publiques:
// pas de definitions publiques

//Fonctions publiques:
unsigned char piloteUART1_octetDisponible(void)
{
  return Serial2.available();
}

unsigned char piloteUART1_octetTransmis(void)
{
  return Serial2.availableForWrite();
}

unsigned char piloteUART1_litUnOctetRecu(void)
{
  return Serial2.read();
}
void piloteUART1_transmet(unsigned char Octet)
{
  Serial2.write(Octet);
}

void piloteUART1_initialise(void)
{
  Serial2.begin(19200);
}



