""" 
Escribir una función que reciba un número entero positivo y devuelva su factorial.


"""""

def factorial(num):
    for n in range(1, num):
        num = num*n
    return num

print(f"{factorial(10)}")

