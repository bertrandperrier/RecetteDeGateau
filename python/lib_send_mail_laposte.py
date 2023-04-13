#! /usr/bin/python
import sys
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def EnvoyerEmail(sujet = "sans sujet", message = "sans message"):
	# email_expediteur == my email address
	# email_destinataire == recipient's email address
	email_expediteur = "<email exp>"
	email_destinataire = "<email dest>"
	mdp_expediteur = "<mot de passe exp>"
	 
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	sujet=sujet.replace("_", " ")
	msg['Subject'] = sujet
	msg['From'] = email_expediteur
	msg['To'] = email_destinataire

	# Create the body of the message (a plain-text and an HTML version).
	text = "echec de l envoie du message html"

	# remplacement _ par espace
	message=message.replace("_", " ")

	html = message

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)


	username = str(email_expediteur)  
	password = str(mdp_expediteur) 
	# Send the message via local SMTP server.
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() ## Specification de la securisation
	s.login(username, password)    ## Authentification

	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	s.sendmail(email_expediteur, email_destinataire, msg.as_string())
	s.quit()
