#!/bin/bash

for cmd in scanimage img2pdf gs;
do
	command -v "$cmd" >/dev/null || { echo "Manque : $cmd"; exit 1; }
done

DEV='airscan:e0:HP DeskJet 3700'
# Si airscan échoue, essayez : DEV='hpaio:/net/deskjet_3700_series?ip=192.168.1.31'
# Ancien (découverte auto) : DEV='airscan:e1:HP DeskJet 3700 series [685789]'

scan_page() {
	for essai in 1 2 3 4 5;
		do
		scanimage -d "$DEV" --format=png --resolution 300 --mode Color -x 210 -y 297 \
		> "$1" 2>/dev/null
		if [ -s "$1" ];
		then
			return 0
		fi
		if [ "$essai" -lt 5 ];
		then
			echo "	(essai $essai/5 échoué, nouvelle tentative...)"
			sleep 2
		fi
	done
	return 1
}


DEST="$(xdg-user-dir DOWNLOAD)"
NOM="${1:-document}"
OUT="$DEST/${NOM%.pdf}.pdf"
TMP=$(mktemp -d) || exit 1
trap 'rm -rf "${TMP:?}"' EXIT
i=1

while true; do
	read -r -p "Insérez la feuille $i puis Entrée (q pour terminer) : " r
	[ "$r" = "q" ] && break
	f="$TMP/page$(printf %03d "$i").png"
	if scan_page "$f"; then
		echo "Page $i scannée."
		i=$((i+1))
	else
		echo "Échec du scan, réessayez la même feuille."
		rm -f "$f"
	fi
done

if [ "$i" -gt 1 ]; then
	if ! img2pdf "$TMP"/page*.png -o "$OUT"; then
		echo "Échec de la création du PDF."
		exit 1
	fi
	echo "PDF créé : $OUT"

	read -r -p "Réduire la taille (O/n) ? " REP
	REP=${REP:-O}	 # Entrée seule = Oui

	if [[ "$REP" =~ ^[OoYy]$ ]]; then
		REDUIT="${OUT%.pdf}_reduit.pdf"
		if gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
					-dNOPAUSE -dQUIET -dBATCH -sOutputFile="$REDUIT" "$OUT" \
			 && [ -s "$REDUIT" ]; then
			mv "$REDUIT" "$OUT"
			echo "PDF réduit : $OUT ($(du -h "$OUT" | cut -f1))"
		else
			echo "Échec de la réduction, le PDF d'origine est conservé."
			rm -f "$REDUIT"
		fi
	fi
else
	echo "Aucune page scannée."
fi





