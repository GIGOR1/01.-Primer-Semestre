import csv

def menu():
    while True:
        try:
            print("\n1.- Registrar puntajes torneo")
            print("2.- Listar puntajes")
            print("3.- Imprimir por tipo")
            print("4.- Salir")
            op = int(input("--> "))
            if op >0 and op <5:
                return op
            else:
                print("Número ingresado fuera de rango!")
        except ValueError:
            print("Dato ingresado debe ser entero!")

def registro(jugadores,juegos,categorias):
    id_jugador = input("Ingrese su ID de jugador: ")
    while True:
        nombre = input("Ingrese nombre y apellido: ").lower().title()
        if all(c.isalpha() or c.isspace() for c in nombre) and len(nombre) >8:
            break
        else:
            print("Nombre ingresado solo permite carácteres alfabéticos y debe ser mayor a 8 carácteres en total.")
    jugador = [id_jugador,nombre]
    for key, values in juegos.items():
        while True:
            respuesta = input(f"¿Es jugador competitivo de: {key}? (Y/N)\n-->").upper()
            if respuesta == "Y" or respuesta == "N":
                break
            else:
                print("Respuesta ingresada debe ser: 'Y' o 'N'")
        if respuesta == "Y":
            while True:
                try:
                    puntaje = int(input("Ingrese puntaje obtenido en dicho juego: "))
                    if puntaje > 0:
                        values = puntaje
                        jugador.append(values)
                        break
                    else:
                        print("Puntaje ingresado no válido")
                except ValueError:
                    print("Dato ingresado debe ser entero!")
        else:
            jugador.append(values)
    while True:
        try:
            categoria = int(input("¿En qué categoría participa?\n1) Principiante\n2) Avanzado\n3) Experto\n--> "))
            if categoria >0 and categoria <4:
                jugador.append(categorias[categoria])
                break
            else:
                print("Número ingresado fuera de rango!")
        except ValueError:
            print("Dato ingresado debe ser entero!")
    jugadores.append(jugador)
    return jugadores

def puntajes(jugadores):
    for fila in range(len(jugadores)):
        print(f"{"Id Jugador".ljust(20)}{"Nombre".ljust(20)}{"VALORANT".ljust(20)}{"FORTNITE".ljust(20)}{"FIFA".ljust(20)}{"Tipo".ljust(20)}")
        for columna in range(len(jugadores[fila])):
            print(f"{str(jugadores[fila][columna]).ljust(20)}",end="")
        print(" ")

def imprimir(jugadores,categorias):
    imprimir = []
    while True:
        try:
            categoria = int(input("Elija la categoría que desea imprimir\n1) Principiante\n2) Avanzado\n3) Experto\n--> "))
            if categoria >0 and categoria <4:
                categoria = categorias[categoria]
                break
            else:
                print("Número ingresado fuera de rango!")
        except ValueError:
            print("Dato ingresado debe ser entero!")
    for fila in range(len(jugadores)):
        for columna in range(len(jugadores[fila])):
            if jugadores[fila][columna] == categoria:
                imprimir.append(jugadores[fila])
    with open("Registro","w",newline="",encoding="utf-8") as datos:
        escritura = csv.writer(datos)
        escritura.writerow(["Id jugador","Nombre","VALORANT","FORTNITE","FIFA","Tipo"])
        escritura.writerows(imprimir)