#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
DominiqueHathi
11/12/2017
version 1.0

La fonction prend en argument la liste des destinataires, des alertes et des alertes en attente.
Elle envoie une alerte correspondant aux listes aux destinataires.
- au démarrage pour indique au client que le système est en fonction
- ensuite, pour alerter en cas de mouvement d'objet
Elle renvoie au MAIN un False en cas d'erreur.
'''


import os
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from .conf import DATA_DIR


name_list = []

#date
date = datetime.datetime.now()

def format_welcome_mail(date):
    #partie entete de mail pour le démarrage
    subject = 'SecureStand vous souhaite le bienvenue'

    # partie corps de message pour le démarrage
    content = """Bonjour,
    votre système SecureStand a bien démarré
    à {}
    
    en pièce jointe vous trouverez un fichier récapitulatif des alertes.
    
    Cordialement,
    Le systeme SecureStand
    """.format(date)

    return subject, content

def format_alert_mail(name_list, date):
     #partie entete de mail pour les alertes
    subject = 'Alerte sur votre stand'

    # partie corps de message pour les alertes
    content = """Bonjour,
    le (les) capteur(s) de votre stand positionné(s) sur le(la) {}
    s'est déclenché
    à {}

    Cordialement,
    Le systeme SecureStand
    """.format(name_list, date)
    return subject, content


def notify(recipients_list, final_alert_list):

    # partie entete de mal commune
    msg = MIMEMultipart()
    msg['From'] = 'secure.stand2017@gmail.com'
    msg['To'] = ','.join(recipients_list)
    print(final_alert_list)

    if len(final_alert_list) == 0:

        #cas du mail de démarrage du sytème
        subject, content = format_welcome_mail(date)

        #add envoi d'un fichier historique
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(DATA_DIR + '/historique.csv',"rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{}"'
                        .format(os.path.basename(DATA_DIR + '/historique.csv')))
        msg.attach(part)

        print(subject, content)
    else:
        #cas du mail alerte
        subject, content = format_alert_mail([item.name for item in final_alert_list], date)

    # partie gestion de mail
    msg['Subject'] = subject
    msg.attach(MIMEText(content))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('secure.Stand2017@gmail.com', 'pythonlinux')
    mailserver.sendmail('secure.Stand2017@gmail.com', recipients_list, msg.as_string())
    print("mail envoyé")
    mailserver.quit()

    return True
