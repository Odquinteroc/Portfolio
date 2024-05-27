
'''
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
'''
def es_primo(num: int)-> bool:
    if num < 2:
        return False
    for i in range(2, num, 1):
        if num  % i == 0:
            return False
    return True


# print(es_primo(3))
primos = []

for i in range(0, 100, 1):
    if es_primo(i):
        primos.append(i)

print(primos)

