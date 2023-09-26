# Escribir un programa que pregunte al usuario los números
# ganadores de la lotería primitiva, los almacene en una lista y los
# muestre por pantalla ordenados de
# menor a mayor.
numeros = list()
while len(numeros)<6:
    n = int(input("Indique numero"))
    if n not  in  numeros:
        numeros.append(n)
    else:
        print("el numero ya esta en la lista")
print(sorted(numeros))