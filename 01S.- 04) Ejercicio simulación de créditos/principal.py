import funciones as f

alumnos = ["Juan Pérez","María García","Carlos López","Ana Mártinez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
creditos = {}
op = 0
while op != 5:
    op = f.menu()
    if op == 1:
        f.creditos(alumnos,creditos)
    elif op == 2:
        if len(creditos) > 0:
            menor,mediano,mayor = f.clasificacion(creditos)
        else:
            print("\nAún no se efectua la simulación de créditos.")
    elif op == 3:
        if len(creditos) > 0:
            f.estadisticas_credito(creditos)
        else:
            print("\nAún no se efectua la simulación de créditos.")
    elif op == 4:
        if len(creditos) > 0:
            f.reporte(menor,mediano,mayor)
        else:
            print("\nAún no se efectua la simulación de créditos.")
    else:
        print("Saliendo del programa...")