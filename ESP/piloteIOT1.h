#ifndef PILOTEIOT1_H
#define PILOTEIOT1_H

//MODULE: piloteIOT1
//DESCRIPTION: pour commander la sortie IOT1
//HISTORIQUE:
// 2018-09-08, Yves Roy, creation

//DEFINITIONS REQUISES PAR LE MODULE:
//Dependances materielles
//(copiez et adaptez ce qui suit dans "main.h")
//#define PILOTEIOT1_SORTIE        P3_bit.P35_T1 

//Dependances logicielles
//(copiez et adaptez ce qui suit dans "main.h")
// pas de d�pendances logicielles

//INFORMATION PUBLIQUE:
//Definitions publiques:
//pas de definitions publiques

//Fonctions publiques:
void piloteIOT1_initialise(void);
void piloteIOT1_metLaSortieA(unsigned char Valeur);

//Variables publiques:
// pas de variables publiques

#endif
