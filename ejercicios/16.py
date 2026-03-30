"""
16. Tienda de mascotas: ventas por categoría 
Registrar ventas de una tienda de mascotas. 
Categorías: 
- alimento 
- juguete 
- accesorio 
Pedir 10 ventas. En cada venta: 
- categoría 
- valor de la compra 
Al final mostrar: 
- cuánto se vendió por cada categoría 
- cuál categoría generó más dinero 
Practica: acumuladores separados. 

"""

alimento = juguete = accesorio = 0

for i in range(10):
    categoria = input("Categoría: ").lower()
    valor = int(input("Valor: "))

    if categoria == "alimento":
        alimento += valor
    elif categoria == "juguete":
        juguete += valor
    else:
        accesorio += valor

print(alimento, juguete, accesorio)