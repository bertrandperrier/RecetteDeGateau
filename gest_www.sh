## Script réalisé par Bertrand Perrier le 17/05/07
 
while [ 1 ]; do
 
while [ "$ANSWER" != "1" ] && [ "$ANSWER" != "2" ]; do

sudo find /home/$USER/backup -name www.zip -exec echo "===ATTENTION une archive www.zip existe déja vous allez l'écraser===" \;

echo "1) faire une sauvegarde de /var/www/"
echo "2) quitter"
read -p "Choix ? " ANSWER 
echo " "
done
#######################################################################################
if [ $ANSWER = 1 ]
   then
	echo "===compression en cours==="
	sudo zip -r /home/bertrand/backup/www.zip /var/www/**
	echo "===compression terminé==="
	echo "===chmod 777 en cours==="
	sudo chmod 777 /home/bertrand/backup/www.zip
	echo "===chmod 777 terminé==="

   fi
#######################################################################################
if [ $ANSWER = 2 ]
   then
	echo " "
	read -p "***   Appuyer sur un touche pour quitter   ***" ANSWER
	exit 0
fi
#######################################################################################
ANSWER=3
done
