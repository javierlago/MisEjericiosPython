#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente
# y el resto de la división entera respectivamente.


n = int(input("Introduza el primer numero"))
m = int(input("Introduza el primer numero"))
print("el resultado de dividir ", n ," entre ", m , " es de ",int(n/m), "y su resto es de " , n % m  )