# Escribir un programa que pregunte por consola el precio
# de un producto en euros con dos decimales y muestre por
# pantalla el número de euros y el número de céntimos del
# precio introducido.

precio = input("Indicar precio con dos decimales separados por un punto")
print(precio[:precio.find(".")]+" euros y "+precio[precio.find(".")+1:]+" centimos")
