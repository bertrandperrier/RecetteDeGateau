#!/bin/bash
# Ce script copie les meta données d'un jpg sur un autre
# créé le 12/07/2025

echo $1
echo $2

# si $1 mais pas $2 supression meta données
if [ "$1" = "-d" ] && [ -f "$2" ]
then
	read -p "Supression meta données (o/N) ? " confirm
	if [ "$confirm" = "O" ] || [ "$confirm" = "o" ]
	then
		exiv2 -d a $1
		exit 1
	else
		echo "Action annulée"
		exit 0
	fi
fi

# un des deux fichiers n'éxistent pas
if [ ! -f "$1" ] || [ ! -f "$2" ]
then
	echo "cp_exif_jpg_to_jpg.sh: saisissez « cp_exif_jpg_to_jpg.sh <jpg_sans_meta_donnée> <jpg_avec_meta_données_à_copier> »"
	echo "Ou saisissez « cp_exif_jpg_to_jpg.sh -d <jpg_avec_meta_données_à_supprimer> »"
	exit 1
fi

# les deux fichiers existent
if [ -f "$1" ] && [ -f "$2" ]
then
	echo "les deux fichiers existent"
else
	echo "cp_exif_jpg_to_jpg.sh: saisissez « cp_exif_jpg_to_jpg.sh <jpg_sans_meta_donnée> <jpg_avec_meta_données_à_copier> »"
	echo "Ou saisissez « cp_exif_jpg_to_jpg.sh -d <jpg_avec_meta_données_à_supprimer> »"
	exit 1
fi



# retrait de l'extension dans le nom du fichier
IMG_without_exif="${1%.*}"
IMG_with_exif="${2%.*}"

# voir les metadonnées
exiv2 $IMG_without_exif.JPG

# exportation des metadonnées
exiv2 -f ex $IMG_with_exif.JPG $IMG_with_exif.exv

# mettre au nom du jpg a importer
mv $IMG_with_exif.exv $IMG_without_exif.exv

# importation des metadonnées
exiv2 in $IMG_without_exif.exv $IMG_without_exif.JPG

# voir les metadonnées
exiv2 $IMG_without_exif.JPG

# suppression du fichier temporaire .exv
if [ -f "$IMG_without_exif.exv" ]
then
	mv $IMG_without_exif.exv /home/$USER/.local/share/Trash/files/
fi
