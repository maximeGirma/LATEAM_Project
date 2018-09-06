#creer un crontab pour le faire marcher. toutes les 5 minutes
#exemple : */5 *   * * *   root    /usr/local/bin/wifi_rebooter.sh

'''
MaximeGirma
12/12/2017
version 1.0

Ce script vérifie l'état de la connexion wifi et si besoin la reboot.
'''
import os
from time import sleep

a = os.system("ping 8.8.8.8 -c 1") #ping google
if a != 0:
    os.system("sudo ifdown --force wlan0") #si le ping échoue --> reconnection au wifi
    sleep(2)
    os.system("sudo ifup wlan0")
