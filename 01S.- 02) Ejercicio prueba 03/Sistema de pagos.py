import Funciones as f

trabajadores = []
cargos = {"ceo": 5000000,
          "analista":2500000,
          "desarrollador":2000000}
tabla = ["Trabajador","Cargo","Sueldo Bruto","Desc.Salud","Desc.AFP","Líquido a pagar"]
salud = 0.07
afp = 0.12

op = 0
while op != 4:
    op = f.menu()
    if op == 1:
        f.registrar(trabajadores, cargos, salud, afp)
    elif op == 2:
        if len(trabajadores) != 0:
            f.mostrar(trabajadores, tabla) 
        else:
            print("Ningún trabajador ha sido registrado.")
    elif op == 3:
        if len(trabajadores) != 0:
            f.imprimir(trabajadores, cargos)
        else:
            print("Ningún trabajador ha sido registrado.")
    else:
        print("Saliendo del programa...")