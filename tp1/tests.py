from TDABatalla import Batalla
import os

set_pruebas = "./set_pruebas"

for file in os.listdir(set_pruebas):
    prueba = file
    file = set_pruebas + "/" + file 
    with open(file, "r") as f:
        batallas = []
        next(f) #salteo "coeficiente_esperado"
        coeficiente_esperado = f.readline()
        next(f) #salteo "ti,bi"
        for line in f:
            ti, bi = line.split(",")
            batallas.append(Batalla(int(ti), int(bi)))

    _, coef = Batalla.optimizar_batallas(batallas)
    if coef == int(coeficiente_esperado):
        print(prueba + "\t...CORRECTA")
    else:
        print(prueba + "\t...ERRONEA")
