import Funciones as f
estudiantes = []

op = 0
num = 0
while op != 5:
    op = f.menu()
    if op == 1:
        f.agregar(estudiantes)
    elif op == 2:
        if len(estudiantes) != 0:
            f.mostrar(estudiantes)
        else:
            print("No hay ningún estudiante registrado.")
    elif op == 3:
        if len(estudiantes) != 0:
            f.buscar(estudiantes)
        else:
            print("No hay ningún estudiante registrado.")

    elif op == 4:
        if len(estudiantes) != 0:
            f.importar(estudiantes)
        else:
            print("No hay ningún estudiante registrado.")
    else:
        print("Saliendo del programa...")