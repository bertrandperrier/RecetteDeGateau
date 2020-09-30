#https://api.gandi.net/docs/livedns/
import requests
import urllib
url = "https://api.gandi.net/v5/domain/domains"
headers = {'authorization': 'Apikey -your-api-key'}
#response = requests.request("GET", url, headers=headers)
#print(response.text)

# Recupere l'Ip externe
page = urllib.urlopen("http://www.monip.org/").read()
ip = page.split("IP : ")[1].split("<br>")[0]
print ("ip")
print (ip)

#api gandy GET
url ="https://api.gandi.net/v5/livedns/domains/your-domaine-name/records/@/A"
response = requests.request("GET", url, headers=headers)
print ("GET")
print(response.text)

next_put = '{"rrset_type":"A","rrset_ttl":300,"rrset_name":"@","rrset_href":"https://api.gandi.net/v5/livedns/domains/your-domaine-name/records/@/A/api/v5/domains/your-domaine-name/records/%40/A","rrset_values":["'

next_put2 = """"]}"""
next_put = next_put+str(ip)+next_put2


#l'adresse ip est differente
if next_put.find(str(ip)) == -1:
	print (next_put.text)
	next_put[rrset_name] = "www"
	print (next_put.text)
	url = "https://api.gandi.net/v5/livedns/domains/your-domaine-name/records"
	#rrset_name="@"
	#rrset_type="A"
	#rrser_values=str(ip)
	response = requests.put(url, data=next_put, headers=headers)
	print("reponse du put")
	print(response.text)
else:
	print ("ip identique, pas de PUT")
