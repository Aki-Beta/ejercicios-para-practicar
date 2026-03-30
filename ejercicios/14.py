"""
14. Cine: control de sala
Pedir la capacidad total de una sala de cine y luego registrar cuántas
personas ingresan.
Por cada persona pedir edad y clasificar:
- niño
- adulto
- adulto mayor
Al final mostrar:
- total de personas ingresadas
- cuántos niños
- cuántos adultos
- cuántos adultos mayores
- si la sala se llenó o no
Practica: ciclos con límite, contadores.

"""

capacidad = int(input("Capacidad: "))
personas = 0
niños = adultos = mayores = 0

while personas < capacidad:
    edad = int(input("Edad: "))
    personas += 1

    if edad < 12:
        niños += 1
    elif edad <= 59:
        adultos += 1
    else:
        mayores += 1

print(personas, niños, adultos, mayores)