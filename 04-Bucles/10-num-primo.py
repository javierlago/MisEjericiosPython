# Pedir numero y mostrar si es numero primo o no

n =int(input("Numero"))
for  i in range(2, n):
   if  (n % i) == 0:
       print("no es primo")
   else:
       print("Es primo")
       break


