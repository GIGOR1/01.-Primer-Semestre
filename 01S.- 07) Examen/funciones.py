import csv
import random
import statistics as stat

def menu():
    while True:
        try:
            print("\n1.- Asignar sueldos aleatorios")
            print("2.- Clasificar sueldos")
            print("3.- Ver estadísticas")
            print("4.- Reporte de sueldos")
            print("5.- Salir del programa")
            op = int(input("--> "))
            if op > 0 and op <6:
                return op
            else:
                print("\n¡Opción ingresada no existe!")
        except ValueError:
            print("\n¡Dato ingresado debe ser un número!")

def asignacion_sueldos(funcionarios,sueldos):
    for usuario in funcionarios:
        sueldos[usuario] = random.randrange(300000, 2500001)
    print("\nSueldos asignados correctamente.")
    return sueldos

def mostrar_sueldos(sueldos):
    menor = {}
    intermedio = {}
    alto = {}
    total = 0

    for key,value in sueldos.items():
        if value <800000:
            menor[key] = value
        if value >= 800000 and value <= 2000000:
            intermedio[key] = value
        if value > 2000000:
            alto[key] = value
    
    print(f"\nSueldos menores a $800.000 \nTOTAL: {len(menor)}\n\n{"Nombre empleado".ljust(20)}Sueldo")
    for key,value in menor.items():
        print(f"{key.ljust(20)}${value}")
    print(f"\nSueldos entre $800.000 y $2.000.000 \nTOTAL: {len(intermedio)}\n\n{"Nombre empleado".ljust(20)}Sueldo")
    for key,value in intermedio.items():
        print(f"{key.ljust(20)}${value}")
    print(f"\nSueldos superiores a $2.000.000 \nTOTAL: {len(alto)}\n\n{"Nombre empleado".ljust(20)}Sueldo")
    for key,value in alto.items():
        print(f"{key.ljust(20)}${value}")

    for value in sueldos.values():
        total+=value

    print(f"\nTOTAL SUELDOS: $ {total}")

def ver_estadisticas(sueldos):
    mayor = 0
    menor = []
    prom = 0

    for value in sueldos.values():
        if value > mayor:
            mayor = value
    for value in sueldos.values():
        menor.append(value)
    menor.sort()
    for value in sueldos.values():
        prom+=value
    prom = prom/len(sueldos)
    media_geometrica = stat.geometric_mean(menor)

    print("\nEstadísticas: ")
    print(f" - Sueldo más alto: ${mayor}")
    print(f" - Sueldo más bajo: ${menor[0]}")
    print(f" - Promedio de sueldos: ${int(prom)}")
    print(f" - Media geométrica: ${int(media_geometrica)}")
    
def reporte_sueldos(sueldos):
    reporte = []
    salud = 0.07
    afp = 0.12
    
    print(f"{"\nNombre empleado".ljust(21)}{"Sueldo Base".ljust(21)}{"Descuento Salud".ljust(21)}{"Descuento AFP".ljust(21)}Sueldo Líquido")
    for key,value in sueldos.items():
        desct_salud = int(value*salud)
        desct_afp = int(value*afp)
        liquido = int(value - desct_salud - desct_afp)
        reporte.append([key,value,desct_salud,desct_afp,liquido])
        print(f"{key.ljust(20)}${str(value).ljust(20)}${str(desct_salud).ljust(20)}${str(desct_afp).ljust(20)}${liquido}")

    with open ("reporte_de_sueldos.csv","w",newline="",encoding="utf-8") as datos:
        escritura = csv.writer(datos)
        escritura.writerow(["Nombre empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo líquido"])
        escritura.writerows(reporte)