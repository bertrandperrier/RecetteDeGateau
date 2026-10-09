#!/bin/bash

scan_page() {
  for essai in 1 2 3 4 5; do
    scanimage -d "$DEV" --format=png --resolution 300 --mode Color -x 210 -y 297 > "$1" 2>/dev/null && [ -s "$1" ] && return 0
    echo "  (essai $essai/5 échoué, nouvelle tentative...)"
    sleep 2
  done
  return 1
}

DEV='airscan:e0:HP DeskJet 3700'
# Ancien (découverte auto) : DEV='airscan:e1:HP DeskJet 3700 series [685789]'


# Si airscan échoue, essayez : DEV='hpaio:/net/deskjet_3700_series?ip=192.168.1.31'
DEST="$(xdg-user-dir DOWNLOAD)"
NOM="${1:-document}"
OUT="$DEST/${NOM%.pdf}.pdf"
TMP=$(mktemp -d)
i=1

while true; do
  read -p "Insérez la feuille $i puis Entrée (q pour terminer) : " r
  [ "$r" = "q" ] && break
  f="$TMP/page$(printf %03d $i).png"
  if scan_page "$f"; then
    echo "Page $i scannée."
    i=$((i+1))
  else
    echo "Échec du scan, réessayez la même feuille."
    rm -f "$f"
  fi
done

if [ $i -gt 1 ]; then
  img2pdf "$TMP"/page*.png -o "$OUT" && echo "PDF créé : $OUT"
else
  echo "Aucune page scannée."
fi
rm -rf "$TMP"



