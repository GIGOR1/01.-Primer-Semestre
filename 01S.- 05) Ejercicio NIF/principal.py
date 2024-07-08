import funciones as f

personas = {}
op = 0
while op != 4:
    op = f.menu()
    if op == 1:
        f.grabar(personas)
    elif op == 2:
        f.buscar(personas)
    elif op == 3:
        f.guardar_archivo(personas)
    else:
        print("Saliendo del programa...")