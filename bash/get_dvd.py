#!/usr/bin/python3
#doc https://api.gandi.net/docs/livedns/

import sys
import urllib.request
import html
from datetime import datetime
import locale
import os

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

verbose = 0
if len(sys.argv) > 1:
	if sys.argv[1] == "-v":
		verbose = 1

# recuperation code html du site
# url='http://www.fnac.com/n899/A-paraitre-DVD-et-Blu-Ray/n899/A-paraitre-DVD-et-Blu-Ray'
url = 'https://www.allocine.fr/film/attendus/'
if verbose:
	print("source : "+url)

code_page_html = urllib.request.urlopen(url).read()
code_page_html = code_page_html.decode()

x = 0
# faire 15 fois
while x < 15:
	# recherche de la prochaine balise
	str1 = 'thumbnail-container thumbnail-link" title="Bande-annonce '
	index = code_page_html.find(str1)
	
	# on garde la ligne du resultat
	resultat = code_page_html[index+43:index+150]
	# print(resultat)

	# on affiche le titre, mais pas les guillemets
	titre_html = code_page_html[index+57:index+43+resultat.find('\"')]
	titre_str = html.unescape(titre_html)
	titre_str = str(titre_str)
	if verbose:
		print(titre_str)
	
	# on affiche la date de sortie
	# on enlevre le début de chaine en trop
	index_date_debut = code_page_html.find('<span class="date">')
	date_str = code_page_html[index_date_debut+19:index_date_debut+36]
	
	# on enleve la fin de chaine en trop
	index_date_fin = date_str.find('<')
	date_str = date_str[0:index_date_fin]
	if verbose:
		print(date_str)
	date_sortie_datetime = datetime.strptime(date_str, '%d %B %Y')
	date_sortie_datetime=str(date_sortie_datetime)
	date_sortie_datetime=date_sortie_datetime[0:10]

	# si la date est aujourd'hui
	aujourdhui = datetime.today()
	aujourdhui = str(aujourdhui)
	aujourdhui = aujourdhui[0:10]
	if(date_sortie_datetime == aujourdhui):
		message = "Le film "+titre_str+" sort aujourdhui"
		if verbose:
			# on affiche l'annonce du film qui sort aujourdhui
			print('python /home/bertrand/linux/script/send_mail_laposte.py \"'+message+'\"')
		else:
			# on envoie par email l'annonce du film qui sort aujourdhui
			os.system('python /home/bertrand/linux/script/send_mail_laposte.py \"'+message+'\"')
	if verbose:
		print (" ")
	# retrait du dernier resultat
	code_page_html=code_page_html[index+500:-1]
	x=x+1
