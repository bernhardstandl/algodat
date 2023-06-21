import time #Zeitmessung
import random #Zufallszahlen
import numpy as np #Array
from llist import dllist #Linked List
import matplotlib.pyplot as plt

zeit1 = [] #Liste 1 für die Zeitmessungen
zeit2 = [] #Liste 2 für die Zeitmessungen
zeit3 = [] #Liste 3 für die Zeitmessungen

for i in range(10,200): #Schleife zur iterativen Erzeugung der Anzahl
    Liste = np.random.randint(low = 0, high = 1000, size = i) #Liste mit Werten von 1-1000 mit der Länge i
    
    start = time.time() #Stoppuhr Start
    ##### Programm Start #####
    # Hier kommt das Programm 1
    ##### Programm Ende ##### 
    ende = time.time() #Stoppuhr Ende
    gesamt = ende-start ##Differenz Start/Stopp
    zeit1.append(gesamt)
    
    start = time.time() #Stoppuhr Start
    ##### Programm Start #####
    # Hier kommt das Programm 2
    ##### Programm Ende ##### 
    ende = time.time() #Stoppuhr Ende
    gesamt = ende-start ##Differenz Start/Stopp
    zeit2.append(gesamt)
    
    start = time.time() #Stoppuhr Start
    ##### Programm Start #####
    # Hier kommt das Programm 3
    ##### Programm Ende ##### 
    ende = time.time() #Stoppuhr Ende
    gesamt = ende-start ##Differenz Start/Stopp
    zeit3.append(gesamt)
    


plt.plot(zeit1,'r') #Plot von Programm 1
plt.plot(zeit2,'g') #Plot von Programm 2
plt.plot(zeit3,'b') #Plot von Programm 3
plt.axis([0, 1000, 0, 0.0006]) #Skalierung der Achsen
plt.show()
