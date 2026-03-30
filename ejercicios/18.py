"""
18. Centro de idiomas: evaluación de estudiantes
Registrar varios estudiantes de un curso de inglés.
Por cada uno pedir:
- nombre
- nota speaking
- nota listening
- nota reading
Calcular promedio simple y clasificar:
- menor de 60 → bajo
- 60 a 79 → medio
- 80 o más → alto
Al final mostrar:
- promedio general del grupo
- mejor estudiante
- cuántos quedaron en cada nivel
Practica: promedios, máximos, contadores.

"""

total_prom = 0
mejor = 0

for i in range(3):
    s = int(input("Speaking: "))
    l = int(input("Listening: "))
    r = int(input("Reading: "))

    prom = (s + l + r) / 3
    total_prom += prom

    if prom > mejor:
        mejor = prom

print("Promedio grupo:", total_prom / 3)
print("Mejor:", mejor)