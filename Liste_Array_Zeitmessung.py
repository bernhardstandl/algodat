#Zeitmessung#
#####Algorithmen und Datenstrukturen #####
import time
import random
import numpy as np

#Liste
start = time.time() #Stoppuhr Start
##### Programm Start #####
random = random.sample(range(1, 1000),999)
ende = time.time() #Stoppuhr Ende
gesamt = ende-start ##Differenz Start/Stopp
print(round(gesamt*1000,2),"ms (Liste)")


#Array
start = time.time() #Stoppuhr Start
##### Programm Start #####
random = np.random.randint(range(1,1000),1000)
##### Programm Ende ##### 
ende = time.time() #Stoppuhr Ende
gesamt = ende-start ##Differenz Start/Stopp
print(round(gesamt*1000,2),"ms Array")
