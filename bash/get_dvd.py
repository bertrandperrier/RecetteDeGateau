#!/usr/bin/python3
#doc https://api.gandi.net/docs/livedns/

import sys
import urllib.request
import html
from datetime import datetime
import locale
import os

locale.setlocale(locale.LC_TIME,'')
# locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

verbose = 0
if len(sys.argv) > 1:
	if sys.argv[1] == "-v":
		verbose = 1

# recuperation code html du site
url = 'https://www.allocine.fr/dvd/nouveau/'

if verbose:
	print("source : "+url)

code_page_html = urllib.request.urlopen(url).read()
code_page_html = code_page_html.decode()
index=0
x = 0
# faire 15 fois
while (x < 15 and index != -1):
	if verbose:
		print("Boucle "+str(x))
	# recherche de la prochaine balise
	index = code_page_html.find('.html">')
	if verbose:
		print(index)
	# on garde la ligne du resultat du titre
	index_titre_debut = code_page_html[index+7:index+150]
	if verbose:
		print(index_titre_debut)

	# on affiche le titre, mais pas la balise de fin
	titre_html = code_page_html[index+7:index+7+index_titre_debut.find('</a>')]
	if verbose:
		print(titre_html)
	titre_str = html.unescape(titre_html)
	titre_str = str(titre_str)
	if verbose:
		print(titre_str)

	#on enleve un peu de caracteres
	code_page_html=code_page_html[index+7+index_titre_debut.find('</a>'):-1]
	
	# on affiche la date de sortie
	# on enlevre le début de chaine en trop

	index_date_debut = code_page_html.find('meta-body')
	
	date_str = code_page_html[index_date_debut+77:index_date_debut+500]
		
	# on enleve Bluray si present
	if date_str.find('Bluray') != -1:
		#print(date_str)
		date_str = date_str[13:-1]
	# on enleve la fin de chaine en trop
	index_date_fin = date_str.find('<')
	date_str = date_str[0:index_date_fin-1]
	
	if verbose:
		print("L70 " + date_str)
	
	#tant que ca commence pas par un numéro isdigit isalpha
	while (date_str[0] == " " or date_str[0].isalpha()):
		date_str = date_str[1:]
		
	if verbose:
		print("L77 " + date_str)
		
	# on enleve le slash n detecte a la fin
	if(date_str.find("\n") > 5 and date_str.find("\n") != -1 and date_str.find("\n") != 0):
		if verbose:
			print("slash n detecte a la fin")
		date_str = date_str[0:date_str.find("\n")]
		
	if verbose:
		print("L86 " + date_str)
	
	# on enleve le slash du debut
	if(date_str.find("\n") < 5 and date_str.find("\n") != -1):
		if verbose:
			print("slash n detecte au debut")
			print(date_str.find("\n"))
		date_str = date_str[date_str.find("\n")+1:]
		
	if verbose:
		print("L96 " + date_str)

	# A FAIRE ENLEVER LE SLASH N EN FIN DE STRING
	if(date_str.find("\n") >5 and date_str.find("\n") != -1):
		if verbose:
			print("slash n detecte en fin. " + str(date_str.find("\n")))
		date_str = date_str[0:date_str.find("\n")]
	
	#tant que ca commence pas par un numéro isdigit isalpha
	while (date_str[0] == ":" or date_str[0] == " " or date_str[0].isalpha()):
		date_str = date_str[1:]
		
	
	
	
	
	
	
	if verbose:
		print("L115 " + date_str)	
	
	date_sortie_datetime = datetime.strptime(date_str, '%d %B %Y')
	date_sortie_datetime = str(date_sortie_datetime)
	date_sortie_datetime = date_sortie_datetime[0:10]

	# si la date est aujourd'hui
	aujourdhui = datetime.today()
	aujourdhui = str(aujourdhui)
	aujourdhui = aujourdhui[0:10]
	
	if verbose:
		print("today : " + aujourdhui)
		print("date : " + date_sortie_datetime)
		
	if(date_sortie_datetime == aujourdhui):
		message = "Le film "+titre_str+" sort aujourdhui"
		#message = message.encode('utf8')
		message = message.replace(' ', '_')
		if verbose:
			# on affiche l'annonce du film qui sort aujourdhui
			print(message)
		else:
			# on envoie par email l'annonce du film qui sort aujourdhui
			os.system('python /home/bertrand/linux/script/send_mail_laposte.py \"'+message+'\"')
	if verbose:
		print ("fin de boucle")
	# retrait du dernier resultat

	# print(code_page_html)
	#code_page_html=code_page_html[index:-1]
	x=x+1
