#!/bin/bash
## Script réalisé et mis à jour par Bertrand Perrier le 11/01/09

# Ce script permet de remplacé les caractère accentué par le codage html
# par exemple é devient eacute;
zenity --info --text="Veuillez attendre l'avertissement de fin du traitement du fichier\n valider pour commencer le traitement" --title="remp_accent_html.sh"
cp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS /tmp/test_accent.php
sed -e "s/é/\&eacute;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/è/\&egrave;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ê/\&ecirc;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/à/\&agrave;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/â/\&acirc;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
##gedit $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
zenity --info --text="Le fichier à été modifié et enregistré avec succés" --title="remp_accent_html.sh"

