## Escribir un programa que pregunte por consola por los productos
# de una cesta de la compra, separados por comas, y muestre por pantalla
# cada uno de los productos en una línea distinta.


cesta = input("Indique productos separados por coma")
# cesta otra solucion es para comprobar que tambien se
# puede hacer sin convertir en un array
cestaotrasolucion = cesta

cesta = cesta.split(",") #convierto en un array

for i in range(len(cesta)):
    print(cesta[i])
print(cestaotrasolucion.replace(",","\n"))