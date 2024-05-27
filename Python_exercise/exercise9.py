
'''
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
'''
def area_poligono(poligono: str)-> float:
    if poligono == 'Triángulo':
        b = float(input('input the base: '))
        h = float(input('input the hight: '))
        a = b*h/2
        return a
    elif poligono== 'Cuadrado':
        l = float((input('Input the side')))
        a = l**2
        return a
    elif poligono == 'Rectángulo':
        l =float(input('input the base: '))
        b = float((input('Input the side')))
        a = l*b
        return a
    
print(area_poligono(input('Input Triángulo, Cuadrado or Rectángulo ')))


    
