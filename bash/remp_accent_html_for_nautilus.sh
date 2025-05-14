#!/bin/bash
## Script réalisé et mis à jour par Bertrand Perrier le 11/01/09
## ajout des majuscules le 13/04/23
## ajout oe collé le 25/08/23
## ajout de 50 caractères le 07/01/25

# Ce script permet de remplacer les caractère accentué par le codage html
# par exemple é devient eacute;


zenity --info --text=$NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
zenity --info --text="Veuillez attendre l'avertissement de fin du traitement du fichier\n valider pour commencer le traitement" --title="remp_accent_html.sh"
cp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS /tmp/backup.php

sed -e "s/é/\&eacute;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/É/\&Eacute;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/è/\&egrave;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/È/\&Egrave;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ê/\&ecirc;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ê/\&Ecirc;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/à/\&agrave;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/À/\&Agrave;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/â/\&acirc;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Â/\&Acirc;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/œ/\&oelig;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Œ/\&OElig;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/á/\&aacute;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Á/\&Aacute;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ã/\&atilde;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ã/\&Atilde;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ä/\&auml;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/Ä/\&Auml;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/å/\&aring;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Å/\&Aring;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/æ/\&aelig;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Æ/\&AElig;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/ë/\&euml;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ë/\&Euml;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/ì/\&igrave;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ì/\&Igrave;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/í/\&iacute;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Í/\&Iacute;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/î/\&icirc;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Î/\&Icirc;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/ï/\&iuml;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ï/\&Iuml;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/ò/\&ograve;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ò/\&Ograve;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ó/\&oacute;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ó/\&Oacute;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ô/\&ocirc;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ô/\&Ocirc;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/õ/\&otilde;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Õ/\&Otilde;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ö/\&ouml;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ö/\&Ouml;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ø/\&oslash;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ø/\&Oslash;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ù/\&ugrave;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ù/\&Ugrave;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ú/\&uacute;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ú/\&Uacute;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/û/\&ucirc;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Û/\&Ucirc;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ü/\&uuml;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ü/\&Uuml;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ñ/\&ntilde;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ñ/\&Ntilde;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ç/\&ccedil;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ç/\&Ccedil;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ý/\&yacute;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/Ý/\&Yacute;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/ß/\&szlig;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/«/\&laquo;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/»/\&raquo;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS 
sed -e "s/§/\&para;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/©/\&copy;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
sed -e "s/€/\&euro;/g" $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS > /tmp/fichier.tmp
mv -f /tmp/fichier.tmp $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS

zenity --info --text="Le fichier à été modifié et enregistré avec succés" --title="remp_accent_html.sh"

