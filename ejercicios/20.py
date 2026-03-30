"""
20. Club recreativo: control de membresías
Registrar varias personas en un club.
Por cada una pedir:
- nombre
- edad
- tipo de plan: básico, premium, familiar
Reglas:
- básico = 50000
- premium = 90000
- familiar = 130000
Además:
- si la persona es menor de 18, mostrar “registro juvenil”
- si tiene 60 o más, mostrar “beneficio senior”
Al final mostrar:
- total recaudado
- cantidad de personas por plan
- plan más vendido
Practica: condicionales, contadores, acumuladores.
"""
total = basico = premium = familiar = 0

while True:
    nombre = input("Nombre (salir): ")
    if nombre == "salir":
        break

    edad = int(input("Edad: "))
    plan = input("Plan: ")

    if plan == "basico":
        total += 50000
        basico += 1
    elif plan == "premium":
        total += 90000
        premium += 1
    else:
        total += 130000
        familiar += 1

    if edad < 18:
        print("Registro juvenil")
    elif edad >= 60:
        print("Beneficio senior")

print(total, basico, premium, familiar)