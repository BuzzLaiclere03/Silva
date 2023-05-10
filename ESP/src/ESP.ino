//247-527Atelier3a: programme de depart pour faire operer le ESP32 en mode cooperatif
//Historique:
// 2022-10-18, Yves Roy, creation a partir du programme 247-527Atelier3a

//INCLUSIONS
#include "main.h"
#include "piloteIOT1.h"
#include "piloteIOB1.h"
#include "piloteUART1.h"
#include "serviceBaseDeTemps.h"
#include "serviceProtocole637.h"
#include "interfaceB1.h"
#include "interfaceT1.h"
#include "processusBoutonConnecte.h"
#include "processusClignotant.h"
#include "serviceTaskServer.h"


//Definitions privees
//pas de definitions privees

//Declarations de fonctions privees:
void main_initialise(void);

//Definitions de variables privees:
//pas de variables privees

//Definitions de fonctions privees:
void main_initialise(void)
{
  piloteIOB1_initialise();
  piloteIOT1_initialise(); 
  piloteUART1_initialise();
  serviceTaskServer_initialise();
  serviceBaseDeTemps_initialise();
  serviceProtocole637_initialise();
  interfaceB1_initialise();
  interfaceT1_initialise();
  processusClignotant_initialise();
  processusBoutonConnecte_initialise();
}

void setup(void) 
{
  main_initialise();
  serviceTaskServer_DemarreLesTachesALaTouteFinDeSetup();
}


void loop(void) 
{
  serviceTaskServer_gestion.execute();
  serviceBaseDeTemps_gereDansLoop();   
}

//Definitions de variables publiques:
//pas de variables publiques

//Definitions de fonctions publiques:
void neFaitRien(void)
{
}
