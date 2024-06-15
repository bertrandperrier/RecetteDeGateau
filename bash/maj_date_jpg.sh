#!/bin/bash
# 18/02/2024
# ce script modifie la date "de mofication" par la "date de la prise" Exif "Image timestamp"
# 16/06/2024 fichier a placer dans /home/$USER/.local/share/nemo/scripts/ ce qui fera apparaitre le menu clic-droit>Script>maj_date_jpg

notify-send "Traitement en cours..."

for selected_uri in $NEMO_SCRIPT_SELECTED_FILE_PATHS; do
	if ! [ $(mimetype -b "$selected_uri") = "image/jpeg" ]
	then
		notify-send "Un fichier n'est pas au format jpg"
		exit 0
	else
		time=$(exiv2 $selected_uri  | grep timestamp | cut -d " " -f5)
		date=$(exiv2 $selected_uri  | grep timestamp | cut -d " " -f4)
		date=$(echo $date | sed 's/:/-/g')
		datetime="${date} ${time}"
		touch -d "${datetime}" $selected_uri
	fi
done
notify-send "date de modification du fichier modifiée"

