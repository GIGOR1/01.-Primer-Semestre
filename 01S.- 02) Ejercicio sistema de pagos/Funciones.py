import csv

def menu():
    while True:
        print(f"\n{"-"*5}Sistema de pagos{"-"*5}")
        print("1.- Registrar trabajador")
        print("2.- Listar todos los trabajadores")
        print("3.- Imprimir planilla de sueldos")
        print("4.- Salir")
        try:
            op = int(input("-->"))
            if op > 0 and op < 5:
                return op
            else:
                print("Opción ingresada fuera de rango!")
        except:
            print("Tipo de dato ingresado debe ser un número!")

def registrar(trabajadores, cargos, salud, afp):
    nombre = input("Ingrese nombre y apellido del trabajador\nNombre: ").lower().title()
    while True:
        validado = False
        cargo = input("Ingrese cargo del trabajador: ").lower()
        for key, value in cargos.items():
            if cargo == key:
                sueldo = value
                cargo = cargo.title()
                validado = True
        if validado:
            break
        else:
            print("Cargo ingresado no existe.")
    desc_salud = int(round((sueldo * salud),0))
    desc_afp = int(round((sueldo * afp),0))
    liquido = int(round((sueldo - desc_salud - desc_afp),0))
    trabajadores.append([
        nombre, cargo, sueldo, desc_salud, desc_afp, liquido
    ])
    return trabajadores

def mostrar(trabajadores, tabla):
    for i in range(len(trabajadores)):
        print("\n")
        for x in tabla:
            print(f"{x.ljust(20)}",end="")
        print("")
        for f in trabajadores[i]:
            print(f"{str(f).ljust(20)}",end="")
    print("")

def imprimir(trabajadores, cargos):
    while True:
        print("1.- Imprimir todas las plantillas")
        print("2.- Imprimir por cargo")
        print("3.- Volver")
        try:
            op = int(input("-->"))
            if op > 0 and op < 4:
                break
            else:
                print("Número ingresado fuera de rango.")
        except ValueError:
            print("Tipo de dato ingresado debe ser un número!")
    if op == 1:
        with open("plantilla_sueldo.csv","w",newline="") as datos:
            escritura = csv.writer(datos)
            escritura.writerow(["Trabajador","Cargo","Sueldo Bruto","Desc.Salud","Desc.AFP","Líquido"])
            escritura.writerows(trabajadores)
    elif op == 2:
        planilla = []
        validado = False
        cargo = input("Ingrese cargo: ").lower()
        for key in cargos.keys():
            if cargo == key:
                validado = True
        if validado:
            cargo = cargo.title()
            for f in range(len(trabajadores)):
                print(f)
                for c in trabajadores[f]:
                    if cargo == c:
                        planilla.append(trabajadores[f])
                        print(planilla)
            with open("plantilla_sueldo.csv","w",newline="") as datos:
                escritura = csv.writer(datos)
                escritura.writerow(["Trabajador","Cargo","Sueldo Bruto","Desc.Salud","Desc.AFP","Líquido"])
                escritura.writerows(planilla)
        else:
            print("Cargo ingresado no existe")
    else:
        print("Volviendo al menú principal...")