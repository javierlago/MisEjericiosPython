""""
El directorio de los clientes de una empresa está organizado en una cadena
de texto como la de más abajo, donde cada línea contiene la información
del nombre, email, teléfono, nif, y el descuento que se le aplica. Las líneas
se separan con el carácter de cambio de línea \n y la primera línea contiene
 los nombres de los campos con la información contenida en el directorio.
"nif;nombre;email;teléfono;descuento\n01234567L
;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J
;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M
;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;
Carmen Sánchez;carmen@mail.com;667677855;15.7"
Escribir un programa que genere un diccionario con la información del
directorio, donde cada elemento corresponda a un cliente y tenga por
 clave su nif y por valor otro diccionario con el resto de la información del
  cliente. Los diccionarios con la información de cada cliente tendrán como
   claves los nombres de los campos y como valores la información de 
   cada cliente correspondientes a los campos. Es decir, un diccionario
    como el siguiente
"""""
diccionario= {}
datos = {}
archivo = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
campos = archivo.split("\n")[0]
campos = campos.split(";")
archivo = archivo.split("\n")
archivo.pop(0);

for n in range(len(archivo)):
    key = ''
    datos = {}
    for z in range(len(archivo[n].split(";"))):
        if z == 0:
            key = archivo[n].split(";")[z]
        else:
            datos[campos[z]] = archivo[n].split(";")[z]


    diccionario[key] = datos


print(diccionario)


