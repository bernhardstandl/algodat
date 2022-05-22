#Zeitmessung#
#####Algorithmen und Datenstrukturen #####
import time
import random
import numpy as np

start = time.time() #Stoppuhr Start
##### Programm Start #####
#random = random.sample(range(1, 1000), 500)
random = np.random.randint(1,1000,500)
##### Programm Ende ##### 

ende = time.time() #Stoppuhr Ende
gesamt = ende-start ##Differenz Start/Stopp

print(round(gesamt*1000,2),"ms")
