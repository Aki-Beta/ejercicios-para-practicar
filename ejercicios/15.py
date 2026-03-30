"""
15. Parqueadero: control de vehículos
Registrar 8 vehículos en un parqueadero.
Por cada uno pedir:
- placa
- tipo: carro o moto
- horas parqueado
Tarifas:
- carro: 4000 por hora
- moto: 2000 por hora
Al final mostrar:
- total recaudado
- cuántos carros ingresaron
- cuántas motos ingresaron
- cuál vehículo pagó más
Practica: ciclos, máximos, acumuladores.
"""

total = 0
carros = motos = 0
mayor_pago = 0

for i in range(8):
    tipo = input("Tipo: ").lower()
    horas = int(input("Horas: "))

    if tipo == "carro":
        pago = horas * 4000
        carros += 1
    else:
        pago = horas * 2000
        motos += 1

    total += pago

    if pago > mayor_pago:
        mayor_pago = pago

print(total, carros, motos, mayor_pago)