#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import termios

verbose = 0
tabl_of_point_cardinal_labyrinthe = []
colonne, ligne = 6,7
tab_emplacement = [0, 0]
tab_gagne = [7, 6]

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
print("\nDirections\n z\nq+d\n s\n\nx pour quitter\n")

if verbose:
	#affichage de la table du labyrinthe
	for i in range(ligne):
		for j in range(colonne):
			print("L:"+str(i)+" C:"+str(j)+" "+str(tabl_of_point_cardinal_labyrinthe[i][j]))

input("Entrer pour commencer")
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
		quit()
		
	# saisie de la direction
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

	# si déplacement autorisé -> déplacement demandé
	if (autor_depl(tab_emplacement, dir_demandee)):
		tab_emplacement=depl(tab_emplacement, dir_demandee)	
