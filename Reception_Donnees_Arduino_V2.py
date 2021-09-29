# -*- coding: utf-8 -*-

"""
Programme Python pour recuperer par le port serie USB les donnes en provenance d'un Arduino
et les sauvegader dans un fichier texte

(c) Frederic Salach - 26/09/2021
"""

#Importation modules Python
import serial
import sys, select, os
from datetime import datetime


#Invitation terminal Python
os.system("clear")
print("*****************************************************************************************")
print("Programme Python d'aquisistion de donneedepuis d'un Arduino en utilisant le port serie")
print("Les donnees sont sauvegarde dans un fichier texte")
print("*****************************************************************************************")


"""Recuperation des donnees"""

#Creation du fichier texte de sauvegarde
nom_fichier_sauvegarde = datetime.now().strftime("%d%m%Y_%H%M%S_") + "sauvegarde.txt" #Recuperation de l'heure et formatage du nom du fichier de sauvegarde
fichier_sauvegarde = open(nom_fichier_sauvegarde, 'w') #Creation du fichier de sauvegarde des données
print(f"Les donnees seront sauvegardees dans le fichier {nom_fichier_sauvegarde}")

#Attente que la touche 'Entree' est pressee
input("Presser sur 'ENTREE' pour demarrer l'aquisistion des données") #Débute l'aquisition des donnes lorsque la touvhe 'Entree' est pressee

#Ouverture de la communication serie
try:
    port_serie = serial.Serial("/dev/cu.usbserial-110", baudrate=9600, timeout=5) #Ouverture communication du port serie avec /dev/cu.usbserial-1140 nom du port serie utilise par l'Arduino
except:
    print('Verifier le nom de la connection serie') #Message d'erreur si connection serie non fonctionelle


#Boucle de recuperation des donnees
while True:

    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]: #Condition pour stopper l'aquisition des donnes lorsque la touvhe 'Entree' est pressee
        line = input()
        break
    
    horodatage = datetime.now().strftime("%d/%m/%Y;%H:%M:%S") #Recuperation de l'heure et formatatge de l'horodatatge
    donnees_a_sauvegarder = horodatage + ";" + port_serie.readline().decode('ascii') #Formatatge des donnes a sauvegarder avec horodatatge et lecture du port serie et decodage des donnees series au format ASCII
    
    print("Presser 'ENTREE' pour arreter l'aquisition :    ", donnees_a_sauvegarder)
    fichier_sauvegarde.write(donnees_a_sauvegarder) #Ecriture des donnees dans le fichier de sauvegarde


#Fermeture du programme
print("Aquisition stoppee")
port_serie.close() #Fermeture de la communication serie
fichier_sauvegarde.close() #Fermeture du fichier de sauvegarde
print("Fin du programme")
print("*****************************************************************************************")


