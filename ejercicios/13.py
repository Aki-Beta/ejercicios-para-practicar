"""
13. Cafetería: descuento por consumo
Registrar varios pedidos en una cafetería hasta que el usuario escriba
“salir”.
Productos:
- café = 4000
- capuchino = 7000
- pastel = 6000
Reglas:
- si la compra supera 20000, aplicar 10% de descuento
- si no, cobrar normal
Mostrar total por cliente y al final total acumulado del día.
Practica: menú simple, ciclos, descuentos

"""

total_dia = 0

while True:
    producto = input("Producto (salir): ").lower()
    if producto == "salir":
        break

    cantidad = int(input("Cantidad: "))

    if producto == "cafe":
        precio = 4000
    elif producto == "capuchino":
        precio = 7000
    elif producto == "pastel":
        precio = 6000

    total = precio * cantidad

    if total > 20000:
        total *= 0.9

    print("Total cliente:", total)
    total_dia += total

print("Total del día:", total_dia)