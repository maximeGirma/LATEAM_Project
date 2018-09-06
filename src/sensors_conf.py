'''

KevinGeorget

12/12/2017

version 1.0



get_sensors_data() definit une classe d'objet "sensor" puis ouvre un fichier CSV

Elle construit ensuite une liste d'objets basées sur les caractèristiques du fichier CSV.

Elle renvoie ensuite cette liste au MAIN.

'''

import csv
from .conf import DATA_DIR


# definition de la class capteur


class Sensor:

    def __init__(self, mac, name):

        self.mac = mac

        self.name = name

        self.last_alert = 0


def get_sensors_data():

    sensors_list_return = []   # création de la liste d'objets "sensors"

    with open(DATA_DIR + '/sensors_conf.csv') as file:     # ouverture du CSV config
        sensors_conf = list(csv.reader(file, delimiter=','))
        file.readline()     # on consomme la 1ere ligne (entrée tableau)
        for row in sensors_conf:
            if row[1] == "":
                sensors_list_return.append(Sensor(row[0], "Aucun objet associé"))  # création/insertion des objets dans
                # la liste
            else:
                sensors_list_return.append(Sensor(row[0], row[1]))

    return sensors_list_return
