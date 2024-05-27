lista11 = [1,2,3,4,5,6]
lista21 = lista11
lista21[2]=4
print(lista11)
print(lista21)

import copy
lista1 = [1,2,3,4,5,6]
lista2 = copy.deepcopy(lista1)
lista2[2]=4
print(lista1)
print(lista2)