#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
# Después el programa debe mostrar el precio habitual de una barra de pan,
# el descuento que se le hace por no ser fresca y el coste final total.

barra_pan = 3.49
numero_barras_vendidas = int(input("Cuantas barras se han vendido"))
descuento = float(0)

print("Precio de la barra de pan ->", barra_pan, "\nTotal de barras vendidas ->", numero_barras_vendidas,
      "\nImporte de barras vendidas->",barra_pan*numero_barras_vendidas,
      "\nDescuento a realizar->", (barra_pan*numero_barras_vendidas)*0.6,
      "\nImporte final->",((barra_pan*numero_barras_vendidas)-((barra_pan*numero_barras_vendidas)*0.6)))