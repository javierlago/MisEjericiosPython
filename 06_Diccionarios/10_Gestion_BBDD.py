"""""
Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
 Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
 y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, 
 preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa
debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente,
 (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función 
de la opción elegida el programa tendrá que hacer lo siguiente:
Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.
"""""
clientes = {}

opcion = 0
while opcion != 6:
    opcion = int(input("Que deseas realizar \n1->Añadir clietne \n2->Eliminar al cliente \n3->Mostrar el cliente "
                       "\n4->Listar a todos los clientes \n5->Listar clientes preferentes \n6->Terminar el programa"))
    if opcion == 1:
        dni = input("Introducir dni")
        nombre = input("Introducir nombre")
        direccion = input("Introducir la direccion")
        telefono = input("Introducir el telefono")
        correo = input("intoducir el correo")
        preferente = input("Es cliente preferente Si/NO") == "si"
        datos = {"nombre": nombre, "direccion": direccion, "telefono": telefono, "correo": correo, "tipo": preferente}
        clientes.update({dni: datos})
    elif opcion == 2:
        dni = input("DNI del cliente a eliminar")
        if clientes.__contains__(dni):
            del clientes[dni]
        else:
            print("El cliente que deseas borrar no se encuentra en la base de datos")
    elif opcion == 3:
        dni = input("DNI del cliente a mostrar")
        if clientes.__contains__(dni):
            print(clientes[dni])
        else:
            print("El cliente que deseas mostrar no se encuentra en la base de datos")
    elif opcion == 4:
        for key, value in clientes.items():
            print(f"{key}{value}")
    elif opcion == 5:
        for key, value in clientes.items():
            if value["tipo"]:
                print(f"{key}{value}")
    elif opcion == 6:
        print("Gracias y vuelva pronto")
