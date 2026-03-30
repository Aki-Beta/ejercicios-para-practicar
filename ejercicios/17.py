"""
17. Peluquería: agenda de atención
Una peluquería atiende 7 clientes al día.
Por cada cliente pedir:
- nombre
- servicio solicitado: corte, cepillado, tintura
- valor pagado
Al final mostrar:
- total del día
- cantidad de clientes por servicio
- servicio más solicitado
Practica: contadores, acumuladores, comparaciones.

"""
total = 0
corte = cepillado = tintura = 0

for i in range(7):
    servicio = input("Servicio: ").lower()
    valor = int(input("Valor: "))

    total += valor

    if servicio == "corte":
        corte += 1
    elif servicio == "cepillado":
        cepillado += 1
    else:
        tintura += 1

print(total)