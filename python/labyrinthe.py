#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import termios
import time

verbose = 0
tabl_of_point_cardinal_labyrinthe = []
tab_emplacement = [0, 0]
dir_prec_demandee = ""
nb_depl = 0
def autor_depl(tab_emplacement, dir_demandee):
	# si la direction demandée n'est pas un mur
	for point_cardinal in tabl_of_point_cardinal_labyrinthe[tab_emplacement[0]][tab_emplacement[1]]:
		if (point_cardinal == dir_demandee):
			return True

def depl(tab_emplacement, dir_demandee):
	#modification des coordonnées de l'emplacement en fct de la direction
	match dir_demandee:
		case "s":
			if (tab_emplacement[0]<ligne):
				tab_emplacement[0]=tab_emplacement[0]+1
		case "n":
			if (tab_emplacement[0]>=1):
				tab_emplacement[0]=tab_emplacement[0]-1
		case "e":
			if (tab_emplacement[1]<colonne):
				tab_emplacement[1]=tab_emplacement[1]+1
		case "o":
			if (tab_emplacement[1]>=1):
				tab_emplacement[1]=tab_emplacement[1]-1

	return tab_emplacement

def readchar() -> str:
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    term = termios.tcgetattr(fd)
    try:
        term[3] &= ~(termios.ICANON | termios.ECHO | termios.IGNBRK | termios.BRKINT)
        termios.tcsetattr(fd, termios.TCSAFLUSH, term)

        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


# construction de la table du labyrinthe
tabl_of_point_cardinal_labyrinthe = [['s',  'se',   'eo', 'so',   'se',  'seo', 'so'],
				['ns',  'ns',  'se', 'no',   'ns',  'ns',  'ns'],
				['ns',  'ns',  'ns', 'se',   'nso', 'ns',  'ns'],
				['ns',  'ns',  'ns', 'ns',   'ns',  'ns',  'ns'],
				['nse', 'nso', 'ns', 'ns',   'ns',  'ns',  'ns'],
				['ns',  'ns',  'n',  'ns',   'n',   'ns',  'ns'],
				['ns',  'ne',  'eo', 'nseo', 'eo',  'no',  'ns'],
				['ne',  'eo',  'eo', 'neo',  'eo',  'o',   'n']]

colonne, ligne = 6,7
tab_gagne = [7, 6]
dir_demandee = "s"
"""
tabl_of_point_cardinal_labyrinthe = [['e',  'eo',   'eo', 'eo',   'eo',  'eo', 'so'],
					['ns',  'ns',  'se', 'no',   'ns',  'ns',  'ns'],
					['ns',  'ns',  'ns', 'se',   'nso', 'ns',  'ns'],
					['ns',  'ns',  'ns', 'ns',   'ns',  'ns',  'ns'],
					['nse', 'nso', 'ns', 'ns',   'ns',  'ns',  'ns'],
					['ns',  'ns',  'n',  'ns',   'n',   'ns',  'ns'],
					['ns',  'ne',  'eo', 'nseo', 'eo',  'no',  'ns'],
					['ne',  'eo',  'eo', 'neo',  'eo',  'o',   'n']]


tabl_of_point_cardinal_labyrinthe =    [['e',  'eo',   'seo',  'eo',   'seo',  'eo',  'so'],
					['se',  'o',   'ns',   's',    'ns',   's',   'ns'],
					['ne',  'eo',  'nso',  'ns',   'ns',   'ns',  'ns'],
					['se',  'so',  'ns',   'ne',   'no',   'ne',  'nso'],
					['ns',  'ns',  'nse',  'seo',  'eo',   'eo',  'nso'],
					['ns',  'ns',  'ns',   'ns',   's',    'se',  'nso'],
					['ns',  'n',   'ns',   'ns',   'ne',   'no',  'ns'],
					['ne',  'eo',  'no',   'ne',   'eo',   'eo',  'no']]
"""
#y, x de 0 à 
tab_gagne = [7, 6]
dir_demandee = "o"

if len(sys.argv) > 1:
	if sys.argv[1] == "-v":
		verbose = True

os.system('clear')

# affichage du labyrinthe
print("_______________")
print("|o|  _  |     |")
print("| | |  _| | | |")
print("| | | |   | | |")
print("| | | | | | | |")
print("|   | | | | | |")
print("| | |_| |_| | |")
print("| |____  ___| |")
print("|___________|x|")

dessin=""
print("__________________")
for i in range(ligne):
		for j in range(colonne):
			match tabl_of_point_cardinal_labyrinthe[i][j]:
				case "n":	dessin+="|_|"
				case "s":	dessin+="| |"
				case "e":	dessin+="|= "
				case "o":	dessin+=" =|"
				case "se":	dessin+="|  "
				case "eo":	dessin+=" = "
				case "so":	dessin+="  |"
				case "ns":	dessin+="| |"
				case "no":	dessin+=" _|"
				case "ne":	dessin+="|_ xxx"
				case "nso":	dessin+="  |"
				case "nse":	dessin+="|  "
				case "seo":	dessin+="   "
				case "neo":	dessin+=" _ "
				case "nseo":	dessin+="   "
		print(dessin)
		dessin = ""
print("------------------")
print("\nDirections\n z\nq+d\n s\n\nx pour quitter\n")

if verbose:
	#affichage de la table du labyrinthe
	for i in range(ligne):
		for j in range(colonne):
			print("L:"+str(i)+" C:"+str(j)+" "+str(tabl_of_point_cardinal_labyrinthe[i][j]))

input("Entrer pour commencer")

mode = input("mode Manuel ou Automatique (M/a)")

if (mode == "A"):
	mode = "a"
else:
	mode =  "m"


while(1):
	# effacement de l'écran
	os.system('clear')
	
	if verbose:
		print("emplacement : "+str(tab_emplacement))
		print("gagne : "+str(tab_gagne))
		print("direction : "+str(tabl_of_point_cardinal_labyrinthe[tab_emplacement[0]][tab_emplacement[1]]))
		
	# affichage de l'emplacement à l'écran
	match tabl_of_point_cardinal_labyrinthe[tab_emplacement[0]][tab_emplacement[1]]:
		case "n":	print("\n#o#\n###")
		case "s":	print("###\n#o#\n\n")
		case "e":	print("###\n#o\n###")
		case "o":	print("###\n o#\n###")
		case "se":	print("###\n#o\n\n")
		case "eo":	print("###\n o\n###")
		case "so":	print("###\n o#\n\n")
		case "ns":	print(" \n#o#\n\n")
		case "no":	print(" \n o#\n###")
		case "ne":	print(" \n#o\n###")
		case "nso":	print(" \n o#\n\n")
		case "nse":	print(" \n#o\n\n")
		case "seo":	print("###\n o\n\n")
		case "neo":	print("  \n o\n###")
		case "nseo":	print(" \n o\n")

	# check sortie du labyrinthe
	if (tab_emplacement[0] == tab_gagne[0] and tab_emplacement[1] == tab_gagne[1]):
		print("gagné")
		print("nb_depl : "+str(nb_depl))
		quit()
	
	if (mode == "m"):
		#saisie de la direction
		while True:
			key = readchar()
			if key == "z":
				dir_demandee="n"
				break
			if key == "q":
				dir_demandee="o"
				break
			if key == "d":
				dir_demandee="e"
				break
			if key == "s":
				dir_demandee="s"
				break
			if key == "x":
				quit()

		
	
		
	if (mode == "a"):
		match tabl_of_point_cardinal_labyrinthe[tab_emplacement[0]][tab_emplacement[1]]:
			case "n":	key = "z"
			case "s":	key = "s"
			case "e":	key = "d"
			case "o":	key = "q"
			case "se":
				if (dir_prec_demandee=="n"): key = "d"
				if (dir_prec_demandee=="o"): key = "s"		
			case "eo":
				if (dir_prec_demandee=="e"): key = "d"
				if (dir_prec_demandee=="o"): key = "q"
			case "so":
				if (dir_prec_demandee=="n"): key = "q"
				if (dir_prec_demandee=="e"): key = "s"
			case "ns":
				if (dir_prec_demandee=="n"): key = "z"
				if (dir_prec_demandee=="s"): key = "s"
			case "no":
				if (dir_prec_demandee=="s"): key = "q"
				if (dir_prec_demandee=="e"): key = "z"
			case "ne":
				if (dir_prec_demandee=="s"): key = "d"
				if (dir_prec_demandee=="o"): key = "z"
			case "nso":
				if (dir_prec_demandee=="n"): key = "q"
				if (dir_prec_demandee=="s"): key = "z"
				if (dir_prec_demandee=="e"): key = "s"
			case "nse":
				if (dir_prec_demandee=="n"): key = "s"
				if (dir_prec_demandee=="s"): key = "d"
				if (dir_prec_demandee=="o"): key = "z"
			case "seo":
				if (dir_prec_demandee=="n"): key = "d"
				if (dir_prec_demandee=="e"): key = "d"
				if (dir_prec_demandee=="o"): key = "q"
			case "neo":
				if (dir_prec_demandee=="s"): key = "q"
				if (dir_prec_demandee=="e"): key = "d"
				if (dir_prec_demandee=="o"): key = "n"
			case "nseo":
				if (dir_prec_demandee=="n"): key = "q"
				if (dir_prec_demandee=="s"): key = "d"
				if (dir_prec_demandee=="e"): key = "z"
				if (dir_prec_demandee=="o"): key = "s"
		
	print("dir : "+key)
	print("dir_demandee : "+dir_demandee)
	print("dir_prec_demandee : "+dir_prec_demandee)
	print("nb_depl : "+str(nb_depl))
	
	if (mode == "a"):
		time.sleep(0.5)
	
	if key == "z":
		dir_demandee="n"
	if key == "q":
		dir_demandee="o"
	if key == "d":
		dir_demandee="e"
	if key == "s":
		dir_demandee="s"
	if key == "x":
		quit()
	dir_prec_demandee=dir_demandee

	# si déplacement autorisé -> déplacement demandé
	if (autor_depl(tab_emplacement, dir_demandee)):
		tab_emplacement=depl(tab_emplacement, dir_demandee)
		nb_depl=nb_depl+1
