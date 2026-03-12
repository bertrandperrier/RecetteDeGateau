#!/bin/bash
lsusb_sony=$(lsusb | grep Sony) # resultat de lsusb grep Sony
size_of_lsusb_sony=${#lsusb_sony} # taille du resultat

if [  $size_of_lsusb_sony -ne 0 ] # si la clef usb Sony est trouvé
then
	echo "Périphérique usb Sony trouvé"
	ls_media=$(ls /media/$USER/ | grep SSD128FAT32) # resultat de ls media
	size_of_ls_media=${#ls_media} # taille de ls_media
	if [ $size_of_ls_media -ne 0 ] # si la clef usb Sony est monté
	then
		read -p "Commencer la sauvegarde (o/N) ? " reponse # demande confirmation
		if [ $reponse = 'o' ]
		then
			echo "##########################"
			echo "# début de la sauvegarde #"
			echo "#####   site web    ######"
			echo "##########################"
			rsync -a --delete --exclude=".*/" --exclude="/home/$USER/snap/" /home/$USER/ /media/$USER/SSD128FAT32/backup_pc_portable/ 
			echo "##########################"
			echo "### fin de la sauvegarde #"
			echo "##########################"
		else
			echo "sauvegarde annulé"
		fi
	else
		echo "Périphérique non monté"
	fi
else
	echo "Périphérique usb Sony non trouvé"
fi



#rsync -vrltpgo

# -a = -rlptgoD
# -p preserve permission
# -g preserve group
# -o preserve owner
# -v verbose
# -r recursive
# -l copy symlinks as symlinks
# -t preserve modification times
# --delete : efface sur la cible les fichiers qui ont disparus du répertoire de départ. 
# -D same as --devices --specials
# --devices preserve device files (super-user only)
# --specials preserve special files


# rsync source destination/ copie le dossier
# rsync source/ destination/ copie le contenu du dossier


