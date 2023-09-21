# Escribir un programa que pregunte al usuario una cantidad a invertir,
# el interés anual y el número de años,
# y muestre por pantalla el capital obtenido en la inversión.

inversion = float(input("Indique el capital a invertir"))
interes = float(input("Indique el interes anual"))
anhos = int(input("Indique el numero de años "))

print("El benedicio obtenido sera de ", (inversion * (interes/100)) * anhos)
