# Escribir un programa que almacene la cadena de
# caracteres contraseña en una variable, pregunte al usuario
# por la contraseña e imprima por pantalla si la contraseña introducida
# por el usuario coincide con la guardada en la variable sin tener
# en cuenta mayúsculas y minúsculas.
contrasenha = "aBc123."

while True:
    respuesta = input("Inroduzca contraseña")
    if respuesta.lower() == contrasenha.lower():
        print("Contraseña correcta")
        break
    else:
        print("Contaseña incorrecta vuelve a intentarlo")

