"""
4. Cine: entrada según edad

El precio de la entrada cambia así:

- niños menores de 12 → 8000
- adultos de 12 a 59 → 12000
- mayores de 60 → 9000

Pide la edad del cliente y muestra cuánto debe pagar.

Practica: condicionales
"""

entrada = [
    (0, 12, "8000"),
    (12, 59, "12000"),
    (60,200, "9000")

]

edad= int(input("Ingrese su edad: "))

for minimo, maximo, costo in entrada: 
    if minimo <= edad <= maximo:
        print(f"valor a pagar : {costo}")
        break
        