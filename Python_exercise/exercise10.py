'''
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
'''

def inverter(text: str)-> str:
    new_text = ''
    for i in range(1, len(text)+1, 1):
        new_text +=text[-i]
    return new_text

print(inverter('Hola mundo'))