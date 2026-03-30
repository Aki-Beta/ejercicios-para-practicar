"""
11. Heladería: factura de varios clientes

Una heladería quiere registrar varios clientes hasta que el usuario
decida salir.

Productos:
- cono = 3000
- vaso = 4000
- banana split = 9000

Por cada cliente:
- pedir producto
- pedir cantidad
- calcular total

Al final mostrar:
- total vendido
- cuántos clientes se atendieron
- cuál producto se pidió más veces

Practica: ciclos, acumuladores, contadores.

"""
def heladeria():
    productos = ["cono", "vaso", "banana split"]
    precios = [3000, 4000, 9000]
    contador_productos = [0, 0, 0]  # para saber cuál se pidió más

    total_vendido = 0
    clientes = int(input("¿Cuántos clientes se atenderán? "))

    for i in range(clientes):
        print("Cliente", i + 1)
        producto = input("Producto (cono, vaso, banana split): ")
        cantidad = int(input("Cantidad: "))

        if producto in productos:
            indice = productos.index(producto)
            total = precios[indice] * cantidad
            total_vendido += total
            contador_productos[indice] += cantidad

            print("Total cliente:", total)

    # Producto más vendido
    max_pedidos = max(contador_productos)
    indice_max = contador_productos.index(max_pedidos)
    producto_mas_vendido = productos[indice_max]

    print("\n--- RESULTADOS ---")
    print("Total vendido:", total_vendido)
    print("Clientes atendidos:", clientes)
    print("Producto más pedido:", producto_mas_vendido)


heladeria()