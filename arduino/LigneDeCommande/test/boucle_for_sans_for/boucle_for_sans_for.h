typedef enum { IDLE, SENDING, FINISHED } boucle_state;

class boucle
{
private:
	int valeur_boucle;
	int valeur_debut;
	int valeur_fin;
	bool condition_fin;
	volatile boucle_state etat_boucle;
	
public:
	boucle(int, int, bool);
	
	boucle_state GetStateBoucle();
	int GetValueBoucle();
	char* GetStateBoucleTxt();
	
	void Refresh(bool );
	bool StartBoucle();
};


