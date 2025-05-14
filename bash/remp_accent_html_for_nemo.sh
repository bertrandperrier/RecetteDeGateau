#!/bin/bash
## Script réalisé et mis à jour par Bertrand Perrier le 11/01/09
## ajout des majuscules le 13/04/23
## ajout oe collé le 25/08/23
## ajout de 50 caractères le 07/01/25

# Ce script permet de remplacer les caractère accentué par le codage html
# par exemple é devient eacute;


zenity --info --text=$NEMO_SCRIPT_SELECTED_FILE_PATHS
zenity --info --text="Veuillez attendre l'avertissement de fin du traitement du fichier\n valider pour commencer le traitement" --title="remp_accent_html.sh"
cp $NEMO_SCRIPT_SELECTED_FILE_PATHS /tmp/backup.php

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
sed -e "s/á/\&aacute;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Á/\&Aacute;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ã/\&atilde;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ã/\&Atilde;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ä/\&auml;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/Ä/\&Auml;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/å/\&aring;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Å/\&Aring;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/æ/\&aelig;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Æ/\&AElig;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/ë/\&euml;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ë/\&Euml;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/ì/\&igrave;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ì/\&Igrave;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/í/\&iacute;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Í/\&Iacute;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/î/\&icirc;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Î/\&Icirc;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/ï/\&iuml;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ï/\&Iuml;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/ò/\&ograve;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ò/\&Ograve;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ó/\&oacute;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ó/\&Oacute;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ô/\&ocirc;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ô/\&Ocirc;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/õ/\&otilde;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Õ/\&Otilde;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ö/\&ouml;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ö/\&Ouml;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ø/\&oslash;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ø/\&Oslash;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ù/\&ugrave;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ù/\&Ugrave;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ú/\&uacute;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ú/\&Uacute;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/û/\&ucirc;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Û/\&Ucirc;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ü/\&uuml;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ü/\&Uuml;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ñ/\&ntilde;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ñ/\&Ntilde;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ç/\&ccedil;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ç/\&Ccedil;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ý/\&yacute;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ý/\&Yacute;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ß/\&szlig;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/«/\&laquo;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/»/\&raquo;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/§/\&para;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/©/\&copy;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/€/\&euro;/g" $NEMO_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NEMO_SCRIPT_SELECTED_FILE_PATHS

zenity --info --text="Le fichier à été modifié et enregistré avec succés" --title="remp_accent_html.sh"

