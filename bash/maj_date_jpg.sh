#!/bin/bash
# 18/02/2024
# ce script modifie la date "de mofication" par la "date de la prise" Exif "Image timestamp"
if [ "$1" = "" ] ; then
	echo -n "saisir le nom du fichier
"
	exit 0
fi

if ! [ -f "$1" ];then
	echo "Le fichier n'existe pas !";
	exit 0
fi

filename=$1
time=$(exiv2 $filename  | grep timestamp | cut -d " " -f5)
date=$(exiv2 $filename  | grep timestamp | cut -d " " -f4)
date=$(echo $date | sed 's/:/-/g')
datetime="${date} ${time}"
touch -d "${datetime}" $filename
echo "date de modification du fichier modifiée"

