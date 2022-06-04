#!/usr/bin/python3
#doc https://api.gandi.net/docs/livedns/

import urllib.request
import html

# recuperation code html du site
# code_page_html = urllib.urlopen('http://www.fnac.com/n899/A-paraitre-DVD-et-Blu-Ray/n899/A-paraitre-DVD-et-Blu-Ray').read()
url = 'https://www.allocine.fr/dvd/nouveau/'
print("source : "+url)
code_page_html = urllib.request.urlopen(url).read()

# recherche de la balise
#index = code_page_html.find('thumbnail-container thumbnail-link" title="')
#resultat = code_page_html[index+43:index+70]

# affichage du 1er resultat
#print "########### 1 ##########"
#print(code_page_html[index+43:index+43+resultat.find('\"')])

# retrait du premier resultat
#code_page_html=code_page_html[index+43:]

# recherche de la prochaine balise
#index = code_page_html.find('thumbnail-container thumbnail-link" title="')

#print "########### 2 ##########"
#resultat = code_page_html[index+43:index+70]
#print(code_page_html[index+43:index+43+resultat.find('\"')])

# retrait du dernier resultat
#code_page_html=code_page_html[index+43:index+10000]
#index = code_page_html.find('thumbnail-container thumbnail-link" title="')

#print "########### 3 ##########"
#resultat = code_page_html[index+43:index+70]
#print(code_page_html[index+43:index+43+resultat.find('\"')])

code_page_html = code_page_html.decode()

x = 0
# faire 15 fois
while x < 15:
	# recherche de la prochaine balise
	str1 = 'thumbnail-container thumbnail-link" title="'
	index = code_page_html.find(str1)
	# on garde la ligne du resultat
	resultat = code_page_html[index+43:index+100]
	# print resultat
	# on affiche le titre, mais pas les guillemets
	print(code_page_html[index+43:index+43+resultat.find('\"')]) #.unescape)
	# on affiche la date de sortie
	index_date = code_page_html.find('span class="spacer"')
	print(code_page_html[index_date-13:index_date-2])
	# retrait du dernier resultat
	code_page_html=code_page_html[index+500:-1]
	x=x+1










