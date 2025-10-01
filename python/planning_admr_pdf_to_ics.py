#!/usr/bin/python3
#
# ce programme convertit un planning de l'ADMR du format pdf au format ics

# importation des modules nécessaires 
from PyPDF2 import PdfReader
import sys
from datetime import datetime
import webbrowser
import pytz.reference
import os.path

# email de l'agenda
email_for_ics = 'xxxxxxx@xxxxxx.xxx'

# notification nombre d'heure avant evenement
reminder_delay_hour = "0"

# notification nombre de minutes avant evenement
reminder_delay_minute = "5"

file_name_pdf = "planning_admr.pdf"
file_name_ics = "planning_admr.ics"
file_name_txt = "planning_admr.txt"

# liste d'éléments des jours et des mois
days_of_the_week = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche","Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
months_of_the_year = ["Janvier", "Février", "Mars", "Avril", "Mai ", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

# pour afficher les infos de débuggage
verbose = 0
debug = 0

nb_interventions = 0

# converti le nom du jour en int (lundi=0, ...=6) lit que les 3 premieres lettres du jour
def day_txt_to_int(arg_day_txt):
	i = 0
	for jours in days_of_the_week:
		if debug:
			print("jours[0:2] :"+str(jours[0:2]))
			print("arg_day_txt[0:2] :"+str(arg_day_txt[0:2]))
		if jours[0:2].lower() == arg_day_txt[0:2].lower():
			if debug:
				print("fct return : "+str(i))
			return i
		i=i+1
	return False

# vérifie si l'argument est le nom d'un jour de la semaine
def is_day_name(arg_day_txt):
	if debug:
		print("len : "+str(len(arg_day_txt)))
	for i in range(len(arg_day_txt)):
		for jour in days_of_the_week:
			if arg_day_txt[i:i+5] == jour[0:5]:
				arg_day_txt=arg_day_txt[i:]
				return arg_day_txt
	return False

# converti le nom d'un mois en int (Janvier=1, ...)
def month_txt_to_int(arg_month_txt):
	i = 1
	for month in months_of_the_year:
		if month[0:4].lower() == arg_month_txt[0:4].lower(): # tester month[0:3]
			if len(str(i)) == 2:
				return i
			else:
				return "0"+str(i)
		i+=1
	return False

# renvoi le décalage horaire avec GMT, -1 en hiver -2 en été
def calc_heure_ete_hiver(annee, mois, jour, heure, minute, seconde):
	heure_input=datetime(annee, mois, jour, heure, minute, seconde)
	#local_tnz = pytz.reference.LocalTimezone() # tz de l'ordinateur
	local_tnz = pytz.timezone("Europe/Paris") # tz de Paris
	decal_heure_ete_hiver_gmt = local_tnz.utcoffset(heure_input)
	decal_heure_ete_hiver_gmt = -int(decal_heure_ete_hiver_gmt.seconds/3600)
	return decal_heure_ete_hiver_gmt

#renvoie le nom de l'intervenant
def find_name_inter(ligne_txt):
	index_txt = len(ligne_txt)-2
	while index_txt != 0:
		if (ligne_txt[index_txt].isdigit()):
			return str(ligne_txt[index_txt+2:index_txt+30])
		index_txt -= 1
	return False

#renvoie un tab des lignes d'un fichier
def file_to_tab(file_to_read):
	file_txt = open(file_name_txt, "r")
	lines_of_file_txt = file_txt.readlines()
	# fermeture du fichier enregistré
	file_txt.close()

	tab_result = []
	for lines in lines_of_file_txt:
		if debug :
			print("ligne du fichier texte : "+str(lines))
		if (is_day_name(lines)):
			if debug :
				print("nom du jour détecté")
			lines = lines[:-1]
			tab_result.insert(99,lines)
		else:
			if verbose or debug: # :-1 pour enlever le \n
				print("########### impossible d'extraire les informations sur la ligne : "+lines[:-1]+" ###########")
	# on ajoute la première intervention
	tab_result[0] = lines_of_file_txt[0][:-1]	
	return tab_result

# pour afficher les infos de débuggage
if len(sys.argv) > 1:
	if sys.argv[1] == "-debug" or sys.argv[1] == "-d":
		debug = 1
	if sys.argv[1] == "-v":
		verbose = 2
	if sys.argv[1] == "-h":
		print("Utilisation :")
		print(os.path.basename(__file__)+"  [OPTION...]\n")
		print("Options de l'application :")
		print("  -debug -d                 affiche tout")
		print("  -v                        mode verbose, montre les dates aux format ics")
		sys.exit()

# variable année, à modifier si le planning ne concerne pas l'année en cours
int_year = int(datetime.today().strftime('%Y'))
a = input("Changer l'année("+str(int_year)+") (o/N)")
if (a == "o" or a == "O"):
	while(1):
		str_year = input("Saisir l'année du planning : ")
		try:
			int_year = int(str_year)
			if len(str_year)==4:
				break
			else:
				print("Saisir l'année sur 4 chiffres")
		except:
			print("Erreur de saisie")
	
else:
	str_year = str(int_year)
	
while True:
	source_planning = input("Source du planning (Pdf/Texte) : ")
	if (source_planning=="pdf" or source_planning=="Pdf" or source_planning=="p" or source_planning=="P" or source_planning=="texte" or source_planning=="Texte" or source_planning=="t" or source_planning=="T"):
		break

if (source_planning == "pdf" or source_planning == "Pdf" or source_planning == "p" or source_planning == "P"):
	print("lecture du fichier pdf")
	# création d'un objet lecteur pdf
	reader = PdfReader(file_name_pdf)
	nb_de_page = len(reader.pages)
	
	#tableau de lignes du pdf
	result_par_ligne = []
	
	for i in range(nb_de_page):
		# récupérer la première page du pdf (0=1ère page)
		if debug:
			print("page : "+str(i))
		page = reader.pages[i]

		# extraction du texte de la page
		text = page.extract_text()
		if debug:
			print("texte de la page "+str(i)+" : "+text)

		index = 0
		x=0

		# converti le texte du pdf en liste d'éléments (1 ligne par élément)
		while x != -1:
			x=text.find("\n")
			if x != -1:
				result_par_ligne.insert(index, text[0:x])
				if debug:
					print("TEXTE DU PDF. Page "+str(i)+" : "+text[0:x])
				
				# on retire le texte traité
				text=text[x+1:-1]
			index = index+1
		
		
		if debug:
			print("Nb de ligne : "+str(index-1))
else:
	#pas de pdf, lecture du fichier "saisie manuelle"
	print("Lecture du fichier : "+file_name_txt)

	
	result_par_ligne=file_to_tab(file_name_txt)



# ouverture du fichier d'enregistrement
f = open(file_name_ics, "w")

# entete au format ics
f.write("BEGIN:VCALENDAR\n")
f.write("PRODID:-//Google Inc//Google Calendar 70.9054//EN\n")
f.write("VERSION:2.0\n")
f.write("CALSCALE:GREGORIAN\n")
f.write("METHOD:PUBLISH\n")
f.write("X-WR-CALNAME:"+email_for_ics+"\n")
f.write("X-WR-TIMEZONE:Europe/Paris\n")
f.write("BEGIN:VTIMEZONE\n")
f.write("TZID:Europe/Paris\n")
f.write("X-LIC-LOCATION:Europe/Paris\n")
f.write("BEGIN:DAYLIGHT\n")

## reflechir sur TZOFFSET est à définir à chaque event


for ligne in result_par_ligne:
	if is_day_name(ligne):
		nom_jour_int = day_txt_to_int(ligne)
		nom_jour_txt = days_of_the_week[nom_jour_int]
		len_jour = len(nom_jour_txt)
		nom_mois = ligne[len_jour+4:len_jour+8]
		num_mois = month_txt_to_int(nom_mois)
		num_jour = ligne[len_jour+1:len_jour+3]
		if debug:
			print("y="+str(int_year)+" mois="+str(num_mois)+" jour="+str(num_jour))
		break

if (calc_heure_ete_hiver(int_year, int(num_mois), int(num_jour), 12, 0, 0) == -1):
	#heure d'hiver
	if debug:
		print("heure d'hiver###############")
	f.write("TZOFFSETFROM:+0200\n")
	f.write("TZOFFSETTO:+0100\n")
else:
	#heure d'été
	if debug:
		print("heure d'été###########")
	f.write("TZOFFSETFROM:+0100\n")
	f.write("TZOFFSETTO:+0200\n")

f.write("TZNAME:CEST\n")
f.write("DTSTART:19700329T020000\n")
f.write("RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU\n")
f.write("END:DAYLIGHT\n")
f.write("BEGIN:STANDARD\n")
if (calc_heure_ete_hiver(int_year, int(num_mois), int(num_jour), 12, 0, 0) == -1):
	#heure d'hiver
	f.write("TZOFFSETFROM:+0200\n")
	f.write("TZOFFSETTO:+0100\n")
else:
	#heure d'été
	f.write("TZOFFSETFROM:+0100\n")
	f.write("TZOFFSETTO:+0200\n")
f.write("TZNAME:CET\n")
f.write("DTSTART:19701025T030000\n")
f.write("RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU\n")
f.write("END:STANDARD\n")
f.write("END:VTIMEZONE\n")

if debug:
	print("nb de ligne : "+str(len(result_par_ligne)))

# extraction des données pour chaque élément du array
for ligne in result_par_ligne:
	if debug:
		print("############### nouvelle boucle ###############")
		if debug:
			print("ligne agenda : "+ligne)
		print("is_day_name : "+str(is_day_name(ligne)))
	# si la ligne commence par le nom d'un jour de semaine
	if is_day_name(ligne):  # déjà vérifié
		if debug:
			print("is_day_name")
		ligne = is_day_name(ligne)
		#récupération du nom du jour de la semaine
		nom_jour_int = day_txt_to_int(ligne)
		nom_jour_txt = days_of_the_week[nom_jour_int]
		if debug:
			print("index jour :"+str(nom_jour_int))
			print("nom_jour_txt :"+nom_jour_txt)
		# calcul de la longeur du nom de la semaine pour un futur parsing
		len_jour = len(nom_jour_txt)
		# extraction du numéro du jour
		num_jour = ligne[len_jour+1:len_jour+3]
		if debug:
			print("num_jour :"+num_jour)
		# extraction des 4 1ère lettres du nom du mois
		nom_mois = ligne[len_jour+4:len_jour+8]
		if debug:
			print("nom_mois 4char :"+str(nom_mois))
		# conversion du nom du mois en int
		num_mois = month_txt_to_int(nom_mois)
		if num_mois == False:
			print("ERREUR : parsing mois "+nom_mois+" n'est pas un nom de mois. "+ligne)
			f.close()
			sys.exit()
		if debug:
			print("num_mois :"+str(num_mois))
			
		# calcul de la longeur du nom du mois et du jour		
		nom_mois = months_of_the_year[int(num_mois)-1]
		len_mois = len(nom_mois)
		len_jour_et_mois = len_mois+len_jour
		
		if debug:
			print("len_jour :"+str(len_jour))
			print("nom_mois entier :"+str(nom_mois))
			print("len_mois :"+str(len_mois))
			print("len_jour_et_mois :"+str(len_jour_et_mois))
		
		# détection d'erreur	
		if not num_jour.isdigit():
			print("ERREUR : parsing numéro du jour "+num_jour+" n'est pas un numéro")
			f.close()
			sys.exit()			
		
		# extraction de l'heure du début d'intervention en fct de la longueur de chaine et calcul en fct de l'heure d'été/hiver
		index_debut_heure=ligne.find("h",len_jour_et_mois)
		str_debut_heure = ligne[index_debut_heure-2:index_debut_heure]
		
		# mise au format de l'heure (2char)
		if str_debut_heure[0] == " ":
			str_debut_heure = str_debut_heure[1]
		if debug :
			print("index_debut_heure :"+str(index_debut_heure))
			print("str_debut_heure :"+str(str_debut_heure))
		
		# détection d'erreur
		if str_debut_heure.isdigit() == False or int(str_debut_heure)>24:
			print("ERREUR : parsing heure de début. "+str_debut_heure+" n'est pas un entier ou est supérieur à 24, ligne :"+ligne)
			f.close()
			sys.exit()	
				
		# mise à l'heure GMT
		int_debut_heure = int(str_debut_heure)
		str_debut_heure = str(int_debut_heure)
		
		#mise au format de l'heure (2char)
		if len(str_debut_heure) == 1:
			str_debut_heure = "0"+str_debut_heure
		if debug:
			print("heure debut :"+str_debut_heure)
			
		# extraction des minutes du début d'intervention en fct de la longueur de chaine
		str_debut_minute = ligne[index_debut_heure+1:index_debut_heure+3]
		if debug:
			print("minute debut :"+str_debut_minute)
			
		# détection d'erreur
		if str_debut_minute.isdigit() == False or int(str_debut_minute)>59:
			print("ERREUR : parsing minutes de début, ligne : "+ligne)
			f.close()
			sys.exit()
			
		# extraction de l'heure de fin d'intervention en fct de la longueur de chaine et mise à l'heure GMT
		index_fin_heure=ligne.find("h",index_debut_heure+1)
		
		# détection d'erreur
		if not ligne[index_fin_heure-2:index_fin_heure].isdigit():
			print("ERREUR : parsing heure de fin. "+str_fin_heure+" n'est pas un entier, ligne : "+ligne)
			f.close()
			sys.exit()
			
		int_fin_heure = int(ligne[index_fin_heure-2:index_fin_heure])
		str_fin_heure = str(int_fin_heure)
		
		#mise au format de l'heure (2char)
		if len(str_fin_heure) == 1:
			str_fin_heure = "0"+str_fin_heure
		if debug:
			print("heure fin :"+str_fin_heure)
				
		# extraction des minutes de fin d'intervention en fct de la longueur de chaine
		str_fin_minute = ligne[index_fin_heure+1:index_fin_heure+3]
		if debug:
			print("minute fin :"+str_fin_minute)
		
		# détection d'erreur
		if str_fin_minute.isdigit() == False or int(str_fin_minute)>59:
			print("ERREUR : parsing minute de fin, ligne :"+ligne)
			f.close()
			sys.exit()
		
		# détection heure de fin < à heure de début
		if (int_debut_heure*60+int(str_debut_minute) > int_fin_heure*60+int(str_fin_minute)):
			print("ERREUR : heure de fin inf à heure de début, ligne :"+ligne)
			f.close()
			sys.exit()

		# concatenation des variables, mise au format ics/google de la date/heure de début de l'évènement
		str_data_dstart = str_year+str(num_mois)+str(num_jour)+"T"+str_debut_heure+str_debut_minute+"00"
		if verbose or debug:
			print("str_data_dstart :"+str_data_dstart)
		
		# concatenation des variables, mise au format ics/google de la date/heure de fin de l'évènement
		str_data_end = str_year+str(num_mois)+str(num_jour)+"T"+str_fin_heure+str_fin_minute+"00"
		if verbose or debug:
			print("   str_data_end :"+str_data_end)
		
			
		# extraction du nom de l'intervenante en fct de la longueur de chaine
		str_nom_inter = find_name_inter(ligne)

		
		# détection d'erreur
		if (str_nom_inter == False):
			print("ERREUR : parsing nom de l'intervenant, ligne :"+ligne)
			f.close()
			sys.exit()
		
		if verbose or debug:
			print("  str_nom_inter :"+str_nom_inter)

		# écriture de l'évènement au format ics dans le fichier file_name_ics
		f.write("BEGIN:VEVENT\n")			
		f.write("DTSTART;TZID=Europe/Paris:"+str_data_dstart+"\n")
		f.write("DTEND;TZID=Europe/Paris:"+str_data_end+"\n")
		# variable aujourd'hui
		aujourdhui = datetime.today().strftime('%Y%m%dT%H%M%SZ')
		f.write("DTSTAMP:"+aujourdhui+"\n")
		f.write("CREATED:"+aujourdhui+"\n")
		f.write("DESCRIPTION:\n")
		f.write("LAST-MODIFIED:"+aujourdhui+"\n")
		f.write("LOCATION:\n")
		f.write("SEQUENCE:1\n")
		f.write("STATUS:CONFIRMED\n")
		# nom de l'intervenante dans le résumé
		f.write("SUMMARY:ADMR "+str_nom_inter+"\n")
		f.write("TRANSP:OPAQUE\n")
		f.write("BEGIN:VALARM\n")
		f.write("ACTION:DISPLAY\n")
		f.write("DESCRIPTION:Intervention de l'ADMR\n")
		# rappel de l'évènement 5 min avant
		f.write("TRIGGER:-P0DT"+reminder_delay_hour+"H"+reminder_delay_minute+"M0S\n")
		f.write("END:VALARM\n")
		f.write("END:VEVENT\n")
		nb_interventions += 1

if debug:
	print("############### fin des boucles ###############")
# pied de page au format ics
f.write("END:VCALENDAR")
# fermeture du fichier enregistré
f.close()
print(str(nb_interventions)+" interventions trouvées")
print("Fichier "+file_name_ics+" enregistré")
print("Importez "+file_name_ics+" sur https://calendar.google.com/calendar/u/1/r/settings/export?pli=1")
# webbrowser.open('https://calendar.google.com/calendar/u/1/r/settings/export?pli=1')
