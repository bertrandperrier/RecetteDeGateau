# -*- coding: utf-8 -*-
from operator import itemgetter
## s = "a e i o a u a y i"
## source=["bof","bien","super","hyper","mega","bien","super","mega","mega"]
name_file="text";
dico={}
print "Lecture du fichier : "+name_file
FileHandle = open(name_file, "r")
## print ("list source:")
for ligne in FileHandle:
	# str to tab
	tab = ligne.split(' ')
	## print (str(len(tab))+" mots dans la ligne")
	for item in tab:
		## suppression des \n
		item=item.replace('\n','')
		## print item 
		# mot existant ?
		if dico.has_key(item):
			dico[item] +=1
		else:
			dico[item] = 1

# affichage resultat
dico_sorted=sorted(dico.iteritems())
print (str(len(dico_sorted))+" mots comptés")
print ("list dico:")
for key,value in dico_sorted: 
	print(key.encode('utf-8'),value) ## il bloque au 1er mot avec accent "adapté"


FileHandle.close()
