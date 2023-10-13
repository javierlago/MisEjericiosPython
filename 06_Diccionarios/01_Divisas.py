# Escribir un programa que guarde en una variable el
# diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte
# al usuario por una
# divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

monedas = {"Euro": "€", "Dollar": "$", "Yen": "¥"}

respuesta = input("Que moneda desear ver?")
if monedas.__contains__(respuesta):
    print(monedas[respuesta])
else:
    print("Esa moneda no se encuentra en nuestro diccionario")
