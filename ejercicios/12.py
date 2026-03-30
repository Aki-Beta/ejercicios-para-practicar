"""
12. Gimnasio: promedio de rendimiento semanal

Registrar 5 personas en un gimnasio.

Por cada una pedir:

- nombre
- días asistidos en la semana
- minutos promedio entrenados por día

Clasificar:
- menos de 3 días → bajo compromiso
- 3 a 4 días → compromiso medio
- 5 o más → compromiso alto

Al final mostrar cuántas personas quedaron en cada categoría.

Practica: ciclos, contadores, condicionales.

"""

registro = {
    0, "nombre", 
    1, "días asistidos a la semana",
    2, "minutos promedio entrenados por día"
} 

clasificar = [
    (0, 2, "bajo compromiso"),
    (3, 4, "compromiso medio"),
    (5, 7, "compromiso alto")
]
calcular = []

for i, sumar in enumerate(registro):  
    print (f'{i}- {registro}')