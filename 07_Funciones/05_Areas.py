"""
Escribir una función que calcule el área de un círculo y otra que calcule 
el volumen de un cilindro usando la primera función.
"""""

import math


def calculo_area():
    d = float(input("indique diametro"))
    return (math.pi * pow(d / 2, 2)).__round__(2)


def volumen_cilindro():
    h = float(input("indicar altura"))
    return (calculo_area() * h).__round__(2)


print(calculo_area())
print(volumen_cilindro())
