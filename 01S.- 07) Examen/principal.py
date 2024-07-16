import funciones as f

trabajadores = ["Juan Pérez", "María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos = {}

op = 0

while op != 5:
    op = f.menu()
    if op == 1:
        f.asignacion_sueldos(trabajadores,sueldos)
    elif op == 2:
        if len(sueldos) != 0:
            f.mostrar_sueldos(sueldos)
        else:
            print("\n¡No se ha generado la asignación de sueldos!")
    elif op == 3:
        if len(sueldos) != 0:
            f.ver_estadisticas(sueldos)
        else:
            print("\n¡No se ha generado la asignación de sueldos!")
    elif op == 4:
        if len(sueldos) != 0:
            f.reporte_sueldos(sueldos)
        else:
            print("\n¡No se ha generado la asignación de sueldos!")
    else:
        print("\nFinalizando programa...")
        print("Desarrollado por Gabriel Igor")
        print("RUT 19.615.206-7")