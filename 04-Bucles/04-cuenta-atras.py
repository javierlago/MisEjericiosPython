# Escribir un programa que pida al usuario un número
# entero positivo y muestre por pantalla la cuenta atrás
# desde ese número hasta cero separados por comas.

n = int(input("Numero"))
int = n
for i in range(n,0,-1):
    print(i,end=",")