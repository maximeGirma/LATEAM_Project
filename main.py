#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

'''
MaximeGirma -- KévinGeorget -- KomlaganTekou -- DominiqueHathi -- 13/12/2017
11/12/2017
version 1.0

La fonction Main est lancée par le systemd au démarrage du Raspberry
Elle centralise toutes les autres fonctions et organise l'ensemble du système.

Elle apelle des fonctions pour charger la configuration et s'assurer de la connexion internet.

Commence ensuite une boucle infinie dans laquelle on va:
1)Scanner les signaux bluetooth -- bluetooth_scan()
2)Traiter les signaux pour ne garder que les pertinents-- mac_filter(), time_filter()
3)envoyer des alertes par e-mail-- notify()
4)Ecrit dans l'historique -- write_histo()
5)Eventuellement, gestion des erreurs dues à une deconnexion wifi -- waiting_list()
A chaque étape des sécurités viennent s'assurer de la bonne marche du système.
'''

from src.auto_mount import auto_mount
auto_mount()#on commence par importer les fichiers de configuration de la clé usb
#import des fichiers .py
from src.blescan import bluetooth_scan
from src.alert_frequence_conf import get_alert_frequence_data
from src.recipients_conf import get_recipients_data
from src.sensors_conf import get_sensors_data
from src.filters import mac_filter
from src.filters import time_filter
from src.notify import notify
from src.update_sensors_list import update_sensors_list
from src.test_conf import test_conf_file
from src.write_historic import write_histo
from src.wifi_conf import wifi_conf

#import des biblios
#from bluepy.btle import Scanner, DefaultDelegate
import time
#import csv
#import os
#import smtplib
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText


print("LA")

if test_conf_file():  # si le test renvoie vrai on peut y aller, sinon, on quitte le main
    print("DEDANS")
    # Déclaration des objets utiles au programme:
    global_list = []    # liste des appareils bluetooth scannés par le BLE
    sensors_list = get_sensors_data()   # liste des objets capteurs déployés (sensors_conf.py)
    alert_list = []     # liste des capteurs détectés lors du scan (blescan.py/mac_filter())
    final_alert_list = []  # liste des capteurs d'alert_list qui ont une alerte plus ancienne que 60s (time_filter.py)
    mail_sended = False  # bool pour savoir si le mail est bien parti
    waiting_list = []   # liste d'attente contenant les capteurs pour qui le mail n'a pas pu être envoyé
    recipients_list = get_recipients_data()  # liste des destinataires des mails d'alerte (recipients_conf.py)
    alert_frequence = get_alert_frequence_data()      # fréquence d'alerte choisie par l'utilisateur RECUP DANS CSV!!!!

    #wifi_conf()  # charge d'éventuelles login wifi
    notify(recipients_list, final_alert_list)  # envoie d'un message de bienvenue

    while True:  # A partir d'ici le programme tournera jusqu'a l'arret du rasp
        print("on est dans la boucle")
        global_list = bluetooth_scan()  # On recupere notre liste d'objets scannés

        if len(global_list) == 0:  # On s'assure qu'il y a quelque chose
            time.sleep(5)  # On attend 5 sec avant de relancer le scan bluetooth
            continue

        alert_list = mac_filter(global_list, sensors_list)  # on crée notre liste d'alerte en filtrant une premiere fois

        if len(alert_list) == 0:  # si ya rien on rescanne immediatement
            continue

        final_alert_list = time_filter(alert_list, alert_frequence)  # filtre la alert_list en fonction de la derniere alerte

        if len(final_alert_list) == 0:  # si ya rien on rescanne immediatement
            continue

        mail_sended = notify(recipients_list, final_alert_list)

        if mail_sended:

            sensors_list = update_sensors_list(sensors_list, final_alert_list)  # met a jour le item.last_alert

            write_histo(recipients_list, final_alert_list)  # ecrit le nom du capteur et l'heure actuelle dans l'histo

            for sensor in waiting_list:  # le mail est parti avec la waiting list, donc on peut la del
                del sensor

        else:                           # si le mail a échoué
            for alert in final_alert_list:
                waiting_list.append(alert)  # ajout des alertes a la waiting list pour le prochain tour
