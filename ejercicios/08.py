"""
8. Tienda deportiva: contar productos caros
Pide el precio de 6 productos deportivos.
Al final indica cuántos cuestan más de 100000.
Practica: ciclo, contador, condicional.
"""
productos = [
    "Balón de fútbol",
    "Raqueta de tenis",
    "Bicicleta",
    "Casco ciclismo",
    "Tenis deportivos",
    "Tabla de surf",
]
precios = {}  # Diccionario: producto -> precio

print("Ingresa el precio de cada producto:n ")

for producto in productos:
    precio = float(input(f"  Precio de '{producto}': $"))
    precios[producto] = precio

# Contar cuántos cuestan más de 100.000
contador = 0

for producto, precio in precios.items():
    estado = "CARO" if precio > 100000 else "Económico"
    print(f"  {producto}: ${precio:,.0f}  →  {estado}")
    if precio > 100000:
        contador += 1
        
print(f"  Productos con precio mayor a $100.000: {contador} de {len(productos)}")