# Escribir un programa en el que se pregunte al usuario
# por una frase y una letra, y muestre por pantalla el número
# de veces que aparece la letra en la frase.

f = input("frase")
l = input("letra")
c =0
for i in range(len(f)):
        if  l.lower() == f[i].lower():
            c += 1


print(f"Tu frase tiene {str(c)} letras -> {l} ")