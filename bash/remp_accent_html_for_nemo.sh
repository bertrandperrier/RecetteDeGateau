#!/bin/bash
## Script réalisé et mis à jour par Bertrand Perrier le 11/01/09
## ajout des majuscules le 13/04/23
## ajout oe collé le 25/08/23
## ajout de 50 caractères le 07/01/25

# Ce script permet de remplacé les caractère accentué par le codage html
# par exemple é devient eacute;

# Ce scripts est à mettre pour :
#    - Caja (Mate) dans ~/.config/caja/scripts
#    - Nautilus (Gnome/Unity) dans ~/.local/share/nautilus/scripts/ $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
#    - Némo (Cinnamon) dans ~/.local/share/nemo/scripts/ $NEMO_SCRIPT_SELECTED_FILE_PATHS

## Script réalisé et mis à jour par Bertrand Perrier le 11/01/09
## ajout des majuscules le 13/04/23
## ajout oe collé le 25/08/23
## ajout de 50 caractères le 07/01/25
## modification de sed, supression du fichier temporaire le 09/07/25
# Ce script permet de remplacer les caractère accentué par le codage html
# par exemple é devient eacute;

zenity --info --text="$NEMO_SCRIPT_SELECTED_FILE_PATHS"
zenity --info --text="Veuillez attendre l'avertissement de fin du traitement du fichier\n valider pour commencer le traitement" --title="remp_accent_html.sh"
cp $NEMO_SCRIPT_SELECTED_FILE_PATHS /tmp/backup.file



echo "$NEMO_SCRIPT_SELECTED_FILE_PATHS" |
while IFS= read -r fichier
do
	[ -z "$fichier" ] && continue

	sed -i \
	-e "s/é/\&eacute;/g" \
	-e "s/É/\&Eacute;/g" \
	-e "s/è/\&egrave;/g" \
	-e "s/È/\&Egrave;/g" \
	-e "s/ê/\&ecirc;/g" \
	-e "s/Ê/\&Ecirc;/g" \
	-e "s/à/\&agrave;/g" \
	-e "s/À/\&Agrave;/g" \
	-e "s/â/\&acirc;/g" \
	-e "s/Â/\&Acirc;/g" \
	-e "s/œ/\&oelig;/g" \
	-e "s/Œ/\&OElig;/g" \
	-e "s/á/\&aacute;/g" \
	-e "s/Á/\&Aacute;/g" \
	-e "s/ã/\&atilde;/g" \
	-e "s/Ã/\&Atilde;/g" \
	-e "s/ä/\&auml;/g" \
	-e "s/Ä/\&Auml;/g" \
	-e "s/å/\&aring;/g" \
	-e "s/Å/\&Aring;/g" \
	-e "s/æ/\&aelig;/g" \
	-e "s/Æ/\&AElig;/g" \
	-e "s/ë/\&euml;/g" \
	-e "s/Ë/\&Euml;/g" \
	-e "s/ì/\&igrave;/g" \
	-e "s/Ì/\&Igrave;/g" \
	-e "s/í/\&iacute;/g" \
	-e "s/Í/\&Iacute;/g" \
	-e "s/î/\&icirc;/g" \
	-e "s/Î/\&Icirc;/g" \
	-e "s/ï/\&iuml;/g" \
	-e "s/Ï/\&Iuml;/g" \
	-e "s/ò/\&ograve;/g" \
	-e "s/Ò/\&Ograve;/g" \
	-e "s/ó/\&oacute;/g" \
	-e "s/Ó/\&Oacute;/g" \
	-e "s/ô/\&ocirc;/g" \
	-e "s/Ô/\&Ocirc;/g" \
	-e "s/õ/\&otilde;/g" \
	-e "s/Õ/\&Otilde;/g" \
	-e "s/ö/\&ouml;/g" \
	-e "s/Ö/\&Ouml;/g" \
	-e "s/ø/\&oslash;/g" \
	-e "s/Ø/\&Oslash;/g" \
	-e "s/ù/\&ugrave;/g" \
	-e "s/Ù/\&Ugrave;/g" \
	-e "s/ú/\&uacute;/g" \
	-e "s/Ú/\&Uacute;/g" \
	-e "s/û/\&ucirc;/g" \
	-e "s/Û/\&Ucirc;/g" \
	-e "s/ü/\&uuml;/g" \
	-e "s/Ü/\&Uuml;/g" \
	-e "s/ñ/\&ntilde;/g" \
	-e "s/Ñ/\&Ntilde;/g" \
	-e "s/ç/\&ccedil;/g" \
	-e "s/Ç/\&Ccedil;/g" \
	-e "s/ý/\&yacute;/g" \
	-e "s/Ý/\&Yacute;/g" \
	-e "s/ß/\&szlig;/g" \
	-e "s/«/\&laquo;/g" \
	-e "s/»/\&raquo;/g" \
	-e "s/§/\&para;/g" \
	-e "s/©/\&copy;/g" \
	-e "s/€/\&euro;/g" \
	-e "s/['’]/\&rsquo;/g" \
	"$fichier"

done

zenity --info --text="Le fichier à été modifié et enregistré avec succés" --title="remp_accent_html.sh"
