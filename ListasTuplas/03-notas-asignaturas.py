# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada
# asignatura, y después las muestre por pantalla con el mensaje
# En <asignatura> has sacado <nota> donde <asignatura> es cada una
# des las asignaturas de la lista y <nota> cada una de las correspondientes
# notas introducidas por el usuario.

asignaturas = ["matematicas","ingles","educacion fisica","historia","filosofia"]
nota = []
for i in range(len(asignaturas)):
    nota.append(int(input(f"Que nota has sacado en {asignaturas[i]}")))
for i in range(len(asignaturas)):
    print(f"Has sacado en {asignaturas[i]} una nota de un {nota[i]}")