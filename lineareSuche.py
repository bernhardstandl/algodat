#Einfache lineare Suche

liste = [3,5,1,10,8,7]
suche = 10

for i in range(len(liste)):
    if liste[i] == suche:
        print("gefunden bei",i)
        break


#Lineare Suche mit Funktion
def lineareSuche(gesucht,Liste):  
    for i in range(len(liste)):
        if liste[i] == suche:
            print("gefunden bei",i)
            break
            
Liste = [3,5,1,10,8,7]
suche = 3
lineareSuche(Liste,suche)



#Lineare Suche mit Funktion und Random Liste
import random

def lineareSuche(gesucht,liste):  
    for i in range(len(liste)):
        if liste[i] == suche:
            print("gefunden bei",i)
            break
            
liste = random.sample(range(0, 11),11)
print(liste)

suche = 10
lineareSuche(suche,liste)



#Lineare Suche mit Funktion und wachsender Random Liste
import random

def lineareSuche(gesucht,liste):  
    for i in range(len(liste)):
        if liste[i] == suche:
            print("gefunden bei",i)
            break

for i in range(100):
    liste = random.sample(range(0, i),i)
    suche = 10
    lineareSuche(suche,liste)
    
    
    
    
#Lineare Suche mit Funktion und wachsender Random Liste und Zeitmessung
import random
import time

def lineareSuche(gesucht,liste):  
    for i in range(len(liste)):
        if liste[i] == suche:
            print("gefunden bei",i)
            break

for i in range(100):
    liste = random.sample(range(0, i),i)
    
    suche = 10
    
    start = time.time() #Stoppuhr Start
    lineareSuche(suche,liste)
    ende = time.time() #Stoppuhr Ende
    
    gesamt = ende-start ##Differenz Start/Stopp
    print(round(gesamt*1000,2),"ms")
    


#Lineare Suche mit Funktion und wachsender Random Liste und Zeitmessung und Visualisierung
import random
import time
import matplotlib.pyplot as plt

zeit = []

def lineareSuche(gesucht,liste):  
    for i in range(len(liste)):
        if liste[i] == suche:
            #print("gefunden bei",i)
            break

for i in range(800):
    liste = random.sample(range(0, i),i)
    
    suche = 10
    
    start = time.time() #Stoppuhr Start
    lineareSuche(suche,liste)
    ende = time.time() #Stoppuhr Ende
    
    gesamt = ende-start ##Differenz Start/Stopp
    zeit.append(gesamt)
    
plt.plot(zeit,'g')
plt.show()



#Variante lineare Suche rekursiv

liste = [3,5,1,10,8,7]
suche = 1

start = 0
ende = len(liste)-1

#print(liste[start])
#print(liste[ende])


def linearNeu(liste,start,ende):
    if liste[start] == suche:
        print("gefunden bei", start)
        return
    if liste[ende] == suche:
        print("gefunden bei", ende)
        return
    start = start+1
    ende = ende-1
    linearNeu(liste,start,ende)
    
linearNeu(liste,start,ende)
        
