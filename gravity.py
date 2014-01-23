# -*- coding: utf8 -*-
erreur = False
s = raw_input('Saissisez le nombre de lignes et de colonnes -->')
# s="3 3"
s=s.split(' ')
try:
	nb_ligne=int(s[0])
	nb_colonne=int(s[1])
except:
	print "erreur saisie : nombres non détectés"
	erreur = True

if len(s)> 2:
	print "erreur saisie : plus de deux chiffres saisies"
	erreur = True

if not erreur:
	colonne=[]
	for i in range(nb_ligne):
		while True:
			print "ligne n°"+str(i)
			temp=(raw_input('-->'))
			temp_s=temp.split()
			# print "nb colonne "+str(nb_colonne)
			if len(temp)==nb_colonne:
				colonne.extend(temp_s)
				break
			print "erreur "+str(nb_colonne)+" colonnes demandées"
	"""
	nb_colonne = 7
	nb_ligne = 9
	colonne = ["kdofjek","d.er.g.",".e.sf..","..qdsf.",".e...d.","d.e.f.q",".....d.",".u..i.o",".p.m..."]
	# nb_colonne = 5
	# nb_ligne = 5
	# colonne = ["yafdj","..e.k","...a.","...f.","....."]
	# nb_colonne = 3
	# nb_ligne = 3
	# colonne = ["ydj","e.k","..."]
	# nb_colonne = 4
	# nb_ligne = 4
	# colonne = ["yfdj","...k","..a.","..f."]
	"""
	print ""
	print "origine"
	print "-------"
	print ""
	for i in range(len(colonne)):
		print colonne[i]
	
	colonne_m= [[0 for x in range(nb_colonne)] for y in range(nb_ligne)]
	# print colonne_m
	
	for i in range(nb_ligne):
		for j in range(nb_colonne):
			# print("i="+str(i)+" j="+str(j))
			colonne_m[i][j] = colonne[i][j]
			
	for temp in range(nb_ligne): # scan de la grille nb_ligne fois
		for i in range(1, nb_ligne): #1,2,3,......l
			for j in range(nb_colonne-1,-1,-1): #c-1,.....,3,2,1,0
				# print("i="+str(i)+" j="+str(j))
				if colonne_m[i][j] == ".":
					colonne_m[i][j]   = colonne_m[i-1][j]
					colonne_m[i-1][j] = "."
	print ""
	print "modifié"
	print "-------"
	print ""
	for i in range(nb_ligne):
			print ''.join(colonne_m[i])
