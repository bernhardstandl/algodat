### Quelle: https://www.geeksforgeeks.org/python-program-for-binary-search/

def binary_search(arr, low, high, x):
 
    # Start der Suche
    if high >= low:
         
        #Finden der Mitte der (Teil) Liste (doppelter Slash = Integer)
        mid = (high + low) // 2
 
        # Falls die gefundene Mitte direkt das gesuchte Element ist
        if arr[mid] == x:
            return mid
 
        #Wenn das gesuchte Element kleiner als der Wert in der Mitte der Liste ist
        #dann suche es links
        elif arr[mid] > x:
            #Rufe die Funktion mit den neuen Start und Ende Stellen zur Suche auf
            #low bleibt (weil links) und das Ende ist die Position vor der Mitte
            return binary_search(arr, low, mid - 1, x)
 
        #Wenn das gesuchte Element größer als der Wert in der Mitte der Liste ist
        #dann suche es rechts
        else:
            #Rufe die Funktion mit den neuen Start und Ende Stellen zur Suche auf
            #low ist das Element rechts der Mitte und das Ende bleibt
            return binary_search(arr, mid + 1, high, x)
 
    else:
        #Falls es kein Ergebnis gibt, gib -1 zurück
        return -1
 

#Testliste
arr = [ 2, 3, 4, 10, 40 ]
#Gesuchter Wert
x = 10
 
# Aufruf der Funktion mit den Startwerten
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Das gesuchte Element befindet sich hier: ", str(result))
else:
    print("Das gesuchte Element konnte nicht gefunden werden!")
    
    
 
