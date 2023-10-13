# Escribir un programa que pida al usuario una palabra y
# muestre por pantalla el número de veces
# que contiene cada vocal.


contador_a = 0

contador_e = 0

contador_i = 0

contador_o=0

contador_u = 0
palabra = input("Palabra")
for i in range(len(palabra)):
         if  palabra[i] == "a":
             contador_a  += 1
         elif palabra[i] == "e":
             contador_e  += 1
         elif palabra[i] == "i":
             contador_i += 1
         elif palabra[i] == "o":
             contador_o += 1
         elif palabra[i] == "u" :
             contador_u += 1



print(f"La palabra tiene \n A->{contador_a}  "
      f"\n E->{contador_e} "
      f"\n I->{contador_i} "
      f"\n O->{contador_o}"
      f"\n U->{contador_u}")


