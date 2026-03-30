"""
6. Parqueadero: cobro por horas
Pide cuántas horas estuvo un carro en un parqueadero.
Reglas:
- primera hora = 5000
- cada hora adicional = 3000
Muestra el total a pagar.
Practica: condicionales y operaciones.
"""
def calcular_pago(horas):
    if horas <= 1:
        return 5000
    else:
        return 5000 + (horas - 1) * 3000


horas = int(input("¿Cuántas horas estuvo el carro? "))
total = calcular_pago(horas)

print("Total a pagar:", total)

students = []

def add_student():
    id = input("Enter ID: ")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    status = input("Enter status (active/inactive): ")

    student = {
        "id": id,
        "name": name,
        "age": age,
        "course": course,
        "status": status
    }

    students.append(student)
    print("Student added successfully")


def show_students():
    for student in students:
        print(student)


def find_student():
    search = input("Enter ID or name: ")

    for student in students:
        if student["id"] == search or student["name"] == search:
            print(student)


def update_student():
    id = input("Enter ID to update: ")

    for student in students:
        if student["id"] == id:
            student["name"] = input("New name: ")
            student["age"] = int(input("New age: "))
            student["course"] = input("New course: ")
            student["status"] = input("New status: ")
            print("Student updated")


def delete_student():
    id = input("Enter ID to delete: ")

    for student in students:
        if student["id"] == id:
            students.remove(student)
            print("Student deleted")