"""""
Escribir un programa que cree un diccionario simulando una cesta de la compra.
 El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que 
 el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el 
 coste total, con el siguiente formato

Lista de la compra:
Articulo1                   Precio
Articulo2                   Precio
........                          .........
Total                         Coste
"""""
cesta_compra = {}
continuar = True
coste_total = 0
while continuar:
    nombre = input("Indique el nombre del producto que deseas añadir")
    precio = float(input("Cual es el precio del producto"))
    cesta_compra[nombre] = precio
    continuar = input("Deseas continuar añadiendo productos Si/No") == "Si"
for a, b in cesta_compra.items():
    print(f"{a}:\t{b}")
    coste_total += b
print(f"Coste:\t{coste_total}")
