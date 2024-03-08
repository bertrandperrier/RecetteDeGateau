#Ãªtre sur que eth1 soit le wifi
L_INT=$(sudo lshw -C network | grep "nom logique" | cut -c 21-);
echo $L_INT
read -p "Saisir l'interface à scanner ? " INTERFACE
sudo iwlist wlp3s0 scanning | grep ESSID | cut -c 28- | sed 's/.$//' 
read -p "***   Appuyer sur un touche pour quitter   ***" ANSWER
