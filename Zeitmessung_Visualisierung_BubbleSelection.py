#Zeitmessung Bubble Sort mit Visualisierung#
#####Algorithmen und Datenstrukturen #####
import time
import random
import numpy as np
import matplotlib.pyplot as plt

zeit_bubble = [] #Liste für die Messungen Bubble Sort
zeit_selection = [] #Liste für die Messungen Selection Sort

for i in range(10,200):
    Liste = np.random.randint(low = 0, high = 1000, size = i) #Liste mit Werten von 1-1000 mit der Länge i
    
    start = time.time() #Stoppuhr Start
    
    ##### Programm Start #####
    N = len(Liste) #Länge der Liste
    for i in range(N): #Schleife außen
        for j in range(N-1): #Schleife innen
            if(Liste[j+1]<Liste[j]): ## Logische Bedingung
                tmp = Liste[j+1] #kleinerer Wert in tmp
                Liste[j+1] = Liste[j] #rechts wird links
                Liste[j] = tmp #links wird tmp
    ##### Programm Ende ##### 

    ende = time.time() #Stoppuhr Ende
    gesamt = ende-start ##Differenz Start/Stopp
    zeit_bubble.append(gesamt)
    
for i in range(10,200):
    Liste = np.random.randint(low = 0, high = 1000, size = i) #Liste mit Werten von 1-1000 mit der Länge i
    
    start = time.time() #Stoppuhr Start
    
    ##### Programm Start #####
    for i in range(len(Liste)): #Alle Elemente der Liste durchlaufen
        minimum = i #Suche nach dem kleinsten Element in der Liste
        for j in range(i+1, len(Liste)):
            if Liste[minimum] > Liste[j]:
                minimum = j

        tmp = Liste[i] #Tausche kleinestes Element an die richtige Stelle
        Liste[i] = Liste[minimum]
        Liste[minimum] = tmp
    ##### Programm Ende ##### 

    ende = time.time() #Stoppuhr Ende
    gesamt = ende-start ##Differenz Start/Stopp
    zeit_selection.append(gesamt)

plt.plot(zeit_bubble,'r')
plt.plot(zeit_selection,'g')
plt.show()
