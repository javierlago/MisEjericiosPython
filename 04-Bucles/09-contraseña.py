#Escribir un programa que almacene la cadena de caracteres contras
# eña en una variable, pregunte al usuario por la contraseña hasta q
# ue introduzca la contraseña correcta.
contasena = "hola"
bandera = False
while not bandera:
    n = input("introducir contraseña")
    if n.lower() == contasena.lower():
        bandera = True
        print("contraseña correcta")
    else:
        print("Contraseña incorrecta prueba otra vez")
