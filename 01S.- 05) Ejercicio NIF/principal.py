import funciones as f

personas = {}
op = 0
while op != 4:
    op = f.menu()
    if op == 1:
        f.grabar(personas)
    elif op == 2:
        if len(personas) != 0:
            f.buscar(personas)
        else:
            print("Ningún usuario ha sido registrado...")
    elif op == 3:
        if len(personas) != 0:
            f.guardar_archivo(personas)
        else:
            print("Ningún usuario ha sido registrado...")
    else:
        print("Saliendo del programa...")