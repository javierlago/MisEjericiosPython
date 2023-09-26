# Escribir un programa que pida al usuario una palabra y
# muestre por pantalla si es un palíndromo.

palabra = input("Escribe una palabra")
if palabra.lower() == palabra[:: -1].lower():
    print("Es un palindromo")
else:
    print("no es un palindromo")