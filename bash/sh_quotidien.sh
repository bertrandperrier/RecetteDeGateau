#!/bin/bash
sh /home/$USER/linux/script/lecteur_fichier.sh
rm /home/$USER/linux/script/liste_id_email ## effacement du journal des id des messages d'exim
sudo ls /var/spool/exim4/input >> /home/$USER/linux/script/liste_id_email ## journalise les id des messages d'exim
message=$(ls -lh /home/$USER/linux/script/liste_id_email | cut -d " " -f5)
if [ $message -eq 0 ]
then
	sudo apt update && sudo apt upgrade && sudo apt dist-upgrade && sudo apt autoremove && apt list --upgradable
	sh /home/$USER/linux/script/grep_updatedns.sh
	sh /home/$USER/linux/script/voir_jour.sh
	geany /home/$USER/Documents/a\ faire.txt
fi
