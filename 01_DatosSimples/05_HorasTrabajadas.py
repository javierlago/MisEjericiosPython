# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde



horas_trabajadas = int(input("Cuantas horas has trabajado"))
precio_hora = float(input("A que precio son pagadas esas horas"))
print("Su salario sera de ", horas_trabajadas*precio_hora)
