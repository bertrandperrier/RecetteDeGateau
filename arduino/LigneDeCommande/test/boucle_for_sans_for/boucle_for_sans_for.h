#ifndef MACLASSE_H
#define MACLASSE_H

typedef enum { IDLE, SENDING, FINISHED } boucle_state;

class boucle
{
public:
	int valeur_boucle;
	int valeur_debut;
	int valeur_fin;
	bool condition_fin;
	volatile boucle_state etat_boucle;
	boucle(int, int, bool);
	boucle_state GetStateBoucle();
	int GetValueBoucle();
	void Refresh(bool );
	bool StartBoucle();
	char* GetStateBoucleTxt();
};
 
#endif


