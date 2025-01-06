#!/bin/bash
if [ $USER != "root" ]
then
	if [ -e $1 ]
	then
		read -p "mettre à la poubelle (o/N) ?" reponse
		if [ $reponse = "o" ]
		then
			mv $1 /home/$USER/.local/share/Trash/files/
			echo "${1} mis à la poubelle"
		else
			echo "annulé"
		fi
	else
		echo "le fichier n'existe pas"
	fi
else
	echo "ne pas utiliser en root"
fi
