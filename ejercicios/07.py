"""
7. Peluquería: turno del día
Pide la hora de llegada de un cliente en formato entero de 0 a 23.
Mostrar:
- mañana si está entre 6 y 11
- tarde si está entre 12 y 17
- noche si está entre 18 y 22
- fuera de horario en cualquier otro caso
Practica: rangos con condicionales.

"""
hora = int(input("Hora (0-23): "))

if 6 <= hora <= 11:
    print("Mañana")
elif 12 <= hora <= 17:
    print("Tarde")
elif 18 <= hora <= 22:
    print("Noche")
else:
    print("Fuera de horario")