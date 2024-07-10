import csv

def menu():
    while True:
        try:
            print("\n1.- Grabar")
            print("2.- Buscar")
            print("3.- Guardar archivos")
            print("4.- Salir")
            op = int(input("-->"))
            if op > 0 and op < 5:
                return op
            else:
                print("Número ingresado fuera de rango!")
        except ValueError:
            print("Tipo de dato ingresado debe ser entero!")

def grabar(registro_usuarios):
    while True:
        NIF = input("Ingrese su NIF: ").upper()
        if len(NIF) == 12 and "-" in NIF:
            break
        else:
            print("NIF ingresado no válido.")
    while True:
        nombre = input("Ingrese su nombre y apellido: ").lower().title()
        if all(letra.isalpha() or letra.isspace() for letra in nombre) and len(nombre)>8 and " " in nombre:
            break
        else:
            print("Solo se permiten carácteres alfabéticos y la suma de nombre y apellido tiene que poseer un mínimo de 8 carácteres.")
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad >= 15:
                break
            else:
                print("Edad ingresada debe ser mayor a 14")
        except ValueError:
            print("Tipo de dato ingresado debe ser entero!")
    usuario = [nombre,edad]
    registro_usuarios[NIF] = usuario

def buscar(registro_usuarios):
    validado = False
    NIF = input("Ingrese NIF(con guión) del usuario que desea buscar: ").upper()
    for keys, values in registro_usuarios.items():
        if NIF == keys:
            print(f"{"Nombre".ljust(20)}{"Edad".ljust(20)}")
            for i in values:
                print(f"{str(i).ljust(20)}",end=" ")
                validado = True
        print("")
    if not validado:
        print("NIF ingresado no coincide con ningún usuario registrado.")

def guardar_archivo(registro_usuarios):
    usuarios = []
    while True:
        try:
            rango1 = int(input("Ingrese la edad de inicio para segmentar búsqueda: "))
            rango2 = int(input("Ingrese la edad de salida para segmentar búsqueda: "))
            if rango1 >14 and rango2 >14 and rango1 <130 and rango2 < 130:
                break
            else:
                print("Edad o edades ingresadas inválidas.")
        except ValueError:
            print("Tipo de dato ingresado debe ser entero!")
            
    for key,values in registro_usuarios.items():
        usuario =[]
        verificado = False
        if values[1] >= rango1 and values[1] <=rango2:
            verificado = True
        if verificado:
            for i in values:
                usuario.append(i)
            usuarios.append(usuario)

    with open("edades_entre_a_y_b.csv","w",newline="",encoding="utf-8") as datos:
        escritura = csv.writer(datos)
        escritura.writerow(["Nombre","Edad"])
        escritura.writerows(usuarios)