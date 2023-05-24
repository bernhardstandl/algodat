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


for i in range(10,1000):
    Liste = np.random.randint(low = 0, high = 1000, size = i) #Liste mit Werten von 1-1000 mit der Länge i

    
    start = time.time() #Stoppuhr Start

    sorted_arr = quicksort(Liste)

    ende = time.time() #Stoppuhr Ende
    
    gesamt = ende-start ##Differenz Start/Stopp
    zeit.append(gesamt)


plt.plot(zeit) 
plt.show()
```

Insertion-Sort
```python
#Zeitmessung Insertion Sort mit Visualisierung#
#####Algorithmen und Datenstrukturen #####
import time
import random
import numpy as np
import matplotlib.pyplot as plt

zeit = [] #Liste für die Messungen


for a in range(10,500):
    Liste = np.random.randint(low = 0, high = 1, size = a) #Liste mit Werten von 1-1000 mit der Länge i

    
    start = time.time() #Stoppuhr Start

    for i in range(1, len(Liste)):
        key = Liste[i]
        for j in range(i - 1, -1, -1):
            if Liste[j] > key:
                Liste[j + 1] = Liste[j]
                Liste[j] = key


    ende = time.time() #Stoppuhr Ende
    
    gesamt = ende-start ##Differenz Start/Stopp
    zeit.append(gesamt)

plt.plot(zeit) 
plt.show()
```
