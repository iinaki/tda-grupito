from TDABatalla import Batalla
import os

set_pruebas = "./set-pruebas"
resultados_esperados = "resultados_esperados.txt"

coeficientes = []

for file in os.listdir(set_pruebas):

    if file == resultados_esperados:
        continue

    file = set_pruebas + "/" + file 
    with open(file, "r") as f:
        batallas = []
        next(f)
        for line in f:
            ti, bi = line.split(",")
            batallas.append(Batalla(int(ti), int(bi)))

    _, coef = Batalla.optimizar_batallas(batallas)
    coeficientes.append(coef)

with open(set_pruebas + "/" + resultados_esperados , "r") as f:
    cont = 0
    correctos = True
    for line in f:
        if int(line) != coeficientes[cont]:
            correctos = False
            break
        cont += 1

if correctos:
    print("RESULTADOS CORRECTOS")
else:
    print("RESULTADOS ERRONEOS")