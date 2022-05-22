Liste = [10,9,8,7,6,5,4,3,2,1] #Liste erstellen

N = len(Liste) #Länge der Liste
for i in range(N): #Schleife außen
    for j in range(N-1): #Schleife innen
        if(Liste[j+1]<Liste[j]): ## Logische Bedingung
            tmp = Liste[j+1] #kleinerer Wert in tmp
            Liste[j+1]= Liste[j] #rechts wird links
            Liste[j] = tmp #links wird tmp


print(Liste) #Ergebnis Programm
