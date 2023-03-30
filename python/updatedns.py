#!/usr/bin/python
#doc https://api.gandi.net/docs/livedns/
import requests
import sys
#import urllib
import urllib.request as url
from urllib.error import HTTPError, URLError
import smtplib    ## Importation du module
import datetime

from socket import timeout

verbose = 0
if len(sys.argv) > 1:
	if sys.argv[1] == "-v":
		verbose = 1
 
headers = {'authorization': 'Apikey <your api key of gandy>'}


ip=""
# Recupere l'Ip externe http://monip.outils-rezo.info/text
try:
	ip = url.urlopen("http://monip.outils-rezo.info/text").read().decode()
	#page = url.urlopen("http://www.monip.org/").read()
	#ip = page.split("IP : ")[1].split("<br>")[0]
	#ip = url.urlopen('http://ip.42.pl/raw').read()
except HTTPError as error:
    logging.error('HTTP Error: Data of %s not retrieved because %s\nURL: %s', name, error, url)
    sys.exit()
except URLError as error:
    if isinstance(error.reason, timeout):
        print ("Timeout Error: Data not retrieved because %s\nURL: %s" % (error, url))
        exit()
    else:
        print ("URL Error: Data not retrieved because %s\nURL: %s" % (error, url))
        exit()

except url.socket.error as e:
	print ("URLError : Une autre erreur avec le serveur : "+str(e))
	exit()
except url.HTTPError as e:
	print ("HTTPError : Le serveur n a pas pu repondre a la demande.")
	print ('Code erreur : ', e.code)
	exit()
except url.URLError as e:
	print ("URLError : Nous n\'avons pas reussi a atteindre le serveur .")
	print ("Code erreur : ", e.reason)
	exit()
except Exception as e:
	print("oups",e)
	exit()



#api gandy GET @
url = "https://api.gandi.net/v5/livedns/domains/<domain name>/records/@/A"
response = requests.request("GET", url, headers=headers)
#print(response.text)


#api gandy GET www
url = "https://api.gandi.net/v5/livedns/domains/<domain name>/records/www/A"
response = requests.request("GET", url, headers=headers)


#l'adresse ip est differente
if response.text.find(str(ip)) == -1:
	now = datetime.datetime.now()
	print (now.strftime("%d/%m/%Y %H:%M:%S "))
	print ("******ip differente, faire le PUT A******")
	if verbose == 0:
		serveur = smtplib.SMTP('smtp.gmail.com', 587) ## Connexion au serveur sortant (en precisant son nom et son port)
		serveur.starttls() ## Specification de la securisation
		serveur.login("<login>", "<password>")    ## Authentification
		message = "subject: envoi put \nenvoi d'un PUT "+str(ip)    ## Message a envoyer
		serveur.sendmail("<your email>", "<your email>", message)    ## Envoie du message
		serveur.quit()    ## Deconnexion du serveur

	next_put = {"rrset_type" : "@",	"rrset_values" : [str(ip)]}
	
	print("PUT A")
	print(next_put)
	url = "https://api.gandi.net/v5/livedns/domains/<domain name>/records/@/A"
	response = requests.put(url, json=next_put, headers=headers)
	print("reponse du put A")
	print(response.text)

	next_put = {"rrset_type" : "www", "rrset_values" : [str(ip)]}
	
	print("PUT www")
	print(next_put)
	url = "https://api.gandi.net/v5/livedns/domains/<domain name>/records/www/A"
	response2 = requests.put(url, json=next_put, headers=headers)
	print("reponse du put www")
	print(response2.text)

	if verbose == 0:
		serveur = smtplib.SMTP('smtp.gmail.com', 587) ## Connexion au serveur sortant (en precisant son nom et son port)
		serveur.starttls() ## Specification de la securisation
		serveur.login("<login>", "<password>")    ## Authentification
		message = "subject: reponse put \nreponse des PUT. put1:"+response.text+". put2:"+response2.text    ## Message a envoyer
		serveur.sendmail("<your email>", "<your email>", message)    ## Envoie du message
		serveur.quit()    ## Deconnexion du serveur
else:
	if verbose:
		print ("******ip identique*****")
