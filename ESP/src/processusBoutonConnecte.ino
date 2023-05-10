//processusBoutonConnecte:
//Historique: 
// 2018-09-08, Yves Roy, creation

//INCLUSIONS
#include "main.h"
#include "xserviceBaseDeTemps.h"
#include "interfaceB1.h"
//#include "interfaceS0000.h"
#include "serviceProtocole637.h"
#include "processusBoutonConnecte.h"

//Definitions privees
//pas de d�finitions privees

//Declarations de fonctions privees:
void processusBoutonConnecte_gere(void);

//Definitions de variables privees:
//pas de variables privees

//Definitions de fonctions privees:
//pas de fonctions privees

//Definitions de variables publiques:
PROCESSUSBOUTONCONNECTE processusBoutonConnecte;
unsigned char processusBoutonConnecte_tabABoutonRelache[3] = {'0', '0', '$'};
unsigned char processusBoutonConnecte_tabABoutonAppuye[3] = {'1', '$', '1'};

//Definitions de fonctions publiques:
void processusBoutonConnecte_gere(void)
{
  if (serviceProtocole637.etatDuModuleDeReception == MODULE_PAS_EN_FONCTION)
  {
    return;
  }
  processusBoutonConnecte.etatDuModule = MODULE_EN_FONCTION;
  
  if (serviceProtocole637.information == INFORMATION_DISPONIBLE)
  {
    serviceProtocole637.information = INFORMATION_TRAITEE;
    
    if(serviceProtocole637.octetsRecus[0] == 1 &&
        serviceProtocole637.octetsRecus[1] == 2 &&
          serviceProtocole637.octetsRecus[2] == 3 &&
            serviceProtocole637.octetsRecus[3] == 4)
    {
        for (int i = 0; i < 4; i++)
        {
          serviceProtocole637.octetsATransmettre[i] = 
            serviceProtocole637.octetsRecus[i] * 2;
        }

      serviceProtocole637.nombreATransmettre = 4;
      serviceProtocole637.requete = REQUETE_ACTIVE;
    }
  }
}

void processusBoutonConnecte_initialise(void)
{
  processusBoutonConnecte.etatDuModule = MODULE_PAS_EN_FONCTION;
  serviceBaseDeTemps_execute[PROCESSUSBOUTONCONNECTE_PHASE] =
      processusBoutonConnecte_gere;
}
