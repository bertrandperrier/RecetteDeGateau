#!/bin/bash
rm /home/$USER/linux/script/liste_id_email ## effacement du journal des id des messages d'exim
sudo ls /var/spool/exim4/input >> /home/$USER/linux/script/liste_id_email ## journalise les id des messages d'exim
taille_fichier=$(ls -lh /home/$USER/linux/script/liste_id_email | cut -d " " -f5) ## calcul taille du fichier
if [ $taille_fichier  -ne 0 ] ## si la taille est sup à zero = presence de message
then
	nb_mesg=$taille_fichier
	id1_email=$(head -n 1 /home/$USER/linux/script/liste_id_email) ## recupere la premiere ligne
	id1_email=${id1_email%??} ## enleve les deux derniers caratères
	sudo exim -Mvb $id1_email ## affiche le contenue du message
	read -p "Effacer email $id_email [o/N] ? " reponse
	if [ "$reponse" = "o" ]
	then
		sudo exim -Mrm $id1_email # effacement du message
	else
		echo "annulé"
	fi
	##echo $nb_mesg" messages / 38"
else
	echo "pas de message"
fi
