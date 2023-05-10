#ifndef PILOTEUART1_H
#define PILOTEUART1_H

//MODULE: piloteUART1
//DESCRIPTION: pour utiliser le UART1 avec Timer1 en mode 2
//HISTORIQUE:
// 2018-09-08, Yves Roy, creation

//DEFINITIONS REQUISES PAR LE MODULE:
//Dependances materielle
//pas de d�pendances mat�rielles

//Dependances logicielles
//(copiez et adaptez ce qui suit dans "main.h")
//pas de d�pendances logicielles

//INFORMATION PUBLIQUE:
//Definitions publiques:
#define PILOTEUART1_DISPONIBLE  1
#define PILOTEUART1_PAS_DISPONIBLE 0
#define PILOTEUART1_TRANSMIS 0
#define PILOTEUART1_PAS_TRANSMIS 1

//Fonctions publiques:
void piloteUART1_initialise(void);
unsigned char piloteUART1_octetDisponible(void);
unsigned char piloteUART1_octetTransmis(void);
unsigned char piloteUART1_litUnOctetRecu(void);
void piloteUART1_transmet(unsigned char Octet);

//Variables publiques:
//pas de variables publiques

#endif
