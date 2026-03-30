"""
10. Academia de baile: asistencia
Pide la cantidad de clases asistidas por un estudiante en un mes.
Reglas:
- menos de 5 → asistencia baja
- entre 5 y 8 → asistencia media
- 9 o más → asistencia alta
Practica: clasificación por rangos.

"""
def clasificar_asistencia(clases):
    if clases < 5:
        return "asistencia baja "
    elif 5 <= clases <= 8:
        return "asistencia media"
    else:
        return "asistencia alta"


clases = int(input("¿Cuántas clases asistió en el mes? "))
print(clasificar_asistencia(clases))