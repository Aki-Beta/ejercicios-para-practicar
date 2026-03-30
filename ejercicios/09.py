"""
9. Spa: servicio disponible
En un spa hay estos servicios:
- masaje
- facial
- manicure
Pide al usuario qué servicio desea y muestra un mensaje confirmando
si existe o no.
Practica: condicionales con texto.

"""
def verificar_servicio(servicio):
    servicios = ["masaje", "facial", "manicure"]
    
    if servicio in servicios:
        return "Servicio disponible "
    else:
        return "Servicio no disponible "


servicio = input("¿Qué servicio deseas? ").lower()
print(verificar_servicio(servicio))