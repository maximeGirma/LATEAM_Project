'''
KevinGeorget
13/12/2017
Version 1.0

La fonction bluetooth_scan utilise la librairie BluePy pour scanner tous les appareils bluetooth
proches. La fonction récupère les adresses MAC de ces appareils et les stocke dans une liste (global_list)
Cette liste d'adresse MAC est ensuite renvoyée à la fonction MAIN.
'''


from bluepy.btle import Scanner


def bluetooth_scan():



    devices = Scanner().scan(10.0)
    global_list = []
    # injecte les adresse Mac de tous les appareils dans une global_list
    for dev in devices:
        global_list.append(dev.addr)

    return global_list

