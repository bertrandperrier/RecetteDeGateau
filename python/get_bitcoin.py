#!/usr/bin/python

import sys
import urllib.request as url
import smtplib
import os
import lib_send_mail_laposte

verbose = 0
if len(sys.argv) > 1:
	if sys.argv[1] == "-v":
		verbose = 1

fichier = open('/home/bertrand/linux/script/get_bitcoin.txt', 'r')
valeur_basse = fichier.read()
fichier.close()
	
#code_html = urllib.urlopen('http://bitcoin.fr').read()
#index = code_html.find('mcw-price')
#if verbose:
	#print('BitCoin.fr')
	#print(code_html[index+114:index+120])
#BT=int(code_html[index+114:index+116]+code_html[index+117:index+120])
#if verbose:
	#print BT


code_html = url.urlopen('https://www.coinhouse.com/fr/cours-bitcoin/').read()

index = code_html.find(b'font-medium font-dm-sans-36 text-32 flex flex-row flex-wrap gap-3">')
if verbose:
	print("BITCOIN")
	print("code html : ")
	print(code_html[index+67:index+69]+code_html[index+70:index+73])
CH=int(code_html[index+67:index+69]+code_html[index+70:index+73])

#code_html = urllib.urlopen('https://www.google.com/finance/quote/BTC-EUR').read()

#index = code_html.find('YMlKec fxKbKc')
#if verbose:
	#print('Google')
	#print(code_html[index+15:index+21])
#GO=int(code_html[index+15:index+17]+code_html[index+18:index+21])
if verbose:
	#print GO
	print('achete   à 35549 et 32872')
	print('rentable à 36588')
	print('vendre   à 50000')
	print('vendu    à 62000')

#ni gain ni perte
#if CH > 38262:
#mise double
"""
if CH > 50000:
	if verbose:
		print("50000 soit 273,3 euros")
	else:
		lib_send_mail_laposte.EnvoyerEmail("Bitcoin haut", "vendre\nValeur BC : "+str(CH)+"\ngain minimum 73,30")
"""
if verbose:
	print('CoinHouse : '+str(CH))
	print('Valeur basse : '+str(valeur_basse))
	

	
if int(CH) < int(valeur_basse):
	with open('/home/bertrand/linux/script/get_bitcoin.txt', "w") as fichier:  #efface le contenu du fichier
		# fichier.write(str(CH))
		fichier = open('/home/bertrand/linux/script/get_bitcoin.txt', "a")
		fichier.write(str(CH))
		fichier.close()
	if verbose:
		print("acheter des BTC : cour bas")
	else:
		lib_send_mail_laposte.EnvoyerEmail("Bitcoin bas", "valeur basse \nValeur BC : "+str(CH)+"\nAcheter des bitcoins")

#if CH < 50000 and CH > 36588:
#	if verbose:
#		print("investissement rentable patienter")
#	else:
#		lib_send_mail_laposte.EnvoyerEmail("Bitcoin rentable", "investissement rentable patienter \nValeur BC : "+str(CH)+"\nvendre a 50 000")

if CH < 36588:
	if verbose:
		print("investissement rentable patienter")
	else:
		lib_send_mail_laposte.EnvoyerEmail("Bitcoin rentable", "acheter des BTC : cour bas\nValeur BC : "+str(CH))
		
