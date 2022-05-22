Liste = [10,9,8,7,6,5,4,3,2,1]
  
for i in range(len(Liste)): #Alle Elemente der Liste durchlaufen
    minimum = i #Suche nach dem kleinsten Element in der Liste
    for j in range(i+1, len(Liste)):
        if Liste[minimum] > Liste[j]:
            minimum = j
                  
    tmp = Liste[i] #Tausche kleinestes Element an die richtige Stelle
    Liste[i] = Liste[minimum]
    Liste[minimum] = tmp
    
print(Liste)
