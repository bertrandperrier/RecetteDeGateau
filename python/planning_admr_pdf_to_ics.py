#!/usr/bin/python3
#
# ce programme convertit un planning de l'ADMR du format pdf au format ics
#
# importing required modules
from PyPDF2 import PdfReader
import sys
from datetime import datetime
import webbrowser
import pytz.reference

file_name_pdf = "planning_admr.pdf"
file_name_ics = "planning_admr.ics"
# variable pour le calcul du décalalge horaire
heure_hiver = -1
heure_ete = -2

decal_heure_ete_hiver_gmt = heure_ete

# tableaux des jours et mois
jours_de_la_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
mois_de_l_annee = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

# pour afficher les infos de débuggage
verbose = 0
if len(sys.argv) > 1:
	if sys.argv[1] == "-v":
		verbose = 1

# converti le nom du jour en int (lundi=0, ...=6)
def day_txt_to_int(jour_txt):
	if verbose:
		print("jour_txt:"+jour_txt)
	i = 0
	for jours in jours_de_la_semaine:
		#if verbose:
			#print("jours : "+jours)
		if jours[0:2] == jour_txt[0:2]:
			return i
		i=i+1
	return False

# vérifie si l'argument est le nom d'un jour de la semaine
def is_day_name(jour_txt):
	is_day = False
	for jour in jours_de_la_semaine:
		#if verbose:
			#print("jours : "+jour)
			#print("jour_txt :"+jour_txt)
		if jour_txt[0:2] == jour[0:2]:
			is_day = True
	return is_day

# converti le nom d'un mois en int (1=Janvier, ...)
def month_txt_to_int(mois_txt):
	i = 1
	for mois in mois_de_l_annee:
		if mois[0:4] == mois_txt[0:4]:
			if len(str(i)) == 2:
				return i
			else:
				return "0"+str(i)
		i=i+1
	return False

def calc_heure_ete_hiver(annee, mois, jour, heure, minute, seconde):
	heure_input=datetime(annee, mois, jour, heure, minute, seconde)
	local_tnz = pytz.reference.LocalTimezone()
	#local_tnz = pytz.timezone("Europe/Paris")
	decal_heure_ete_hiver_gmt = local_tnz.utcoffset(heure_input)
	decal_heure_ete_hiver_gmt = -int(decal_heure_ete_hiver_gmt.seconds/3600)
	return decal_heure_ete_hiver_gmt

# création d'un objet lecteur pdf
reader = PdfReader(file_name_pdf)
 
 
# récupérer la première page du pdf (0=1ère page)
page = reader.pages[0]

# extraction du texte de la page
text = page.extract_text()
if verbose:
	print(text)
result_par_ligne = []
index = 0
x=0

# converti le texte du pdf en array (1 ligne par élément)
while x != -1:
	x=text.find("\n")
	if x != -1:
		result_par_ligne.insert(index, text[0:x]) 
		text=text[x+1:-1]
	index = index+1

# ouverture du fichier d'enregistrement
f = open(file_name_ics, "w")

# entete au format ics
#TZOFFSETFROM est le décalage heure d'été est en fonctionnement
#TZOFFSETTO est le décalage heure standard est en fonctionnement.

f.write("BEGIN:VCALENDAR\n")
f.write("PRODID:-//Google Inc//Google Calendar 70.9054//EN\n")
f.write("VERSION:2.0\n")
f.write("CALSCALE:GREGORIAN\n")
f.write("METHOD:PUBLISH\n")
f.write("X-WR-CALNAME:<your email>\n")
f.write("X-WR-TIMEZONE:Europe/Paris\n")
f.write("BEGIN:VTIMEZONE\n")
f.write("TZID:Europe/Paris\n")
f.write("X-LIC-LOCATION:Europe/Paris\n")
f.write("BEGIN:DAYLIGHT\n")

f.write("TZOFFSETFROM:+0200\n")
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
	if verbose:
		print("is_day_name :"+str(is_day_name(ligne)))
	# si la ligne commence par le nom d'un jour de semaine
	if is_day_name(ligne):
		if verbose:
			print("ligne agenda :"+ligne)
		#récupération du nom du jour de la semaine 
		nom_jour = jours_de_la_semaine[day_txt_to_int(ligne)]
		if verbose:
			print("jour int :"+str(day_txt_to_int(ligne)))
			print("jour :"+str(nom_jour))
		# calcul de la longeur du nom de la semaine pour un futur parsing
		len_jour = len(nom_jour)
		# extraction du numéro du jour
		num_jour = ligne[len_jour+1:len_jour+3]
		if verbose:
			print("num jour :"+num_jour)
		# extractoin du nom du mois
		nom_mois = ligne[len_jour+4:len_jour+8]
		# conversion du nom du mois en int
		num_mois = month_txt_to_int(nom_mois)
		if verbose:
			print("num_mois :"+str(num_mois))
		# longeur du nom du mois et du jour
		len_mois = len(nom_mois)+len_jour
		
		decal_heure_ete_hiver_gmt = calc_heure_ete_hiver(2023, int(num_mois), int(num_jour), 12, 0, 0)
		if verbose:
			print("decal_heure_ete_hiver_gmt :"+str(decal_heure_ete_hiver_gmt))
		# extraction de l'heure du début d'intervention en fct de la longueur de chaine et calcul en fct de l'heure d'été/hiver
		int_debut_heure = int(ligne[len_mois+8:len_mois+10])+decal_heure_ete_hiver_gmt
		str_debut_heure = str(int_debut_heure)

		if len(str_debut_heure) == 1:
			str_debut_heure = "0"+str_debut_heure
		if verbose:
			print("heure debut :"+str_debut_heure)
		# extraction des minutes du début d'intervention en fct de la longueur de chaine
		str_debut_minute = ligne[len_mois+11:len_mois+13]
		if verbose:
			print("minute debut :"+str_debut_minute)
		

		
		# extraction de l'heure de fin d'intervention en fct de la longueur de chaine et calcul en fct de l'heure d'été/hiver
		int_fin_heure = int(ligne[len_mois+16:len_mois+18])+decal_heure_ete_hiver_gmt
		str_fin_heure = str(int_fin_heure)
		if len(str_fin_heure) == 1:
			str_fin_heure = "0"+str_fin_heure
		
		if verbose:
			print("heure fin :"+str_fin_heure)
		# extraction des minutes de fin d'intervention en fct de la longueur de chaine
		str_fin_minute = ligne[len_mois+19:len_mois+21]
		if verbose:
			print("minute fin :"+str_fin_minute)
		# concatenation des variables, mise au format ics/google de la date/heure de début de l'évènement
		str_data_dstart = "2023"+num_mois+num_jour+"T"+str_debut_heure+str_debut_minute+"00Z"
		if verbose:
			print(str_data_dstart)
		# concatenation des variables, mise au format ics/google de la date/heure de fin de l'évènement
		str_data_end = "2023"+num_mois+num_jour+"T"+str_fin_heure+str_fin_minute+"00Z"
		if verbose:
			print(str_data_end)
		# extraction du nom de l'intervenante en fct de la longueur de chaine
		str_nom_inter = ligne[len_mois+28:len_mois+70]
		if verbose:
			print("str_nom_inter :"+str_nom_inter)

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
		f.write("END:VEVENT\n")


# pied de page au format ics
f.write("END:VCALENDAR")
# fermeture du fichier enregistré
f.close()



# ouvrir l'url https://calendar.google.com/calendar/u/1/r/settings/export?pli=1

#webbrowser.open('https://calendar.google.com/calendar/u/1/r/settings/export?pli=1')
