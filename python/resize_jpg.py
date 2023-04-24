#! /usr/bin/python
import cv2
import os
import sys

# si il n'y a pas d'argument
if len(sys.argv)<2:
	print("Veuillez entrer un nom de dossier");
	print("Action annulée");
	sys.exit();
path = str(sys.argv[1])

# verif si le dossier contient / en fin de string
if (path[len(path) - 1:] != "/"):
	print("Manque / à la fin du nom du dossier")
	sys.exit();

# verif si le dossier existe
if not os.path.exists(path):
	print("Le dossier n'éxiste pas");
	print("Action annulée");
	sys.exit();

# verif si le dossier vignettes existe
if  os.path.exists(path+"vignettes"):
	print("Dossier vignettes éxiste déjà");
	print("Action annulée");
	sys.exit();

#demande confirmation de l'action
item = input("Redimensionner les fichiers jpg du dossier %s (o/N) ? " % sys.argv[1])

if (item != "o" or item != "O"):
	print("Action annulée1");
	#sys.exit();

# verif si le dossier vignettes existe
if not os.path.exists(path+"vignettes"):
	os.makedirs(path+"vignettes")
else:
	print("Dossier vignettes éxiste déjà");
	print("Action annulée");
	sys.exit();
	
files = os.listdir(path)
for name in files:
	if (name != "vignettes" and name[-3:] == "jpg"):
		print("redimensionnement "+name+" en cours")
		src = cv2.imread(path+name, cv2.IMREAD_UNCHANGED)
		#percent by which the image is resized
		scale_percent = 75
		#calculate the 75 percent of original dimensions
		width = int(src.shape[1] * scale_percent / 100)
		height = int(src.shape[0] * scale_percent / 100)
		# dsize
		dsize = (width, height)
		# resize image
		output = cv2.resize(src, dsize)
		cv2.imwrite(path+"/vignettes/"+name,output)
		print("redimensionnement "+name+" terminé")
