# -*- coding: utf8 -*-
liste_dep=[1000, 75, 25, 56, 125, 2, 35, 121,234,56,789,98,76,54,323,45,6,7,89,0]


def trier_tab(liste_triee):
	for j in range(1,len(liste_triee)):
		i=0
		while i < len(liste_triee)-1:
			if liste_triee[i]>liste_triee[i+1]:
				(liste_triee[i+1],liste_triee[i])=(liste_triee[i],liste_triee[i+1])
				# print ("i="+str(i))
				# print (str(liste_triee[i])+" : "+str(liste_triee[i+1]))
			i+=1
	return liste_triee

print("a trier="+str(liste_dep))
liste_triee=trier_tab(liste_dep)
print("resultat="+str(liste_triee))
