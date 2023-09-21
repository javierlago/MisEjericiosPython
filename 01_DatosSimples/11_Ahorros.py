# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
# Estos ahorros debido a intereses, que no se cobran hasta finales de año,
# se te añaden al balance final de tu cuenta de ahorros.
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
# introducida por el usuario.
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
# Redondear cada cantidad a dos decimales.

ahorros = float(input("uanto dinero desea depositar"))
interes = 4/100
# adaptaion pidiendole al usuario el numero de años en el que desea calcular el rendimiento
anos = int(input("A cuantos años deseas realizar el calculo"))

for i in range(anos) :
    ahorros = ahorros + (ahorros*interes)
    print( "El año", i+1, "tus ahorros seran de ", round(ahorros,2))

