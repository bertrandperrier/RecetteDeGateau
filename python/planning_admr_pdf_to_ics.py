#!/usr/bin/python3
#
# ce programme convertit un planning de l'ADMR du format pdf au format ics
# to do : use .split(' ')

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
year = "2024"
# liste d'éléments des jours et des mois
days_of_the_week = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
months_of_the_year = ["Janvier", "Février", "Mars", "Avril", "Mai ", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

# variable année, à modifier si le planning ne concerne pas l'année en cours
int_year = int(datetime.today().strftime('%Y'))

# pour afficher les infos de débuggage
verbose = 0
debug = 0
if len(sys.argv) > 1:
	if sys.argv[1] == "-debug":
		debug = 1
	if sys.argv[1] == "-v":
		verbose = 2
	if sys.argv[1] == "-h":
		print("Utilisation :")
		print(os.path.basename(__file__)+"  [OPTION...]\n")
		print("Options de l'application :")
		print("  -debug                    mode verbose")
		print("  -v                        show date value in ics format")
		sys.exit()

# converti le nom du jour en int (lundi=0, ...=6)
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
	arg_day_txt=arg_day_txt.lower()
	is_day = False
	for jour in days_of_the_week:
		if arg_day_txt[0:5] == jour[0:5]:
			is_day = True
	return is_day

# converti le nom d'un mois en int (Janvier=1, ...)
def month_txt_to_int(arg_month_txt):
	i = 1
	for month in months_of_the_year:
		if month[0:4].lower() == arg_month_txt[0:4].lower():
			if len(str(i)) == 2:
				return i
			else:
				return "0"+str(i)
		i=i+1
	return False

# renvoi le décalage horaire avec GMT, -1 en hiver -2 en été
def calc_heure_ete_hiver(annee, mois, jour, heure, minute, seconde):
	heure_input=datetime(annee, mois, jour, heure, minute, seconde)
	#local_tnz = pytz.reference.LocalTimezone() # tz de l'ordinateur
	local_tnz = pytz.timezone("Europe/Paris") # tz de Paris
	decal_heure_ete_hiver_gmt = local_tnz.utcoffset(heure_input)
	decal_heure_ete_hiver_gmt = -int(decal_heure_ete_hiver_gmt.seconds/3600)
	return decal_heure_ete_hiver_gmt

#renvoie le nom de l'intervenante
def find_name_inter(ligne_txt):
	r=0
	i = len(ligne_txt)-1
	while i != 0:
		if (ligne_txt[i].isdigit()):
			r = i
			return str(ligne_txt[r+2:r+30])
		i -= 1
	return False
	
# création d'un objet lecteur pdf
reader = PdfReader(file_name_pdf)

# récupérer la première page du pdf (0=1ère page)
page = reader.pages[0]

# extraction du texte de la page
text = page.extract_text()
if debug:
	print(text)
result_par_ligne = []
index = 0
x=0

# converti le texte du pdf en liste d'éléments (1 ligne par élément)
while x != -1:
	x=text.find("\n")
	if x != -1:
		result_par_ligne.insert(index, text[0:x]) 
		text=text[x+1:-1]
	index = index+1

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
#TZOFFSETFROM est le décalage heure d'été est en fonctionnement
f.write("TZOFFSETFROM:+0200\n")
#TZOFFSETTO est le décalage heure standard est en fonctionnement.
f.write("TZOFFSETTO:+0100\n")
f.write("TZNAME:CEST\n")
f.write("DTSTART:19700329T020000\n")
f.write("RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU\n")
f.write("END:DAYLIGHT\n")
f.write("BEGIN:STANDARD\n")
f.write("TZOFFSETFROM:+0200\n")
f.write("TZOFFSETTO:+0100\n")
f.write("TZNAME:CET\n")
f.write("DTSTART:19701025T030000\n")
f.write("RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU\n")
f.write("END:STANDARD\n")
f.write("END:VTIMEZONE\n")

# extraction des données pour chaque élément du array
for ligne in result_par_ligne:
	if debug:
		print("############### nouvelle boucle ###############")
		print("is_day_name :"+str(is_day_name(ligne)))
	# si la ligne commence par le nom d'un jour de semaine
	if is_day_name(ligne):
		if debug:
			print("ligne agenda :"+ligne)
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
			print("ERROR : parsing month "+nom_mois+" is not name of month")
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
		
		# calcul décalage entre l'heure du pdf et gmt (-1 en hiver, -2 en été)
		decal_heure_ete_hiver_gmt = calc_heure_ete_hiver(int_year, int(num_mois), int(num_jour), 12, 0, 0)
		if debug:
			print("decal_heure_ete_hiver_gmt :"+str(decal_heure_ete_hiver_gmt))
		
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
		int_debut_heure = int(str_debut_heure)+decal_heure_ete_hiver_gmt
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
			print("ERREUR : parsing minutes de début, line :"+ligne)
			f.close()
			sys.exit()
			
		# extraction de l'heure de fin d'intervention en fct de la longueur de chaine et mise à l'heure GMT
		index_fin_heure=ligne.find("h",index_debut_heure+1)
		int_fin_heure = int(ligne[index_fin_heure-2:index_fin_heure])+decal_heure_ete_hiver_gmt
		str_fin_heure = str(int_fin_heure)
		
		#mise au format de l'heure (2char)
		if len(str_fin_heure) == 1:
			str_fin_heure = "0"+str_fin_heure
		if debug:
			print("heure fin :"+str_fin_heure)
		
		# détection d'erreur
		if str_fin_heure.isdigit() == False or int(str_fin_heure)>24:
			print("ERREUR : parsing heure de fin. "+str_fin_heure+" n'est pas un entier ou est supérieur à 24, ligne :"+ligne)
			f.close()
			sys.exit()
		
		# extraction des minutes de fin d'intervention en fct de la longueur de chaine
		str_fin_minute = ligne[index_fin_heure+1:index_fin_heure+3]
		if debug:
			print("minute fin :"+str_fin_minute)
		
		# détection d'erreur
		if str_fin_minute.isdigit() == False or int(str_fin_minute)>59:
			print("ERROR : parsing ending minute, line :"+ligne)
			f.close()
			sys.exit()
		
		# détection heure de fin < à heure de début
		if (int_debut_heure*60+int(str_debut_minute) > int_fin_heure*60+int(str_fin_minute)):
			print("ERROR : hour ending befor hour begin , line :"+ligne)
			f.close()
			sys.exit()
		
		# concatenation des variables, mise au format ics/google de la date/heure de début de l'évènement
		str_data_dstart = year+str(num_mois)+str(num_jour)+"T"+str_debut_heure+str_debut_minute+"00Z"
		if verbose or debug:
			print("str_data_dstart :"+str_data_dstart)
		
		# concatenation des variables, mise au format ics/google de la date/heure de fin de l'évènement
		str_data_end = year+str(num_mois)+str(num_jour)+"T"+str_fin_heure+str_fin_minute+"00Z"
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

		# écriture de l'évènement au format ics/google dans le fichier file_name_ics
		f.write("BEGIN:VEVENT\n")
		f.write("DTSTART:"+str_data_dstart+"\n")
		f.write("DTEND:"+str_data_end+"\n")
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
		f.write("DESCRIPTION:This is an event reminder\n")
		# rappel de l'évènement 5 min avant
		f.write("TRIGGER:-P0DT"+reminder_delay_hour+"H"+reminder_delay_minute+"M0S\n")
		f.write("END:VALARM\n")
		f.write("END:VEVENT\n")
	else:
		print("######### ERREUR LECTURE DE LIGNE #########");
		print("ligne -> "+ligne);
		f.close()
		sys.exit()
if is_day_name(ligne):
	# pied de page au format ics
	f.write("END:VCALENDAR")
	# fermeture du fichier enregistré
	f.close()
	print("Fichier "+file_name_ics+" enregistré")
	print("https://calendar.google.com/calendar/u/1/r/settings/export?pli=1")
	# webbrowser.open('https://calendar.google.com/calendar/u/1/r/settings/export?pli=1')
