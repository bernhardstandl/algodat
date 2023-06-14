import time
from llist import sllist
import numpy as np


zeit_darray = []
zeit_vliste = []
zeit_array = []

von = 1
bis = 100

for i in range(1000):
    # Creating list using Python default list
    start_time = time.time()

    my_list = []
    for _ in range(i):
        my_list.append(random.randint(von, bis))

    end_time = time.time()
    list_time = end_time - start_time
    zeit_darray.append(list_time)

    # Creating list using sllist module
    start_time = time.time()

    my_llist = sllist()
    for _ in range(i):
        my_llist.append(random.randint(1, 100))

    end_time = time.time()
    llist_time = end_time - start_time
    zeit_vliste.append(llist_time)

    # Creating array using NumPy
    start_time = time.time()

    my_array = np.random.randint(1, 100, i)

    end_time = time.time()
    array_time = end_time - start_time
    zeit_array.append(array_time)

plt.plot(zeit_darray,'r')
plt.plot(zeit_vliste,'g')
plt.plot(zeit_array,'b')
plt.axis([0, 1000, 0, 0.0006])
plt.show()
