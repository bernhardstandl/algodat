Insertion-Sort
```python
#Zeitmessung Insertion Sort mit Visualisierung#
#####Algorithmen und Datenstrukturen #####
import time
import random
import numpy as np
import matplotlib.pyplot as plt

zeit = [] #Liste für die Messungen


for a in range(10,2000):
    Liste = np.random.randint(low = 0, high = 1500, size = a) #Liste mit Werten von 1-1000 mit der Länge i

    
    start = time.time() #Stoppuhr Start

    for i in range(1, len(Liste)):
        key = Liste[i]
        j = i - 1
        while j >= 0 and Liste[j] > key:
            Liste[j + 1] = Liste[j]
            j -= 1
        Liste[j + 1] = key


    ende = time.time() #Stoppuhr Ende
    
    gesamt = ende-start ##Differenz Start/Stopp
    zeit.append(gesamt)

plt.plot(zeit) 
plt.show()
```

Quick-Sort
```python
#Zeitmessung Quick Sort mit Visualisierung#
#####Algorithmen und Datenstrukturen #####
import time
import random
import numpy as np
import matplotlib.pyplot as plt

zeit = [] #Liste für die Messungen

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


for i in range(10,2000):
    Liste = np.random.randint(low = 0, high = 112500, size = i) #Liste mit Werten von 1-1000 mit der Länge i

    
    start = time.time() #Stoppuhr Start

    sorted_arr = quicksort(arr)

    ende = time.time() #Stoppuhr Ende
    
    gesamt = ende-start ##Differenz Start/Stopp
    zeit.append(gesamt)

plt.plot(zeit) 
plt.show()
```
