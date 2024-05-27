'''
- Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. 
'''	
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def list_intersection(lista, lista2: list)-> list:
    a = set(lista2)
    b = set(lista)
    return list(a.intersection(b))

print(list_intersection(a,b))

def list_to_set(lista: list)-> set:
    return set(lista)

print(list_to_set(a))

ccc= [i for i in list_to_set(a) if i in list_to_set(b)]
print(ccc)


aa = set(a)
bb = set(b)
cc = list(aa.intersection(bb))
print(cc)



