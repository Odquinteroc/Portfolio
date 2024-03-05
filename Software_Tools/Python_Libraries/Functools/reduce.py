from functools import reduce

#1
list1=[1,2,3,4,5,6,10,15,20]
a = map(lambda x: x + 5, list1)
c = list(a)
print(c)

#2

b = filter(lambda n: n > 10, c)
d = list(b)
print(d)

#3

e = reduce(lambda x, y: x*y, d)
print(e) 

#4

def procces_numbers(lista): 
    a = map(lambda x: x + 5, lista)
    b = list(a)
    #print(b)
    c = filter(lambda n: n > 10, b)
    d = list(c)
    #print(d)
    e = reduce(lambda x, y: x*y, d)
    #print(e)
    return(e)
#5
h = [2,4,6,8,10]
print(procces_numbers(h))
#6




