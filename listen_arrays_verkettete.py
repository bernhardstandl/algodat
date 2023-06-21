import time
from llist import sllist
import numpy as np
import random


# Standard Liste in Python (Dynamisches Array)
start_time = time.time()

my_list = []
for _ in range(1000):
    my_list.append(random.randint(1, 100))

end_time = time.time()
list_time = end_time - start_time



# Verkettte Liste mit dem Modul LLIST
start_time = time.time()

my_llist = sllist()
for _ in range(1000):
    my_llist.append(random.randint(1, 100))

end_time = time.time()
llist_time = end_time - start_time



# Array mit Numpy
start_time = time.time()

my_array = np.random.randint(1, 100, 1000)

end_time = time.time()
array_time = end_time - start_time



# Printing the time taken for each method
print("Time taken to create list (default):", list_time)
print("Time taken to create list (llist module):", llist_time)
print("Time taken to create array (NumPy):", array_time)
