import csv

def menu():
    print("1.- Encriptar")
    print("2.- Desencriptar")
    print("3.- Salir")
    while True:
        try:
            op=int(input("-> "))
            if op > 0 and op < 4:
                return op
            else:
                print("Número ingresado fuera de rango.")
        except ValueError:
            print("Tipo de dato ingresado debe ser un número!")
        
def encriptar(cenit, polar, palabras):
    palabra = input("Ingrese palabra que desea encriptar: ").upper()
    palabra_encriptada = ""
    for letra in palabra:
        validado = False
        for i in range(len(cenit)):
            if letra == cenit[i]:
                letra_encriptada = polar[i]
                palabra_encriptada = palabra_encriptada + letra_encriptada
                validado = True
        for i in range(len(polar)):
            if letra == polar[i]:
                letra_encriptada = cenit[i]
                palabra_encriptada = palabra_encriptada + letra_encriptada
                validado = True
        if not validado:
            palabra_encriptada+= letra
    palabra = {palabra : palabra_encriptada}
    palabras.append(palabra)
    return palabras

def desencriptar(palabras):
    for i in range(len(palabras)):
        for key, value in palabras[i].items():
            print(f"Palabra: {key.lower().title()}\nEncriptación: {value.lower().title()}\n")

def archivo_csv(palabras):
    encriptacion = []    
    for i in range(len(palabras)):
        palabra = []
        for key, value in palabras[i].items():
            palabra.append(key.lower().title())
            palabra.append(value.lower().title())
        encriptacion.append(palabra)

    with open("Palabras encriptadas","w",newline="") as datos:
        escritura = csv.writer(datos)
        escritura.writerow(["Palabras","Encriptacion"])
        escritura.writerows(encriptacion)