"""
3. Cafetería: total de una compra sencilla

En una cafetería venden:

- café = 4000
- té = 3500
- jugo = 5000

Pide al usuario qué bebida quiere y cuántas unidades desea comprar.
Luego muestra el total a pagar.

Practica: condicionales, variables, multiplicación.
"""

producto = input("Producto: ").lower()
cantidad = int(input("Cantidad: "))

if producto == "cafe":
    precio = 4000
elif producto == "te":
    precio = 3500
elif producto == "jugo":
    precio = 5000

total = precio * cantidad
print("Total:", total)