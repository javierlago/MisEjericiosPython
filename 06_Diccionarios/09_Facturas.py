""""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número 
de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir 
una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará
por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura 
se preguntará por el número de factura y se eliminará del diccionario.
Después de cada operación el programa debe mostrar por pantalla la 
cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""""

facturas = {}
total_pagar=0
pagado = 0
continuar = True
while continuar:
    operacion = input("Que operacion desea realizar Insertar/Pagar/Terminar")
    if operacion.lower() == "insertar":
        key = input("Introducir el numero de factura")
        value = float(input("Coste de la factura?¿"))
        facturas[key] = value
        total_pagar += value
        print(f"Total a pagar {total_pagar} y has pagado {pagado}")
    elif operacion.lower() == "pagar":
        key = input("Indique numero de factura a pagar")
        if key in facturas:
            pagado += facturas.get(key)
            total_pagar -= facturas.get(key)
            del facturas[key]
        else:
            print("El numero de factura que ha indicado no existe")
        print(f"Total a pagar {total_pagar} y has pagado {pagado}")
    elif operacion.lower() == "terminar":
        print(f"Total a pagar {total_pagar} y has pagado {pagado}")
        continuar = False
