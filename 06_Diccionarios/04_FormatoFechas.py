""""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa
 y muestre por pantalla la misma fecha en formato dd de 
 <mes> de aaaa donde <mes> es el nombre del mes.
"""""

import datetime

meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
         9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
while True:
    fecha_input = input("Indica la fecha en el fomato dd/mm/yyy")
    try:
        fecha = datetime.datetime.strptime(fecha_input, "%d/%m/%Y")
        break
    except ValueError:
        print("La fecha que has indicado no esta en el formato adecuado")

print(f"El {fecha.day} del {meses[fecha.month]} del {fecha.year}")

"""
# Solucion propuesta por la web
meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])
"""
