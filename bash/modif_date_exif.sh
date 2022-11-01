#!/bin/bash
# Gestion des nom de fichier contenant des espaces
IFS=$'\n'
# met à jour la date de modification des jpg du dossier courant à partir de la date de prise de vue d'exif
# envoie de la liste des fichier dans une variable database
database=$(find -name "*.jpg")


# boucle utilisant la variable database
	

for file in `find -name "*.jpg"`; do	
	test_ok=$(exif --tag="Date et heure" "$file")
	if [ -n "$test_ok" ]
		then
			echo 'Traitement de'
			echo $file
			touch -d "$(exif --tag="Date et heure" "$file" | grep Value | sed "s/^.\{9\}//g" | sed "s/\:/\-/"| sed "s/\:/\-/")" "$file"
	fi
done


database=$(find -name "*.JPG")


# boucle utilisant la variable database
	

for file in `find -name "*.JPG"`; do	
	test_ok=$(exif --tag="Date et heure" "$file")
	if [ -n "$test_ok" ]
		then
			echo 'Traitement de'
			echo $file
			touch -d "$(exif --tag="Date et heure" "$file" | grep Value | sed "s/^.\{9\}//g" | sed "s/\:/\-/"| sed "s/\:/\-/")" "$file"
	fi
done

# Gestion des nom de fichier contenant des espaces
IFS=$' \t\n'

