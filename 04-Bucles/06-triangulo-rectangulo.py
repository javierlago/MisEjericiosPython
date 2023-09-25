# Escribir un programa que pida al usuario un número entero y
# muestre por pantalla un triángulo rectángulo como el de más abajo,
# de altura el número introducido.

n = int(input("Indique tamaño"))

for i in range(1,n+1):
    print("*" *i)