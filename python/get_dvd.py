#!/usr/bin/python3

import sys
import urllib.request
import html
from datetime import datetime
import locale
import os
import lib_send_mail_laposte

locale.setlocale(locale.LC_TIME,'')
# locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')

def supprime_accent(ligne):
        """ supprime les accents du texte source """
        accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
        sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
        i = 0
        while i < len(accent):
            ligne = ligne.replace(accent[i], sans_accent[i])
            i += 1
        return ligne
        
def main(argv):
	verbose = 0
	if len(argv) == 2:
		if len(argv[1]) >= 2:
			if argv[1] == "-v":
				verbose = 1
			if len(argv[1]) >= 3:
				if argv[1] == "-va" or argv[1] == "-av":
					verbose = 2
	else:
		verbose = 0

	# si la date est aujourd'hui
	aujourdhui = datetime.today()
	aujourdhui = str(aujourdhui)
	aujourdhui = aujourdhui[0:10]
	#aujourdhui = "2022-11-17"
				
	# recuperation code html du site
	url = 'https://www.allocine.fr/dvd/nouveau/'
	url = 'https://www.allocine.fr/film/sorties-semaine/'
	url = 'https://www.allocine.fr/film/agenda/sem-2025-04-16/'
	url = 'https://www.allocine.fr/film/agenda/sem-'+aujourdhui+'/'
	# url = 'https://www.allocine.fr/film/agenda/'
	if verbose >= 1:
		print("source : "+url)

	# code_page_html = urllib.request.urlopen(url).read()
	request_site = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
	code_page_html = urllib.request.urlopen(request_site).read()


	code_page_html = code_page_html.decode()
	index=0
	x = 0
	erreur_extract_date = False

	# faire 15 fois
	while (index != -1 and x<22): ##index == -1 or x>=22
		if verbose >= 2:
			print("\nBoucle "+str(x))
		
		# recherche de la prochaine balise
		index = code_page_html.find('.html">')
		if verbose >= 2:
			print("Index : "+str(index))
		# on garde la ligne du resultat du titre
		index_titre_debut = code_page_html[index+7:index+150]
		if verbose >= 2:
			print("DEBUT "+index_titre_debut+" FIN")

		# on affiche le titre, mais pas la balise de fin
		titre_html = code_page_html[index+7:index+7+index_titre_debut.find('</a>')]
		if verbose >= 2:
			print("L73 "+titre_html)
		# on enlève les balises html
		#titre_str = html.unescape(titre_html)
		titre_str = titre_html
		titre_str = str(titre_str)
		if verbose >= 2:
			print("L79 "+titre_str)

		#on enleve un peu de caracteres
		code_page_html=code_page_html[index+7+index_titre_debut.find('</a>'):-1]
		
		# on affiche la date de sortie
		# on enlevre le début de chaine en trop

		index_date_debut = code_page_html.find('<span class="date">')
		
		date_str = code_page_html[index_date_debut+1:index_date_debut+500]
		if verbose >= 2:
			print("L91 DATE_STR : " + date_str)
		
		# on enleve Bluray si present
		if date_str.find('Bluray') != -1:
			date_str = date_str[10:-1]
		# on enleve la fin de chaine en trop
		index_date_fin = date_str.find('<')
		date_str = date_str[18:index_date_fin]
		
		if verbose >= 2:
			print("L101 " + date_str)
		
		#tant que ca commence pas par un numéro isdigit isalpha
		while (date_str[0] == " " or date_str[0].isalpha()):
			date_str = date_str[1:]
			
		if verbose >= 2:
			print("L108 " + date_str)
			
		# on enleve le slash n detecte a la fin
		if(date_str.find("\n") > 5 and date_str.find("\n") != -1 and date_str.find("\n") != 0):
			if verbose >= 2:
				print("slash n detecte a la fin")
			date_str = date_str[0:date_str.find("\n")]
			
		if verbose >= 2:
			print("L117 " + date_str)
		
		# on enleve le slash du debut
		if(date_str.find("\n") < 5 and date_str.find("\n") != -1):
			if verbose >= 2:
				print("slash n detecte au debut")
				print(date_str.find("\n"))
			date_str = date_str[date_str.find("\n")+1:]
			
		if verbose >= 2:
			print("L127 " + date_str)

		# A FAIRE ENLEVER LE SLASH N EN FIN DE STRING
		if(date_str.find("\n") >5 and date_str.find("\n") != -1):
			if verbose >= 2:
				print("slash n detecte en fin. " + str(date_str.find("\n")))
			date_str = date_str[0:date_str.find("\n")]
		
		#tant que ca commence pas par un numéro isdigit isalpha
		while (date_str[0] == ":" or date_str[0] == " " or date_str[0].isalpha()):
			date_str = date_str[1:]

		if verbose >= 2:
			print("L140 " + date_str)
				
		try:
			date_sortie_datetime = datetime.strptime(date_str, '%d %B %Y')
		except ValueError as inst:
			if verbose >= 1:
				print("Erreur extraction date : ", inst)
			erreur_extract_date = True
		if verbose >= 2:
			print("L149 date_sortie_datetime : "+str(date_sortie_datetime))
		
		# s'il n'y a pas de date, on passe au titre suivant
		if (not erreur_extract_date):
			date_sortie_datetime = str(date_sortie_datetime)
			date_sortie_datetime = date_sortie_datetime[0:10]
		

				
			if(date_sortie_datetime == aujourdhui):
				if verbose >= 1:
					print("date : " + date_sortie_datetime)
				
				message = "Le film <b>"+titre_str+"</b> sort aujourdhui"

				#message = message.encode('utf-8')
				message = supprime_accent(message)
				
				
				html = """\
				<html>
				  <head></head>
				  <body>
				    <p>Le film <b><a href="https://www.allocine.fr/rechercher/?q="""+titre_str+"""\">"""+titre_str+"""</a></b> sort aujourdhui</p>
				  </body>
				</html>
				"""
			
			
				if verbose >= 1:
					# on affiche l'annonce du film qui sort aujourdhui
					print(message)
				else:
					# on envoie par email l'annonce du film qui sort aujourdhui
					lib_send_mail_laposte.EnvoyerEmail("sortie_dvd", html)
			if verbose >= 2:
				print ("fin de boucle")

			x=x+1

if __name__ == '__main__':
	sys.exit(main(sys.argv))
