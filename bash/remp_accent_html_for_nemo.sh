#!/bin/bash
## Script réalisé et mis à jour par Bertrand Perrier le 11/01/09
## ajout des majuscules le 13/04/23
## ajout oe collé le 25/08/23

# Ce script permet de remplacé les caractère accentué par le codage html
# par exemple é devient eacute;

# Ce scripts est à mettre pour :
#    - Caja (Mate) dans ~/.config/caja/scripts
#    - Nautilus (Gnome/Unity) dans ~/.local/share/nautilus/scripts/ $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
#    - Némo (Cinnamon) dans ~/.local/share/nemo/scripts/ $NEMO_SCRIPT_SELECTED_FILE_PATHS

zenity --info --text=$NEMO_SCRIPT_SELECTED_FILE_PATHS
zenity --info --text="Veuillez attendre l'avertissement de fin du traitement du fichier\n valider pour commencer le traitement" --title="remp_accent_html.sh"
cp $NEMO_SCRIPT_SELECTED_FILE_PATHS /tmp/test_accent.php
sed -e "s/é/\&eacute;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/É/\&Eacute;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/è/\&egrave;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/È/\&Egrave;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ê/\&ecirc;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ê/\&Ecirc;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/à/\&agrave;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/À/\&Agrave;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/â/\&acirc;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Â/\&Acirc;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/œ/\&oelig;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Œ/\&OElig;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS

zenity --info --text="Le fichier à été modifié et enregistré avec succés" --title="remp_accent_html.sh"

