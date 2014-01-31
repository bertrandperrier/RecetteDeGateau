# -*- coding: utf8 -*-
NbEspace = 0
NbLigne = 0
name_file="text";
print "Lecture du fichier : "+name_file
f = open(name_file, "r")
for ligne in f:
	NbLigne +=1
	while " " in ligne:
		position = ligne.find(" ")
		ligne = ligne[position+1:]
		NbEspace +=1
print("nombre de mots")
print NbEspace+1+NbLigne-1
f.close()
