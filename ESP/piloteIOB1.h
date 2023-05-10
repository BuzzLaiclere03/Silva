#ifndef PILOTEIOB1_H
#define PILOTEIOB1_H

//MODULE: piloteIOB1
//DESCRIPTION: pour lire l'entree IOB1
//HISTORIQUE:
// 2018-09-08, Yves Roy, creation

//DEFINITIONS REQUISES PAR LE MODULE:
//Dependances materielles
//(copiez et adaptez ce qui suit dans "main.h")
//#define PILOTEIOB1_ENTREE P3_bit.P32_INT0  

//Dependances logicielles
//(copiez et adaptez ce qui suit dans "main.h")
//pas de d�pendances logicielles

//INFORMATION PUBLIQUE:
//Definitions publiques:
//pas de definitions publiques

//Fonctions publiques:
void piloteIOB1_initialise(void);
unsigned char piloteIOB1_litLEntree(void);

//Variables publiques:
//pas de variables publiques

#endif
