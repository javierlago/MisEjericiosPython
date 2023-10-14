"""""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con 
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, 
correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un 
nuevo dato debe imprimirse el contenido del diccionario.
"""""
persona = {}
nombre  = input( "Introducir nombre")
persona["nombre"]= nombre
for a, b in persona.items():
    print(f"Se ha añadido el campo {a} con el dato {b}")
edad = int(input("Introducir edad"))
persona["edad"]= edad
for a, b in persona.items():
    print(f"Se ha añadido el campo {a} con el dato {b}")
sexo = input("Inmdique cual es su sexo")
persona[sexo] = sexo
for a, b in persona.items():
    print(f"Se ha añadido el campo {a} con el dato {b}")
telefono = int(input("Indique su numero de telefono"))
for a, b in persona.items():
    print(f"Se ha añadido el campo {a} con el dato {b}")
correo = input("Indique su correo electronico")
persona["correo"] = correo
for a, b in persona.items():
    print(f"Se ha añadido el campo {a} con el dato {b}")

"""
Solucion propuesta por la web
persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"
"""

