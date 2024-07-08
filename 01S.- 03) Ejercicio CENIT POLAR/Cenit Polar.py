import Funciones as f

cenit = ["C","E","N","I","T"]
polar = ["P","O","L","A","R"]
palabras_encriptadas = []

op = 0
while op != 3:
    op = f.menu()
    if op == 1:
        f.encriptar(cenit,polar,palabras_encriptadas)
    if op == 2:
        if len(palabras_encriptadas) != 0:
            f.desencriptar(palabras_encriptadas)
        else:
            print("Ninguna palabra ha sido ingresada de momento.")
    if op == 3:
        print("Saliendo del programa...")
        f.archivo_csv(palabras_encriptadas)