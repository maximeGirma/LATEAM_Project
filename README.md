

# Context

Nous sommes une equipe projet, en formation de dev au Cesi.

# Projet SecureStand

Dans le cadre de notre stage, nous avons réalisé un projet client.
Nous l'appelons SecureStand

Notre client, une société de sécurité, veut un produit lui permettant de surveiller des objets (pc portable, 
coffre, etc...) sur un stand d'exposition.
cette protection doit permettre d'alerter le client par email.

Les pré-requis:
- utilisation d'un Raspberry Pi 3 (wifi et bluetooth 4.0)
- utilisation d'un capteur Jaalee

# Lateam

Notre équipe est constituée de 4 stagiaires, Kevin Georget, Maxime Girma, Dominique Ha-Thi et Komlagan Tekou.

# Methodologie

Nous nous sommes inspirés de la méthode Agile.

# Gestion de projet

Nous utiliserons Trello.

# Le projet

Le choix du langage est imposé par la formation et nous travaillerons en python 3.5.
Nous importerons les bibliothèques smtp pour l'envoi de mail et bluepy pour le scan des objets blueooth.

l'architecture logicielle est orchestré par main.py
cette fonction permet
- le scan des objets autour du Raspberry
- le traitement (ou filtre) des objets du clients à surveiller
- l'envoi d'un email à un destinataire
- l'hiistorisation des alertes

le fonctionnement est opérationnel.

# Utilisation

pour utiliser l'application, il faut:
- python3
- la librairie Bluepy

Dans la solution complète, le raspberry execute en automatique le programme.

Pour l'éxécutermanuellement :
$ python3 main.py

# Remerciements

recemerciements à nos intervenants pour leur aide.

