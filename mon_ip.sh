## Script réalisé et mis à jour par Bertrand Perrier le 28/05/07

echo "GET http://www.monip.net | sed -nre 's/^.* (([0-9]{1,3}\.){3}[0-9]{1,3}).*$/\1/p'"
GET http://www.monip.net | sed -nre 's/^.* (([0-9]{1,3}\.){3}[0-9]{1,3}).*$/\1/p'
##GET www.monip.org | grep "IP" | cut -d= -f3

read -p "***   Appuyer sur un touche pour quitter   ***" ANSWER
