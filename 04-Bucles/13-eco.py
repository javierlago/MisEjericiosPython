# Escribir un programa que muestre el eco de
#  tdo lo que el usuario introduzca hasta que el usuario escriba
#  “salir” que terminará.

palabra = ""
while palabra != "salir":
    palabra = input("Que quieres decirme")
    if palabra.lower() != "salir":
        print(palabra)
    else :
        print("Vuelve pronto")