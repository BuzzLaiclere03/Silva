//processusClignotant:
//Historique: 
// 2018-09-24, Yves Roy, creation

//INCLUSIONS
#include "main.h"
#include "xserviceBaseDeTemps.h"
#include "interfaceT1.h"
#include "processusClignotant.h"

//Definitions privees
#define PROCESSUSCLIGNOTANT_COMPTE_POUR_ALLUME (\
  PROCESSUSCLIGNOTANT_TEMPS_ALLUME_EN_MS * SERVICEBASEDETEMPS_FREQUENCE_EN_HZ \
  /1000.0)

#define PROCESSUSCLIGNOTANT_COMPTE_PAR_PERIODE  (\
  PROCESSUSCLIGNOTANT_PERIODE_EN_MS * SERVICEBASEDETEMPS_FREQUENCE_EN_HZ \
  /1000.0)
    
//Declarations de fonctions privees:
void processusClignotant_gere(void);

//Definitions de variables privees:
unsigned int processusClignotant_compteur;
//pas de variables privees

//Definitions de fonctions privees:
void processusClignotant_gere(void)
{
  processusClignotant_compteur++;
  if (processusClignotant_compteur < PROCESSUSCLIGNOTANT_COMPTE_POUR_ALLUME)
  {
    interfaceT1_allume();
    return;
  }
  if (processusClignotant_compteur < PROCESSUSCLIGNOTANT_COMPTE_PAR_PERIODE)
  {
    interfaceT1_eteint();
    return;
  }
  processusClignotant_compteur = 0;
}

//Definitions de variables publiques:
//pas de variables publiques

//Definitions de fonctions publiques:
void processusClignotant_initialise(void)
{
  processusClignotant_compteur = 0;
  serviceBaseDeTemps_execute[PROCESSUSCLIGNOTANT_PHASE] =
      processusClignotant_gere;
}
