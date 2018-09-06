'''
maximeGirma
14/12/2017
version 1.0

La fonction recupere le fichier de configuration wifi, regarde si le précendent fichier
est différent, si c'est le cas elle charge le nouveau et redemmare pour charger la nouvelle
configuration.
'''

import os
import csv
from .conf import DATA_DIR

def get_conf_wifi(): #recupere les données pour configurer le wi-fi
    return_list = []
    with open(DATA_DIR + "/config_wifi.csv","r") as file: # ouverture du csv
        params_wifi = list(csv.reader(file,delimiter=","))
    return [param[1] for param in params_wifi[0:3]]#retourne SSID, PSSWD et type de securité

def config_wpa_supplicant(wifi_SSID,wifi_PASSWRD,wifi_safety_type):#chargement d'un template WPA_supplicant
    with open(DATA_DIR + "/wpa_template","r") as wpa_template:
#on remplit le template avec les infos recupérées precedemment
        connect_login = wpa_template.read().format(wifi_SSID,wifi_PASSWRD,wifi_safety_type)

    with open("/etc/wpa_supplicant/wpa_supplicant.conf","r") as fichier_wpa:
        wpa_original = fichier_wpa.read()

    if wpa_original != connect_login:
#On n'écrit que si les deux fichiers sont différents
        with open("/etc/wpa_supplicant/wpa_supplicant.conf","w") as fichier_wpa:
            fichier_wpa.write(connect_login)
        os.system("sudo reboot")#on reboot pour charger la nouvelle conf
    print("WIFI CORRECT")

def wifi_conf():

    params_wifi = get_conf_wifi()

    wifi_SSID = params_wifi[0] #les deux variables sont des str
    wifi_PASSWRD = params_wifi[1]
    wifi_safety_type = params_wifi[2]

    config_wpa_supplicant(wifi_SSID,wifi_PASSWRD,wifi_safety_type)
