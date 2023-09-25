# Escribir un programa que pregunte al usuario una cantidad
# a invertir, el interés anual y el número de años, y muestre
# por pantalla el capital obtenido en la inversión cada año que
# dura la inversión.

cantidad = int(input("Cantidad"))
interes = input("Interes")
anos = input("Años")

for i in range(1,int(anos)):
    cantidad = cantidad + (cantidad*(int(interes)/100))
    print("El año " , i, "tu capital sera de ", round(float(cantidad), 2))
