#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
# pregunte al usuario por una fruta, un número de kilos
# y muestre por pantalla el precio de ese número de kilos de fruta.
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello

menu_frutas = {"naranja": 10, "pera": 12, "melocoton": 14,"sandia": 22,"platano":9}

nombre_fruta = input("Que fruta desea comprar")
bandera = False

while bandera == False:
    if not menu_frutas.__contains__(nombre_fruta.lower()):
        print("No disponemos de esa fruta")
        nombre_fruta = input("Que fruta desea comprar")
    else:
        bandera = True
        kilos = input("Cuantos kilos de fruta desea ")
        print(menu_frutas[nombre_fruta.lower()])
        print(f"La compra de {kilos} de {nombre_fruta} le saldra en {menu_frutas[nombre_fruta.lower()] * int(kilos)} ")
