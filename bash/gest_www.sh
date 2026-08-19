## Script réalisé par Bertrand Perrier le 17/05/07

while [ 1 ]; do
 
sudo find /home/$USER/backup -name www.zip -exec echo "===ATTENTION une archive www.zip existe déja vous allez l'écraser===" \;

echo "1) faire une sauvegarde de /var/www/"
echo "2) quitter"
read -p "Choix ? " ANSWER 
echo " "

#######################################################################################
if [ $ANSWER = 1 ]
   then
	echo "===compression en cours==="
	sudo zip -r /home/$USER/backup/www.zip /var/www/**
	echo "===compression terminé==="
	echo "===chmod 777 en cours==="
	sudo chmod 777 /home/$USER/backup/www.zip
	echo "===chmod 777 terminé==="

   fi
#######################################################################################
if [ $ANSWER = 2 ]
   then
	exit 0
fi
#######################################################################################
done
