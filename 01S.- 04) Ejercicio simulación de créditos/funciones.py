import csv
import random

def menu():
    while True:
        try:
            print("\n1.- Simulación de créditos en AWS")
            print("2.- Clasificación de créditos")
            print("3.- Cálculo de estadísticas de créditos")
            print("4.- Generación de reporte de créditos")
            print("5.- Salir del programa")
            op = int(input("--> "))
            if op > 0 and op < 6:
                return op
            else:
                print("Opción ingresada no existe!")
        except ValueError:
            print("Tipo de dato ingresado debe ser un número!")

def creditos(alumnos, simulacion):
    for i in range(len(alumnos)):
        simulacion[alumnos[i]] = random.randrange(50,200)
    print("\nSimulación de créditos creada exitosamente!")
    return simulacion

def clasificacion(simulacion):
    menores_100 = {}
    entre_100_150 = {}
    mayor_150 = {}
    for key,value in simulacion.items():
        if value < 100:
            menores_100[key]=value
        if value > 99 and value <= 150:
            entre_100_150[key]=value
        if value > 150:
            mayor_150[key]=value
    print("\nCréditos inferiores a 100: ")
    for key,value in menores_100.items():
        print(f"{key}: ${value}")
    print("\nCréditos entre 100 y 150: ")
    for key,value in entre_100_150.items():
        print(f"{key}: ${value}")
    print("\nCréditos superiores a 150: ")
    for key,value in mayor_150.items():
        print(f"{key}: ${value}")
    return menores_100,entre_100_150,mayor_150

def estadisticas_credito(simulacion):
    valores = []
    prom = 0
    for value in simulacion.values():
        valores.append(value)
        prom += value
    prom = prom/len(valores)
    minimo = min(valores)
    maximo = max(valores)
    print(f"\nEl máximo crédito es de: {maximo}")
    print(f"El mínimo crédito es de: {minimo}")
    print(f"El promedio de créditos es de: {prom}")

def reporte(minimo,intermedio,mayor):
    lista = []
    for key,value in minimo.items():
        estudiante = [key,value,"menor a 100"]
        lista.append(estudiante)
    for key,value in intermedio.items():
        estudiante = [key,value,"entre 100 y 150"]
        lista.append(estudiante)
    for key,value in mayor.items():
        estudiante = [key,value,"mayor a 150"]
        lista.append(estudiante)
    with open("Créditos estudiantes","w",newline="",encoding="utf-8") as datos:
        escritura = csv.writer(datos)
        escritura.writerow(["Alumnos","Créditos","Clasificación"])
        escritura.writerows(lista)