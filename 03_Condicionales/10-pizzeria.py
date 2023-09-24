# La pizzería Bella Napoli ofrece pizzas vegetarianas
# y no vegetarianas a sus clientes. Los ingredientes para
# cada tipo de pizza aparecen a continuación.
#

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.


# Escribir un programa que pregunte al usuario si quiere una
# pizza vegetariana o no, y en función de su respuesta le muestre
# un menú con los ingredientes disponibles para que elija. Solo
# se puede eligir un ingrediente además de la mozzarella y el
# tomate que están en todas la pizzas. Al final se debe mostrar
# por pantalla si la pizza elegida es vegetariana o no y todos
# los ingredientes que lleva.

basepizza = ["mozzarela", "tomate"]
veggie = ["Pimiento","Tofu"]
normal = ["Peperoni","Jamon","Salmon"]

while True:
    respuesta = input("Elegir pizza veggie/normal")
    if respuesta == "veggie" or respuesta == "normal":
        break
    else:
        print("Debes de indicar uno de estos dos nombres veggie/normal")

if respuesta == "veggie":
    print(veggie)

    while True:
        ingrediente = input("Seleccionar ingrediente de la lista")
        if ingrediente in veggie:
            break
        else:
            print("Debes escoger uno de la lista")
            print(veggie)
    basepizza.append(ingrediente)
else:
    print(normal)
    while True:
        ingrediente = input("Seleccionar ingrediente de la lista")
        if ingrediente in normal:
            break
        else:
            print("Debes escoger uno de la lista")
            print(normal)
    basepizza.append(ingrediente)
print("Has elegido una pizza ", respuesta, "con los siguientes ingredieste", basepizza)