'''
KevinGeorget
12/12/2017
version 1.0

Les deux fonctions de filtre viennent appliquer un traitement à leur liste d'entrée et
retournent une liste au MAIN

La fonction mac_filter() prend en argument la liste globale de tous les objets scannés
et la liste des capteur(sensors_list)
Elle compare la liste globale aux adresses mac des objets stockés dans la liste des capteurs
(sensors_list[].MAC). Si ils sont présents ils sont ajouté a une liste renvoyé au MAIN

La fonction time_filter() prend la liste d'alerte en argument.
Elle verifie que la dernière alerte pour un objet donné remonte bien à plus de <alert_frequence> secondes
Si oui l'objet est ajouté à la final_alerte_list.
Puis la la final_alert_list est renvoyeée au MAIN

'''



import time

def mac_filter(global_list,sensors_list): #compare les MAC des appareils bluetooth scannés avec les MAC des capteurs

    alert_list_return = []                   #purge de la liste d'alerte en entrée de fonction
    for scanned_mac in global_list:             #compare chaque élement de global_list
        for sensor in sensors_list:
            sensor_mac = sensor.mac
            is_a_sensor = (scanned_mac == sensor_mac)
            if is_a_sensor:
                alert_list_return.append(sensor)

    return alert_list_return


def time_filter(alert_list,alert_frequence):

    final_alert_list_return = []

    for item in alert_list:         # on itère sur chaque objet de alert_list

        if (time.time() - item.last_alert) > alert_frequence:  # si la dernière alerte est plus ancienne que 60 sec

            final_alert_list_return.append(item)  # on ajoute l'objet dans la liste finale

    return final_alert_list_return
