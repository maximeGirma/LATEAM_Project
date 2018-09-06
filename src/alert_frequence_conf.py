'''
MaximeGirma
13/12/2017 -- 11H51
Version 1.0

Cette fonction récupère le contenu d'un fichier CSV, s'assure qu'il est conforme (sinon utilise une
valeur par défaut) puis le renvoie à la fonction MAIN
Cette valeur servira à configurer le délai entre deux alertes.
'''


import csv
from .conf import DATA_DIR


def get_alert_frequence_data():

    alert_frequence = 0

    try:
        with open(DATA_DIR + '/alert_frequence.csv') as file: # ouverture du csv
            temporary = list(csv.reader(file))# les 3 lignes suivantes servent à recuperer un int en le sortant
            temporary2 = temporary[0]#          par à coup de la double liste
    except FileNotFoundError:
        alert_frequence = 60
        print("NO ALERT_FREQUENCE.CSV")
        return alert_frequence

    try:
        alert_frequence = int(temporary2[0]) #On verifie que la valeur est un entier
    except ValueError:
        alert_frequence = 60 #assignation valeur par défaut

    if alert_frequence < 0: # on verifie que l'entier est positif
        alert_frequence = 60 #assignation valeur par defaut


    return alert_frequence
