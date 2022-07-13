Liste = [10,9,8,7,6,5,4,3,2,1] #Liste erstellen

N = len(Liste) #Länge der Liste
print("Eingabe Liste=",Liste)
print("Liste Länge=",N)

for i in range(N): #Schleife außen
  
    #Schleife innen N=länge des Arrays, -i=Verkürzung des Bereichs in jedem Durchlauf, -1=vorletztes+letztes vergleichen
    
    print("\nDurchlauf",i,"Länge=",N-i-1)
    for j in range(N-i-1):  
        if(Liste[j+1]<Liste[j]): ## Logische Bedingung
                    
            tmp = Liste[j+1] #kleinerer Wert in tmp
            Liste[j+1]= Liste[j] #rechts wird links
            Liste[j] = tmp #links wird tmp
            print(j+1,"Liste in Durchlauf", i,Liste)   

print(Liste) #Ergebnis Programm


