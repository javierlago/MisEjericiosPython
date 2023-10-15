""""
Escribir una función que reciba una muestra de números en una lista y devuelva su media.


"""""
listado = [10, 3, 4, 5, 6]


def hacer_media(lista):
    num = 0
    for n in lista:
        num += n
    return float(num/len(lista))


print(hacer_media(listado))
