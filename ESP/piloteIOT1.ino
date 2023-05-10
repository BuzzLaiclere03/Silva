//piloteIOT1:
//Historique: 
// 2018-09-08, Yves Roy, creation

//INCLUSIONS
#include "main.h"
#include "piloteIOT1.h"

//Definitions privees
//pas de d�finitions privees

//Declarations de fonctions privees:
//pas de fonction privees

//Definitions de variables privees:
//pas de variables privees

//Definitions de fonctions privees:
//pas de fonctions privees

//Definitions de variables publiques:
// pas de variables publiques

//Definitions de fonctions publiques:
void piloteIOT1_metLaSortieA(unsigned char Valeur)
{
  digitalWrite(PILOTEIOT1_BROCHE, Valeur);
}

void piloteIOT1_initialise(void)
{
  pinMode(PILOTEIOT1_BROCHE, OUTPUT);
}




