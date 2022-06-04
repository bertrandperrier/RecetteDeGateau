#!/usr/bin/python
#doc https://api.gandi.net/docs/livedns/
import requests
import sys
import urllib
import smtplib    ## Importation du module
import datetime

verbose = 0
if len(sys.argv) > 1:
	if sys.argv[1] == "-v":
		verbose = 1
 
headers = {'authorization': 'Apikey g1ylRLygkJxgLQ2sG7XM6v63'}





# Recupere l'Ip externe
try:
	page = urllib.urlopen("http://www.monip.org/").read()
	ip = page.split("IP : ")[1].split("<br>")[0]
	#ip = urllib.urlopen('http://ip.42.pl/raw').read()
except urllib.request.socket.timeout as e:
	print (" Time-out .")
	exit()
except urllib.request.socket.error as e:
	print ("URLError : Une autre erreur avec le serveur .")
	exit()
except urllib.request.HTTPError as e:
	print ("HTTPError : Le serveur n a pas pu repondre a la demande.")
	print ('Code erreur : ', e.code)
	exit()
except urllib.request.URLError as e:
	print ("URLError : Nous n\'avons pas reussi a atteindre le serveur .")
	print ("Code erreur : ", e.reason)
except Exception as e:
	print("oups",e)


#print (ip)
#api gandy GET @
url = "https://api.gandi.net/v5/livedns/domains/bertrandperrier.fr/records/@/A"
response = requests.request("GET", url, headers=headers)
#print("GET @")
#print(response.text)


#api gandy GET www
url = "https://api.gandi.net/v5/livedns/domains/bertrandperrier.fr/records/www/A"
response = requests.request("GET", url, headers=headers)
## print("GET www")


#l'adresse ip est differente
if response.text.find(str(ip)) == -1:
	now = datetime.datetime.now()
	print (now.strftime("%d/%m/%Y %H:%M:%S "))
	print ("******ip differente, faire le PUT A******")
	if verbose == 0:
		serveur = smtplib.SMTP('smtp.gmail.com', 587) ## Connexion au serveur sortant (en precisant son nom et son port)
		serveur.starttls() ## Specification de la securisation
		serveur.login("bertrandperrier", "aqshqdvsdjtmrasx")    ## Authentification
		message = "subject: envoi put \nenvoi d'un PUT "+str(ip)    ## Message a envoyer
		serveur.sendmail("bertrandperrier@gmail.com", "bertrandperrier@laposte.net", message)    ## Envoie du message
		serveur.quit()    ## Deconnexion du serveur

	next_put = {"rrset_type" : "@",	"rrset_values" : [str(ip)]}
	
	print("PUT A")
	print next_put
	url = "https://api.gandi.net/v5/livedns/domains/bertrandperrier.fr/records/@/A"
	response = requests.put(url, json=next_put, headers=headers)
	print("reponse du put A")
	print(response.text)

	next_put = {"rrset_type" : "www", "rrset_values" : [str(ip)]}
	
	print("PUT www")
	print next_put
	url = "https://api.gandi.net/v5/livedns/domains/bertrandperrier.fr/records/www/A"
	response2 = requests.put(url, json=next_put, headers=headers)
	print("reponse du put www")
	print(response2.text)

	if verbose == 0:
		serveur = smtplib.SMTP('smtp.gmail.com', 587) ## Connexion au serveur sortant (en precisant son nom et son port)
		serveur.starttls() ## Specification de la securisation
		serveur.login("bertrandperrier", "aqshqdvsdjtmrasx")    ## Authentification
		message = "subject: reponse put \nreponse des PUT. put1:"+response.text+". put2:"+response2.text    ## Message a envoyer
		serveur.sendmail("bertrandperrier@gmail.com", "bertrandperrier@laposte.net", message)    ## Envoie du message
		serveur.quit()    ## Deconnexion du serveur
else:
	if verbose:
		print ("******ip identique*****")
