from llist import sllist
import numpy as np


# Standard Liste in Python (Dynamisches Array)
dynamisches_array = []
for _ in range(1000):
    dynamisches_array.append(random.randint(1, 100))



# Verkettte Liste mit dem Modul LLIST
verkettete_liste = sllist()
for _ in range(1000):
    verkettete_liste.append(random.randint(1, 100))


# Array mit Numpy
array = np.random.randint(1, 100, 1000)
