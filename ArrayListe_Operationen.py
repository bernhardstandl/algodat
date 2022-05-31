#Operationen auf Listen/Arrays#
##### Algorithmen und Datenstrukturen #####
import numpy as np

######## Liste ########
Liste = [1,2,3,4,5,6]
print(Liste)

#Hinzufügen ans Ende
Liste.append(7)
print(Liste)

#Hinzufügen an Stelle x
Liste.insert(1,10)
print(Liste)

#Löschen von Eintrag mit Wert x
Liste.remove(5)
print(Liste)

#Löschen von Eintrag an Stelle x
Liste.pop(0)
print(Liste)



######## Array ########
Array = np.array([1,2,3,4,5])

#Hinzufügen ans Ende
Array1 = np.append(Array,[10,11])
print(Array)
print(Array1)

#Hinzufügen an Stelle x
Array2 = np.insert(Array,1,20)
print(Array)
print(Array2)

#Löschen von Eintrag mit Wert x
print(Array)
Array4 = np.delete(Array, np.where(Array == 4))
print(Array4)

#Löschen von Eintrag an Stelle x
Array3 = np.delete(Array,1)
print(Array)
print(Array3)


