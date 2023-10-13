# Escribir un programa que almacene las asignaturas de
# un curso (por ejemplo Matemáticas, Física, Química, Historia y
# Lengua) en una lista, pregunte al usuario la nota que ha sacado en
# cada asignatura y elimine de la lista las asignaturas aprobadas. Al final
# el programa debe mostrar por pantalla las asignaturas que el usuario
# tiene que repetir.

asignatura = ["Matematicas", "Ingles", "Lengua", "filo", "mate", "historia"]
p = 0
for i in range(len(asignatura)-1, -1, -1):
  p = int(input("Que nota has sacado en "+asignatura[i]))
  if p >= 5:
      asignatura.pop(i)

print(asignatura)
