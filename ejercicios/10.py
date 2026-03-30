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

def menu():
    while True:
        print("\n1. Add student")
        print("2. Show students")
        print("3. Find student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")

        option = input("Choose an option: ")

        if option == "1":
            add_student()
        elif option == "2":
            show_students()
        elif option == "3":
            find_student()
        elif option == "4":
            update_student()
        elif option == "5":
            delete_student()
        elif option == "6":
            break
        else:
            print("Invalid option")

menu()