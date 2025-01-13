#! /usr/bin/python
import cv2
import os
import sys

#vérifie si l'arguement se termine par jpg
def isJpg(NameOfFile):
	if (NameOfFile[-3:] == "jpg" or NameOfFile[-3:] == "JPG"):
		return True;
	else:
		return False;

# si il n'y a pas d'argument
if len(sys.argv)<2:
	print("Veuillez entrer un nom de dossier")
	print("Action annulée")
	sys.exit();
arg_path = str(sys.argv[1])

# verif si il  a un dossier ou des fichiers
if (isJpg(arg_path)):
	OneFileToResize=True;
else:
	OneFileToResize=False;

# si c'est un dossier, verif si le dossier contient / en fin de string
if (not OneFileToResize and not arg_path[len(arg_path)-1:] == "/"):
	print("Manque / à la fin du nom du dossier")
	sys.exit();

# verif si le dossier existe
if not os.path.exists(arg_path):
	print("Le fichier ou dossier n'éxiste pas");
	print("Action annulée");
	sys.exit();

# verif si le dossier vignettes existe
if  os.path.exists(arg_path+"vignettes"):
	print("Dossier vignettes éxiste déjà")
	print("Action annulée")
	sys.exit();

#demande confirmation de l'action
if OneFileToResize==False:
	item = input("Redimensionner les fichiers jpg du dossier %s (o/N) ? " % arg_path)
else:
	item = input("Redimensionner le fichier %s (o/N) ? " % arg_path)

if (item != "o" and item != "O"):
	print("Action annulée")
	sys.exit();

# verif si le dossier vignettes existe -> création du dossier
if OneFileToResize==False:
	if not os.path.exists(arg_path+"vignettes"):
		os.makedirs(arg_path+"vignettes")
	else:
		print("Dossier vignettes éxiste déjà")
		print("Action annulée")
		sys.exit();

# récupération de la liste des fichiers ou du fichier
if OneFileToResize==False:
	files = os.listdir(arg_path)
else:
	files = [1]
	files[0] = arg_path


for name in files:
	if (isJpg(name)):
		if OneFileToResize==False:
			print("redimensionnement "+name+" en cours vers vignettes/")
			src = cv2.imread(arg_path+name, cv2.IMREAD_UNCHANGED)
		else:
			print("redimensionnement du fichier "+name+" en cours")
			src = cv2.imread(name, cv2.IMREAD_UNCHANGED)
		#percent by which the image is resized
		scale_percent = 25
		#calcul de 25% de la dimension originale
		width = int(src.shape[1] * scale_percent / 100)
		height = int(src.shape[0] * scale_percent / 100)
		# format dsize
		dsize = (width, height)
		# redimensionnement de l'image
		output = cv2.resize(src, dsize)
		if OneFileToResize==False:
			cv2.imwrite(arg_path+"/vignettes/"+name,output)
		else:
			cv2.imwrite("mini_"+name,output)
		print("redimensionnement "+name+" terminé")

