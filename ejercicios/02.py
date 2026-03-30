"""
2. Gimnasio: acceso por edad

Un gimnasio ofrece clases según la edad:

-menor de 13 → no puede ingresar
-de 13 a 17 → clase juvenil
-de 18 a 59 → clase general
-60 o más → clase senior
Pide la edad de una persona y muestra a qué grupo pertenece.

Practica: if, elif, else.
"""

from messsages import bienvenida

print (bienvenida[1])

edad = int (input("Ingrese su edad: "))

if edad < 13: 
    print("No puedes ingresar")
elif edad >= 13 and edad < 18: 
    print ("Ingresa a clase juvenil")
elif edad >= 18 and edad < 60: 
    print ("Ingresa a clase general")
else:
    print ("Ingresa a clase senior")