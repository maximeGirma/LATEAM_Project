#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-
'''
DominiqueHathi
11/12/2017
version 1.0

La fonction écrit un historique dans un fichier texte. Cet historique comprend le nom des capteurs envoyés
par e-mail, l'heure et la date ainsi que les destinataires.
'''
import datetime # import pour gérer les dates
import csv
from .conf import DATA_DIR


def write_histo(recipients_list, final_alert_list):

    date = str(datetime.datetime.now())

    #definiton de ce qu'il y a à écrire
    name_list = []
    for item in final_alert_list:
        name_list.append(item.name)



    data = [name_list,recipients_list,date]
    print(data)

    # utilitaire pour écrire dans un file historique
    with open(DATA_DIR + '/historique.csv','a') as csvfile:
        newFileWriter = csv.writer(csvfile)
        newFileWriter.writerow(data)
        print('yess write')

    return
