# Escribir un programa que pida al usuario dos números y
# muestre por pantalla su división. Si el divisor es cero el
# programa debe mostrar un error.

n = int(input("Primer numero"))

while True:
    m = int(input("Segundo numero"))
    if m != 0:
        break
    else:
        print("El divisor no puede ser 0")

print(int(n/m))



