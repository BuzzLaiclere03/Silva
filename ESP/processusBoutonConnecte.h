#ifndef PROCESSUSBOUTONCONNECTE_H
#define PROCESSUSBOUTONCONNECTE_H

//MODULE: processusBoutonConnecte
//DESCRIPTION: implemente la gestion des messages que s'echangent l'ensemble
//de developpement Dallas et un ensemble STM32F4-DISCO programme avec le logiciel
//247-637 S-0000. Un octet dont la valeur correspond a l'etat d'un bouton est
//transmis au STM32 a chaque fois qu'un octet est recu. Le processus utilise
//un pointeur de fonctions qui est fourni par le module serviceBaseDeTemps.

//HISTORIQUE:
// 2018-09-24, Yves Roy, creation

//DEFINITIONS REQUISES PAR LE MODULE:
//Dependances materielles
//(copiez et adaptez ce qui suit dans "main.h")
//pas de dependances materielles

//Dependances logicielles
//(copiez et adaptez ce qui suit dans "main.h")
//#define PROCESSUSBOUTONCONNECTE_PHASE 0

//INFORMATION PUBLIQUE:
//Definitions publiques:

typedef struct
{
  unsigned char etatDuModule;  
} PROCESSUSBOUTONCONNECTE;

//Fonctions publiques:
void processusBoutonConnecte_initialise(void);

//Variables publiques:
extern PROCESSUSBOUTONCONNECTE processusBoutonConnecte;

#endif
