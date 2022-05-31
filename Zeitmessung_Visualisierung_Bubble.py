#Zeitmessung Bubble Sort mit Visualisierung#
#####Algorithmen und Datenstrukturen #####
import time
import random
import numpy as np
import matplotlib.pyplot as plt

zeit = [] #Liste für die Messungen

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
    zeit.append(gesamt)

plt.plot(zeit) 
plt.show()
