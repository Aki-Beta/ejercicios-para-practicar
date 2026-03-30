"""
5. Tienda de mascotas: alimento por tipo de animal

Pide el tipo de mascota:

- perro
- gato
- conejo

Luego muestra una recomendación de alimento según el animal.

Practica: comparaciones con texto.

"""
animal = input("Animal: ").lower()

if animal == "perro":
    print("Alimento para perro")
elif animal == "gato":
    print("Alimento para gato")
elif animal == "conejo":
    print("Alimento para conejo")
