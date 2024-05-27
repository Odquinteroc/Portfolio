'''

Write a function named capitals. The function should take a single parameter. Your function should return a list of all the capital letters from a string that is passed into the function.
'''

def returnCapitalLetter (text: str) -> str:
    '''
    lista = []
    for i in text:
       if i.isupper():
            lista.append(i)
    return lista
    '''
    x = [letter for letter in text if letter.isupper()]
    yield x


print(next(returnCapitalLetter('ABcdFG')))