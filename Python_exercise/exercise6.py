'''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''

def anagrama (text1: str, text2: str) -> bool:
    if text1.lower() == text2.lower() :
        return False
        
    lista1=[]
    lista2=[]
    for i in text1.lower():
        lista1.append(i)
    lista1.sort()
    for i in text2.lower():
        lista2.append(i)  
    lista2.sort()
    return lista1 == lista2
      
    
print(anagrama('amor', 'roma'))