'''
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
'''
# def word_count(text: str)-> dict:
#     dic ={}
#     for i in text:
#         if i in dic:
#             dic[i] += 1
#         else:
#             dic[i] = 1
#     return dic

# print(word_count('hheoooo'))

dic ={}
text = input('Ingresa un texto:')
for i in text:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in dic:
    print(i, dic[i])
