import funciones as f

participantes = []

juegos = {"VALORANT" : 0,
          "FORTNITE" : 0,
          "FIFA" : 0}

categorias = { 1 : "Principiante",
               2 : "Avanzado",
               3 : "Experto"}

op = 0
while op != 4:
    op = f.menu()
    if op == 1:
        f.registro(participantes,juegos,categorias)
    elif op == 2:
        if len(participantes) > 0:
            f.puntajes(participantes)
        else:
            print("Ningún participante ha sido registrado todavía.")
    elif op == 3:
        if len(participantes) > 0:
            f.imprimir(participantes,categorias)
        else:
            print("Ningún participante ha sido registrado todavía.")
    else:
        print("Saliendo del programa...")