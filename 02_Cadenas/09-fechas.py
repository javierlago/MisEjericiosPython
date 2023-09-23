# Escribir un programa que pregunte al usuario la fecha
# de su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
# el día, el mes y el año. Adaptar el programa anterior para que
# también funcione cuando el día o el mes se introduzcan
# con un solo carácter.

fecha = input("Indique fecha de nacimiento")
dia = fecha[:fecha.find("/")]
mesano = fecha[fecha.find("/")+1:]
mes = mesano[:mesano.find("/")]
ano = mesano[mesano.find("/")+1:]
print("Has nacido el dia "+ dia + " en el mes " + mes + " y en el año " + ano)



