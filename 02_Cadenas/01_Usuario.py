# Escribir un programa que pregunte el nombre del usuario en la consola y un
# número entero e imprima por pantalla en líneas distintas el nombre del usuario
# tantas veces como el número introducido.

nombre = input("Introducir nombre ")
numero = int(input("Escriba un numero"))
#Este ejercicio se puede hacer con un for pero la manera mas ssencilla es la que
#esta a continuacion
print((nombre + "\n") * numero)

for i in range(numero) :
    print(nombre)