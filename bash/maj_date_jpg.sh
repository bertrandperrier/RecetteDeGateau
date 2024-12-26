#!/bin/sh
# 18/02/2024
# ce script modifie la date "de modification" par la "date de la prise" Exif "Image timestamp"
# 16/06/2024 fichier a placer dans /home/$USER/.local/share/nemo/scripts/ ce qui fera apparaitre le menu clic-droit>Script>maj_date_jpg
# test si argument
notify-send "Traitement en cours..."

echo $NEMO_SCRIPT_SELECTED_FILE_PATHS
if [ -z "$1" ]; then
	echo "par d argument"
else
	echo "argument"
	$NEMO_SCRIPT_SELECTED_FILE_PATHS = $1
fi
for selected_uri in $NEMO_SCRIPT_SELECTED_FILE_PATHS; do
	echo "fichier en cours : " $selected_uri
	if ! [ $(mimetype -b "$selected_uri") = "image/jpeg" ]
	then
		notify-send "Un fichier n'est pas au format jpg"
		exit 0
	else
		time=$(exiv2 $selected_uri  | grep timestamp | cut -d " " -f5)
		echo "time" $time
		date=$(exiv2 $selected_uri  | grep timestamp | cut -d " " -f4)
		echo "date" $date
		if [[ -z "$time" ]]; then
			echo "date non renseigné"
		else
			date=$(echo $date | sed 's/:/-/g')
			datetime="${date} ${time}"
			touch -d "${datetime}" $selected_uri
			echo "date de modification du fichier modifiée"
		fi
	fi
done
notify-send "Fin de traitement"

