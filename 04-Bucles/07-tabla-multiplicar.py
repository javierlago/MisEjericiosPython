# Programa que genere la tabla de multiolicar
n = 10
for i in range(1, n + 1):
    print("TABLA DEL ",i)
    for z in range(1, n + 1):
        print(i, "*", z, "=", (i * z))
