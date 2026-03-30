"""
6. Parqueadero: cobro por horas
Pide cuántas horas estuvo un carro en un parqueadero.
Reglas:
- primera hora = 5000
- cada hora adicional = 3000
Muestra el total a pagar.
Practica: condicionales y operaciones.
"""
def calcular_pago(horas):
    if horas <= 1:
        return 5000
    else:
        return 5000 + (horas - 1) * 3000


horas = int(input("¿Cuántas horas estuvo el carro? "))
total = calcular_pago(horas)

print("Total a pagar:", total)