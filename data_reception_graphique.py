"""
Ce programme permet de tracer en temps réel sur un graphique les données issues d'un arduino
Frédéric Salach 12/10/2021
"""

#IMPORTATION DES MODULES PYTHON
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import MaxNLocator
import serial
import datetime as dt


#FONCTION ANIMATION
def animate(i, liste_xt, liste_y0):

    #AQUISITION DU PORT SERIE
    line=ser.readline()
    #MISE EN FORME ET PARSING
    line_as_list = line.strip()
    line_as_list = line.split()
    y0 = float(line_as_list[1])
    print(' Signal A0 : ',y0) #PRINT VALEUR Y0

    #AJOUT AUX LISTE
    liste_xt.append(dt.datetime.now().strftime('%H:%M:%S.%f')) #AJOUT DE l'HEURE A LISTE_XT
    liste_y0.append(y0)

    #LIMITATION NOMBRE DE POINT A AFFICHER
    liste_xt = liste_xt[-100:]
    liste_y0 = liste_y0[-100:]

    #GRAPH LES DONNEES XT ET Y0
    fig_sp.clear()
    fig_sp.plot(liste_xt, liste_y0, "r+-", linewidth=1, label="A0")
    fig_sp.axes.xaxis.set_major_locator(MaxNLocator(20)) #LIMITE LE NOMBRE DE VALEUR SUR L'AXE X

    # MISE EN FORME DU GRAPHIQUE
    plt.xticks(rotation=90, ha='right', fontsize = 8)
    plt.yticks(fontsize = 8)
    plt.subplots_adjust(bottom=0.30,)
    plt.title('Signal=f(Temps)', fontsize = 8)
    plt.ylabel('Signal', fontsize = 8)
    plt.legend(loc = "upper left", fontsize = 8)





#INITIALISATION DES LISTES
liste_xt = []
liste_y0= []    

#INITIALISATION DU PORT SERIE
ser = serial.Serial()
ser.port = '/dev/cu.usbserial-110'
ser.baudrate = 9600
ser.timeout = 10
ser.open()
if ser.is_open==True:
	print("\nAll right, serial port now open. Configuration:\n")
	print(ser, "\n") #PRINT PARAMETRES DU PORT SERIE

#INITIALISATION DU GRAPHIQUE
fig = plt.figure(figsize=(8, 5), dpi=96)
fig_sp = fig.add_subplot(1, 1, 1)

#LANCE L'ANIMATION
ani = animation.FuncAnimation(fig, animate, fargs=(liste_xt, liste_y0), interval=100)
plt.show()
