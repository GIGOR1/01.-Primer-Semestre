import random
import json

def menu():
    while True:
        print(f"\n{"-"*5}Registro estudiantil{"-"*5}")
        print("1.- Agregar estudiantes")
        print("2.- Mostrar todos los estudiantes")
        print("3.- Buscar estudiantes por nombre")
        print("4.- Exportar registro")
        print("5.- Salir")
        try:
            op = int(input("--> "))
            if op > 0 and op <6:
                return op
        except ValueError:
            print("\nTipo de dato ingresado debe ser un número!")

def agregar(estudiantes):
    while True:
        nombre = input("Ingrese nombre del estudiante que desea agregar: ").lower().title()
        if nombre.isalpha() and len(nombre) > 1:
            break
        else:
            print("Nombre ingresado solo permite carácteres alfabéticos y debe poseer más de 1 carácter.")
    while True:
        apellido = input("Ingrese apellido del estudiante que desea agregar: ").lower().title()
        if apellido.isalpha() and len(apellido) > 1:
            break
        else:
            print("Apellido ingresado solo permite carácteres alfabéticos y debe poseer más de 1 carácter.")
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if edad > 16  and edad < 90:
                break
            else:
                print("Edad ingresada no válida.")
        except ValueError:
            print("Tipo de dato ingresado debe ser un número!")
    ID = random.randrange(10000000, 99999999)
    estudiantes.append({
        "Nombre" : nombre,
        "Apellido" : apellido,
        "Edad" : edad,
        "ID" : ID
    })
    return estudiantes

def mostrar(estudiantes):
    for i in estudiantes:
        print(f"\nEstudiante: {i["Nombre"]} {i["Apellido"]}\nEdad: {i["Edad"]}\nID: {i["ID"]}")

def buscar(estudiantes):
    validado = False
    nombre = input("Ingrese nombre del estudiante que desea buscar: ").lower().title()
    apellido = input("Ingrese apellido del estudiante que desea buscar: ").lower().title()
    for i in estudiantes:
        if nombre == i["Nombre"] and apellido == i["Apellido"]:
            print(f"Edad: {i["Edad"]}\nID: {i["ID"]}")
            validado = True
    if not validado:
        print("Estudiante ingresado no existe.")

def importar(estudiantes):
    with open("Registro_alumnos.json","w") as datos:
        json.dump(estudiantes, datos, indent=1)